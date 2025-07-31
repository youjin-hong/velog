# 📌 Velog 글 요약

| 항목   | 내용 |
|--------|------|
| **제목** | Husky로 Typescript 타입 체크하기 |
| **날짜** | Wed, 09 Jul 2025 14:55:39 GMT |
| **링크** | [https://velog.io/@so356hot/Husky%EB%A1%9C-Typescript-%ED%83%80%EC%9E%85-%EC%B2%B4%ED%81%AC%ED%95%98%EA%B8%B0](https://velog.io/@so356hot/Husky%EB%A1%9C-Typescript-%ED%83%80%EC%9E%85-%EC%B2%B4%ED%81%AC%ED%95%98%EA%B8%B0) |

---

<blockquote>
<p><em>배포 실패율 30% → 5%로 줄인 실전 경험</em></p>
</blockquote>
<h3 id="🚨-이런-상황-경험해보셨나요">🚨 이런 상황, 경험해보셨나요?</h3>
<p>&quot;PR 승인받고 머지했는데 또 타입 에러로 배포 실패... 😭&quot;</p>
<p>로컬에서는 잘 돌아가던 코드가 배포 단계에서 타입 에러로 실패하는 상황, 
개발하면서 한 번쯤 겪어보지 않으셨나요?</p>
<p>한 번의 타입 에러 수정을 위해 
issue 생성 → feature branch 작업 → PR 생성 → approve 대기 → merge 
이 과정을 반복하며 최소 nn분씩 날린 경험을 다들 한 번씩은 해보셨을 것 같아요.</p>
<p><strong>저희 팀의 실제 상황:</strong></p>
<ul>
<li>배포 10번 중 2-3번은 타입 에러로 실패</li>
<li>한 번의 수정 사이클에 최소 1시간 소요</li>
<li>개발자들의 스트레스 지수 📈📈📈</li>
</ul>
<p>이 모든 문제를 Husky로 해결한 이야기를 소개해보려 합니다.</p>
<hr />
<h3 id="🔧-husky-도입-계기">🔧 Husky 도입 계기</h3>
<p><strong>[기존]</strong></p>
<p>로컬에서도 타입 설정 (<code>tsconfig.json</code>)을 엄격하게 설정해서 타입 정의 오류나 누락이 발생했을 때에도 오류 메세지를 표시하긴 하지만, <code>react</code> 프로젝트 특성 상 여러 모듈을 <code>import</code>하여 사용하다보니 여러 파일을 동시에 작업할 때 이런 문제를 놓치고 지나쳐 <code>main</code>에 머지하고 CI/CD가 끝나고 build 실패가 뜨고 나서야 발견하는 상황이 종종 있었습니다. </p>
<blockquote>
<p><strong>❗문제 상황</strong></p>
</blockquote>
<ul>
<li>개발 중 평균적으로  배포 10번 시도할 때 타입 오류로 2~3번 실패</li>
<li>한번의 수정 사이클:<br /><code>issue</code> 생성 → <code>feature branch</code> 작업 → <code>pull request</code> 생성 → 팀원 <code>approve</code> 대기 → <code>merge</code> (최소 1시간 소요)</li>
</ul>
<p>한번에 build 오류가 해결되면 그나마 다행이지만 여러번 실패할 때에는 이 과정을 반복해야 했기 때문에 개발 효율성이 떨어진다고 느꼈는데요. </p>
<p>이런 비효율적인 프로세스를 개선하고자 <code>commit/push</code> 단계에서 사전에 타입 오류를 검출할 수 있는 방법을 찾던 중 <code>husky</code>라는 도구를 발견하게 되었습니다.
<br /></p>
<p><strong>[husky 도입 후]</strong> </p>
<p><code>husky</code>는 단어 그대로 “충성스러운 개”라는 의미로, Git의 특정 이벤트 (<code>commit</code>, <code>add</code>, <code>push</code>) 전/후로 실행되는 <code>hook</code>을 쉽게 관리할 수 있게 해주는 도구입니다. </p>
<p>팀에서 개발 시작 전 prettier, eslint, 커밋 메시지 등 다양한 룰을 정의해두지만, 개발 과정에서 시간에 쫓기거나 실수로 이를 놓치는 경우가 빈번했습니다. 룰을 지키지 않으면 설정해둔 의미가 없기 때문에 특정 Git 이벤트에서 자동화를 통해 룰을 강제로 준수하게 할 필요가 있다고 판단을 했습니다. </p>
<p><code>Git Hook</code>을 직접 설정하려면 <code>.git/hooks</code> 디렉토리에서 작업해야 하는데 이를 일일이 작업할 수도 있지만, 간편하게 <code>husky</code>라는 패키지를 이용할 수 있습니다. </p>
<p>일단 기본적인 <code>prettier</code>, <code>eslint</code>검사와 <code>husky</code>도입의 핵심 동기였던 타입 체크 를 자동화 하려고 합니다. </p>
<p><code>hook</code> 실행 시점은 <code>commit</code> 전에 한번, <code>push</code> 전에 한번 수행해서 문제가 있는 코드가 원격 저장소에 업로드되기 전에 로컬에서 차단하고 싶어 <code>pre-commit</code>, <code>pre-push</code> 단계에 설정을 해주었습니다. </p>
<p>우선 실행 플로우는 아래와 같습니다. </p>
<pre><code class="language-text">1. 코드 작성 및 수정
   ↓
2. git add .
   ↓
3. git commit -m &quot;commit message&quot;
   ↓
4. PRE-COMMIT 훅 실행 (로컬)
   ├── npx lint-staged (스테이징된 파일만 검사)
   │   ├── ESLint/Prettier 실행
   │   └── 포맷팅 자동 수정
   ├── npm run type-check (전체 프로젝트 타입 체크)
   └── ✅ 통과 시 커밋 완료 / ❌ 실패 시 커밋 차단
   ↓
5. git push origin feature-branch
   ↓
6. PRE-PUSH 훅 실행 (로컬)
   ├── npm run lint (전체 프로젝트 린트)
   ├── npm run type-check (전체 프로젝트 타입 체크)
   ├── npm run build (실제 빌드 테스트)
   └── ✅ 통과 시 푸시 완료 / ❌ 실패 시 푸시 차단
   ↓
7. GitHub에 코드 업로드
   ↓
8. Pull Request 생성
   ↓
9. main 브랜치 머지
   ↓
10. Vercel CI/CD 파이프라인 실행 (원격)
    ├── npm install
    ├── npm run build
    └── 배포</code></pre>
<br />

<p><strong>[테스트 시나리오]</strong></p>
<p>다음과 같은 타입 오류를 의도적으로 만들어 <code>Husky</code>가 정상적으로 차단하는지 확인해보겠습니다.</p>
<blockquote>
<p>1)  <strong>Props 타입 정의 누락</strong>: <code>testSummary</code> 매개변수의 타입 미정의
2) <strong>타입 불일치</strong>: <code>string</code>타입 변수에 <code>number</code> 값 할당</p>
</blockquote>
<p><em><strong>⇒ 예상 결과: 2개의 타입 오류 검출 후 커밋 차단</strong></em></p>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/bd010887-0d66-439e-9d92-1ad7d9ff1ab1/image.png" /></p>
<pre><code class="language-typescript">    // interface TestRatingBarsProps {
    //   testSummary: {
    //     totalSuccessTests: number;
    //     totalFailTests: number;
    //     routingSuccessCount: number;
    //     routingFailCount: number;
    //     interactionSuccessCount: number;
    //     interactionFailCount: number;
    //     mappingSuccessCount: number;
    //     mappingFailCount: number;
    //   };
    // }

    export default function TestRatingBars({ testSummary }) {
      const test: string = -1236;

      console.log(test);
    }</code></pre>
