# 📌 Velog 글 요약

| 항목   | 내용 |
|--------|------|
| **제목** | [스무디 한 잔 마시며 끝내는 리액트 + TDD] 4장 - react-testing-library 설정하기 |
| **날짜** | Mon, 11 Aug 2025 06:34:07 GMT |
| **링크** | [https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-4%EC%9E%A5-react-testing-library-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0](https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-4%EC%9E%A5-react-testing-library-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0) |

---

<blockquote>
<p><strong>참고자료</strong></p>
</blockquote>
<ul>
<li><a href="https://github.com/youjin-hong/TDD_study">TDD 실습 Github Repo</a></li>
<li><a href="https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-3%EC%9E%A5">3장 정리본</a></li>
<li><a href="https://testing-library.com/">@testing-library 공식 문서</a></li>
<li><a href="https://github.com/testing-library/react-testing-library">react-testing-library Github</a></li>
</ul>
<p>지난 시간에 리액트의 역사와 자바스크립트 테스트 프레임워크인 Jest에 대해서 간략하게 살펴보았습니다. 이번 시간에는 React 프로젝트를 만들고, react-testing-library에 대해 실습해보는 시간을 가져보겠습니다. </p>
<p>이번 장에서 create-react-app을 CRA라고 부르도록 하겠습니다.</p>
<hr />
<h2 id="✨-4-리액트-테스트-react-testing-library">✨ 4. 리액트 테스트: react-testing-library</h2>
<h3 id="span-stylebackground-colorlavenderreact-testing-libraryspan"><span style="background-color: lavender;">react-testing-library</span></h3>
<p><strong>React Testing Library</strong>는 React 컴포넌트를 테스트하기 위한 DOM 테스팅 라이브러리입니다. Jest가 일반적인 Javascript 테스트 프레임워크라면, React Testing Library는 JSX와 DOM을 다루는 React 컴포넌트를 위한 테스트 도구입니다. </p>
<br />

<p><strong><span style="background-color: yellow;">react-testing-library의 장점</span></strong></p>
<ul>
<li><p><strong>사용자 중심 테스트 유틸리티 제공</strong></p>
<ul>
<li>실제 사용자가 DOM을 사용하는 방식과 유사하게 테스트 작성</li>
<li>텍스트, 링크, 버튼 등을 사용자 관점에서 찾아 테스트</li>
</ul>
</li>
<li><p><strong>구현 세부사항과 분리된 테스트</strong></p>
<ul>
<li>컴포넌트의 내부 구현 방식이 아닌 결과물을 테스트</li>
<li>리팩토링 시에도 테스트 코드 수정 불필요</li>
<li>장기간 유지 가능한 안정적인 테스트 코드 ➡️ 개발 생산성 향상</li>
</ul>
</li>
<li><p>** 실제 DOM 환경에서 테스트**</p>
<ul>
<li>react-dom 위에서 동작하여 더 신뢰할 수 있는 테스트</li>
<li>인스턴스가 아닌 메모리상에 실제 DOM을 생성해 테스트하므로 정확도 높음</li>
</ul>
<br />

</li>
</ul>
<p><strong><span style="background-color: yellow;">프로젝트 준비</span></strong>
react-testing-library는 리액트의 컴포넌트를 테스트하기 위한 라이브러리이므로 리액트 프로젝트를 하나 생성해줍니다. </p>
<p>다음 명령어를 chap_4 폴더 위치에서 react-testing-library를 사용할 리액트 프로젝트를 만들어주었습니다.
<code>npx create-react-app react-testing-library-test</code></p>
<br />

<h3 id="span-stylebackground-colorlavenderreact-testing-library-설치-및-설정span"><span style="background-color: lavender;">react-testing-library 설치 및 설정</span></h3>
<p>react-testing-library는 Jest와 마찬가지로 CRA로 생성한 리액트 프로젝트에 기본적으로 같이 설치됩니다. 저는 CRA을 사용하여 리액트 프로젝트를 생성했기 때문에 추가적인 라이브러리 설치를 진행하지 않았습니다.</p>
<p>만약, CRA로 프로젝트를 생성하지 않는 경우(eg. Vite)에는 다음의 명령어를 실행하여 react-testing-library를 설치해야 합니다. 
<code>npm install --save-dev @testing-library/react</code></p>
<br />

