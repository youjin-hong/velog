<h3 id="javascript-변수-타입"><strong>[javascript 변수 타입]</strong></h3>
<ul>
<li><strong>원시 타입 (Primitive type]</strong></li>
</ul>
<p>데이터 복사가 일어날 때, 메모리 공간을 “<strong>새로”</strong> 확보해 <strong>독립적인 값</strong>을 저장한다.
즉, 값이 그대로 <strong>“복사”</strong>가 되고<strong>,</strong>  새로운 메모리 공간에 <strong>“할당”</strong> 된다.</p>
<pre><code class="language-jsx">let a = 100;
a = 50;</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/adcae96b-0a8a-4221-a993-553a7cad4d39/image.png" /></p>
<p><code>a</code> 변수에 100을 할당하면 메모리에 <code>Number</code>타입의 100이라는 값이 생성되고, <code>a</code>는 메모리에 생성된 100의 메모리 주소를 가리킨다. </p>
<p>그 후 <code>a</code>에 50을 재할당하면 메모리에 생성된 값이 50으로 바뀌는 것이 아니라 새로운 <code>Number</code> 타입의 50이라는 값을 새로운 메모리에 생성하고 <code>a</code>가 가리키던 메모리가 바뀐다</p>
<p>변수 <code>a</code>에 값을 재할당함으로써 쓰이지 않는 100은 가비지 컬렉터에 의해 삭제된다.</p>
<p>→ 메모리에는 50과 100의 값이 모두 존재한다
⇒ 원시 타입은 불변성을 띄기 때문에 기존에 메모리에 생성된 값들은 변경 불가능하다</p>
<pre><code class="language-jsx">let a = 100;
let b = a;
a = 50;

console.log(b);</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/e9f569d2-3a33-466b-80b1-cd19962fb2d4/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/ba005931-d4a7-46e9-bbf6-51ab9facda5f/image.png" /></p>
<p><code>b</code>라는 새로운 변수에 <code>a</code>를 할당하게 되면 <code>b</code>는 <code>a</code>의 <strong>값을</strong> <strong>통째로 복사</strong>해 메모리 변수에 담게 된다. 
변수 <code>a</code>는 50으로 재할당이 되더라도 <code>b</code>는 영향을 받지 않는다.</p>
<ul>
<li><strong>참조 타입 (객체 등→ 원시 타입을 제외한 나머지)</strong></li>
</ul>
<p>메모리에 직접 접근하지 않고, <strong>메모리의 주소</strong>에 대한 <strong>간접 참조</strong>를 통해 메모리에 접근한다.</p>
<p>즉, 변수에 객체 그대로 저장되는 것이 아니라, 객체가 저장돼 있는 메모리 주소인 <strong>참조 값이 저장</strong>된다. </p>
<p>→ 객체가 할당된 변수를 복사할 땐 객체 자체가 복사되지 않고 <strong>참조값이 복사</strong>된다.</p>
<blockquote>
<p><strong>참조 타입의 특징
💨</strong> 변수의 크기가 동적으로 변할 수 있다.
<strong>💨 <code>Heap</code></strong>에는 참조 타입의 데이터(value)와 Heap의 데이터 주소가 함께 저장된다.
<strong>💨 <code>Call Stack</code></strong>에는 메모리 주소와 참조할 Heap의 주소가 같이 저장된다.</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/76e635a9-ecf6-410e-a3b4-3bd160e3f503/image.png" /></p>
<pre><code class="language-jsx">let myArray = [];
let copyArray = myArray;

myArray.push('hihi~!');

console.log(copyArray);</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/c02c170c-3545-4593-af73-c113b710d341/image.png" /></p>
<p>변수는 2개이지만 <strong>동일한 객체에 대한 참조 값(주소 값)이 저장</strong>되기 때문에 같은 값이 변수에 할당되는 것을 볼 수 있다.</p>
<pre><code class="language-jsx">// 두 변수가 같은 객체를 참조 -&gt; 같은 메모리 주소를 가짐
let a = {};
let b = a; // 참조에 의한 복사

alert( a == b ); // true,
alert( a === b ); // true</code></pre>
<pre><code class="language-jsx">// 두 객체가 독립됨 -&gt; 서로 다른 메모리 주소를 가짐
let a = {};
let b = {};

