# 📌 Velog 글 요약

| 항목   | 내용 |
|--------|------|
| **제목** | 프로그래머스 "로그인 성공?" 문제로 익히는 Javascript Map 객체 활용법 |
| **날짜** | Thu, 11 Sep 2025 09:39:02 GMT |
| **링크** | [https://velog.io/@so356hot/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EC%84%B1%EA%B3%B5-%EB%AC%B8%EC%A0%9C%EB%A1%9C-%EC%9D%B5%ED%9E%88%EB%8A%94-Javascript-Map-%EA%B0%9D%EC%B2%B4-%ED%99%9C%EC%9A%A9%EB%B2%95](https://velog.io/@so356hot/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EC%84%B1%EA%B3%B5-%EB%AC%B8%EC%A0%9C%EB%A1%9C-%EC%9D%B5%ED%9E%88%EB%8A%94-Javascript-Map-%EA%B0%9D%EC%B2%B4-%ED%99%9C%EC%9A%A9%EB%B2%95) |

---

<h3 id="span-stylebackground-colorlavender1-문제-상황span"><span style="background-color: lavender;">1. 문제 상황</span></h3>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/8c5077a7-b161-4669-b0f1-4753b938c604/image.png" /></p>
<p>프로그래머스 코딩테스트 lv.0 문제 중, 정답률 78%인 무난한 문제이다. 계속 정답률 89%인 문제들만 쭉 풀다가 갑자기 78%인 문제를 보니 살짝 어렵다고 느껴져서 시간을 평소보다 더 쏟았던 것 같다. 고민 끝에 <code>find()</code> 라는 자바스크립트 내장 메서드를 이용해 <code>db</code> 2차원 배열 안의 원소(배열)의 첫 번째 인덱스와 <code>id_pw</code>라는 배열의 첫번째 인덱스가 같은 것을 찾아내어 변수에 담은 다음, 조건문을 통해 값을 return 하도록 작성하였다. </p>
<pre><code class="language-javascript">// find를 이용한 풀이
function solution(id_pw, db) {
  const user = db.find((item) =&gt; item[0] === id_pw[0]);

  if (!user) return &quot;fail&quot;;

  if (user[1] === id_pw[1]) {
    return &quot;login&quot;;
  } else {
    return &quot;wrong pw&quot;;
  }
}</code></pre>
<p>그러나, 다른 사람이 푼 풀이 중에 <code>Map</code>을 이용한 풀이가 있었는데 성능/가독성/확장성 면에서 모두 더 효율적인 풀이 같아 <code>Map</code>이라는 자바스크립트 자료형에 대해 알아보려고 한다. </p>
<pre><code class="language-javascript">// Map을 활용한 풀이
function solution(id_pw, db) {
  const [id, pw] = id_pw;
  const map = new Map(db);
  return map.has(id) ? (map.get(id) === pw ? &quot;login&quot; : &quot;wrong pw&quot;) : &quot;fail&quot;;
}</code></pre>
<br />

<h3 id="span-stylebackground-colorlavender2-map이란span"><span style="background-color: lavender;">2. Map이란?</span></h3>
<p>자바스크립트에는 두 가지 자료구조, <strong>배열</strong>과 <strong>객체</strong>가 있다. 하지만 이 두 자료구조만으로는 표현의 한계가 있기 때문에 자바스크립트에서는 특별한 객체인 <strong>Map</strong>을 추가적으로 지원하고 있다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/4a44c890-2cbc-4fce-bdb1-1516d7b74f5f/image.png" /></p>
<p>Map의 type이 Object로 출력이 되기 때문에 &quot;그냥 객체 아니야?&quot;라고 생각할 수 있지만 Map이 <strong>특별한 객체</strong>라고 한 데에는 이유가 있다. </p>
<p>일반 객체와 Map 둘 다 <code>key</code>와 <code>value</code>의 쌍으로 데이터를 저장하는 자료구조이다. 
그러나 일반 객체의 <code>key</code>는 <code>string</code> 또는 <code>Symbol</code>의 타입만 가질 수 있는 반면, 
Map의 <code>key</code>는 자료형을 허용하기 때문에 <code>string</code>, <code>Symbol</code> 뿐만 아니라 모든 자료형을 허용하여 객체, 배열 등 모든 데이터 타입이 허용된다. </p>
<p>그래서 Map을 특별한 객체라고 부르는 것이다. </p>
<table>
<thead>
<tr>
<th>특징</th>
<th>일반 객체 <code>{}</code></th>
<th>Map</th>
</tr>
</thead>
<tbody><tr>
<td><strong>키 타입</strong></td>
<td>string, Symbol만</td>
<td>모든 데이터 타입</td>
</tr>
<tr>
<td><strong>크기 확인</strong></td>
<td><code>Object.keys(obj).length</code></td>
<td><code>map.size</code></td>
</tr>
<tr>
<td><strong>순서 보장</strong></td>
<td>ES2015(ES6)부터 보장</td>
<td>항상 보장</td>
</tr>
<tr>
<td><strong>반복(순회)</strong></td>
<td><code>for...in</code>, <code>Object.keys()</code></td>
<td><code>for...of</code>, <code>forEach()</code></td>
</tr>
<tr>
<td><strong>성능</strong></td>
<td>작은 데이터에 적합</td>
<td>빈번한 추가/삭제에 최적화</td>
</tr>
<tr>
<td><strong>JSON 변환</strong></td>
<td><code>JSON.stringify()</code> 지원</td>
<td>직접 변환 불가</td>
</tr>
</tbody></table>
<br />

<h3 id="span-stylebackground-colorlavender3-객체-vs-map-성능-비교span"><span style="background-color: lavender;">3. 객체 vs Map 성능 비교</span></h3>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/52e516f4-6625-4c5c-9781-32e61942e7e3/image.png" />
<img alt="" src="https://velog.velcdn.com/images/so356hot/post/28c01db8-75a5-4649-a79f-ff6b4240b3c5/image.png" /></p>
<p>위의 사진은 일반 객체(Object)와 Map의 성능비교를 위해 javascript 코드를 작성하고 보기좋게 표로 만든 html을 캡쳐한 것이다. </p>
<p>삽입, 조회, 삭제, 순회, 크기 확인 전반적인 측면에서 Map이 성능이 좋은 것을 확인할 수 있다.
그 중에서도 특히 <strong>삭제</strong>와 <strong>크기 확인</strong>에서 Map의 압도적인 성능을 볼 수 있다. </p>
<br />

<h3 id="span-stylebackground-colorlavender4-map-전용-메서드들span"><span style="background-color: lavender;">4. Map 전용 메서드들</span></h3>
<p>Map도 type이 Obeject이기 때문에 아래 사진의 결과와 같이 일반 객체처럼 사용할 순 있다. 
<img alt="" src="https://velog.velcdn.com/images/so356hot/post/3bd98193-f0f0-45f0-90ba-0e35466f7be6/image.png" /></p>
<p>그러나, 이것은 Map을 사용하는 의미도 없을 뿐더러 여러 제약에 걸릴 수 있기 때문에 값을 추가/삭제/재할당/조회 등의 연산을 할 때에는 Map의 전용 메서드들을 사용해야 한다. </p>
<p>다음은 Map의 전용 메서드들이다. </p>
<h4 id="🟢-new-map">🟢 new Map()</h4>
<p>생성자를 이용해 Map 객체를 만드는 메서드이다. </p>
<pre><code class="language-javascript">let map = new Map();</code></pre>
<h4 id="🟢-mapsetkey-value">🟢 map.set(key, value)</h4>
<p>key를 이용해 값을 저장하는 메서드이다. </p>
<pre><code class="language-javascript">let map = new Map();

map.set('Map은', '특별한 객체');</code></pre>
<h4 id="🟢-mapgetkey">🟢 map.get(key)</h4>
<p>key에 해당하는 value를 반환한다. 
이때 key가 존재하지 않으면 undefined를 반환한다. </p>
<pre><code class="language-javascript">let map = new Map();

map.set('Map은', '특별한 객체');

map.get('Map은');   // '특별한 객체'
map.get('Map은~?'); // undefined</code></pre>
<h4 id="🟢-maphaskey">🟢 map.has(key)</h4>
<p>key가 존재하면 true, 존재하지 않으면 false를 반환한다. </p>
<pre><code class="language-javascript">let map = new Map();

map.set('Map은', '특별한 객체');

map.has('Map은');   // true
map.has('Map은~?'); // false</code></pre>
<h4 id="🟢-mapdeletekey">🟢 map.delete(key)</h4>
<p>key에 해당하는 요소를 삭제한다. </p>
<pre><code class="language-javascript">let map = new Map();

map.set('Map은', '특별한 객체');

map.delete('Map은');   // true

console.log(map); // Map(0) {size: 0}</code></pre>
<h4 id="🟢-mapclear">🟢 map.clear()</h4>
<p>맵 안의 모든 요소를 삭제한다. </p>
<pre><code class="language-javascript">let map = new Map();

map.set('가', '나디는 귀여워');
map.set(123, '4567');
map.set({name: 'hong'}, 'jinnie');

console.log(map);  // Map(3) {'가' =&gt; '나디는 귀여워', 123 =&gt; '4567', {…} =&gt; 'jinnie'}

map.clear();

console.log(map); // Map(0) {size: 0}</code></pre>
<h4 id="🟢-mapsize">🟢 map.size</h4>
<p>요소의 개수를 반환한다. 
참고로 size는 메서드가 아닌 프로퍼티이기 때문에 map.size()로 메서드처럼 쓰게 되면 TypeError가 발생한다. 따라서 map.size로 올바르게 써줘야 한다. </p>
<pre><code class="language-javascript">let map = new Map();

map.set('가', '나디는 귀여워');
map.set(123, '4567');
map.set({name: 'hong'}, 'jinnie');

map.size  // 3</code></pre>
<br />

<h3 id="span-stylebackground-colorlavender5-로그인-성공-문제-풀이-분석span"><span style="background-color: lavender;">5. &quot;로그인 성공?&quot; 문제 풀이 분석</span></h3>
<p>이렇게 간단히 Map에 대해서 알아보았다. 그럼 다시 돌아와서 &quot;로그인 성공?&quot; 문제를 Map으로 풀어보며 풀이를 분석해보자. </p>
<p><strong>문제 ⬇️</strong>
<img alt="" src="https://velog.velcdn.com/images/so356hot/post/8c5077a7-b161-4669-b0f1-4753b938c604/image.png" /></p>
<p><strong>전체 풀이 ⬇️</strong></p>
<pre><code class="language-javascript">// Map을 활용한 풀이
function solution(id_pw, db) {
  const [id, pw] = id_pw;
  const map = new Map(db);
  return map.has(id) ? (map.get(id) === pw ? &quot;login&quot; : &quot;wrong pw&quot;) : &quot;fail&quot;;
}</code></pre>
<p><strong>한 줄씩 풀이 분석하기 ⬇️</strong></p>
<blockquote>
<ul>
<li>id_pw는 2개의 원소가 들어있는 배열이다. 따라서 구조분해할당을 통해 배열의 첫번째 원소는 <code>id</code>, 두번째 원소는 <code>pw</code>로 사용한다는 뜻이다. </li>
</ul>
</blockquote>
<pre><code class="language-javascript">const [id, pw] = id_pw;</code></pre>
<blockquote>
<ul>
<li>Map 생성자에 2차원 배열 <code>db</code>를 전달하여 Map 객체를 생성한다. 이때 <code>db</code>의 각 배열 요소 <code>[key, value]</code>가 자동으로 키-값 쌍으로 변환된다. 이러한 map을 콘솔에 찍어보면 아래와 같이 출력된다.  </li>
</ul>
</blockquote>
<pre><code class="language-javascript">  const map = new Map(db);</code></pre>
<pre><code class="language-bash">// 결과
Map(3) {
  'programmer02' =&gt; '111111',
  'programmer00' =&gt; '134',
  'programmer01' =&gt; '1145'
}</code></pre>
<blockquote>
<ul>
<li>로직 순서대로 설명:</li>
</ul>
</blockquote>
<ul>
<li><code>map.has(id)</code>: <code>map.has(key)</code> 메서드를 이용해 입력받은 <code>id</code>가 Map에 존재하는지 확인</li>
<li>존재하면: <code>map.get(key)</code> 메서드를 이용해 <code>map.get(id) === pw</code>로 비밀번호 일치 여부 확인<ul>
<li>일치하면 &quot;login&quot; 반환</li>
<li>불일치하면 &quot;wrong pw&quot; 반환  </li>
</ul>
</li>
<li>존재하지 않으면: &quot;fail&quot; 반환<pre><code class="language-javascript">return map.has(id) ? (map.get(id) === pw ? &quot;login&quot; : &quot;wrong pw&quot;) : &quot;fail&quot;;</code></pre>
</li>
</ul>
<br />

<h3 id="span-stylebackground-colorlavender회고span"><span style="background-color: lavender;">회고</span></h3>
<p>코딩테스트 문제를 풀기 시작한지 얼마 안되긴 했지만, 그동안 여러 풀이들에서 Map 객체를 이용한 풀이를 볼 수 있었다. 하지만 Map은 뭐 당연히 객체이겠거니...정도만 생각하고 정확히 뭔지, 어떻게 동작하는지 알지 못했고 Map이 뭔질 모르니 당연하게도(?) 일반 객체의 key에는 문자열이나 Symbol만 올 수 있다는 사실도 정확하게 인지하지 못하고 있었다. 그러다보니 문제를 풀 때 Map은 커녕 일반 객체도 이용하기가 두려워져 항상 배열로만 풀었고, Map을 볼 때마다 처음 보는 <code>has()</code>, <code>set()</code>, <code>get()</code>, <code>delete()</code> 등의 메서드를 보면 덜컥 겁이 났다. 그러다 마음 먹고 Map에 대해 공부를 해보니 이렇게 편하고 성능 좋은 객체가 또 있나하는 생각이 들었다. Map이 일반 객체보다 전반적으로 성능이 좋다고 해서 Map을 남발하면 또 안되겠지만, 데이터 크기가 크고, 수정이 잦은 데이터에서는 일반 객체보다 Map이 더 효율적이지 않을까?라는 생각이 들었다. 앞으로 문제를 풀 때 Map을 활용해볼 일이 생긴다면 적극적으로 Map을 사용해봐야겠다. </p>
