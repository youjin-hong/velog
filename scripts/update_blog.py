import feedparser
import git
import os
import re
from datetime import datetime

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
    invalid_chars = r'[<>:"/\\|?*]'
    filename = re.sub(invalid_chars, '-', filename)
    filename = re.sub(r'-+', '-', filename)
    filename = filename.strip(' -')
    if len(filename) > 250:
        filename = filename[:250]
    return filename

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
    changed_posts = []

    # 각 글을 파일로 저장하고 커밋
    for entry in feed.entries:
        file_name = sanitize_filename(entry.title) + '.md'
        file_path = os.path.join(posts_dir, file_name)

        # description이 없을 수 있으므로 getattr 사용
        new_content = f"""---
        title: "{entry.title.replace('"', "'")}
        date: {entry.published if hasattr(entry, 'published') else datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        link: {entry.link}
        ---
        {getattr(entry, 'description', '')}
        """
        
        should_update = False

        if not os.path.exists(file_path):
            should_update = True
            action = "새 글 추가"
        else:
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

        if should_update:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"{action}: {entry.title}")
                changed_posts.append(file_path)
            except Exception as e:
                print(f"파일 업데이트 중 오류 발생: {entry.title}, 오류: {e}")
                continue

    if changed_posts:
        try:
            for file_path in changed_posts:
                repo.git.add(file_path)

            if len(changed_posts) == 1:
                commit_msg = f"Update post: {os.path.basename(changed_posts[0]).replace('.md', '')}"
            else:
                commit_msg = f"Update {len(changed_posts)} posts"

            repo.git.commit('-m', commit_msg)
            print(f"커밋 완료: {commit_msg}")
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