<p>이렇게 일부러 타입 오류의 상황을 만들고 <code>commit</code>을 해주면 아래와 같이 타입 오류를 반환하여 <code>commit</code>취소가 되는 것을 확인할 수 있습니다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/992a5911-98fd-4dc3-bb32-6102a891034b/image.png" /></p>
<pre><code class="language-bash">    $ git commit -m &quot;[ #85 | Test ] husky로 타입 체크 테스트&quot;
    ✔ Backed up original state in git stash (a8715fa)
    ✔ Running tasks for staged files...
    ✔ Applying modifications from tasks...
    ✔ Cleaning up temporary files...

    &gt; front@0.0.0 type-check
    &gt; tsc --project tsconfig.app.json --noEmit

    src/pages/test/_components/testDetail/TestRatingBars.tsx:18:42 - error TS7031: Binding element 'testSummary' implicitly has an 'any' type.

    18 export default function TestRatingBars({ testSummary }) {
                                                ~~~~~~~~~~~

    src/pages/test/_components/testDetail/TestRatingBars.tsx:19:9 - error TS2322: Type 'number' is not assignable to type 'string'.

    19   const test: string = -1236;
               ~~~~

    Found 2 errors in the same file, starting at: src/pages/test/_components/testDetail/TestRatingBars.tsx:18     

    husky - pre-commit hook exited with code 2 (error)</code></pre>
<p>이제 정상적인 코드로 수정 후, 다시 <code>commit</code>을 해보겠습니다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/21dba026-0616-4073-b44b-0f1a12c7a7d3/image.png" /></p>
<pre><code class="language-typescript">    interface TestRatingBarsProps {
      testSummary: {
        totalSuccessTests: number;
        totalFailTests: number;
        routingSuccessCount: number;
        routingFailCount: number;
        interactionSuccessCount: number;
        interactionFailCount: number;
        mappingSuccessCount: number;
        mappingFailCount: number;
      };
    }

    export default function TestRatingBars({ testSummary }: TestRatingBarsProps) {
      const test: number = -1236;

      console.log(test);
    }
</code></pre>
<p>그럼 정상적으로 <code>commit</code>이 이뤄지는 것을 볼 수 있습니다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/f684e862-5fd6-4b8d-ab25-f0f36babef7a/image.png" /></p>
<pre><code class="language-bash">    $ git commit -m &quot;[ #85 | Test ] husky로 타입 체크 테스트&quot;
    ✔ Backed up original state in git stash (3323163)
    ✔ Running tasks for staged files...
    ✔ Applying modifications from tasks...
    ✔ Cleaning up temporary files...

    &gt; front@0.0.0 type-check
    &gt; tsc --project tsconfig.app.json --noEmit

    [feat/85-husky 957dc9a] [ #85 | Test ] husky로 타입 체크 테스트
     4 files changed, 16 insertions(+), 20 deletions(-)</code></pre>
<p><strong>[정량적 개선 목표]</strong></p>
<p>이렇게 <code>husky</code>를 도입하고나서의 기대하는 효과는 로컬에서 개발 후 <code>commit</code>전에 미처 발견하지 못했던 <code>prettier</code>, <code>eslint</code>포맷팅 누락과 타입 정의 오류/누락 문제를 미리 파악하며 build 실패율을 줄여 배포 안정성을 높이는 것입니다. </p>
<ul>
<li>build 실패율: 20-30% → 5% 이하로 감소</li>
<li>타입 오류 수정 사이클 시간: 평균 1시간 → 즉시 해결</li>
</ul>
<hr />
<h3 id="⚙️-설치--설정-과정">⚙️ 설치 &amp; 설정 과정</h3>
<p><strong>1. 허스키 설치 및 초기화</strong>
→ 설치하고 초기화를 진행하면 <code>husky</code> 폴더가 생성되는데, 이곳은 Git hooks 스크립트가 저장되는 공간입니다. </p>
<pre><code class="language-bash">    npm install --save-dev husky
    npx husky init</code></pre>
<p><strong>2. <code>package.json</code>에 <code>prepare</code> 스크립트 확인</strong></p>
<pre><code class="language-jsx">    {
      &quot;scripts&quot;: {
      ...
        &quot;prepare&quot;: &quot;husky install&quot;
      }
    }</code></pre>
<p><strong>3. <code>Lint-staged</code> 설치</strong>
→ 2번까지만 설정을 해주면 한 번 commit을 할 때마다 전체 파일에 대해 검사를 하기 때문에 시간이 오래 걸리는데요. 그래서 변경된(staging) 파일에 대해서만 검사를 하기 위해 설치해줍니다. </p>
<pre><code class="language-bash">    npm install lint-staged --save-dev</code></pre>
<p><strong>4. 이제 <code>.husky</code> 폴더 아래 hook을 실행하고 싶은 단계의 파일을 생성해줍니다.</strong> 
우리는 pre-commit, pre-push 훅을 생성해주었습니다. 직접 파일을 만들어줘도 되고, 아래 명령어를 터미널에 입력해 만들어줘도 됩니다. </p>
<pre><code class="language-bash">    echo &quot;npm test&quot; &gt; .husky/pre-commit
    echo &quot;npm test&quot; &gt; .husky/pre-push </code></pre>
<pre><code>아래와 같이 옵션을 설정해줍니다. </code></pre><pre><code class="language-jsx">    // .husky/pre-commit
    #!/bin/sh
    . &quot;$(dirname &quot;$0&quot;)/_/husky.sh&quot;
    npx lint-staged  // staging된 파일만 검사</code></pre>
<pre><code class="language-jsx">    // .husky/pre-push
    #!/bin/sh
    . &quot;$(dirname &quot;$0&quot;)/_/husky.sh&quot;
    npm run lint  // 전체 프로젝트 lint
    npm run build // 실제 build 테스트 (build 가능한지 확인)</code></pre>
<p><strong>5. <code>package.json</code>에 <code>lint-staged</code> 설정을 해줍니다.</strong>
→ 아래 확장자 파일 형식에 맞는 파일들을 대상으로 검사가 수행될 것임을 의미합니다. </p>
<pre><code class="language-jsx">      &quot;lint-staged&quot;: {
        &quot;*.{js,jsx,ts,tsx}&quot;: [
          &quot;eslint --fix&quot;,
          &quot;prettier --write&quot;
        ]
      },</code></pre>
<p><strong>6. (추가) typescript 오류 검출을 위한 설정을 해줍니다.</strong>
→ 우리는 <code>tsconfig.json</code>이 <code>tsconfig.app.json</code>과 <code>tsconfig.node.json</code> 2개의 파일을 reference하고 있으므로 <code>tsconfig.app.json</code> 에 typescript 설정을 수정해주었습니다. </p>
<pre><code class="language-jsx">    {
      &quot;compilerOptions&quot;: {
        &quot;noEmit&quot;: true,  // 빌드하지 않고 타입 체크만
        &quot;strict&quot;: true   // 엄격한 타입 체크
      },
      &quot;include&quot;: [
        &quot;src/**/*&quot;,         
        &quot;src/**/*.ts&quot;,
        &quot;src/**/*.tsx&quot;
      ]
    }</code></pre>
<p><strong>7. <code>package.json</code>에 <code>&quot;type-check&quot;</code> 추가해줍니다.</strong>
→ <code>tsconfig.json</code> 단일 파일로 존재한다면 <code>tsconfig.app.json</code>을 <code>tsconfig.json</code>으로 바꿔주면 됩니다.</p>
<pre><code class="language-jsx">      &quot;scripts&quot;: {
      ...
        &quot;prepare&quot;: &quot;husky install&quot;,
        &quot;type-check&quot;: &quot;tsc --project tsconfig.app.json --noEmit&quot;
      },</code></pre>
<p><strong>8. <code>pre-commit</code>, <code>pre-push</code> 훅에 설정을 추가해줍니다.</strong></p>
<pre><code class="language-jsx">    // .husky/pre-commit
    #!/bin/sh
    . &quot;$(dirname &quot;$0&quot;)/_/husky.sh&quot;
    npx lint-staged  // staging된 파일만 검사
    npm run type-check // 전체 타입 체크 (추가)</code></pre>
<pre><code class="language-jsx">    // .husky/pre-push
    #!/bin/sh
    . &quot;$(dirname &quot;$0&quot;)/_/husky.sh&quot;
    npm run lint  // 전체 프로젝트 lint
    npm run type-check  // 전체 타입 체크 (추가)(중복이지만 안전)
    npm run build // 실제 build 테스트 (build 가능한지 확인)</code></pre>
<hr />
<h3 id="🎯-결론">🎯 결론</h3>
<p>Husky 도입으로 얻은 가장 큰 성과는:</p>
<ul>
<li>✅ 개발자의 스트레스 감소</li>
<li>✅ 배포 안정성 향상 (build 실패율: 20-30% → 5% 이하로 감소)</li>
<li>✅ 팀 전체 생산성 증대 (타입 오류 수정 사이클 시간: 평균 1시간 → 즉시 해결)</li>
</ul>
<p>다른 블로그들을 보니 commit 메세지 설정을 많이 하던데 이것도 한 번 적용해보면 좋을 것 같고 다른 어떤 설정들을 많이 쓰는지, 우리 프로젝트에 뭐를 적용하면 개발이 더 편리해질 지 고민해보면 좋을 것 같다는 생각을 했습니다. </p>
<p><strong>참고 자료</strong></p>
<p><a href="https://typicode.github.io/husky/get-started.html">Husky 공식 문서</a></p>