<h3 id="span-stylebackground-colorlavender기본-사용법span"><span style="background-color: lavender;">기본 사용법</span></h3>
<p><strong><span style="background-color: yellow;">기본 테스트 구조</span></strong></p>
<pre><code class="language-javascript">// src/App.test.js의 기본 구조
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () =&gt; {
  render(&lt;App /&gt;);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});</code></pre>
<p><strong><span style="background-color: yellow;">핵심 함수들</span></strong></p>
<ul>
<li><p><code>render()</code></p>
<ul>
<li>React 컴포넌트를 메모리상의 DOM에 렌더링</li>
<li>다양한 유용한 객체들을 반환 (container, screen 등)</li>
</ul>
</li>
<li><p><code>screen</code></p>
<ul>
<li>렌더링된 화면(DOM)에 접근하는 객체</li>
<li>다양한 요소 검색 메서드 제공</li>
</ul>
</li>
<li><p><code>container</code></p>
<ul>
<li>render 함수가 반환하는 객체 중 하나</li>
<li>리액트 컴포넌트가 화면에 표시되는 부분을 담고 있는 객체</li>
</ul>
<br />

</li>
</ul>
<h3 id="span-stylebackground-colorlavender실전-테스트-예제span"><span style="background-color: lavender;">실전 테스트 예제</span></h3>
<p><strong><span style="background-color: yellow;">전체 App.test.js 코드</span></strong></p>
<pre><code class="language-javascript">import { render, screen } from '@testing-library/react';
import App from './App';

describe(&quot;&lt;App /&gt;&quot;, () =&gt; {
  it(&quot;renders component correctly&quot;, () =&gt; {
    const { container } = render(&lt;App /&gt;);

    // 링크 요소 테스트
    const linkElement = screen.getByText(/learn react/i);
    expect(linkElement).toBeInTheDocument();

    // 이미지 요소 테스트
    expect(container.getElementsByClassName(&quot;App-logo&quot;)).toHaveLength(1);
    expect(container.getElementsByClassName(&quot;App-logo&quot;)[0]).toHaveAttribute(
      &quot;src&quot;,
      &quot;logo.svg&quot;
    );

    // 문단 요소 테스트
    expect(container.getElementsByTagName(&quot;p&quot;)).toHaveLength(1);
    expect(container.getElementsByTagName(&quot;p&quot;)[0]).toHaveTextContent(
      &quot;Edit src/App.js and save to reload&quot;
    );

    // 스냅샷 테스트
    expect(container).toMatchSnapshot();
  });
});</code></pre>
<p><strong><span style="background-color: yellow;">주요 검증 함수들</span></strong></p>
<ul>
<li><code>toBeInTheDocument()</code>: DOM에 존재하는지 확인</li>
<li><code>toHaveLength()</code>: 요소의 개수 확인</li>
<li><code>toHaveAttribute()</code>: 속성값 확인</li>
<li><code>toHaveTextContent()</code>: 텍스트 내용 확인</li>
</ul>
<br />

<h3 id="span-stylebackground-colorlavender스냅샷-테스트span"><span style="background-color: lavender;">스냅샷 테스트</span></h3>
<p><strong><span style="background-color: yellow;">목적과 동작</span></strong></p>
<ul>
<li>컴포넌트의 렌더링 결과를 파일로 저장하여 변경사항 감지</li>
<li>의도치 않은 UI 변경을 방지하는 안전장치</li>
<li><code>src/__snapshots__/</code> 폴더에 <code>App.test.js.snap</code> 파일 생성</li>
</ul>
<br />


<p><strong><span style="background-color: yellow;">스냅샷 업데이트</span></strong></p>
<pre><code class="language-bash"># 테스트 실행 중 터미널에 'u' 키를 눌러 스냅샷 업데이트 가능
npm run test</code></pre>
<p>테스트를 통과하면 아래와 같은 결과를 확인할 수 있습니다. </p>
<pre><code class="language-bash">PASS  src/App.test.js
  &lt;App /&gt;
    ✓ renders component correctly (35 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total</code></pre>
<blockquote>
<p><strong>💡핵심 포인트</strong></p>
</blockquote>
<ul>
<li>Jest와 함께 사용: React Testing Library는 테스트 실행기가 아니므로 Jest와 함께 사용해야 함</li>
<li>사용자 관점 중심: 개발자가 아닌 실제 사용자가 보고 사용하는 관점에서 테스트 작성</li>
<li>결과 중심 테스트: &quot;어떻게 구현&quot;이 아닌 &quot;사용자에게 무엇이 보이는지&quot;에 집중</li>
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
