---
title: VITE + REACT + TYPESCRIPT에 MSW 적용해보기
date: Fri, 25 Oct 2024 07:11:05 GMT
link: https://velog.io/@so356hot/VITE-REACT-TYPESCRIPT%EC%97%90-MSW-%EC%A0%81%EC%9A%A9%ED%95%B4%EB%B3%B4%EA%B8%B0
---

<h3 id="msw-소개">MSW 소개</h3>
<p>api를 사용할 때 나타날 수 있는 다양한 문제점들이 있다. </p>
<ul>
<li><strong>API 명세가 지연되는 경우</strong>
: 백엔드에서 API 작업이 완료되지 않아 명세가 나오지 않는 경우, 프론트엔드 개발자들은 무기한으로 대기해야 할 수 있다.</li>
<li><strong>테스트 코드 비효율성</strong>
: 테스트 코드에서 실제 api를 사용하는 경우, 비용 문제가 발생할 수 있고 실제로 네트워크 요청을 보내는 만큼 속도가 느려질 수 있다. 무엇보다 프론트엔드의 테스트 코드가 프론트에서 통제할 수 없는 api에 의존하기 때문에 의존성 문제가 생긴다.</li>
</ul>
<p>이러한 문제를 해결할 수 있는 도구가 바로 MSW이다. </p>
<h3 id="msw란">MSW란?</h3>
<p>MSW는 브라우저나 Node.js 환경에서 API 요청을 모킹할 수 있는 라이브러리이다. MSW는 실제 네트워크 요청을 가로채 모의 응답을 제공하며, 백엔드와의 통합 전 단계에서 개발과 테스트를 독립적으로 수행할 수 있도록 돕는다.</p>
<h3 id="msw의-특징">MSW의 특징</h3>
<ul>
<li><strong>독립성</strong>
: MSW는 어떠한 라이브러리나 프레임워크에도 영향을 받지 않으며, 브라우저와 Node.js 환경에서 플러그인 없이 사용할 수 있다.</li>
<li><strong>실제 네트워크 요청을 mocking</strong>
: msw는 <code>fetch()</code> 나 <code>axios</code> 같은 네트워크 요청을 보내는 함수를 단순히 모킹하는 것이 아니라, 실제로 보내진 네트워크 요청을 가로채는 방식으로 모킹을 한다. 이로 인해 개발 중 발생할 수 있는 문제를 더 일찍 발견하고 해결할 수 있다.</li>
<li><strong>재사용성</strong>
: 한 번 작성한 MSW 코드가 여러 테스트 도구와 실제 프로덕션 환경에서도 재사용 가능하므로 활용도가 높다.</li>
</ul>
<h3 id="msw의-장점">MSW의 장점</h3>
<ul>
<li><strong>백엔드 의존성 제거</strong>
: 백엔드 API 없이도 자체 데이터를 관리하며 프론트엔드 개발을 진행할 수 있다. 백엔드 작업이 지연되어 API를 직접 테스트해볼 수 없을 때 유용하다.</li>
<li><strong>테스트 효율성 향상</strong>
: MSW는 테스트 코드와 통합해 API 요청을 모킹할 수 있기 때문에 API 테스트에 발생하는 의존성 문제를 해결하고 비용과 속도를 개선할 수 있다.</li>
<li><strong>API 실패 케이스 대응</strong>
: MSW를 사용하면 API의 실패 응답이나 오류 상황을 손쉽게 시뮬레이션 할 수 있기 대문에 성공 케이스 뿐만 아니라 실패 케이스에 대한 처리를 더 철저하게 할 수 있다.</li>
<li><strong>storybook과 통합 기능</strong>
: storybook과 통합해 UI 컴포넌트의 다양한 동작을 실제 API 없이 테스트할 수 있다.</li>
</ul>
<h3 id="msw-원리">MSW 원리</h3>
<p>MSW는 브라우저와  Node.js 환경에서 네트워크 요청을 모킹해 실제 서버와의 통신 없이 모의 응답을 제공한다.</p>
<ul>
<li><strong>브라우저 환경에서의 동작 원리</strong>
: 브라우저 환경에서는 브라우저에서 제공하는 service worker를 이용해서 요청을 가로채고, 이를 클라이언트 측에서 모킹된 응답으로 처리한다.</li>
<li><strong>Node.js (노드 환경)에서의 동작 원리</strong>
: 반면 노드 환경에서는 HTTP와 같은 네트워크 프로토콜을 모킹하는 방식으로 동작한다.</li>
</ul>
<p>브라우저 중심으로 MSW 동작 원리를 자세히 살펴보자. </p>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/5c5e4143-91e2-4dc0-8201-3b22df09e126/image.png" /></p>
<ul>
<li><strong>브라우저에서 요청 발생 (1. Request)</strong>
: 먼저, 사용자가 웹에서 API 호출을 하거나 네트워크 요청이 발생한다.</li>
<li><strong>Service worker가 요청을 감지</strong>
: 브라우저의 Service Worker가 이 브라우저의 요청을 알아챈다.</li>
<li><strong>MSW로 요청 전달 (2. Request clone)</strong>
: 그러나 service worker는 이 요청을 실제 서버로 보내지 않고 클라이언트에 설치된 MSW 라이브러리로 전달한다.</li>
<li><strong>모킹 핸들러 매칭 (3. Match against mocks)</strong>
: 그럼 MSW 라이브러리는 해당 요청에 대한 핸들러를 찾아 핸들러에 등록된 모킹된 응답을 생성한&amp;반환한다.</li>
<li><strong>모킹된 응답 반환 (4. Mocked response) &amp; (5. respondWith(mockedResponse))</strong>
: 생성도니 모킹 응답은 service worker를 통해 다시 브라우저로 전달되고, 최종적으로 브라우저는 이 모킹된 응답을 받는다.</li>
</ul>
<p>⇒ 이러한 과정을 통해 실제 서버와의 통신 하지 않고도 API 요청을 처리할 수 있다. </p>
<p>좀 더 쉽게 일상적인 비유를 추가해 설명해보자면 MSW의 동작 원리는 식당의 주문 시스템과 비슷하다</p>
<ol>
<li>손님(브라우저)이 주문(API 요청)을 한다.</li>
<li>점원(service worker)가 주문을 받는다.</li>
<li>점원은 실제 주방(서버)에 가는 대신, 미리 준비된 메뉴(mock 응답)을 가져온다.</li>
<li>점원이 손님에게 음식(응답)을 서빙한다.</li>
</ol>
<p>이러한 과정으로 실제 주방(서버)와의 소통 없이도 손님(브라우저)는 음식(데이터)를 받을 수 있다.</p>
<h3 id="msw-코드-작성-포인트">MSW 코드 작성 포인트</h3>
<p>앞서 MSW의 개념과 원리를 알아보았으니, 이제 이를 실제 코드에 적용하는 방법을 간단히 살펴보자.</p>
<p><strong>예시) 유저 정보를 등록하는 요청 처리</strong></p>
<ul>
<li>클라이언트에서 유저 정보를 받아와서 이 유저를 등록해달라는 <strong>POST 요청</strong>을 서버에 보낸다.</li>
<li>서버는 해당 유저 정보를 <strong>리스트에 등록</strong>한 후, <strong>GET 요청</strong>이 있을 때 이 리스트를 반환한다.</li>
</ul>
<p><strong>실제 서버 로직과 MSW의 차이점</strong></p>
<p>post 요청이 들어오면 서버는 유저 정보를 데이터베이스에 저장하고, 유저 리스트를 정렬한 후 반환할 것이다. 그러나 MSW로 모킹할 땐 서버 로직을 그대로 구현할 필요는 없다. 이 때 생각해야 할 것이 바로 프론트엔드의 “역할”과 “책임”이다. 프론트엔드는 말 그대로 앞단을 담당하고 있기 때문에 서버 로직까지 신경 쓸 필요는 없다는 의미이다.</p>
<p><strong>MSW의 특징을 활용한 테스트</strong></p>
<p>MSW는 실제 네트워크 요청을 모킹해주기 때문에, 서버 로직보다 다양한 상태 코드에 따른 응답 처리에 집중하는 것이 더 중요하다.</p>
<p>예를 들어 </p>
<ul>
<li>성공적인 응답 (200, 204 등)을 잘 처리했는지</li>
<li>에러 응답(404, 500 등)이 발생했을 때도 예상대로 동작했는지</li>
</ul>
<p>이와 같은 상황을 다루는 테스트 케이스를 작성하면, 프론트엔드에서 서버와 통신할 때 발생할 수 있는 다양한 경우를 대비할 수 있다.</p>
<p><strong>테스트 커버리지 고려사항</strong></p>
<p>어디까지 테스트 코드를 작성해야 할 지에 대해서는 팀별 컨벤션, 그리고 리소스에 따라 다르겠지만 몇가지 키워드로 기준을 세워볼 수 있다.</p>
<ul>
<li>핵심 기능에 가까운 테스트인가?
: 당연하지만 핵심 기능일수록 테스트 커버리지를 높이는 것을 고려해볼 수 있다.</li>
<li>프론트의 책임을 다시 생각해보자
: 예를 들어 데이터를 정렬해서 보여주는 것은 프론트의 책임이 아닐 것이다.</li>
<li>직접 작성한 코드에 집중하자
: 이를테면 비동기 요청을 할 때 직접 작성한 코드가 있을 것이고 내부/외부 라이브러리 코드를 이용하는 로직(fetch, axios, react query 등)이 있을 것이다. 
이런 라이브러리들은 이미 검증된 기능이기 때문에, 우리가 직접 작성한 서비스 로직이 예상대로 동작하는지 확인하는 데 집중해야 한다.
예를 들어 react query를 이용해 유저에 대한 네트워크 처리를 담당하고 있는 로직이라면, React Query의 내부 동작을 테스트할 필요는 없지만, 이 라이브러리를 사용하는 서비스 로직이 올바르게 작동하는지는 테스트를 해봐야 한다.</li>
</ul>
<h3 id="리액트에서-msw-사용하기">리액트에서 MSW 사용하기</h3>
<p>리액트 애플리케이션에서 MSW를 활용하려면 먼저 MSW를 설치하고, 요청 핸들러를 정의해야 한다. </p>
<p>요청 핸들러는 실제 api 요청을 모킹할 때 어떤 응답을 반환할 지 결정하기 때문이다. </p>
<p>이후에 애플리케이션 진입점에서 MSW를 초기화하여 네트워크 요청을 가로챌 수 있도록 설정한다.</p>
<p>회원가입, 로그인을 MSW로 테스트해보자. </p>
<p>MSW <strong>설치하기</strong></p>
<pre><code class="language-bash">npm install msw@latest --save-dev</code></pre>
<p><strong>서비스 워커 등록</strong></p>
<p>이것을 등록하는 이유는 위의 예시에서 살펴봤듯이 MSW가 브라우저 환경에서 동작하기 위해 service worker API를 이용해 네트워크 요청을 가로채고 모의 응답으로 처리하기 때문이다.</p>
<p>이를 public에 위치시키는 이유는 public에 있는 파일들은 애플리케이션의 입구 근처 같은 곳으로, 이곳에 파일을 두면 vite가 자동으로 파일을 웹에서 호스팅 해주어 브라우저가 쉽게 로드할 수 있기 때문이다.</p>
<pre><code class="language-bash">npx msw init ./public --save</code></pre>
<p><strong>폴더 구조</strong></p>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/30f45159-6678-4d16-80ef-2a7453ea2238/image.png" /></p>
<p><strong>초기 세팅</strong></p>
<p>src 폴더 아래에 mocks 폴더를 생성 후, browser.ts 파일을 생성하여 아래와 같이 setupWorker를 등록해준다</p>
<pre><code class="language-jsx">// src/mocks/browser.ts
// 클라이언트에서 api요청 모킹을 처리해주는 파일
import { setupWorker } from &quot;msw/browser&quot;;
import { handlers } from &quot;./handlers&quot;; // 요청 핸들러들을 불러옴

