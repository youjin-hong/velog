# 📌 Velog 글 요약

| 항목   | 내용 |
|--------|------|
| **제목** | Javascript 정규 표현식 문법 정리 및 문제 풀어보기 |
| **날짜** | Fri, 08 Aug 2025 09:48:04 GMT |
| **링크** | [https://velog.io/@so356hot/Javascript-%EC%A0%95%EA%B7%9C-%ED%91%9C%ED%98%84%EC%8B%9D-%EB%AC%B8%EB%B2%95-%EC%A0%95%EB%A6%AC](https://velog.io/@so356hot/Javascript-%EC%A0%95%EA%B7%9C-%ED%91%9C%ED%98%84%EC%8B%9D-%EB%AC%B8%EB%B2%95-%EC%A0%95%EB%A6%AC) |

---

<p>리액트로 개발할 때에는 전화번호라던가, 비밀번호, 이메일 같은 유효성 검사를 걸 때 지원하는 라이브러리가 많기도 하고, 또 이걸 다 외울 필요는 없다고 생각해서 그때그때 검색해서 찾아쓰곤 했었는데요. 요즘 코딩테스트 문제를 풀면서 정규표현식으로도 풀 수 있는 문제가 많았는데 생긴 것부터 외계어처럼 복잡해보여 항상 다른 메서드나 방법으로 풀곤 했는데, 이번에 프로그래머스 코딩테스트 &quot;3개의 구분자&quot; 문제는 정규표현식으로 푸는 게 제일 직관적이고 깔끔했습니다. 그래서 그때그때 찾아서 쓰더라도 기본적인 개념을 알아야 좀 더 잘 활용할 수 있을 것 같아 이번 시간에는 정규 표현식이 무엇인지, 어떻게 쓰는지, 그리고 이 글을 쓰게 된 가장 큰 이유인 코딩테스트 문제를 마지막에 함께 풀어보는 시간을 가지려고 합니다. </p>
<h2 id="1-정규표현식이란">1. 정규표현식이란?</h2>
<h3 id="✔️-언제-쓰는-건가요">✔️ 언제 쓰는 건가요?</h3>
<p>공식문서에 따르면 정규표현식(정규식)은 <strong>문자열</strong>에서 특정 문자 조합을 찾기 위한 패턴이라고 합니다. </p>
<p>일상에서 웹사이트나 앱에서 로그인/회원가입이나, 개인 정보를 입력하는 동작을 할 때 많이 경험 하셨을 것 같습니다. 보편적으로 input에 전화번호를 입력하라고 했을 때 <code>00(0)-000(0)-0000</code> 형식을 지키지 않았을 때 양식에 맞게 올바르게 입력하라는 경고창이 바로 정규표현식에 필터링되어 걸리는 것입니다. </p>
<p>정규표현식은 대표적으로 아래와 같은 역할을 하며, </p>
<blockquote>
<ol>
<li>문자 검색(search)</li>
<li>문자 대체(replace)</li>
<li>문자 추출(extract)</li>
</ol>
</blockquote>
<p>실무에서 이런 상황에 자주 쓰입니다. </p>
<blockquote>
<p>📧 e-mail, 전화번호 형식 검증
🔍 특정 단어나 패턴 찾기
🔃 문자열 치환 (replace)
✂️ 문자열 나누기 (split)</p>
</blockquote>
<pre><code class="language-javascript">// 예시: 전화번호 형식인지 확인
const phonePattern = /^\d{3}-\d{4}-\d{4}$/;
phonePattern.test('010-1234-5678')  // true
phonePattern.test('전화번호 아님')    // false
phonePattern.test('01012345678')    // true</code></pre>
<br />

<h3 id="✔️-어떻게-만드나요-두-가지-방법">✔️ 어떻게 만드나요? (두 가지 방법)</h3>
<blockquote>
<p><strong>1) 정규 표현식 리터럴</strong>: 슬래시(/)로 패턴을 감싸서 작성합니다. </p>
</blockquote>
<pre><code class="language-javascript">const regex = /ab+c/;</code></pre>
<p>➡️<strong>바뀔 일이 없는 패턴</strong>의 경우에 적합 (∵리터럴 식은 스크립트를 불러올 때 컴파일)</p>
<blockquote>
<p><strong>2) <code>RegExp</code> 객체의 생성자 호출</strong></p>
</blockquote>
<pre><code class="language-javascript">const regex = new RegExp('ab+c');</code></pre>
<p>➡️<strong>바뀔 수 있는 패턴</strong> or <strong>사용자 입력 등 외부 출처에서 가져오는 패턴</strong>의 경우에 적합 
(∵생성자 함수는 식이 런타임에 컴파일)</p>
<hr />
<h2 id="2-정규식의-핵심-문법과-메타-문자">2. 정규식의 핵심 문법과 메타 문자</h2>
<h3 id="✔️-정규식-기본-구조">✔️ 정규식 기본 구조</h3>
<p>정규식의 기본적인 구조는 아래와 같습니다. 
슬래시(/)로 패턴을 감싸고, 필요한 경우 플래그를 추가하여 사용합니다. </p>
<blockquote>
<h3 id="patternflag"><code>/pattern/flag</code></h3>
</blockquote>
<ul>
<li><code>/</code>: 시작, 종료 기호</li>
<li><code>pattern</code>: 정규식 패턴</li>
<li><code>flag</code>: 고급 검색을 위한 설정 기능</li>
</ul>
<br />

