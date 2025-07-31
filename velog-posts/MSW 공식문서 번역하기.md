---
        title: "MSW 공식문서 번역하기
        date: Wed, 05 Jun 2024 17:10:35 GMT
        link: https://velog.io/@so356hot/MSW-%EA%B3%B5%EC%8B%9D%EB%AC%B8%EC%84%9C-%EB%B2%88%EC%97%AD%ED%95%98%EA%B8%B0
        ---
        <h1 id="공식문서-번역하기">공식문서 번역하기</h1>
<p><a href="https://mswjs.io/docs/getting-started">https://mswjs.io/docs/getting-started</a></p>
<p>MSW (Mock Service Worker)은 API 요청을 가로채고 모킹(Mocking)할 수 있는 도구이다.
일반적으로 개발 환경에서 사용되며, 로컬 개발 환경에서 mocking된 API 응답을 제공하여
백엔드가 아직 준비되지 않았거나, test를 위해 실제 API를 호출하지 않도록 한다. </p>
<p>개발자들은 아래와 같은 다양한 용도로 MSW를 사용한다.</p>
<ul>
<li>API 모의</li>
<li>개발 중 네트워크 debug</li>
<li>팀 전체에 작업 표시</li>
<li>나가는 트래픽 monitoring</li>
<li>등등</li>
</ul>
<p>위처럼 모든 사용 사례에 적합한 단일 tutorial을 작성하는 것은 매우 어렵다. </p>
<p>그러나, 좋은 소식은 MSW 작업은 사용 방법과 위치에 관계없이 동일한 흐름을 따른다는 것이다. </p>
<p>아래에서, Node.js 애플리케이션에 MSW를 통합하는 완전한 기본 tutorial을 찾을 수 있다. 
이 tutorial은 작업 참조용으로 작성되었고, 원하는 통합을 달성하려면 아래의 각 섹션의 추가 링크를 따라가는 것이 좋을 것이다.</p>
<h3 id="1단계-설치">1단계: 설치</h3>
<p>프로젝트에서 다음 명령을 실행하여 MSW를 개발 의존성으로 설치한다.</p>
<p>이 방법의 장점은 버전 관리를 npm으로 할 수 있고, 프로젝트의 다른 부분과 통합이 잘 된다는 점이다. 설치 후에는 MSW를 설정하고 사용하기 위한 script를 추가해 로컬 환경에서 mocking할 수 있다.</p>
<p><code>npm install msw@latest —save-dev</code></p>
<blockquote>
<p>필요한 경우엔, <a href="https://mswjs.io/docs/recipes/using-cdn"><strong><em>CDN</em></strong></a> (Content Delivery Network)에서 MSW를 설치할 수 있다.</p>
</blockquote>
<p>CDN를 사용하면 MSW를 외부 서버에서 직접 불러와 사용할 수 있다. 
이 방법은 설치 과정이 필요 없고, 간단히 HTML 파일에 script를 추가해 사용할 수 있다. </p>
<p>CDN의 장점은 다음 과 같다. </p>
<ul>
<li>빠르게 테스트 해보고 싶을 때</li>
<li>설정이 간단한 프로젝트에서 사용할 때</li>
<li>로컬 설치 없이 간단히 사용하고 싶을 때</li>
</ul>
<p>그러나, CDN을 사용하면 외부 네트워크를 통해 라이브러리를 불러오기 때문에 인터넷 연결이 필요하고, 버전 관리를 직접 하기가 어려울 수 있다. </p>
<p>그래서 프로젝트의 일관성을 위해 npm 설치를 선호하는 경우가 많다고 한다.</p>
<h3 id="2단계-설명">2단계: 설명</h3>
<p>다음으로, <a href="https://mswjs.io/docs/concepts/request-handler"><strong><em>Request handlers</em></strong></a>를 사용해 네트워크를 설명할 수 있다. (예: http.get(), graphql.query())</p>
<p>request handler는 요청을 가로채서(<a href="https://mswjs.io/docs/basics/intercepting-requests"><strong><em>intercepting a request</em></strong></a>) 해당 응답을 처리(<a href="https://mswjs.io/docs/basics/mocking-responses"><strong><em>handling its response</em></strong></a>)하는 역할을 담당한다. 
이는 모의(mocked) 응답일 수도 있고, 실제 응답과 모의 응답의 조합일 수 있으며 트래픽에 영향을 주지 않고 단순히 트래픽만 monitoring하려는 경우, 아무 응답도 하지 않을 수 있다. </p>
<ul>
<li><p><em>트래픽(traffic)이란?</em></p>
<p>  네트워크 통신에서 주고받는 데이터 흐름.
  웹 애플리케이션의 경우, 클라이언트(웹 브라우저)와 서버 간의 HTTP 요청과 응답이 트래픽에 해당한다.</p>