alert( a == b ); // false</code></pre>
<p>이렇게 객체가 할당된 변수를 복사하면 객체에 대한 참조 값이 1개 더 만들어지기 때문에 
객체를 복사할 때에는 주로 깊은 복사(1차원까지) 또는 깊은 복사(2차원 이상)를 한다.</p>
<hr />
<h3 id="객체에서의-얕은-복사-깊은-복사"><strong>[객체에서의 얕은 복사, 깊은 복사]</strong></h3>
<ol>
<li><strong>얕은 복사 (Shallow Copy)</strong></li>
</ol>
<p>얕은 복사는 객체를 복사할 때 원본 값과 복사된 값이 같은 <strong>메모리 주소</strong>를 가리키는 것이다. 
따라서 원본이나 복사본을 변경하게 되면 다른 객체가 변경될 수 있다. </p>
<ol start="2">
<li><strong>깊은 복사 (Deep Copy)</strong></li>
</ol>
<p>깊은 복사는 얕은 복사처럼 참조 주소 값이 복사 되는 것이 아니라, <strong>값만 복사</strong> 되는 것이다.
즉, 원본과의 참조와 완전히 끊어진 객체를 말한다. (독립적)</p>
<blockquote>
<p><strong>Javascript에서 내장 객체로 복사하는 방법</strong>
💨 <code>spread oprator</code> (ES6에 새로 추가된 문법)
💨 <code>Object.assign()</code>
****💨 <code>Array.prototype.concat()</code>
💨 <code>Array.prototype.slice()</code>
💨 <code>Array.from()</code>
💨 <code>Object.create()</code></p>
</blockquote>
<pre><code class="language-jsx">// 얕은 복사
// - 원본 배열과 복사된 배열이 같은 객체를 참조
// - 복사한 배열의 값을 변경하면 원본 배열의 값도 변경됨

let arr = [1, 2, {a: 3}];
let shallowCopy = arr; 

shallowCopy[0] = 10;
shallowCopy[2].a = 100;

console.log(&quot;=== shallowCopy ===&quot;);
console.log(arr); // [10, 2, {a: 100}] -&gt; 원본도 변경됨
console.log(shallowCopy);   // [10, 2, {a: 100}]

// 깊은 복사 (1차원 요소)
// - 배열의 1차원 요소만 복사
// - 배열의 요소가 객체라면 해당 객체의 &quot;참조&quot;만 복사
// - 원본 배열과 복사된 배열이 같은 객체를 참조
// - 복사한 배열의 객체값을 변경하면 1차원 요소의 원본 배열의 객체값은 변경되지 않음
// - 그러나 2차원 이상의 요소는 원본 객체의 주소를 여전히 참조하고 있기 때문에 
// 복사본 변경 시, 원본도 변경됨

// spread operator로 객체 복사
arr = [1, 2, {a: 3}];
let deepCopy = [...arr];  // 또는 arr.slice() 등 

deepCopy[0] = 10;
deepCopy[2].a = 100;

console.log(&quot;=== deepCopy ===&quot;);
console.log(arr); // [1, 2, {a: 100}]
console.log(deepCopy);   // [10, 2, {a: 100}]

// Object.assign()으로 객체 복사
const origin = {a:1, b:{c:2}};
// origin의 정보를 빈 객체인 {} 안에 복사 -&gt; ShallowCopy의 주소가 달라짐을 의미 (새 메모리에 저장)
const shallowCopy = Object.assign({}, origin); 

shallowCopy.a = 10;
console.log(origin.a);  // 1 -&gt; 원본 객체 변경x
console.log(shallowCopy.a) // 10 -&gt; 복사본만 변경됨

shallowCopy.b.c = 20;
console.log(origin.b.c); // 20 -&gt; 원본 객체의 중첩된 객체 변경됨

// 깊은 복사 (2단계 깊이까지 복사하고 싶다면)
// - 모든 레벨의 요소를 새로운 메모리 공간에 복사
// - 배열 내에 중첩된 객체, 배열이 있을 때 유용함
// - 원본 배열과 복사한 배열이 독립적으로 동작

arr = [1, 2, {a: 3}];
// JSON.stringfy()로 객체 복사
// 이 메소드를 사용하면 객체를 json &quot;문자열&quot;로 변환하면서 원본 객체와의 참조가 끊어진다.
// 그 다음 JSON.parse()로 다시 객체로 변환한다.
let deepDeepCopy = JSON.parse(JSON.stringify(arr));

deepDeepCopy[0] = 10;
deepDeepCopy[2].a = 100;

console.log(&quot;=== deepDeepCopy ===&quot;);
console.log(arr); // [1, 2, {a: 3}]
console.log(deepDeepCopy);   // [10, 2, {a: 100}]</code></pre>
<hr />
<blockquote>
<p><strong>[참고 사이트]</strong></p>
<p><a href="https://ko.javascript.info/object-copy">https://ko.javascript.info/object-copy</a></p>
<p><a href="https://developer.mozilla.org/ko/docs/Glossary/Shallow_copy">https://developer.mozilla.org/ko/docs/Glossary/Shallow_copy</a></p>
</blockquote>