<h3 id="✔️-주요-메타문자">✔️ 주요 메타문자</h3>
<p>정규 표현식에서 메타 문자는 문자열 검색이나 패턴 매칭을 도와주는데요. 일반적으로 많이 쓰이는 메타 문자는 다음과 같습니다. </p>
<ul>
<li><code>.</code>: 임의의 <strong>한 문자</strong>와 일치</li>
<li><code>^(캐럿)</code>: <strong>문자열의 시작 부분</strong>과 일치</li>
<li><code>$(달러)</code>: <strong>문자열의 끝 부분</strong>과 일치</li>
<li><code>*</code>: <strong>앞 문자가 0번 이상 반복</strong>되는 것과 일치</li>
<li><code>+</code>: <strong>앞 문자가 1번 이상 반복</strong>되는 것과 일치</li>
<li><code>?</code>: <strong>앞 문자가 0번 또는 1번 나타나는 것</strong>과 일치</li>
<li><code>{ }</code>: <strong>반복 횟수</strong>를 지정
eg. <code>{m, n}</code>은 <code>앞 문자 최소 m번, 최대 n번 반복</code></li>
<li><code>[ ]</code>: <strong>대괄호 안 문자 중 적어도 하나</strong> 일치</li>
<li><code>\(역슬래시)</code>: <strong>메타 문자의 의미를 해제</strong>
eg. <code>\.</code>은 마침표 문자와, <code>\\</code>는 백슬래시와 일치</li>
<li><code>|(파이프)</code>: <strong>OR</strong> 연산자를 나타냄</li>
<li><code>( )</code>: <strong>그룹</strong>을 정의</li>
</ul>
<hr />
<h2 id="3-문자-그룹-만들기">3. 문자 그룹 만들기</h2>
<p>제가 이 문자 그룹을 코딩 테스트에 사용하고 정규 표현식을 공부해야겠다고 생각한 바로 이 부분이기 때문에 조금 더 자세히 살펴보겠습니다. </p>
<h3 id="✔️-abc-이런-대괄호는-뭔가요">✔️ <code>[abc]</code> 이런 대괄호는 뭔가요?</h3>
<p>대괄호(<code>[ ]</code>) 안의 문자 중 <strong>하나라도 일치</strong>하면 매칭됩니다. </p>
<pre><code class="language-javascript">/[abc]/.test('apple');   // true (a가 있음)
/[abc]/.test('banana');  // true (a, b가 있음)
/[abc]/.test('mizzue');  // false (a, b, c가 없음)</code></pre>
<br />