<p>  MSW를 사용할 때, “트래픽을 모니터링한다”는 것은 클라이언트와 서버 사이에서 주고받는 요청과 응답을 관찰하고 기록하는 것을 의미한다.
  이렇게 하면 요청의 내용을 분석하거나 문제가 발생했을 때 디버깅을 할 수 있다. </p>
<p>  ⇒ 따라서, 트래픽은 네트워크 상의 데이터 이동, 즉 <strong>클라이언트가 서버에 보내는 요청</strong>과 <strong>서버가 클라이언트에 보내는 응답</strong>을 의미한다. 
  MSW는 이러한 트래픽을 가로채고 필요한 대로 응답을 조작하거나 단순히 기록할 수 있는 기록을 제공한다.</p>
</li>
</ul>
<p>이 튜토리얼에서는 요청에 대한 단일 HTTP request handler를 정의하고<br /><code>GET https://example/.com/user</code>  모의 JSON 응답으로 응답해보자.</p>
<pre><code class="language-jsx">// src/mocks/handlers.js
import { http, HttpResponse } from 'msw';

export const handlers = [
    // &quot;GET https://example.com/user&quot; 가로채고...
    http.get('https://example.com/user', () =&gt; {
        // ...이 JSON 응답을 사용해 응답한다.
        return HttpResponse.json({
            id: 'c7b3d8e0-5e0b-4b0f-8b3a-3b9f4b3d3b3d',
            firstName: 'John',
            lastName: 'Maverick',
            })
        }),
    ]</code></pre>
<blockquote>
<p>작은 규모로 시작해, 네트워크 설명을 포함한 전체 내용을 담은 단일 <code>handlers.js</code> 모듈을 작성한다. 
시간이 지나면서 핸들러를 재구조화(재구성)하고 실행 중에 이를 재정의(수정)하는 방법을 배울 수 있다.</p>
</blockquote>
<p>동시에 동일한 handler배열을 포함해 REST(<a href="https://mswjs.io/docs/network-behavior/rest"><strong><em>Restful API</em></strong></a>) 또는 GraphQL(<a href="https://mswjs.io/docs/network-behavior/graphql"><strong><em>GraphQL API</em></strong></a>)과 같은 다양한 API를 설명할 수 있다. </p>
<p>MSW를 사용한 서버 API 설명에 대해 자세히 알아볼 수 있고, 
MSW를 최대한 효과적으로 사용하려면 TypeScript를 사용해 요청 핸들러에 타입을 지정하면 좋다. 실제 API의 타입 정의(OpenAPI 문서나 GraphQL Code Generator)를 사용하는 경우 특히 유용하다.
<strong>OpenAPI 문서</strong>나 <strong>GraphQL Code Generator</strong>를 통해 생성된 타입 정의를 활용하면, API 모킹이 더욱 정확하고 효율적이다. 이렇게 하면 API 변경 사항에 대한 반응 속도가 빨라지고, 타입 안전성을 유지할 수 있다.</p>
<h3 id="3단계-통합">3단계: 통합</h3>
<p>MSW는 환경 수준에서 적용되기 때문에 어떤 framework, 요청 라이브러리 및 다른 도구와도 통합된다. 따라서 브라우저에서 사용할 지, Node.js 프로세스에서 사용할 지 (또는 둘 다) 결정하기만 하면 된다. 사용하는 환경에 관계없이 동일한 request handler를 계속 재사용할 수 있다.</p>
<p>이 튜토리얼에서는 다음과 같은 Node.js 통합 모듈을 생성해 MSW를 일반 Node.js 프로세스에 통합해보자. </p>
<pre><code class="language-jsx">// src/mocks/node.js
import { setupServer } from 'msw/node';
import { handlers } from './handler';

