# 📌 Velog 글 요약

| 항목   | 내용 |
|--------|------|
| **제목** | Javascript 나머지 연산자(%) 활용법: 프로그래머스 공 던지기 순환 배열로 풀기 |
| **날짜** | Sun, 31 Aug 2025 13:53:52 GMT |
| **링크** | [https://velog.io/@so356hot/Javascript-%EB%82%98%EB%A8%B8%EC%A7%80-%EC%97%B0%EC%82%B0%EC%9E%90-%ED%99%9C%EC%9A%A9%EB%B2%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B3%B5-%EB%8D%98%EC%A7%80%EA%B8%B0-%EB%AC%B8%EC%A0%9C%EB%A1%9C-%EB%B0%B0%EC%9A%B0%EB%8A%94-%EC%88%9C%ED%99%98-%EB%B0%B0%EC%97%B4-%ED%8C%A8%ED%84%B4](https://velog.io/@so356hot/Javascript-%EB%82%98%EB%A8%B8%EC%A7%80-%EC%97%B0%EC%82%B0%EC%9E%90-%ED%99%9C%EC%9A%A9%EB%B2%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B3%B5-%EB%8D%98%EC%A7%80%EA%B8%B0-%EB%AC%B8%EC%A0%9C%EB%A1%9C-%EB%B0%B0%EC%9A%B0%EB%8A%94-%EC%88%9C%ED%99%98-%EB%B0%B0%EC%97%B4-%ED%8C%A8%ED%84%B4) |

---

<h2 id="🚀-들어가며">🚀 들어가며</h2>
<p>프로그래머스 &quot;공 던지기&quot; 문제를 풀면서 주어진 배열을 순환시켜 풀고 싶은데, 어떻게 풀어야할까 하며 reduce, map, while문 등 내가 아는 지식을 총동원 해보았지만 모든 테스트 케이스를 충족시키진 못했다. 그래서 결국 다른 사람들이 푼 해답 코드를 보았는데 의외로 간단했다. 바로 <strong>&quot;나머지 연산(remainder)&quot;</strong>을 사용하는 것이었다. 나머지 연산은 짝수/홀수 구할 때나 약수 구할 때 주로 사용해보았는데, 순환 배열을 만들 때도 사용할 수 있다는 걸 처음 알게 되었고 이 개념은 이 문제 뿐 아니라 배열 회전, 순환 큐, 링크드 리스트 등 여러 알고리즘 문제에서도 다뤄지는 개념인 것 같아 기본 개념이지만 제대로 이해하고 쓰고자 오늘은 나머지 연산자에 대해 다뤄보려고 한다. 다른 언어에서는 이 풀이를 <strong>&quot;모듈러(modulo)연산&quot;</strong> 이라고 하는데 이 차이는 마지막에 간단히 살펴보도록 하겠다. </p>
<br />

<h2 id="🌱-나머지-연산자의-기본-개념">🌱 나머지 연산자(%)의 기본 개념</h2>
<h3 id="span-stylebackground-colorffe6e6나머지-연산이란span"><span style="background-color: #FFE6E6;">나머지 연산이란?</span></h3>
<p>나머지 연산은 왼쪽 피연산자를 오른쪽 피 연산자로 나눴을 때의 나머지를 구한다. <strong>부호는 항상 왼쪽 피연산자의 부호를 따른다.</strong> </p>
<p>$$
x ;% ; y
$$</p>
<h3 id="span-stylebackground-colorffe6e6나머지-연산의-수학적-원리span"><span style="background-color: #FFE6E6;">나머지 연산의 수학적 원리</span></h3>
<p>자바스크립트의 나머지 연산자는 &quot;remainder operator&quot;라고 하며, <code>%</code> 기호로 나타내지만, <strong>비율</strong>을 나타내는 퍼센트와는 관련이 없다. 바로 위에서도 언급했지만 표현식 <code>x % y</code>는 <code>x</code>를 <code>y</code>로 나눈 후 <strong>그 나머지(remainder)</strong>를 <strong>정수</strong>로 반환해주는 것이다. 이 때 반환값은 왼쪽 피연산자의 부호를 따르는 데 이는 모듈러 연산의 차이를 이해하는 데 필요하니 기억해두자. </p>
<p>이해하기 쉽게 코드로 살펴보자.</p>
<pre><code class="language-javascript">// 왼쪽 피연산자가 양수일 때
let 왼쪽_피연산자 = 14;
let 오른쪽_피연산자 = 3;

let 나머지 = 왼쪽_피연산자 % 오른쪽_피연산자;
console.log(나머지); // 출력: 2</code></pre>
<pre><code class="language-javascript">// 왼쪽 피연산자가 음수일 때
let 왼쪽_피연산자 = -14;
let 오른쪽_피연산자 = 3;

let 나머지 = 왼쪽_피연산자 % 오른쪽_피연산자;
console.log(나머지); // 출력: -2</code></pre>
<pre><code class="language-javascript">console.log(13 % 5);   // 3
console.log(13 % -5);  // 3

console.log(-13 % 5);  // -3
console.log(-13 % -5);  // -3</code></pre>
<br />

<h2 id="📝-간단한-사용법과-예시">📝 간단한 사용법과 예시</h2>
<h3 id="span-stylebackground-colorffe6e6홀수짝수-판별span"><span style="background-color: #FFE6E6;">홀수/짝수 판별</span></h3>
<pre><code class="language-javascript">function isEven(num) {
  return num % 2 === 0;
}

function isOdd(num) {
  return num % 2 === 1;
}

console.log(isEven(4)); // true
console.log(isEven(5)); // false
console.log(isOdd(7));  // true</code></pre>
<h3 id="span-stylebackground-colorffe6e6배열-인덱스-순환하기span"><span style="background-color: #FFE6E6;">배열 인덱스 순환하기</span></h3>
<pre><code class="language-javascript">const colors = ['red', 'blue', 'green'];

function getColor(index) {
  return colors[index % colors.length];
}

console.log(getColor(0)); // 'red' (0 % 3 = 0)
console.log(getColor(1)); // 'blue' (1 % 3 = 1)
console.log(getColor(2)); // 'green' (2 % 3 = 2)
console.log(getColor(3)); // 'red' (3 % 3 = 0)
console.log(getColor(4)); // 'blue' (4 % 3 = 1)</code></pre>
<h3 id="span-stylebackground-colorffe6e6기본-패턴-익히기span"><span style="background-color: #FFE6E6;">기본 패턴 익히기</span></h3>
<pre><code class="language-javascript">// 1. 특정 배수마다 실행
for(let i = 1; i &lt;= 20; i++) {
  if (i % 5 === 0) {
    console.log(`${i}는 5의 배수입니다.`);
  }
}
// 결과: 5, 10, 15, 20에서만 출력

// 2. 그룹 나누기
const students = ['서은광', '이민혁', '이창섭', '임현식', '프니엘', '육성재'];
const groups = [[], [], []]; // 3개 그룹

students.forEach((student, index) =&gt; {
  const groupIndex = index % 3;
  groups[groupIndex].push(student);
});

console.log(groups); 
// 결과: [['서은광', '이민혁'], ['이창섭', '임현식'], ['프니엘', '육성재']]

// 3. 시간 계산
function convertMinutes(totalMinutes) {
  const hours = Math.floor(totalMinutes / 60);
  const minutes = totalMinutes % 60;
  return `${hours}시간 ${minutes}분`;
}

console.log(convertMinutes(150)); // 2시간 30분
console.log(convertMinutes(75)); // 1시간 15분</code></pre>
<br />

<h2 id="🧩-프로그래머스-공-던지기-문제-풀이">🧩 프로그래머스 &quot;공 던지기&quot; 문제 풀이</h2>
<h3 id="span-stylebackground-colorffe6e6문제-설명--요구-사항span"><span style="background-color: #FFE6E6;">문제 설명 &amp; 요구 사항</span></h3>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/1b8348e9-9b4c-460a-8e42-c493ebe00ccd/image.png" /></p>
<h3 id="span-stylebackground-colorffe6e6어떻게-접근해야-할까span"><span style="background-color: #FFE6E6;">어떻게 접근해야 할까?</span></h3>
<blockquote>
<p>🔍 <strong>문제 분석</strong></p>
</blockquote>
<ul>
<li>동그랗게 서 있음 → 순환 배열</li>
<li>오른쪽으로 한 명 건너뛰기 → 매번 2칸씩 이동</li>
<li>k번째 던지는 사람 → k번 반복</li>
</ul>
<p><strong>※ 테스트 케이스로 이해하기</strong></p>
<pre><code class="language-javascript">[1, 2, 3, 4] 배열에서 k=2일 때:
- 시작: 1번 (인덱스 0)
- 첫 번째: 1 → 3번 (0에서 2칸 이동 → 인덱스 2)
- 두 번째: 3 → 1번 (2에서 2칸 이동 → 인덱스 4, 🔴 하지만 이 때 4는 배열 크기 초과)</code></pre>
<h3 id="span-stylebackground-colorffe6e6순환-구조의-아이디어span"><span style="background-color: #FFE6E6;">순환 구조의 아이디어</span></h3>
<p>계속 배열 인덱스를 순환시키기 위해 <strong>나머지 연산(%)</strong>을 이용하는 것이다. </p>
<pre><code class="language-javascript">// 🔴 인덱스 4는 배열 크기 4를 넘어감
// 4 % 4 = 0 → 다시 인덱스 0으로 돌아가는 것을 이용

인덱스 0: 1번 → 인덱스 2: 3번 → 인덱스 0: 1번 (🟢순환!)</code></pre>
<blockquote>
<p><strong>※ 규칙 찾기</strong></p>
</blockquote>
<ul>
<li>k번째로 던지려면 <code>(k-1) x 2</code>칸 이동해야 함</li>
<li>배열 크기를 넘으면 <code>% numbers.length</code>로 순환</li>
<li>최종 공식: <code>((k-1)x2 % numbers.length</code></li>
</ul>
<br />

<h2 id="✅-문제-해결-코드--풀이">✅ 문제 해결 코드 &amp; 풀이</h2>
<h3 id="span-stylebackground-colorffe6e6단계별-풀이-과정span"><span style="background-color: #FFE6E6;">단계별 풀이 과정</span></h3>
<p><strong>1단계: 패턴 파악</strong></p>
<pre><code class="language-javascript">// k번째 = 시작점에서 (k-1)x2칸 이동한 위치
function solution(numbers, k) {
  return (k - 1) * 2;
}</code></pre>
<p><strong>2단계: 순환 처리</strong></p>
<pre><code class="language-javascript">// 배열 크기를 넘어가면 나머지 연산으로 순환
function solution(numbers, k) {
  return ((k - 1) * 2) % numbers.length;
}</code></pre>
<p><strong>3단계: 결과 반환</strong></p>
<pre><code class="language-javascript">// 최종 인덱스로 해당 번호 찾기
function solution(numbers, k) {
  return numbers[((k - 1) * 2) % numbers.length];
}</code></pre>
<h3 id="span-stylebackground-colorffe6e6완성된-전체-코드span"><span style="background-color: #FFE6E6;">완성된 전체 코드</span></h3>
<pre><code class="language-javascript">// 최종 인덱스로 해당 번호 찾기
function solution(numbers, k) {
  return numbers[((k - 1) * 2) % numbers.length];
}</code></pre>
<br />

<h2 id="💡-알아두면-좋은-지식-modulo-vs-remainder">💡 알아두면 좋은 지식: Modulo vs Remainder</h2>
<h3 id="span-stylebackground-colorffe6e6모듈러-연산과-나머지-연산의-차이점span"><span style="background-color: #FFE6E6;">모듈러 연산과 나머지 연산의 차이점</span></h3>
<p>우리가 지금까지 사용한 javascript의 <code>%</code> 연산자는 엄밀히 말하면 <strong>나머지 연산자(remainder operator)</strong>이다. </p>
<blockquote>
<p>둘의 차이를 쉽게 말하면, </p>
</blockquote>
<ul>
<li><strong>모듈러 연산(modulo)</strong>: 나머지가 항상 <strong>0 이상의 양수</strong></li>
<li><strong>나머지 연산(remainder)</strong>: <strong>첫 번째 피연산자의 부호</strong>를 따름</li>
</ul>
<p>모듈러 연산과 나머지 연산의 차이는 개념을 이해하면 쉽게 알 수 있다. 
<strong>모듈러(modulo) 연산</strong>은 두 정수를 나눴을 때 나머지가 <strong>항상 0이상인 양수</strong>가 되도록 정의하고, <strong>나머지(remainder) 연산</strong>은 위에서도 언급했는데, <strong>항상 첫 번째 피연산자의 부호</strong>를 따른다. </p>
<p>그래서 위의 공던지기 문제도 두 피연산자가 모두 양수일 경우는 모듈러 연산과 같은 나머지를 갖지만, 그 외의 경우에는 모듈러 연산과 다르기 때문에 엄밀히 말하면 이 풀이는 모듈러 연산이 아닌 나머지 연산을 이용해 풀었다고 해야 맞는 말이다.</p>
<h3 id="span-stylebackground-colorffe6e6음수-처리-방식의-차이span"><span style="background-color: #FFE6E6;">음수 처리 방식의 차이</span></h3>
<pre><code class="language-javascript">// 나머지 연산 결과 (첫 번째 피연산자 부호 따름)
console.log(7 % 3);    // 1 (양수)
console.log(-7 % 3);   // -1 (음수)
console.log(7 % -3);   // 1 (양수)
console.log(-7 % -3);  // -1 (음수)</code></pre>
<pre><code class="language-javascript">// 모듈러 연산 결과 (항상 0 이상)
7 mod 3 = 1    ✅
-7 mod 3 = 2   ❌ JavaScript에서는 -1</code></pre>
<h3 id="span-stylebackground-colorffe6e6javascript에서의-주의할-점span"><span style="background-color: #FFE6E6;">Javascript에서의 주의할 점</span></h3>
<p>배열 인덱스에서 음수 처리 시 주의해야 한다. </p>
<pre><code class="language-javascript">const arr = [1, 2, 3, 4];
let index = -1;

// 🔴 잘못된 방법 (음수 인덱스)
console.log(arr[index % arr.length]); // undefined (-1 % 4 = -1)

// 🟢 올바른 방법 (항상 양수 인덱스)
console.log(arr[((index % arr.length) + arr.length) % arr.length]); // 4</code></pre>
<h3 id="span-stylebackground-colorffe6e6다른-언어와의-비교span"><span style="background-color: #FFE6E6;">다른 언어와의 비교</span></h3>
<table>
<thead>
<tr>
<th>언어</th>
<th>연산자</th>
<th>연산 방식</th>
<th><code>-7 % 3</code></th>
<th><code>-8 % 3</code></th>
<th><code>7 % -3</code></th>
</tr>
</thead>
<tbody><tr>
<td><strong>JavaScript</strong></td>
<td><code>%</code></td>
<td>Remainder (피제수 부호)</td>
<td><code>-1</code></td>
<td><code>-2</code></td>
<td><code>1</code></td>
</tr>
<tr>
<td><strong>Java</strong></td>
<td><code>%</code></td>
<td>Remainder (피제수 부호)</td>
<td><code>-1</code></td>
<td><code>-2</code></td>
<td><code>1</code></td>
</tr>
<tr>
<td><strong>C/C++</strong></td>
<td><code>%</code></td>
<td>Remainder (피제수 부호)</td>
<td><code>-1</code></td>
<td><code>-2</code></td>
<td><code>1</code></td>
</tr>
<tr>
<td><strong>Python</strong></td>
<td><code>%</code></td>
<td><strong>Modulo (항상 양수)</strong></td>
<td><code>2</code></td>
<td><code>1</code></td>
<td><code>-2</code></td>
</tr>
</tbody></table>
<br />

<h2 id="🔍-javascript에서-자주-사용되는-나머지-연산-사례">🔍 Javascript에서 자주 사용되는 나머지 연산 사례</h2>
<h3 id="span-stylebackground-colorffe6e6웹-개발-페이지네이션-캐러셀span"><span style="background-color: #FFE6E6;">웹 개발: 페이지네이션, 캐러셀</span></h3>
<p><strong>📄 페이지네이션</strong></p>
<pre><code class="language-javascript">// 페이지 번호 순환 (1, 2, 3, 1, 2, 3...)
function Pagination({ totalPages }) {
   const [currentPage, setCurrentPage] = useState(1);

   const nextPage = () =&gt; {
       setCurrentPage(prev =&gt; (prev % totalPages) + 1);
   };

   const prevPage = () =&gt; {
       setCurrentPage(prev =&gt; prev === 1 ? totalPages : prev - 1);
   };

   return (
       &lt;div&gt;
           &lt;button onClick={prevPage}&gt;이전&lt;/button&gt;
           &lt;span&gt;Page {currentPage}&lt;/span&gt;
           &lt;button onClick={nextPage}&gt;다음&lt;/button&gt;
       &lt;/div&gt;
   );
}</code></pre>
<br />

<p><strong>🔃 무한 캐러셀</strong></p>
<pre><code class="language-javascript">// 이미지 슬라이더 구현
const images = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg'];
let currentIndex = 0;

function nextSlide() {
    currentIndex = (currentIndex + 1) % images.length;
    updateSlider();
}

function prevSlide() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    updateSlider();
}

function updateSlider() {
    const slider = document.querySelector('.slider');
    slider.style.transform = `translateX(-${currentIndex * 100}%)`;

// 현재 이미지 표시
    document.querySelector('.current-image').src = images[currentIndex];
}

// 자동 슬라이드 (3초마다)
setInterval(nextSlide, 3000);</code></pre>