<h3 id="✔️-a-z-0-9-범위로-지정하기">✔️ <code>[a-z]</code>, <code>[0-9]</code> 범위로 지정하기</h3>
<p>하이픈(<code>-</code>)으로 범위를 정할 수 있습니다. </p>
<pre><code class="language-javascript">/[a-z]/        // 소문자 a부터 z까지
/[A-Z]/        // 대문자 A부터 Z까지
/[0-9]/        // 숫자 0부터 9까지
/[a-zA-Z0-9]/  // 알파벳 + 숫자 조합

// 실제 사용 예시
/^[a-z]+$/.test(&quot;hello&quot;);  // true
/^[a-z]+$/.test(&quot;Hello&quot;);  // false (대문자 H 때문에)

// 숫자만 있는지 확인
/^[0-9]+$/.test(&quot;123&quot;);   // true
/^[0-9]+$/.test(&quot;12a3&quot;);  // false (a 때문에)</code></pre>
<br />

<h3 id="✔️-abc-제외하고-싶을-때">✔️ <code>[^abc]</code> 제외하고 싶을 때</h3>
<p>캐럿(<code>^</code>)을 대괄호 안의 맨 앞에 쓰면 <strong>&quot;~가 아닌&quot;</strong>의 의미가 됩니다. </p>
<pre><code class="language-javascript">/[^0-9]/   // 숫자가 아닌 문자
/[^a-z]/   // 소문자가 아닌 문자
/[^abc]/   // a, b, c가 아닌 문자</code></pre>
<br />

<h3 id="✔️-자주-쓰이는-단축-문자-클래스-d-w-s">✔️ 자주 쓰이는 단축 문자 클래스 (<code>\d</code>, <code>\w</code>, <code>\s</code>)</h3>
<p>자바스크립트에 여러 내장 메서드처럼 자주 쓰는 패턴들은 미리 만들어져 있습니다. </p>
<ul>
<li><code>\d</code>: 숫자 ( = <code>[0-9]</code>)</li>
<li><code>\D</code>: 숫자가 아닌 것 ( = <code>[^0-9]</code>)</li>
<li><code>\w</code>: 단어문자 (알파벳+숫자+<code>_</code>) ( = <code>[a-zA-Z0-9_]</code>)</li>
<li><code>\W</code>: 단어문자가 아닌 것 (알파벳+숫자+<code>_</code>) ( = <code>[^a-zA-Z0-9_]</code>)</li>
<li><code>\s</code>: 공백 문자(스페이스, 탭 등) ( = <code>[ \t\n\r]</code>)</li>
<li><code>\S</code>: 공백이 아닌 문자 ( = <code>[^ \t\n\r]</code>)</li>
</ul>
<pre><code class="language-javascript">// 자주 쓰는 예시로 살펴보기

// 숫자만 추출하기
&quot;가격: 15,000원&quot;.match(/\d+/g); // [&quot;15&quot;, &quot;000&quot;]

// 단어만 추출하기  
&quot;hello-world_123&quot;.match(/\w+/g); // [&quot;hello&quot;, &quot;world_123&quot;]

// 공백 제거하기
&quot;  hello   world  &quot;.replace(/\s+/g, &quot; &quot;); // &quot; hello world &quot;</code></pre>
<hr />
<h2 id="4-옵션-설정하기-플래그">4. 옵션 설정하기 (플래그)</h2>
<h3 id="✔️-주요-플래그">✔️ 주요 플래그</h3>
<blockquote>
<p><code>g</code> : 전체 찾기
<code>i</code> : 대소문자 무시
<code>m</code> : 여러 줄 모드</p>
</blockquote>
<h4 id="🌍-g-전체-찾기">🌍 <code>g</code>: 전체 찾기</h4>
<p><code>g</code> 플래그가 없으면 <strong>첫 번째만 찾고 끝</strong>납니다. </p>
<pre><code class="language-javascript">const text = &quot;apple banana apple&quot;;

