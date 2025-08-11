# 📌 Velog 글 요약

| 항목   | 내용 |
|--------|------|
| **제목** | [스무디 한 잔 마시며 끝내는 리액트 + TDD] 5장 - React + Typescript 개발 환경 구축하기 |
| **날짜** | Mon, 11 Aug 2025 06:39:00 GMT |
| **링크** | [https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-5-React-Typescript-%EA%B0%9C%EB%B0%9C-%ED%99%98%EA%B2%BD-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0](https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-5-React-Typescript-%EA%B0%9C%EB%B0%9C-%ED%99%98%EA%B2%BD-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0) |

---

<blockquote>
<p><strong>참고자료</strong></p>
</blockquote>
<ul>
<li><a href="https://github.com/youjin-hong/TDD_study">TDD 실습 Github Repo</a></li>
<li><a href="https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-4%EC%9E%A5-react-testing-library-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0">4장 정리본</a></li>
</ul>
<hr />
<h2 id="✨-5-react--typescript-개발-환경-구축하기">✨ 5. React + Typescript 개발 환경 구축하기</h2>
<h3 id="span-stylebackground-colorlavendertypescript를-선택하는-이유span"><span style="background-color: lavender;">Typescript를 선택하는 이유</span></h3>
<blockquote>
<p><strong>Javascript vs Typescript</strong></p>
</blockquote>
<ul>
<li><strong>Javascript</strong>: 런타임에 변수 타입 결정 → 실행 전까지 타입 오류 발견 불가</li>
<li><strong>Typescript</strong>: 컴파일 시점에 타입 검사 → 개발 단계에서 오류 조기 발견</li>
</ul>
<p><strong>Typescript의 장점</strong>
✅ 자바스크립트 저반에 걸쳐 사용 가능 (Flow보다 범용적)
✅ 풍부한 타입 정의 파일 (DefinitelyTyped)
✅ 뛰어난 에디터 지원 (특히 VSCode)
✅ 개발 생산성 향상</p>
<h3 id="span-stylebackground-colorlavendertypescript-프로젝트-설정span"><span style="background-color: lavender;">Typescript 프로젝트 설정</span></h3>
<p><strong><span style="background-color: yellow;">기본 프로젝트 생성</span></strong></p>
<pre><code class="language-bash"># CRA로 기본 프로젝트 생성
npx create-react-app library

# TypeScript 의존성 설치
npm install --save-dev typescript @types/node @types/react @types/react-dom @types/jest</code></pre>
<blockquote>
<p><strong>설치한 라이브러리의 타입 정의 파일</strong></p>
</blockquote>
<ul>
<li><code>typescript</code>: 타입스크립트 라이브러리</li>
<li><code>@types/node</code>: 노드의 타입이 정의된 타입 정의 파이</li>
<li><code>@types/react</code>: 리액트의 타입이 정의된 타입 정의 파일</li>
<li><code>@types/react-dom</code>: react-dom의 타입이 정의된 타입 정의 파일</li>
<li><code>@types/jest</code>: Jest의 타입이 정의된 타입 정의 파일</li>
</ul>
<br />

<p><strong><span style="background-color: yellow;">tsconfig.json 설정</span></strong></p>
<pre><code class="language-json">{
  &quot;compilerOptions&quot;: {
    &quot;target&quot;: &quot;es5&quot;,
    &quot;lib&quot;: [&quot;DOM&quot;, &quot;DOM.Iterable&quot;, &quot;ESNext&quot;],
    &quot;allowJs&quot;: true,
    &quot;skipLibCheck&quot;: true,
    &quot;esModuleInterop&quot;: true,
    &quot;allowSyntheticDefaultImports&quot;: true,
    &quot;strict&quot;: true,
    &quot;forceConsistentCasingInFileNames&quot;: true,
    &quot;noFallthroughCasesInSwitch&quot;: true,
    &quot;module&quot;: &quot;esnext&quot;,
    &quot;moduleResolution&quot;: &quot;node&quot;,
    &quot;resolveJsonModule&quot;: true,
    &quot;isolatedModules&quot;: true,
    &quot;noEmit&quot;: true,
    &quot;jsx&quot;: &quot;react-jsx&quot;,
    &quot;baseUrl&quot;: &quot;src&quot;  // 절대 경로 설정
  },
  &quot;include&quot;: [&quot;src&quot;, &quot;custom.d.ts&quot;]
}</code></pre>
<br />

