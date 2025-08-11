# 📌 Velog 글 요약

| 항목   | 내용 |
|--------|------|
| **제목** | [스무디 한 잔 마시며 끝내는 리액트 + TDD] 3장 |
| **날짜** | Mon, 11 Aug 2025 06:30:31 GMT |
| **링크** | [https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-3%EC%9E%A5](https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-3%EC%9E%A5) |

---

<blockquote>
<p><strong>참고 자료</strong></p>
</blockquote>
<ul>
<li><a href="https://github.com/youjin-hong/TDD_study">TDD 실습 Github Repo</a></li>
<li><a href="https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-1-2-3%EC%9E%A5-%EB%A6%AC%EC%95%A1%ED%8A%B8-%EA%B8%B0%EB%B3%B8-%EA%B0%9C%EB%85%90-%EC%9D%B4%ED%95%B4-%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%99%98%EA%B2%BD-%EC%84%B8%ED%8C%85-zpmyuh7x">1, 2장 정리</a></li>
</ul>
<hr />
<h2 id="✨-3-리액트의-테스트---jest">✨ 3. 리액트의 테스트 - Jest</h2>
<h3 id="span-stylebackground-colorlavenderjest의-장점span"><strong><span style="background-color: lavender;">Jest의 장점</span></strong></h3>
<p>Jest는 Javascript 테스트 프레임워크로 React에서 가장 많이 쓰이며 이외에 Typescript, Node, Angular, Vue 등에서도 사용할 수 있습니다.
Jest의 장점은 아래와 같습니다. </p>
<p><strong><span style="background-color: #eaeaea;">1) 제로 설정</span></strong>
많은 테스트 프레임워크들이 테스트를 하기 위해 초기에 많은 설정을 해야 한다. Jest는 테스트를 쉽게 시작하고, 테스트에 집중하게 하기 위해 제로 설정을 지향하고 있습니다. </p>
<p><strong><span style="background-color: #eaeaea;">2) 스냅샷</span></strong>
테스트하다 보면 일일이 확인하기 힘든 객체가 존재할 때가 있습니다. Jest는 이러한 객체를 캡쳐하듯이 그대로 저장한 후, 추후에 값이 변경되면 에러를 표시하는 스냅샷 기능을 제공합니다. React에서는 이 스냅샷 기능을 통해 렌더링된 컴포넌트의 변경 사항이 있는지 체크합니다. </p>
<p><strong><span style="background-color: #eaeaea;">3) 모의 객체</span></strong>
테스트 범위를 벗어나는 객체들을 간단하게 Mocking 함으로써 실제로 테스트해야 할 부분을 집중해서 테스트할 수 있게 합니다. </p>
<p><strong><span style="background-color: #eaeaea;">4) 테스트 코드의 분리</span></strong>
Jest의 테스트 코드는 완전히 분리돼 있으며, 분리된 테스트는 동시에 실행할 수 있습니다. 따라서 Jest는 분리된 테스트 코드를 동시에 실행해 빠른 성능을 제공합니다. </p>
<p><strong><span style="background-color: #eaeaea;">5) 간단한 API</span></strong>
Jest는 쉽고 간단하게 테스트할 수 있는 API를 제공하며, --coverage 옵션으로 코드 커버리지를 간단하게 확인할 수 있습니다. </p>
<br />

<h3 id="span-stylebackground-colorlavender프로젝트-준비span"><strong><span style="background-color: lavender;">프로젝트 준비</span></strong></h3>
<p>Jest는 Javascript 테스트 프레임워크이므로 우선 자바스크립트 프로젝트를 생성해 테스트 해보려고 합니다.</p>
<ul>
<li>레포지토리 위에 &quot;jest-test&quot; 폴더를 생성</li>
<li><code>cd jest-test</code></li>
<li><code>npm init</code></li>
<li>모두 Enter 눌러 진행 후 package.json 생성된 것을 확인</li>
<li>package.json 파일과 같은 위치에 index.js 생성</li>
<li><blockquote>
<p>테스트 대상이 될 Javascript 코드를 작성할 예정</p>
</blockquote>
</li>
</ul>
<br />