export const worker = setupWorker(...handlers); // 서버 설정</code></pre>
<p><strong>애플리케이션에 MSW 연결</strong></p>
<p>애플리케이션 진입점에서 API 모킹을 위한 서비스 워커 설정</p>
<pre><code class="language-jsx">// main.tsx
import { StrictMode } from &quot;react&quot;;
import { createRoot } from &quot;react-dom/client&quot;;
import App from &quot;./App.tsx&quot;;
import { BrowserRouter } from &quot;react-router-dom&quot;;

// API 모킹을 설정하는 비동기 함수로, MSW(서비스 워커)를 설정해 브라우저에서 네트워크 요청을 모킹
async function enableMocking() {
  // vite의 경우
  // 개발 환경에서만 MSW를 활성화
  if (!import.meta.env.DEV) {
    return;
  }

// 해당 파일에서 설정한 MSW의 worker 객체를 동적 로딩해 모킹을 설정
  const { worker } = await import(&quot;./mocks/browser.ts&quot;);

  // 가져온 서비스 워커를 브라우저에서 시작해 API 요청을 가로채고, 정의된 핸들러로 응답 반환
  worker.start();
}

const rootElement = document.getElementById(&quot;root&quot;)!;

// enableMocking() 함수가 완성된 후에 앱의 렌더링을 시작 =&gt; 모킹이 활성화된 후에만 앱이 렌더링 되도록 보장
enableMocking().then(() =&gt; {
  const root = createRoot(rootElement);
  root.render(
    &lt;StrictMode&gt;
      &lt;BrowserRouter&gt;
        &lt;App /&gt;
      &lt;/BrowserRouter&gt;
    &lt;/StrictMode&gt;
  );
});</code></pre>
<p>연결이 잘 되었으면 아래와 같은 메세지가 출력되는 것을 확인할 수 있다</p>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/571437e5-1634-48e7-aa1a-c9f16706c79f/image.png" /></p>
<p>이렇게 설정을 해주었으면 필요한 api 요청을 mocks 폴더에 handler.ts 파일을 추가하여 작성해준다.
여기서 백엔드에서 제공해주는 api와 응답 형식을 그대로 작성하여 상태 코드에 따른 메세지와 데이터 응답을 구현할 수 있다.</p>
<pre><code class="language-jsx">// src/mocks/handler.ts
import { http } from &quot;msw&quot;;