<p><strong><span style="background-color: yellow;">파일 확장자 변경</span></strong></p>
<blockquote>
<p><strong>자바스크립트 파일 ➡️ 타입스크립트 파일</strong></p>
</blockquote>
<ul>
<li><code>./src/App.js</code> → <code>./src/App.tsx</code></li>
<li><code>./src/App.test.js</code> → <code>./src/App.test.tsx</code></li>
<li><code>./src/index.js</code> → <code>./src/index.tsx</code></li>
<li><code>./src/reportWebVitals.js</code> → <code>./src/reportWebVitals.ts</code></li>
<li><code>./src/setupTests.js</code> → <code>./src/setupTests.ts</code></li>
</ul>
<br />

<p><strong><span style="background-color: yellow;">SVG 타입 정의 (custom.d.ts)</span></strong></p>
<pre><code class="language-typescript">declare module &quot;*.svg&quot; {
  import * as React from &quot;react&quot;;

  export const ReactComponent: React.FunctionComponent&lt;
    React.SVGProps&lt;SVGSVGElement&gt; &amp; { title?: string }
  &gt;;

  const src: string;
  export default src;
}</code></pre>
<p>그 다음 App.test.tsx에 4장의 테스트 코드를 복사해 붙여넣어줍니다. 단, 우리가 지금 사용하고 있는 react-testing-library의 버전에 맞춰서 container 메소드 대신 semantic queries를 사용해줍니다. </p>
<pre><code class="language-jsx">import React from &quot;react&quot;;
import { render, screen } from &quot;@testing-library/react&quot;;
import App from &quot;./App&quot;;