// g 플래그 없음 - 첫 번째만 찾음
text.match(/apple/); // [&quot;apple&quot;] (첫 번째만)

// g 플래그 있음 - 전체 찾음  
text.match(/apple/g); // [&quot;apple&quot;, &quot;apple&quot;] (모두 찾음)</code></pre>
<br />

<h4 id="🔡i-대소문자-무시">🔡<code>i</code>: 대소문자 무시</h4>
<p>대소문자 구분 없이 찾고 싶을 때 사용합니다. </p>
<pre><code class="language-javascript">const text = &quot;Hello HELLO hello&quot;;

/hello/g.exec(text); // [&quot;hello&quot;] (마지막 것만)
/hello/gi.exec(text); // [&quot;Hello&quot;, &quot;HELLO&quot;, &quot;hello&quot;] (모두)</code></pre>
<br />

<h4 id="🗒️m-여러-줄-모드">🗒️<code>m</code>: 여러 줄 모드</h4>
<p>캐럿(<code>^</code>)과 달러(<code>$</code>)가 각 줄의 시작/끝을 의미합니다. </p>
<pre><code class="language-javascript">const multiLine = `첫 번째 줄
두 번째 줄  
세 번째 줄`;

// m 플래그 없음
/^두/.test(multiLine); // false

// m 플래그 있음
/^두/m.test(multiLine); // true</code></pre>
<h4 id="🔧-기타-옵션들-s-u-y">🔧 기타 옵션들 (s, u, y)</h4>
<ul>
<li><code>s</code>: <code>.</code>이 개행문자(<code>\n</code>)도 매칭하게 함</li>
<li><code>u</code>: 유니코드 모드 (이모지 등 처리)</li>
<li><code>y</code>: 그 숫자와 일치하는 index 문자만 검색</li>
</ul>
<hr />
<h2 id="5-javascript에서-사용하는-방법">5. JavaScript에서 사용하는 방법</h2>
<h3 id="✔️-리터럴-메서드-match-search-replace-split">✔️ 리터럴 메서드: <code>match</code>, <code>search</code>, <code>replace</code>, <code>split</code></h3>
<h4 id="📌-match---찾기">📌 match() - 찾기</h4>
<pre><code class="language-javascript">const text = &quot;전화번호: 010-1234-5678, 02-9876-5432&quot;;

// 전화번호 패턴 찾기
text.match(/\d{2,3}-\d{3,4}-\d{4}/g);
// [&quot;010-1234-5678&quot;, &quot;02-9876-5432&quot;]</code></pre>
<br />

<h4 id="🚩-search---위치-찾기">🚩 search() - 위치 찾기</h4>
<pre><code class="language-javascript">&quot;hello world&quot;.search(/world/); // 6 (인덱스 반환)
&quot;hello world&quot;.search(/xyz/); // -1 (없으면 -1)</code></pre>
<br />

<h4 id="🔃-replace---바꾸기">🔃 replace() - 바꾸기</h4>
<pre><code class="language-javascript">
// 모든 숫자를 *로 바꾸기
&quot;abc123def456&quot;.replace(/\d/g, &quot;*&quot;); // &quot;abc***def***&quot;

// 전화번호 형식 바꾸기
&quot;010-1234-5678&quot;.replace(/(\d{3})-(\d{4})-(\d{4})/, &quot;$1.$2.$3&quot;);
// &quot;010.1234.5678&quot;</code></pre>
<br />

<h4 id="✂️-split---나누기">✂️ split() - 나누기</h4>
<pre><code class="language-javascript">// 여러 구분자로 나누기
&quot;사과,바나나;오렌지:포도&quot;.split(/[,:;]/);
// [&quot;사과&quot;, &quot;바나나&quot;, &quot;오렌지&quot;, &quot;포도&quot;]</code></pre>
<br />

<h3 id="✔️-regexp-메서드-test-exec">✔️ <code>RegExp</code> 메서드: <code>test</code>, <code>exec</code></h3>
<h4 id="✅-test---있는지-확인">✅ test() - 있는지 확인</h4>
<pre><code class="language-javascript">const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