export const server = setupServer(...handlers)</code></pre>
<p>Node.js와 브라우저용과 같은 환경 의존적인 통합 모듈을 생성하는 것을 권장한다고 한다. 
이렇게 하면 다양한 도구에서 동일한 통합을 재사용할 수 있다. 
javascript로 작성된 모든 도구는 브라우저 (실제 브라우저, Playwright, Cypress, Storybook) 또는 Node.js (Vitest, Jest, React Native)에서 실행된다. 
각자의 도구의 환경에 따라 적절한 통합 모듈을 불러오면 된다.</p>
<p>우리가 만든 Node.js 통합 모듈은 MSW를 어떤 Node.js 프로세스에서도 실행할 수 있도록 설정하지만, 실제로 아직 시작하진 않는다. 
요청 가로채기를 시작하려면 Node.js 프로세스에서 <code>server.listen()</code>을 호출해야 한다.</p>
<pre><code class="language-jsx">// src/index.js
import { server } from './mocks/node';

server.listen();

// 이것은 네트워크 요청을 수행하고 응답을 출력하는 간단한 Node.js 애플리케이션이다.
async function app() {
    const response = await fetch('https//example.com/user');
    const user = await response.json();
    console.log(user);
}

app();</code></pre>
<blockquote>
<p><code>process.env.NODE_ENV</code> 또는 다른 기준에 따라 조건부로 MSW를 시작할 수도 있다.</p>
</blockquote>
<p>이제 애플리케이션을 실행하면 실제로 네트워크 요청을 하지 않고도 모의 응답이 출력된다.</p>
<pre><code class="language-jsx">node ./src/index.js

{
    id: 'c7b3d8e0-5e0b-4b0f-8b3a-3b9f4b3d3b3d',
    firstName: 'John',
    lastName: 'Maverick'
}</code></pre>
<p>MSW를 다양한 환경에 통합하는 방법에 대해 자세히 알아보자.</p>
<ul>
<li><a href="https://mswjs.io/docs/integrations/browser"><strong><em>브라우저</em></strong></a> (React 애플리케이션이나 Storybook과 같은 브라우저 환경에 MSW를 통합한다.)</li>
<li><a href="https://mswjs.io/docs/integrations/node"><strong><em>Node.js</em></strong></a> (Express 애플리케이션이나 테스트 실행기와 같은 Node.js에 MSW를 통합한다.)</li>
<li><a href="https://mswjs.io/docs/integrations/react-native"><strong><em>React Native</em></strong></a> (React Native 애플리케이션에 MSW를 통합한다.)</li>
</ul>
<h3 id="사용-예">사용 예</h3>
<p>아래 저장소에서는 Jest, Vitest, Cypress, Playwright, Angular, Svelte, Remix 등과 같은 도구와 함께 Mock Service Worker를 사용하는 방법에 대한 기능적이고 완전하며 최소한의 예제를 찾을 수 있따. 
이것들을 해당 도구와 MSW를 통합할 때 참고 자료로 쓰면 좋을 것이다. </p>
<p><a href="https://github.com/mswjs/examples">https://github.com/mswjs/examples</a></p>
<blockquote>
<p>문제가 생기면 각 사용 예를 재생산 저장소로 전환한다.</p>
</blockquote>
<h3 id="도움이-필요하다면">도움이 필요하다면?</h3>
<p>새 도구로 시작하는 것은 어려울 수 있지만 혼자서는 할 수 없다. 
따라서 문제가 발생할 때마다 가장 좋은 곳은 디버깅 런북이다. </p>
<p><a href="https://mswjs.io/docs/runbook">https://mswjs.io/docs/runbook</a></p>
<p>또한 아래의 링크에서 도움을 받을 수 있다. </p>
<ul>
<li><strong>MSW<a href="https://discord.com/invite/z29WbnfDC5">디스코드</a></strong></li>
<li><a href="https://github.com/mswjs/msw/discussions"><strong>GITHUB</strong></a><strong>에서 토론하기</strong></li>
</ul>
        