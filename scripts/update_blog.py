import feedparser
import git
import os
import re
from datetime import datetime
import yaml

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@so356hot'

# 깃허브 레포지토리 경로
repo_path = '.'

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

def sanitize_filename(filename):
    """파일명에서 유효하지 않은 문자를 제거하거나 대체"""
    # 파일명에 사용할 수 없는 문자들을 대체
    invalid_chars = r'[<>:"/\\|?*]'
    filename = re.sub(invalid_chars, '-', filename)
    
    # 연속된 대시를 하나로 통합
    filename = re.sub(r'-+', '-', filename)
    
    # 앞뒤 공백과 대시 제거
    filename = filename.strip(' -')
    
    # 파일명이 너무 길면 자르기 (확장자 제외 255자 제한)
    if len(filename) > 250:
        filename = filename[:250]
    
    return filename

def escape_yaml_string(text):
    """YAML에서 안전한 문자열로 변환"""
    if not text:
        return '""'
    
    # 특수 문자가 있으면 따옴표로 감싸기
    if any(char in text for char in [':', '"', "'", '\n', '\r', '\\', '[', ']', '{', '}', '|', '>', '#']):
        # 내부 따옴표 이스케이프
        escaped = text.replace('"', '\\"')
        return f'"{escaped}"'
    
    return text

try:
    # 레포지토리 로드
    repo = git.Repo(repo_path)
    
    # RSS 피드 파싱
    print("RSS 피드를 가져오는 중...")
    feed = feedparser.parse(rss_url)
    
    if not feed.entries:
        print("RSS 피드에서 글을 찾을 수 없습니다.")
        exit()
    
    print(f"{len(feed.entries)}개의 글을 찾았습니다.")
    
    # 변경된 글들을 추적 (새 글 + 수정된 글)
    changed_posts = []
    
    # 각 글을 파일로 저장하고 커밋
    for entry in feed.entries:
        # 파일 이름 생성
        file_name = sanitize_filename(entry.title) + '.md'
        file_path = os.path.join(posts_dir, file_name)
        
        # YAML front matter를 안전하게 생성
        title = escape_yaml_string(entry.title)
        date_str = entry.published if hasattr(entry, 'published') else datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        link = escape_yaml_string(entry.link)
        
        # 새 콘텐츠 생성
        new_content = f"""---
title: {title}
date: {date_str}
link: {link}
---

{entry.description}
"""
        
        # 파일 업데이트 여부 확인
        should_update = False
        
        if not os.path.exists(file_path):
            # 새 글인 경우
            should_update = True
            action = "새 글 추가"
        else:
            # 기존 글인 경우 - 내용 비교
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    existing_content = file.read()
                
                if existing_content != new_content:
                    should_update = True
                    action = "글 수정"
                    
            except Exception as e:
                print(f"기존 파일 읽기 오류: {entry.title}, 오류: {e}")
                should_update = True
                action = "파일 재생성"
        
        # 파일 업데이트
        if should_update:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                
                print(f"{action}: {entry.title}")
                changed_posts.append(file_path)
                
            except Exception as e:
                print(f"파일 업데이트 중 오류 발생: {entry.title}, 오류: {e}")
                continue
    
    # 변경된 글이 있을 때만 커밋
    if changed_posts:
        try:
            # 모든 변경된 파일을 스테이징
            for file_path in changed_posts:
                repo.git.add(file_path)
            
            # 커밋 메시지 생성
            if len(changed_posts) == 1:
                commit_msg = f"Update post: {os.path.basename(changed_posts[0]).replace('.md', '')}"
            else:
                commit_msg = f"Update {len(changed_posts)} posts"
            
            # 커밋
            repo.git.commit('-m', commit_msg)
            print(f"커밋 완료: {commit_msg}")
            
            # 푸시
            repo.git.push()
            print("푸시 완료!")
            
        except git.exc.GitCommandError as e:
            print(f"Git 명령 실행 중 오류 발생: {e}")
        except Exception as e:
            print(f"커밋/푸시 중 오류 발생: {e}")
    else:
        print("변경된 글이 없습니다.")

except git.exc.InvalidGitRepositoryError:
    print("유효하지 않은 Git 저장소입니다.")
except Exception as e:
    print(f"스크립트 실행 중 오류 발생: {e}")