<h3 id="span-stylebackground-colorlavenderjest-설치span"><strong><span style="background-color: lavender;">Jest 설치</span></strong></h3>
<ul>
<li><code>npm install --save-dev jest</code></li>
<li>package.json 파일에서 scripts: {&quot;test&quot;: &quot;jest --watch&quot;}로 수정</li>
<li><code>npm run test</code>로 jest 실행</li>
<li>a 키로 변경된 파일과 관계없이 모든 테스트를 실행할 수 있도록 선택</li>
</ul>
<br />

<h3 id="span-stylebackground-colorlavender사용-방법span"><strong><span style="background-color: lavender;">사용 방법</span></strong></h3>
<ul>
<li>jest-test 폴더 아래에 index.test.js 파일 생성 </li>
<li><blockquote>
<p>Jest는 파일 확장자가 .test.js로 끝나는 파일들을 텍스트 파일로 인식해 실행하기 때문에 이 테스트 파일에 index.js 파일에 관한 테스트를 작성</p>
</blockquote>
</li>
<li>index.js 파일에 다음과 같이 작성<pre><code class="language-javascript">const sum = (a, b) =&gt; {
return a + b;
};
</code></pre>
</li>
</ul>
<p>module.exports = {
  sum,
};</p>
<pre><code>- index.test.js 파일에 다음과 같이 작성
```javascript
const { sum } = require(&quot;./index&quot;);

// describe 함수: Jest가 제공하는 함수로, 여러 테스트를 한 그룹으로 묶고 설명을 붙이기 위해 사용
// 첫 번째 매개변수: 명령 프롬프트에 표시할 설명
// 두 번째 매개변수: 여러 테스트를 그룹으로 묶을 콜백 함수
describe(&quot;test index.js file&quot;, () =&gt; {
  // it 함수: 실제 테스트가 실행되는 테스트 명세를 작성할 때 사용
  // 첫 번째 매개변수: 테스트 명세의 설명
  // 두 번째 매개변수: 실제로 테스트를 실행하는 테스트 코드 작성
  it(&quot;sum 1 + 2 to equal 3&quot;, () =&gt; {
    expect(sum(1, 2)).toBe(3);
  });
});</code></pre><p>-&gt; 위에서 npm run test로 Jest가 파일을 감시하고 있다가, 변경되면 테스트를 다시 실행하도록 jest --watch 명령어를 실행해뒀기 때문에 파일을 작성하고 저장하면 자동으로 테스트 코드를 실행합니다. 따라서 터미널에 다음과 같은 화면을 확인할 수 있습니다. 
<img alt="" src="https://velog.velcdn.com/images/so356hot/post/88348604-0a5d-4bb3-80ce-0748d804545e/image.png" /></p>
<ul>
<li>index.js에 return a + b를 return a * b로 바꾸면 테스트가 실패하는 것을 확인
<img alt="" src="https://velog.velcdn.com/images/so356hot/post/31d34f39-b11c-48f7-ab31-c59abebd9319/image.png" /></li>
</ul>
<br />

<h3 id="span-stylebackground-colorlavendermatcherspan"><strong><span style="background-color: lavender;">Matcher</span></strong></h3>
<p>위에서 toBe()라는 Matcher를 사용해 테스트 코드를 작성해보았습니다. Matcher는 Jest가 제공하는 함수로, 결과값을 비교해 테스트 성공 여부를 판단합니다. 
toBe 외에 Jest에서 자주 사용되는 Matcher도 함께 살펴봅시다. </p>
<ul>
<li><strong>1) toEqual</strong></li>
<li><strong>2) toBeTruthy, toBeFalsy</strong></li>
<li><strong>3) toContain</strong></li>
<li>기타</li>
</ul>
<br />

<h3 id="span-stylebackground-colorlavender코드-커버리지span"><strong><span style="background-color: lavender;">코드 커버리지</span></strong></h3>
<p>테스트 코드 커버리지란, 테스트 대상이 되는 소스 코드 중에서 테스트 코드를 통해 검증된 코드의 비율을 말합니다. 
코드 커버리지를 통해 테스트 코드가 얼마나 많은 소스 코드를 테스트하고 있는지 나타내는 중요한 지표입니다. 이 지표를 통해 테스트 코드가 작성되지 않은 코드를 확인할 수 있습니다. </p>
<ul>
<li><code>npx jest --coverage</code>로 코드 커버리지 확인</li>
</ul>
<hr />
<h2 id="💡-새롭게-알게-된-점">💡 새롭게 알게 된 점</h2>
<h3 id="span-stylebackground-colorlavender❗라이브러리와-프레임워크의-차이span"><span style="background-color: lavender;">❗라이브러리와 프레임워크의 차이</span></h3>
<p>리액트가 라이브러리라는 것은 알고 있었지만, 프레임워크와 라이브러리의 정확한 차이는 최근에야 알게 되었습니다. 
<strong>프레임워크</strong>는 애플리케이션의 제어 흐름을 주도하며, 개발자는 그 틀 안에서 코드를 작성합니다.
<strong>라이브러리</strong>는 개발자가 애플리케이션의 제어 흐름을 주도하며, 필요할 때만 기능을 불러와 사용하는 것입니다. </p>
<p>즉, 둘의 차이는 <strong>'제어 흐름의 주도권'</strong>에 있는 것입니다. 이 개념이 처음에는 이해가 잘 안됐는데, 이번 챕터를 공부하며 찾아보니 먹는 것에 비유한 글을 보고 쉽게 이해할 수 있었습니다.</p>
<blockquote>
<p><strong>라이브러리를 이용하는 것</strong>
중식당에서 내가 원하는 시점에 원하는 음식을 선택하고 종업원에게 주문
➡️ 해당 음식을 제어하는 건 바로 &quot;나&quot;</p>
</blockquote>
<blockquote>
<p><strong>프레임워크를 사용하는 것</strong>
중식당에서 식당이 미리 정해둔 세트 메뉴를 주문하는 것.
이미 정해진 요리와 순서를 그대로 따름
➡️  식당이 내 점심 식사의 흐름을 제어 </p>
</blockquote>
<br />

<h3 id="span-stylebackground-colorlavender❗왜-spa는-동시다발적으로-빈번히-dom-변경이-발생하는지span"><span style="background-color: lavender;">❗왜 SPA는 동시다발적으로 빈번히 DOM 변경이 발생하는지?</span></h3>
<p>SPA에서 빈번하게 DOM 변경이 발생해서 최적화하기 위해 React에서 가상 DOM의 개념을 도입했다고 하는데, SPA에서 DOM 변경이 자주 일어난다는 말과, 그래서 왜 가상 DOM이 필요했던 건지 궁금해서 MPA와 SPA의 차이점을 찾아보았습니다. 
근본적인 차이는 <strong>페이지 vs 컴포넌트</strong>라고 이해하면 될 것 같습니다. </p>
<blockquote>
<p><strong>MPA의 동작 방식</strong></p>
</blockquote>
<ul>
<li>사용자가 링크를 클릭하면 서버에 새로운 페이지를 요청</li>
<li>브라우저는 기존 페이지를 완전히 버리고 새로운 HTML을 받아서 처음부터 렌더링</li>
<li>결과적으로 DOM 변경은 &quot;페이지 단위&quot;로, &quot;가끔씩&quot; 발생</li>
</ul>
<blockquote>
<p><strong>SPA의 동작 방식</strong></p>
</blockquote>
<ul>
<li>한 번 로드된 후에는 페이지 이동 없이 JavaScript가 모든 것을 제어</li>
<li>사용자의 모든 인터랙션(클릭, 입력, 스크롤 등)이 즉시 DOM 조작으로 연결</li>
<li>결과적으로 DOM 변경은 &quot;컴포넌트 단위&quot;로, &quot;실시간&quot;으로 발생</li>
</ul>
<p>이렇게 책에서 &quot;빈번한 DOM의 변경 (in SPA)&quot;라고 해서 이게 단점이라고 느낄 수도 있지만, 이걸 가상 DOM으로 보완했으며 오히려 장점입니다. 왜냐하면 사용자와 애플리케이션 간의 상호작용을 깜빡임 없이 실시간으로 반영해 부드러운 UX를 제공하기 때문입니다. 그렇지만 그만큼 성능 최적화 (메모이제이션, lazy loading 등)와 같은 상태 관리가 더욱 중요해질 것 같습니다. </p>
<br />

<h3 id="span-stylebackground-colorlavender❗양방향-데이터-바인딩과-단방향-데이터-바인딩의-차이span"><span style="background-color: lavender;">❗양방향 데이터 바인딩과 단방향 데이터 바인딩의 차이</span></h3>
<p>책에서 설명하고 있지만 &quot;데이터 바인딩&quot;이 뭔지 잘 모르겠..어서 좀 더 찾아보았습니다. 
데이터 바인딩이란, <strong>애플리케이션의 UI 요소와 데이터 간의 연결을 설정하고 유지하는 기술</strong>입니다. </p>
<p>쉽게 말하면 데이터와 화면을 자동으로 &quot;동기화&quot;시켜주는 것입니다.</p>
<blockquote>
<p><strong>단방향 데이터 바인딩</strong></p>
</blockquote>
<ul>
<li>데이터 → UI 한 방향으로만 흐름</li>
<li>데이터가 변경되면 UI가 자동으로 업데이트</li>
<li>예측 가능하고 디버깅이 쉬움</li>
<li>예: React의 기본 방식</li>
</ul>
<blockquote>
<p><strong>양방향 데이터 바인딩</strong> </p>
</blockquote>
<ul>
<li>데이터 ↔ UI 양방향으로 흐름</li>
<li>데이터가 변경되면 UI 업데이트 + UI에서 변경하면 데이터도 자동 업데이트</li>
<li>코드가 간결하지만 복잡한 앱에서는 데이터 흐름 추적이 어려울 수 있음</li>
<li>예: Vue.js의 v-model, Angular의 기본 방식</li>
</ul>
<pre><code class="language-javascript">// 단방향 (React)
const [name, setName] = useState('');
&lt;input value={name} onChange={(e) =&gt; setName(e.target.value)} /&gt;

// 양방향 (Vue)
&lt;input v-model=&quot;name&quot; /&gt;</code></pre>
<h2 id="❓-어려웠던-점">❓ 어려웠던 점</h2>
<p>이번 1, 2, 3 챕터는 도입 부분으로 간단한 내용을 다루고 있어서 크게 어려운 점은 없었던 것 같습니다. 
그러나 SPA의 특징, 단방향 데이터와 양방향 데이터의 차이, 그리고 가상 DOM이 왜 나오게 되었는지에 대해 고민해본 적도 없고 이해하기 마냥 어렵다고만 생각했었는데 이 책을 읽으며 Javascript의 역사부터 React 탄생 배경, 브라우저 렌더링 과정, 가상 DOM 개념의 도입까지 정리된 것을 보며 흐름을 파악하기가 수월했고, 특히 프로젝트할 때 자주 사용하는 React를 이제는 단순히 &quot;사용법&quot;만 아는 것이 아니라, 왜 이런 방식으로 동작하는지, 특징, 장점에 대해 조금 더 알게 된 것 같고 앞으로 쓸 때 조금 더 리액트를 잘 활용할 수 있게 고민하며 쓸 수 있게 된 것 같습니다. </p>
<h2 id="🙋-궁금한-점--다음에-다루고-싶은-내용">🙋‍ 궁금한 점 / 다음에 다루고 싶은 내용</h2>
<p>자바스크립트로 Jest를 사용하는 법에 대해 알아보았으니 다음에는 React에서 Jest를 적용해보고 싶고, Vite로 테스트 환경을 만들려고 했으나 CRA와 다른 점이 많아 우선 책에 나와있는 대로 CRA로 테스트 환경을 만들었는데, CRA와 Vite 차이에 대해 공부를 하고 다시 Vite로 설정을 해봐야겠다는 생각이 들었습니다. (CRA가 모든 파일 구성을 만들어줘서 간편하긴 한 것 같은데 체감상 너무 느리다고 느꼈습니다.) </p>