emailPattern.test(&quot;user@example.com&quot;); // true
emailPattern.test(&quot;잘못된이메일&quot;); // false</code></pre>
<br />

<h4 id="🔬-exec---자세한-정보">🔬 exec() - 자세한 정보</h4>
<pre><code class="language-javascript">const pattern = /(\d{4})-(\d{2})-(\d{2})/;
const result = pattern.exec(&quot;오늘은 2024-03-15입니다&quot;);

console.log(result[0]); // &quot;2024-03-15&quot; (전체 매칭)
console.log(result[1]); // &quot;2024&quot; (첫 번째 그룹)
console.log(result[2]); // &quot;03&quot; (두 번째 그룹)
console.log(result[3]); // &quot;15&quot; (세 번째 그룹)</code></pre>
<br />

<h3 id="✔️-각각-언제-쓰면-좋을까요">✔️ 각각 언제 쓰면 좋을까요?</h3>
<table>
<thead>
<tr>
<th align="left">메서드</th>
<th align="left">용도</th>
<th align="left">반환값</th>
</tr>
</thead>
<tbody><tr>
<td align="left"><code>test()</code></td>
<td align="left">패턴 존재 여부 확인</td>
<td align="left"><code>true</code> 또는 <code>false</code></td>
</tr>
<tr>
<td align="left"><code>match()</code></td>
<td align="left">매칭된 모든 내용을 배열로 반환</td>
<td align="left">매칭된 문자열 배열 또는 <code>null</code></td>
</tr>
<tr>
<td align="left"><code>search()</code></td>
<td align="left">매칭된 부분의 시작 인덱스 반환</td>
<td align="left">인덱스(숫자) 또는 <code>-1</code></td>
</tr>
<tr>
<td align="left"><code>replace()</code></td>
<td align="left">매칭된 부분을 새로운 문자열로 교체</td>
<td align="left">새로운 문자열</td>
</tr>
<tr>
<td align="left"><code>split()</code></td>
<td align="left">정규식을 구분자로 사용하여 문자열 분리</td>
<td align="left">나뉜 문자열의 배열</td>
</tr>
</tbody></table>
<hr />
<h2 id="6-코딩테스트-문제로-배워보기">6. 코딩테스트 문제로 배워보기</h2>
<h4 id="✔️-프로그래머스-코딩테스트-level-0-3개의-구분자">✔️ [프로그래머스 코딩테스트] level 0. 3개의 구분자</h4>
<pre><code>[문제 설명]
임의의 문자열이 주어졌을 때 문자 &quot;a&quot;, &quot;b&quot;, &quot;c&quot;를 구분자로 사용해 문자열을 나누고자 합니다.

예를 들어 주어진 문자열이 &quot;baconlettucetomato&quot;라면 나눠진 문자열 목록은 [&quot;onlettu&quot;, &quot;etom&quot;, &quot;to&quot;] 가 됩니다.

문자열 myStr이 주어졌을 때 위 예시와 같이 &quot;a&quot;, &quot;b&quot;, &quot;c&quot;를 사용해 나눠진 문자열을 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

단, 두 구분자 사이에 다른 문자가 없을 경우에는 아무것도 저장하지 않으며, return할 배열이 빈 배열이라면 [&quot;EMPTY&quot;]를 return 합니다.</code></pre><p>이 문제를 정규 표현식으로 풀어보겠습니다. </p>
<pre><code class="language-javascript">// [풀이]

// [abc]: a, b, c 중 하나를 구분자로 사용하여 a, b, c가 적어도 한 번 등작하면 매칭
// filter로 빈 문자열 제거
// 결과가 없으면 ['EMPTY'] 반환
function solution(myStr) {
    const result = myStr.split(/[abc]/).filter((str) =&gt; str !== '')

    return result.length === 0 ? ['EMPTY'] : result
}</code></pre>