export type Users = {
  username: string;
  password: string;
};

// 로그인 요청 데이터 타입 정의
interface LoginRequest {
  username: string;
  password: string;
}

interface RegisterRequest {
  username: string;
  password: string;
}

// 사용자의 리스트 (let으로 변경하여 새 사용자 추가 가능하도록 함)
const users: Users[] = [
  {
    username: &quot;so356hot&quot;,
    password: &quot;hyjhyj486!&quot;,
  },
  {
    username: &quot;borami&quot;,
    password: &quot;test1234&quot;,
  },
  {
    username: &quot;sunny&quot;,
    password: &quot;test1234&quot;,
  },
];

export const handlers = [
  // 회원가입 요청을 처리하는 핸들러
  http.post(&quot;http://localhost:8000/register&quot;, async ({ request }) =&gt; {
    const { username, password } = (await request.json()) as RegisterRequest;

    // 입력값 검증
    if (!username || !password) {
      return new Response(
        JSON.stringify({
          message: &quot;아이디와 비밀번호를 모두 입력해주세요.&quot;,
        }),
        {
          status: 400,
          headers: {
            &quot;Content-Type&quot;: &quot;application/json&quot;,
          },
        }
      );
    }

    // 사용자 이름 중복 체크
    const existingUser = users.find((user) =&gt; user.username === username);
    if (existingUser) {
      return new Response(
        JSON.stringify({
          message: &quot;이미 존재하는 아이디입니다.&quot;,
        }),
        {
          status: 409,
          headers: {
            &quot;Content-Type&quot;: &quot;application/json&quot;,
          },
        }
      );
    }

    // 새 사용자 추가
    const newUser = { username, password };
    users.push(newUser);

    return new Response(
      JSON.stringify({
        message: &quot;회원가입이 완료되었습니다.&quot;,
        user: { username: newUser.username },
      }),
      {
        status: 201,
        headers: {
          &quot;Content-Type&quot;: &quot;application/json&quot;,
        },
      }
    );
  }),

  // 로그인 요청을 처리하는 핸들러
  http.post(&quot;http://localhost:8000/login&quot;, async ({ request }) =&gt; {
    const { username, password } = (await request.json()) as LoginRequest;

    const user = users.find(
      (user) =&gt; user.username === username &amp;&amp; user.password === password
    );

    if (user) {
      return new Response(
        JSON.stringify({
          message: &quot;로그인 성공&quot;,
          user: { username: user.username },
        }),
        {
          status: 200,
          headers: {
            &quot;Content-Type&quot;: &quot;application/json&quot;,
          },
        }
      );
    } else {
      return new Response(
        JSON.stringify({
          message: &quot;등록되지 않은 회원입니다&quot;,
        }),
        {
          status: 401,
          headers: {
            &quot;Content-Type&quot;: &quot;application/json&quot;,
          },
        }
      );
    }
  }),
];</code></pre>
<p>이렇게 MSW는 API 명세 지연이나 테스트 코드 의존성 문제를 해결할 수 있는 도구로 프론트엔드에서 많이 사용된다고 한다.  이를 이용하면 백엔드 작업이 완료되지 않아도 프론트엔드 개발을 계속 진행할 수 있고, 다양한 상황을 테스트하고 대비하는 데 유용하기 때문이다. </p>
<hr />
<p><strong>참고 자료</strong>
<a href="https://www.npmjs.com/package/msw">https://www.npmjs.com/package/msw</a></p>
<p><a href="https://mswjs.io/docs/best-practices/typescript/">https://mswjs.io/docs/best-practices/typescript/</a></p>
<p><a href="https://mswjs.io/docs/integrations/browser">https://mswjs.io/docs/integrations/browser</a>
<br /></p>
<p><strong>msw 구현한 github 주소</strong>
<a href="https://github.com/youjin-hong/msw">https://github.com/youjin-hong/msw</a></p>