describe(&quot;&lt;App /&gt;&quot;, () =&gt; {
  it(&quot;renders all main components&quot;, () =&gt; {
    render(&lt;App /&gt;);

    // Logo 확인
    const logo = screen.getByRole(&quot;img&quot;, { name: /logo/i });
    expect(logo).toHaveAttribute(&quot;src&quot;, &quot;logo.svg&quot;);
    expect(logo).toHaveClass(&quot;App-logo&quot;);

    // Edit 텍스트 확인 (분할된 텍스트 처리)
    expect(screen.getByText(/edit/i)).toBeInTheDocument();
    expect(screen.getByText(&quot;src/App.tsx&quot;)).toBeInTheDocument();
    expect(screen.getByText(/and save to reload/i)).toBeInTheDocument();

    // Learn React 링크 확인
    const learnLink = screen.getByRole(&quot;link&quot;, { name: /learn react/i });
    expect(learnLink).toHaveAttribute(&quot;href&quot;, &quot;https://reactjs.org&quot;);
  });
});</code></pre>
<br />

<h3 id="span-stylebackground-colorlavenderstyled-components로-스타일링span"><span style="background-color: lavender;">styled-components로 스타일링</span></h3>
<p><strong><span style="background-color: yellow;">설치 및 설정</span></strong> </p>
<pre><code class="language-bash">npm install --save styled-components
npm install --save-dev @types/styled-components jest-styled-components</code></pre>
<blockquote>
<p><strong>styled-components의 장점</strong>
✅ 클래스명 충돌 방지
✅ 컴포넌트 기반 스타일 관리
✅ 직관적인 동적 스타일링
✅ 자동 CSS 최적화</p>
</blockquote>
<br />

<h3 id="span-stylebackground-colorlavender절대-경로-설정span"><span style="background-color: lavender;">절대 경로 설정</span></h3>
<p><strong><span style="background-color: yellow;">tsconfig.json에 baseUrl 추가</span></strong> </p>
<pre><code class="language-json">{
  &quot;compilerOptions&quot;: {
    &quot;baseUrl&quot;: &quot;src&quot;  // 이 한 줄로 절대 경로 사용 가능!
  }
}</code></pre>
<p><strong><span style="background-color: yellow;">사용 예시</span></strong> </p>
<pre><code class="language-javascript">// ❌ 복잡한 상대 경로
import Component from '../../../components/Component'

// ✅ 명확한 절대 경로  
import Component from 'components/Component'</code></pre>
<br />

<h3 id="span-stylebackground-colorlavenderprettier-자동-포맷팅span"><span style="background-color: lavender;">Prettier 자동 포맷팅</span></h3>
<p><strong><span style="background-color: yellow;">설치</span></strong></p>
<pre><code class="language-bash">npm install --save-dev husky lint-staged prettier</code></pre>
<p><strong><span style="background-color: yellow;">.prettierrc.js 설정</span></strong></p>
<pre><code class="language-javascript">module.exports = {
  jsxBracketSameLine: true,
  singleQuote: true,
  trailingComma: &quot;all&quot;,
  printWidth: 100,
};</code></pre>
<p><strong><span style="background-color: yellow;">package.json에 Git Hook 설정</span></strong> </p>
<pre><code class="language-json">{
  &quot;scripts&quot;: {},
  &quot;husky&quot;: {
    &quot;hooks&quot;: {
      &quot;pre-commit&quot;: &quot;lint-staged&quot;
    }
  },
  &quot;lint-staged&quot;: {
    &quot;src/**/*.{js,jsx,ts,tsx,json,css,scss,md}&quot;: [
      &quot;prettier --write&quot;
    ]
  }
}</code></pre>
<blockquote>
<p><strong>💡핵심 포인트</strong></p>
</blockquote>
<ul>
<li><strong>TypeScript</strong>: 타입 안전성으로 런타임 오류 예방</li>
<li><strong>Testing Library</strong>: 사용자 중심 테스트로 더 견고한 코드</li>
<li><strong>styled-components</strong>: 컴포넌트 기반 스타일 관리</li>
<li><strong>절대 경로</strong>: 명확하고 유지보수하기 쉬운 import</li>
<li><strong>Prettier</strong>: 일관된 코드 스타일 자동 적용</li>
</ul>
<hr />
<hr />
<h2 id="💡-새롭게-알게-된-점">💡 새롭게 알게 된 점</h2>
<h3 id="span-stylebackground-colorlavender❗dom을-다루는-게-왜-단순한-자바스크립트의-테스트로-정확한-오류를-잡아내기-어려운지span"><span style="background-color: lavender;">❗DOM을 다루는 게 왜 단순한 자바스크립트의 테스트로 정확한 오류를 잡아내기 어려운지?</span></h3>
<p>DOM은 브라우저 환경에서만 존재하는 객체이기 때문에, 단순히 자바스크립트 테스트 환경에서는 아래와 같은 이유들로 컴포넌트의 <strong>실제 동작</strong>과 <strong>테스트 환경</strong> 차이로 인해 정확한 오류 검출이 어려워집니다. </p>
<ul>
<li><strong>브라우저 API 부재</strong>
: <code>document</code>, <code>window</code> 등의 브라우저 전용 객체가 없다. </li>
<li><strong>이벤트 시스템 미지원</strong>
: 클릭, 입력 등의 실제 사용자 상호작용을 시뮬레이션하기 어렵다. </li>
<li><strong>렌더링 로직 부재</strong>
: 실제 화면에 어떻게 표시되는지 확인 불가</li>
<li><strong>스타일 적용 확인 불가</strong>
: CSS 스타일이나 레이아웃 변화를 테스트할 수 없다. </li>
</ul>
<br />

<h3 id="span-stylebackground-colorlavender❗react-testing-library는-실제-dom-노드에서-작동하므로-더-신뢰할-수-있는-테스트를-할-수-있다고-했는데-왜-더-신뢰할-수-있는-건지span"><span style="background-color: lavender;">❗react-testing-library는 실제 DOM 노드에서 작동하므로 더 신뢰할 수 있는 테스트를 할 수 있다고 했는데, 왜 더 신뢰할 수 있는 건지?</span></h3>
<p>다른 테스트 프레임워크는 인스턴스 기반으로 접근합니다. </p>
<pre><code class="language-javascript">// Enzyme 등의 접근 방식 (인스턴스 기반)
const wrapper = shallow(&lt;MyComponent /&gt;);
wrapper.instance().someMethod(); // 내부 구현에 의존</code></pre>
<p>반면 react-testing-library는 실제 DOM 노드에 접근하여 실제 사용자 행동과 유사한 테스트를 제공합니다.</p>
<pre><code class="language-javascript">// 실제 DOM 기반 테스트
render(&lt;MyComponent /&gt;);
const button = screen.getByRole('button');
fireEvent.click(button); // 실제 사용자 행동과 유사</code></pre>
<p><strong>신뢰할 수 있는 이유?</strong></p>
<ul>
<li><p><strong>실제 DOM 사용</strong></p>
<ul>
<li>브라우저에서 실행되는 것과 동일한 환경</li>
</ul>
</li>
<li><p><strong>사용자 중심 테스트</strong></p>
<ul>
<li>내부 구현이 아닌 사용자가 보는 화면 기준</li>
<li>접근성을 고려한 요소를 선택</li>
</ul>
</li>
<li><p><strong>통합 테스트 지향</strong></p>
<ul>
<li>컴포넌트 간의 상호작용까지 검증</li>
<li>실제 사용 시나리오와 유사한 테스트</li>
</ul>
</li>
<li><p><strong>구현 세부사항과 분리</strong></p>
<ul>
<li>내부 state나 props가 아닌 결과물에 집중</li>
<li>리팩토링 시에도 테스트가 깨지지 않음</li>
</ul>
</li>
</ul>
<h2 id="❓-어려웠던-점">❓ 어려웠던 점</h2>
<p>cra와 react 19 버전, 그리고 업그레이드된 react-testing-library 의 변경된 사항들 때문에 책을 클론코딩하면 테스트 실패가 뜨는 게 너무 번거로웠습니다. 직접 겪었던 사례를 몇 가지 들어보자면, 테스트 코드에서 container나 parentElement 등을 쓰면 &quot;직접적인 DOM 노드 사용을 피하라&quot;는 메세지가 많이 떴습니다. 어떤 코드는 이 메시지가 뜨면서도 테스트는 통과하기도 했지만 대부분은 fail이 떴습니다. 초반에는 버전 업그레이드에 따른 권장 방식에 맞춰 부모 요소에 직접 접근하지 않고 getByRole이나 testId로 접근하여 오류를 하나씩 해결하며 클론 코딩을 진행했는데, 작성해야 할 코드가 점점 길어질수록 번거로웠습니다. vite로 마이그레이션을 해야하나 싶었지만 이번 스터디의 내 목표는 testing-library의 사용법을 익히는 것이기 때문에 CRA에서 VITE로의 마이그레이션은 안할 것 같습니다. </p>
<h2 id="🙋-궁금한-점--다음에-다루고-싶은-내용">🙋‍ 궁금한 점 / 다음에 다루고 싶은 내용</h2>
<p>4, 5, 6장의 내용이 생각보다 많아서 한번에 공부하다 보니 제대로 개념 정립이 되지 않은 것 같습니다. 오류 메시지도 해결할 겸 다시 복기해보려고 합니다. </p>
