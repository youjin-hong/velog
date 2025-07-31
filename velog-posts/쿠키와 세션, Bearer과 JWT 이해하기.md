# 📌 Velog 글 요약

| 항목   | 내용 |
|--------|------|
| **제목** | 쿠키와 세션, Bearer과 JWT 이해하기 |
| **날짜** | Fri, 01 Nov 2024 03:07:57 GMT |
| **링크** | [https://velog.io/@so356hot/%EC%BF%A0%ED%82%A4%EC%99%80-%EC%84%B8%EC%85%98-Bearer%EA%B3%BC-JWT-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0](https://velog.io/@so356hot/%EC%BF%A0%ED%82%A4%EC%99%80-%EC%84%B8%EC%85%98-Bearer%EA%B3%BC-JWT-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0) |

---

<h2 id="들어가기-전에">들어가기 전에…</h2>
<h3 id="인증과-인가-authentication-vs-authorization">인증과 인가 (Authentication vs Authorization)</h3>
<p><strong>인증(Authentication)</strong>은 사용자가 “누구인지” 확인하는 과정이다. 웹 애플리케이션에서는 일반적으로 사용자 이름(아이디)와 비밀번호를 입력하여 로그인하는 과정에서 이뤄진다. 이러한 신원을 확인하는 것은 해당 웹의 시스템에 접근하기 위해서는 필수적이다. </p>
<p><strong>인가(Authorization)</strong>는 신원 인증이 완료된 사용자에게 특정 자원에 대한 접근 권한을 부여하는 과정이다. 이 과정은 사용자가 해당 시스템 내에서 수행할 수 있는 작업을 결정한다. 왜냐하면 사용자마다 접근할 수 있는 자원과 수행할 수 있는 일이 다를 수 있기 때문에 인가는 보안 유지와 권한 관리에 중요한 역할을 한다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/0c112bd1-f474-4ca6-bfd7-83ffc1d0d251/image.png" /></p>
<p>예를 들어, 누군가 oo학교 전용 사이트에 로그인하여 “학생”으로 인증을 받았다면, 이 학생은 자신이 수강한 과목과 성적을 조회할 수 있는 권한만 가질 수 있을 것이다. </p>
<p>반면에 oo학교 전용 사이트에 로그인하여 “교수”로 인증을 받았다면, 자신의 수업을 듣는 학생들의 정보와 성적을 수정, 삭제 및 열람할 수 있는 권한을 가질 수 있다.</p>
<h3 id="웹-애플리케이션의-http-특징과-쿠키와-세션을-사용하는-이유">웹 애플리케이션의 HTTP 특징과 쿠키와 세션을 사용하는 이유</h3>
<p>웹 애플리케이션은 일반적으로 서버 ↔ 클라이언트 구조로 동작하며, HTTP 프로토콜을 이용해 통신을 한다. 이 HTTP 프로토콜은 <strong>Connectionless(비연결성</strong>), <strong>Stateless(무상태)</strong>의 특징을 지닌다. </p>
<ul>
<li><strong>Connectionless (비연결성)</strong>
서버와 클라이언트가 연결 상태를 유지하지 않는 방식이다. 서버는 1요청에 대한 1응답 후 연결을 끊어 리소스를 절약한다. 만약 서버와 클라이언트가 계속 연결되어 있다면 서버 비용이 크게 증가한다.</li>
<li><strong>Stateless (무상태)</strong>
서버가 클라이언트의 이전 상태를 저장하지 않는 방식이다. 상태를 저장하지 않기 때문에 서버는 클라이언트의 이전 요청을 알 수 없다.</li>
</ul>
<p>이런 HTTP 프로토콜의 특성 때문에 예를 들어 사용자가 로그인을 해야만 글을 CRUD를 할 수 있다고 할 때, 사용자는 매 요청을 보낼 때마다 로그인하여 자신임을 인증하여 권한을 부여 받아야 할 것이다. 이러한 불편함을 보완하기 위해 쿠키와 세션이 사용된다.</p>
<p>이제 쿠키와 세션을 통해 어떻게 인증과 인가를 구현할 수 있는지, 그리고 이를 지원하는 서버측 세션, 클라이언트측 쿠키, Bearer 토큰, JWT에 대해 알아보고자 한다.</p>
<hr />
<h3 id="쿠키-cookie">쿠키 (Cookie)</h3>
<p>쿠키는 클라이언트 측에서 관리되는 작은 정보 파일로, 서버가 사용자 브라우저(개발자 도구 → Application → Cookie Storage)로 전송하여 저장하고 브라우저는 이후 요청 시 데이터를 서버로 전송한다. 주로 인증 관련 정보를 담아 서버가 사용자의 상태를 식별할 수 있도록 돕는다.</p>
<p><strong>쿠키의 특징</strong></p>
<ul>
<li>만료 시간 설정 가능
쿠키는 만료 시간(<code>Expire</code> or <code>Max-Age</code> )을 설정해 특정 시간 후 자동으로 삭제되거나 브라우저 종료 시 삭제되도록 한다.</li>
<li>보안 설정
쿠키는 <code>HttpOnly</code> 옵션을 통해 자바스크립트 접근을 제한하고, <code>Secure</code> 옵션으로 HTTPS 연결에서만 전송되도록 설정할 수 있다.</li>
<li>크로스 사이트 속성
<code>SameSite</code> 속성을 통해 쿠키의 크로스 사이트 전송을 제어해 보안 위험을 줄일 수 있다.</li>
</ul>
<p>예를 들면 사용자가 로그인을 해서 서버가 해당 사용자의 인증 정보(아이디, 또는 토큰 등)를 쿠키에 저장하여 이후 요청에서도 인증된 상태를 유지한다.</p>
<p><strong>쿠키 옵션, Set Cookie 할 경우 설정할 수 있는 다양한 옵션</strong></p>
<ul>
<li><code>쿠키명-쿠키값</code>
기본적인 쿠키값이다.  myCookie=test 같이 쌍으로 설정한다.</li>
<li><code>Expires=날짜</code>
만료 기한으로, 이 기한이 지나면 쿠키가 제거된다. 기본값은 클라이언트가 종료될 때까지이다.</li>
<li><code>Max-Age=초</code>
Expire과 비슷하지만 날짜 대신 초를 입력할 수 있다. 해당 초가 지나면 쿠키가 제거된다. 
Expire보다 우선 순위가 높다.</li>
<li><code>Domain=도메인명</code>
쿠키가 전송될 도메인을 특정할 수 있다. 기본값은 현재 도메인이다. 프론트랑 백엔드랑 도메인이 다를 경우 반드시 설정을 해줘야 한다.</li>
<li><code>Path=URL</code>
쿠키가 전송될 URL을 특정할 수 있다. 기본값은 “/”이고, 
이 경우 모든 URL에서 쿠키를 전송할 수 있다.</li>
<li><code>Secure</code>
HTTPS일 경우에만 쿠키가 전송된다.</li>
<li><code>HttpOnly</code>
true로 설정할 경우, 자바스크립트에서 쿠키에 접근할 수 없다. 쿠키 조작, 해킹을 방지하기 위해 설정하는 것이 좋다.</li>
</ul>
<h3 id="세션-session">세션 (Session)</h3>
<p>쿠키의 정보는 노출되고 수정되는 위험이 있다. 그래서 쿠키와 세션을 같이 사용하는데, 중요한 정보는 서버에서 관리하고 클라이언트에서는 세션 키만 제공하는 방식을 사용한다. 
서버에서 세션 객체(session)을 생성 후, 고유한 키인 세션id를 생성한다.
이 세션 id는 클라이언트의 쿠키에 저장돼 이후 요청 때마다 쿠키가 서버로 전송되며, 서버는 이 세션id를 통해 사용자의 세션 데이터를 불러와서 로그인 상태 등의 인증 정보를 유지한다.</p>
<p><strong>세션의 특징</strong></p>
<ul>
<li><strong>서버 메모리 사용</strong>
세션 데이터는 서버 메모리에 저장되기 때문에 사용자 수가 증가할수록 서버에 부담이 된다. 이를 보완하기 위해 세션 스토리지에 세션 정보를 저장하는 방식을 사용하기도 한다.</li>
<li><strong>쿠키 기반 세션 id</strong>
세션 id는 주로 쿠키에 담겨 클라이언트에서 관리되며, 서버는 세션 id를 통해 해당 사용자의 세션 데이터를 불러온다.</li>
<li><strong>보안</strong>
세션 id는 민감한 정보를 포함하지 않으며, 세션 정보는 서버에 저장되므로 보안성이 높다.</li>
</ul>
<p><strong>세션 동작 방식</strong></p>
<ol>
<li>클라이언트가 서버에 접속할 때 <strong>세션 id를 발급</strong> 받는다.</li>
<li>클라이언트는 <strong>세션 id에 대해 쿠키에 저장</strong>하고 갖고 있는다.</li>
<li>클라이언트는 서버에 요청할 때, 해당 <strong>쿠키(세션 id가 들어있는)를 서버에 전달</strong>해서 요청한다.</li>
<li>서버는 세션 id를 전달 받아서 별다른 작업 없이 <strong>세션 id로 세션에 있는 클라이언트의 정보를 가져와서 사용</strong>한다.</li>
<li>클라이언트 정보를 가지고 서버 요청을 처리해 <strong>클라이언트에게 응답</strong>한다.</li>
</ol>
<p><strong>쿠키와 세션의 차이점</strong></p>
<table>
<thead>
<tr>
<th></th>
<th>쿠키(Cookie)</th>
<th>세션(Session)</th>
</tr>
</thead>
<tbody><tr>
<td><strong>저장 위치</strong></td>
<td>클라이언트 (브라우저)</td>
<td>서버</td>
</tr>
<tr>
<td><strong>만료 시점</strong></td>
<td>설정된 만료 시간에 따라 삭제 또는 브라우저가 닫힐 때 삭제</td>
<td>서버에서 관리하며, 일반적으로 사용자가 로그아웃하거나 세션 만료 시 삭제</td>
</tr>
<tr>
<td><strong>보안성</strong></td>
<td>쿠키는 클라이언트에 저장되므로 보안 위험이 있음. <code>HttpOnly</code> 및 <code>Secure</code> 옵션으로 제어 가능</td>
<td>민감한 정보를 서버에 저장하므로 비교적 안전함</td>
</tr>
<tr>
<td><strong>용도</strong></td>
<td>주로 간단한 사용자 정보 유지 (예: 로그인 정보 (인증 정보))</td>
<td>인증된 사용자 세션 관리 (예: 로그인 상태, 권한 정보 등)</td>
</tr>
</tbody></table>
<p>이렇게 보안면에서는 세션이 더 우수하다. 쿠키도 만료시간이 있지만 파일로 저장되기 때문에 브라우저를 종료해도 정보가 계속 남아있을 수 있다. 반면에 세션은 브라우저가 종료되면 만료시간에 상관없이 삭제된다.</p>
<p>그러나 사용자가 많아지게 되면 서버에 부담이 될 수 있고, 요청속도는 쿠키가 더 빠르기 때문에 쿠키가 많이 사용되지만, 쿠키에 민감한 사용자 정보를 저장할 경우 탈취, 악용의 위험성이 있어 데이터를 직접 쿠키에 저장하지 않고, 암호화된 토큰 형식으로 저장하는 방식을 사용한다. 특히 쿠키에는 주로 JWT를 많이 담아 보낸다. 
이 방법 외에도 자주 사용되는 Authorization Bearer 방식까지 살펴보며 쿠키와 Authorization의 차이점, JWT 구현 방법, JWT를 쿠키에 어떻게 저장하는지, 쿠키의 보안을 강화하는 방법에 대해 알아보자.</p>
<blockquote>
<p><strong>요약하자면</strong>, 
전통적인 방식이 서버에서 세션을 사용해서 생성한 세션id를 클라이언트의 쿠키에 저장하는 방식으로 토큰 관리를 하는 방식인데, <br />
세션이 서버 측에서 관리하는 것이기 때문에 매번 인증 처리 문제 같은 서버 측의 상태 관리 부담을 덜기 위해 서버에서 상태를 저장하지 않는 JWT를 쿠키에 담아 토큰을 관리하는 방식을 SPA에서는 많이 사용되고 있다.</p>
</blockquote>
<h3 id="authorization-bearer-방식">Authorization Bearer 방식</h3>
<p>Authorization 헤더는 HTTP 요청에서 인증 정보를 전달하는 표준 방식으로, Bearer 토큰 방식은 이 중에서도 가장 널리 사용되는 방식이며, JWT를 전달하는 데 주로 사용된다.</p>
<p>로컬 스토리지에 access token을 저장하고, 요청을 보낼 때 아래와 같이 헤더에 넣어서 사용한다.
이 방식을 사용하면 클라이언트가 토큰을 직접 관리하고, 서버는 매 요청에서 전달 받은 토큰을 통해 클라이언트를 검증한다.</p>
<pre><code class="language-jsx">// 예시 Authorization: Bearer &lt;token&gt;
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...</code></pre>
<p><strong>Authorization  Bearer 토큰의 특징</strong></p>
<ul>
<li>모든 HTTP 요청의 헤더에 토큰을 포함해야 한다.</li>
<li>쿠키와 다르게 브라우저가 자동으로 전송하지 않아 프론트에서 따로 처리를 해줘야 한다. 이는 CSRF 공격 방지에 유리하다.</li>
<li>주로 REST API나 SPA에서 사용된다.</li>
</ul>
<hr />
<h3 id="jwt-json-web-token">JWT (JSON Web Token)</h3>
<p><strong>JWT란?</strong></p>
<p>JWT는 JSON 형식의 데이터를 저장하는 토큰으로, API 요청을 인증하는 수단으로 활용된다.</p>
<p>이 토큰은 암호화가 안되고 4KB의 사이즈 제한이 있는 쿠키의 단점과, 서버 자원을 사용한다는 세션의 단점을 보완하여 토큰 변조가 불가능하고, 내용에 포함해서 전송하기 때문에 서버에서 DB 조회를 안해도 된다는 특징을 지닌다.</p>
<p><strong>[cookie를 이용한 로그인 방식]</strong></p>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/1c2dfdb6-e868-4382-8151-5012bd53eb56/image.png" /></p>
<p><strong>[session을 이용한 로그인 방식]</strong></p>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/6c0783a7-5174-4b57-bcc9-081a137f0d84/image.png" /></p>
<p><strong>[JWT를 이용한 로그인 방식]</strong></p>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/40f5809f-1b09-4edd-ac7f-cf68b904aea1/image.png" /></p>
<p><strong>JWT의 구조(Header, Payload, Signature)</strong></p>
<p>JWT는 점(.)으로 구분된 세 부분으로 구성된다. </p>
<ul>
<li><strong>Header(헤더)</strong>
토큰의 종류와 해시 알고리즘 정보가 들어있다.</li>
</ul>
<pre><code class="language-jsx">{
  &quot;alg&quot;: &quot;HS256&quot;,  // 서명 알고리즘
  &quot;typ&quot;: &quot;JWT&quot;     // 토큰 유형
}</code></pre>
<ul>
<li><strong>Payload(페이로드)</strong>
토큰의 내용물이 인코딩된 부분이다.</li>
</ul>
<pre><code class="language-jsx">{
  &quot;id&quot;: &quot;671f4814a357da705766a9a5&quot;,  // 사용자 고유 ID
  &quot;name&quot;: &quot;so356hot&quot;,   // 사용자 이름 (id)
  &quot;iat&quot;: 1516239022,    // 발행 시간
  &quot;exp&quot;: 1516242622     // 만료 시간
}</code></pre>
<ul>
<li><strong>Signature(서명)</strong>
인코딩된 Header와 Payload를 더한 뒤, secret Key로 해싱해서 생성되는 일련의 문자열로, secret Key를 이용해 복화화하여 토큰이 변조되었는의 여부를 확인할 수 있다.<ul>
<li>JWT 비밀키로 만들어지고, 이 비밀키가 노출되면 토큰 위조가 가능하다.</li>
<li>비밀키는 별도의 개발환경 (eg. env 파일) 안에서 관리해야 한다. (공개된 곳에 올라가지 않도록)</li>
</ul>
</li>
</ul>
<pre><code class="language-jsx">HMACSHA512(
  base64UrlEncode(header) + &quot;.&quot; +
  base64UrlEncode(payload),
  // 시크릿 키 들어가는 부분
)</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/ebf4e0a3-6fce-49ee-bcb8-9723222e9819/image.png" /></p>
<p><strong>JWT 작동 원리</strong></p>
<ol>
<li>사용자가 로그인을 하면 서버는 JWT를 생성하고 클라이언트에게 전달한다. </li>
<li>클라이언트는 서버로부터 받은 JWT를 저장한다. (로컬스토리지, 쿠키 등)</li>
<li>이후 요청 시 JWT를 함께 서버로 전송한다.</li>
<li>서버는 JWT 검증 후 요청을 처리한다.</li>
</ol>
<p><strong>JWT의 특징</strong></p>
<ul>
<li><strong>Stateless(무상태)</strong>
JWT는 서버 상태를 저장할 필요가 없는 Stateless이다. 이로 인해 서버 간 공유가 가능하여 확장성이 좋다.</li>
<li>다양한 환경에서의 활용
다양한 프로그래밍 언어에서 지원되며, 모바일 앱에서도 사용이 용이하다.</li>
<li>쿠키와 세션보다 더 많은 데이터를 포함할 수 있으며, 서버에서 DB 조회를 하지 않고도 클라이언트 정보를 알 수 있다.</li>
<li>그러나 토큰의 크기가 상대적으로 크고, 한 번 발급된 토큰은 만료 기간이 될 때까지 계속해서 유효하여 보안이 취약하며, 보안 취약점이 발생했을 때 모든 토큰을 무효화하기 어렵다.</li>
</ul>
<p>때문에 JWT를 Bearer 토큰 형식이나 Cookie에 담아 저장하는 방식이 사용되고 있다.</p>
<h3 id="jwt를-bearer과-쿠키에-활용하기">JWT를 Bearer과 쿠키에 활용하기</h3>
<p><strong>JWT를 Bearer Token 형식에 사용하기</strong></p>
<p>Bearer 토큰 방식은 HTTP Authorization 헤더를 사용해 JWT를 전송하는 방법이다. 클라이언트는 서버에 요청을 보낼 때 헤더에 JWT를 포함시켜 인증을 요청한다.</p>
<p><strong>JWT를 Bearer 토큰 형식에 사용했을 때의 장점</strong></p>
<ul>
<li><strong>CSRF 공격 방지</strong>
클라이언트가 직접 토큰을 관리하기 때문에 CSRF 공격에 대한 방어가 강화된다.</li>
<li><strong>사용법이 간단</strong>
JWT는 HTTP Authorization 헤더에 그냥 추가하여 요청을 보내면 되기 때문에 사용이 직관적이다.</li>
</ul>
<p><strong>JWT를 Bearer 토큰 형식에 사용했을 때의 단점</strong></p>
<ul>
<li><strong>보안 위험</strong>
Bearer 토큰이 URL이나 로컬 스토리지에 저장될 경우, XSS 공격에 취약할 수 있다.</li>
<li><strong>만료된 토큰 처리</strong>
만료된 토큰에 대한 처리가 복잡해질 수 있다. 클라이언트가 만료된 토큰을 가지고 요청을 보낼 경우, 
서버에서 이를 감지하고 에러 처리를 해야 한다.</li>
</ul>
<pre><code class="language-jsx">// 클라이언트 요청 예시
fetch('https://api.example.com/data', {
  headers: {
    'Authorization': `Bearer ${token}`
  }
});</code></pre>
<pre><code class="language-jsx">// 서버 측 검증 예시 (Node.js Express)
app.use((req, res, next) =&gt; {
  const authHeader = req.headers.authorization;
  if (!authHeader) return res.sendStatus(401); // Authorization 헤더가 없으면 401 Unauthorized

  const token = authHeader.split(' ')[1]; // 'Bearer ' 이후의 토큰 추출
  jwt.verify(token, process.env.JWT_SECRET, (err, user) =&gt; {
    if (err) return res.sendStatus(403); // 유효하지 않은 토큰이면 403 Forbidden
    req.user = user; // 요청 객체에 사용자 정보 추가
    next(); // 다음 미들웨어로 진행
  });
});</code></pre>
<p><strong>Cookie 저장 형식</strong></p>
<p>쿠키를 이용해 JWT를 저장하는 방식이다. JWT를 HTTPOnly 쿠키에 저장해 클라이언트의 자바스크립트에서 접근할 수 없게 함으로써 보안을 강화한다. </p>
<p><strong>JWT를 Cookie에 사용했을 때의 장점</strong></p>
<ul>
<li><strong>보안성</strong>
쿠키는 HttpOnly와 Secure 옵션을 설정해 클라이언트에서 자바스크립트로 접근할 수 없게 하고, HTTPS를 통해서만 전송되도록 하여 보안을 강화할 수 있다.</li>
<li><strong>자동 전송</strong>
브라우저가 자동으로 쿠키를 관리하기 때문에, 매번  Authorization 헤더에 토큰을 포함시킬 필요가 없다.</li>
<li><strong>세션 관리에 용이</strong>
서버에서 쿠키를 관리하기 때문에 유효한 세션을 쉽게 관리할 수 있다.</li>
</ul>
<p><strong>JWT를 Cookie에 사용했을 때의 단점</strong></p>
<ul>
<li><strong>CSRF 공격 위험</strong>
쿠키 방식은 CSRF 공격에 취약할 수 있다. 이를 방지하기 위해 SameSite 옵션을 설정해야 한다.</li>
<li><strong>서버 의존성</strong>
서버가 쿠키를 처리하기 때문에 서버 자원에 의존하게 된다. 또한, 쿠키의 크기 제한(약 4KB) 때문에 저장할 수 있는 정보에 제약이 있다.</li>
<li><strong>다양한 환경에서의 호환성</strong>
개발과 프로덕션 같이 환경에 따라 쿠키 설정이 다를 수 있기 때문에 적절한 설정이 필요하다.</li>
</ul>
<pre><code class="language-jsx">// JWT 토큰 생성
const payload = { id: userDoc._id, username: userDoc.username };
const token = jwt.sign(payload, secretKey, {
  expiresIn: TOKEN_EXPIRE_TIME, // 만료 시간 설정
});

// 쿠키 옵션 설정
const cookieOptions = {
  httpOnly: true, // 자바스크립트에서 접근 불가
  secure: process.env.NODE_ENV === 'production', // HTTPS에서만 전송
  sameSite: process.env.NODE_ENV === 'production' ? 'strict' : 'lax', // CSRF 방지
  maxAge: COOKIE_EXPIRE_TIME, // 쿠키 만료 시간 설정
  path: '/', // 쿠키가 유효한 경로
};

// 응답 전송
return res.cookie('token', token, cookieOptions).json({
  status: 200,
  success: true,
  message: '로그인 성공',
  successCode: 'LOGIN_SUCCESS',
  data: { id: userDoc._id, username: userDoc.username },
});</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/2009e632-da83-4e32-8762-04b6688eb489/image.png" /></p>
<p><strong>그 외의 쿠키를 사용할 때 고려해보면 좋을 사항</strong></p>
<ul>
<li><strong>만료 및 갱신</strong>
JWT는 만료 시간이 설정되어 있으므로, 클라이언트는 주기적으로 토큰을 갱신하는 로직을 구현해야 한다. Acecess Token의 만료 시간을 짧게 가져가고 Refresh Token을 사용하는 방식도 고려할 수 있다.</li>
<li><strong>서버 검증</strong>
매 요청 시 토큰의 유효성을 검증하여 불법적인 접근을 차단해야 한다. 유효하지 않은 토큰에 대해 401 Unauthorized 응답을 반환하는 것이 중요하다.</li>
</ul>
<hr />
<h3 id="요약">요약</h3>
<p><strong>인증과 인가의 기본 개념</strong></p>
<ul>
<li>인증(Authentication)은 사용자의 신원을 확인하는 과정이며, 인가(Authorization)는 인증된 사용자에게 특정 자원에 대한 접근 권한을 부여하는 과정이다⁠⁠</li>
<li>HTTP 프로토콜의 Connectionless, Stateless 특성으로 인해 쿠키와 세션이 사용된다⁠⁠</li>
</ul>
<p><strong>쿠키와 세션의 특징</strong></p>
<ul>
<li>쿠키는 클라이언트 측에서 관리되는 작은 정보 파일로, 만료 시간 설정과 보안 옵션 설정이 가능하다⁠⁠</li>
<li>세션은 서버 측에서 관리되며, 세션 ID를 통해 클라이언트의 상태를 유지한다⁠⁠</li>
<li>쿠키는 클라이언트에 저장되어 보안 위험이 있지만, 세션은 서버에 저장되어 비교적 안전하다⁠⁠</li>
</ul>
<p><strong>JWT와 Bearer 토큰</strong></p>
<ul>
<li>JWT는 JSON 형식의 데이터를 저장하는 토큰으로, Header, Payload, Signature로 구성된다⁠⁠</li>
<li>Bearer 토큰 방식은 HTTP Authorization 헤더를 사용해 JWT를 전송하는 방법으로, CSRF 공격 방지에 유리하다⁠⁠</li>
<li>JWT를 쿠키에 저장하면 HttpOnly와 Secure 옵션을 통해 보안을 강화할 수 있지만, CSRF 공격에 취약할 수 있다⁠</li>
</ul>
<hr />
<h3 id="참고-자료">참고 자료</h3>
<p><a href="https://www.okta.com/kr/identity-101/authentication-vs-authorization/">https://www.okta.com/kr/identity-101/authentication-vs-authorization/</a></p>
<p><a href="https://f-lab.kr/insight/cookie-vs-session">https://f-lab.kr/insight/cookie-vs-session</a></p>
<p><a href="https://jwt.io/">https://jwt.io/</a></p>
<p><a href="https://ko.javascript.info/cookie">https://ko.javascript.info/cookie</a></p>
