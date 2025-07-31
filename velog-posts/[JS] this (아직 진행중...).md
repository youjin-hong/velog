# 📌 Velog 글 요약

| 항목   | 내용 |
|--------|------|
| **제목** | [JS] this (아직 진행중...) |
| **날짜** | Mon, 05 Aug 2024 14:37:02 GMT |
| **링크** | [https://velog.io/@so356hot/this](https://velog.io/@so356hot/this) |

---

<p>JavaScript에서 <code>this</code>는 <strong>함수나 메서드가 어떻게 호출되었는지</strong>에 따라 그 값이 결정되는 동적인 특성을 가지고 있다. </p>
<p>이는 함수의 실행 컨텍스트에 따라 달라지며, 함수가 어떻게 호출되었는지에 따라 <code>this</code> 값이 결정된다. 즉, <code>this</code>는 실행 시점에 결정되며, 선언 시점에서는 그 값을 알 수 없다.</p>
<p>호출 시 <code>this</code>가 결정된다는 것을 <strong>동적으로 바인딩되었다</strong>고 한다. 따라서 함수 정의가 어떻게 되었는지보다 누가 어떻게 호출했는지에 유의해야 한다. 자바스크립트의 함수는 호출될 때, 매개변수로 전달되는 인자값 외에 <code>arguments</code> 객체와 <code>this</code>를 암묵적으로 전달받는다.</p>
<hr />
<p><strong>용어 정리</strong></p>
<ul>
<li><strong>함수</strong>: <code>function fun() {}</code>과 같은 형태로 정의되어, <code>fun()</code> 형태로 호출할 수 있는 함수</li>
<li><strong>메서드</strong>: <code>obj.fun()</code> 형태로 호출할 수 있도록 객체 내에서 정의된 함수</li>
</ul>
<hr />
<h3 id="1-일반-함수로-호출된-경우">1. 일반 함수로 호출된 경우</h3>
<p>일반 함수로 호출된 경우, <code>this</code>는 전역 객체 (브라우저 환경에서는 <code>window</code>)에 바인딩된다. 
전역 함수뿐만 아니라 내부 함수의 경우도 <code>this</code>는 외부 함수가 아닌 전역 객체에 바인딩된다. 
또한, 메서드의 내부 함수일 경우에도 <code>this</code>는 전역 객체에 바인딩된다. 콜백 함수의 경우에도 <code>this</code>는 전역 객체에 바인딩된다.</p>
<pre><code class="language-jsx">var ga = '안녀어어어어어어';

console.log(ga);  // 안녀어어어어어어
console.log(window.ga);   // 안녀어어어어어어

function foo() {
  console.log('invoked!');
}
window.foo(); // invoked!</code></pre>
<pre><code class="language-jsx">function foo() {
  console.log(&quot;foo's this: &quot;,  this);  // window
  function bar() {
    console.log(&quot;bar's this: &quot;, this); // window
  }
  bar();
}
foo();</code></pre>
<pre><code class="language-jsx">const person = {
  name: '홍',
  sayName: function() {
    console.log(&quot;sayName's this:&quot;, this);  // {name: '홍', sayName: ƒ}
    console.log(&quot;sayName's this:&quot;, this.name);  // sayName's this: 홍
    const innerFun = function() {
      console.log(&quot;innerFun's this:&quot;, this);  // window
      console.log(`안녕하세요 ${this.name}님`); // 안녕하세요 undefined님
    }
    innerFun();
  }
};

person.sayName();</code></pre>
<pre><code class="language-jsx">var value = 1;

var obj = {
  value: 100,
  foo: function() {
    setTimeout(function() {
      console.log(&quot;callback's this:&quot;, this);  // window
      console.log(&quot;callback's this.value:&quot;, this.value); // 1
    }, 100);
  }
};

obj.foo();
// setTimeout 함수를 화살표 함수로 바꿔주면 상위 스코프인 obj를 가리키게 할 수 있다.</code></pre>
<pre><code class="language-jsx">const person = {
  name: '홍',
  sayName: function() {
    const innerFun = () =&gt; {
      return `안녕하세요 ${this.name}님`; // 안녕하세요 홍님
    }
    console.log(innerFun());
  }
};

person.sayName();</code></pre>
<p>화살표 함수에서는 <code>this</code>가 존재하지 않기 때문에 외부 스코프의 <code>this</code>를 그대로 사용한다. </p>
<p>일반 함수의 <code>this</code>는 함수가 호출될 때 결정되나, 화살표 함수는 함수가 정의될 때 렉시컬 스코프(함수의 상위 스코프를 결정하는 방식)처럼 정의된 위치에 따라 외부 스코프의 <code>this</code>를 캡처해서 사용한다.</p>
<h3 id="2-메서드로-호출된-경우">2. 메서드로 호출된 경우</h3>
<p>메서드로 호출된 경우, <code>this</code>는 해당 메서드가 속한 객체를 가리킨다. <code>sayName()</code> 앞에 <code>.</code>을 붙여서 호출한 객체인 <code>person</code>이 <code>this</code>가 가리키는 객체가 된다.</p>
<pre><code class="language-jsx">var obj1 = {
  name: 'Lee',
  sayName: function() {
    console.log(this.name);
  }
};

var obj2 = {
  name: 'Kim'
};

obj2.sayName = obj1.sayName;

obj1.sayName();  // Lee
obj2.sayName();  // Kim</code></pre>
<pre><code class="language-jsx">const person = {
  name: 'Seo',
  sayName() {
    console.log(this.name); // Seo
  }
};

person.sayName();</code></pre>
<h3 id="3-함수가-호출될-때-apply-call-bind가-사용된-경우-명시적-바인딩">3. 함수가 호출될 때 <code>apply</code>, <code>call</code>, <code>bind</code>가 사용된 경우 (명시적 바인딩)</h3>
<p><code>Function.prototype</code>에 정의되어 있는 <code>call</code>, <code>apply</code>, <code>bind</code> 메서드를 이용해 <code>this</code>를 바인딩하는 것을 명시적 바인딩이라고 한다. </p>
<p>이 메서드들은 <code>this</code>를 가리키는 것이 무엇인지 명시적으로 지정한다.</p>
<ul>
<li><code>call</code>: 함수를 호출하면서 <code>this</code>를 바인딩하며, 인자를 쉼표로 구분하여 받는다.</li>
<li><code>apply</code>: 함수를 호출하면서 <code>this</code>를 바인딩하며, 인자를 배열로 받는다.</li>
<li><code>bind</code>: 함수를 호출하지 않고 <code>this</code>를 바인딩한 새로운 함수를 반환한다.</li>
</ul>
<pre><code class="language-jsx">const person = {
  name: '홍',
  sayName: function() {
    let that = this;   // 비전역 변수에 할당
    console.log(&quot;sayName's this:&quot;, this);  // {name: '홍', sayName: ƒ}
    console.log(&quot;sayName's this:&quot;, this.name);  // sayName's this: 홍
    const innerFun = function() {
      console.log(&quot;innerFun's this:&quot;, that);  // {name: '홍', sayName: ƒ}
      console.log(`안녕하세요 ${that.name}님`); // 안녕하세요 홍님
    }
    innerFun();
  }
};

person.sayName();</code></pre>
<pre><code class="language-jsx">function sayName(a, b) {
  console.log(this.name, a, b);
}

const obj = {
  name: '홍',
};

sayName.call(obj, 1, 2); // 홍 1 2</code></pre>
<pre><code class="language-jsx">function sayName(a, b) {
  console.log(this.name, a, b);
}

const obj = {
  name: '홍 ',
};

sayName.apply(obj, [1, 2]); // 홍 1 2</code></pre>
<pre><code class="language-jsx">function sayName(a, b) {
  console.log(this.name, a, b);
}

const obj = {
  name: '홍 ',
};

const bound = sayName.bind(obj, 1);
bound(2); // 홍 1 2</code></pre>
<p><code>bind</code>를 사용하면 새로운 함수를 반환하기 때문에 한 번 바인딩되면 그 이후로 바뀌지 않는다.</p>
<pre><code class="language-jsx">function sayName() {
  return this.name;
}

const boundSayName1 = sayName.bind({ name: '찬' });
const boundSayName2 = boundSayName1.bind({ name: '홍 ' }); // 새롭게 바인딩되지 않는다

console.log(boundSayName1()); // 찬
console.log(boundSayName2()); // 찬
console.log(boundSayName1.apply({ name: 'apply' })); // 찬

const obj = {
  name: 'obj',
  sayName,
  boundSayName1,
  boundSayName2,
};

console.log(obj.name, obj.sayName(), obj.boundSayName1(), obj.boundSayName2()); // obj obj 찬 찬</code></pre>
<p>아래 코드의 경우, <code>callCB</code> 함수는 일반 함수를 호출하기 때문에 <code>obj.sayName</code>을 인자로 넣어도 <code>sayName</code>을 일반 함수로 호출된다. </p>
<p>따라서 <code>this</code>는 전역 객체를 참조하게 되고, 전역에는 <code>name</code> 속성이 없기 때문에 <code>undefined</code>가 출력된다.</p>
<pre><code class="language-jsx">const obj = {
  name: 'timegambit',
  sayName() {
    console.log(this.name);
  },
};

function callCB(cb) {
  cb();
}

callCB(obj.sayName);  // undefined</code></pre>
<p><code>obj</code>의 <code>name</code>인 <code>timegambit</code>을 출력하기 위한 바인딩 방법은 두 가지가 있다.</p>
<p>첫 번째는 <code>bind</code> 메서드를 사용하는 것이다. 이 메서드를 사용하면 <code>this</code>를 명시적으로 <code>obj</code> 객체로 바인딩할 수 있다.</p>
<pre><code class="language-jsx">callCB(sayName.bind(obj));</code></pre>
<p>두 번째는 화살표 함수를 사용하는 것이다. </p>
<p>화살표 함수는 상위 컨텍스트의 <code>this</code>를 유지하기 때문에 이를 이용해 해결할 수 있다. </p>
<p>이 경우, 화살표 함수 내부의 <code>this</code>는 상위 컨텍스트인 <code>obj</code>를 참조하게 된다.</p>
<pre><code class="language-jsx">const obj = {
  name: 'timegambit',
  sayName() {
    console.log(this.name);
  },
};

function callCB(cb) {
  cb();
}

callCB(() =&gt; obj.sayName());</code></pre>
<h3 id="4-생성자-함수-내부에서-호출된-경우">4. 생성자 함수 내부에서 호출된 경우</h3>
<p>생성자 함수에서 <code>this</code>는 새로운 객체를 참조한다.</p>
<p><code>new</code> 키워드로 생성자 함수를 호출할 때, <code>this</code>는 새로 생성된 객체를 가리킨다.</p>
<pre><code class="language-jsx">// 생성자 함수
function Person(name) {
  this.name = name;
}

var me = new Person('Lee');
console.log(me); // Person {name: &quot;Lee&quot;}

// new 연산자와 함께 생성자 함수를 호출하지 않으면 생성자 함수로 동작하지 않는다.
var you = Person('Kim');
console.log(you); // undefined</code></pre>
<hr />
<h3 id="중첩된-객체일-경우의-this">중첩된 객체일 경우의 <code>this</code></h3>
<p>중첩된 객체에서의 this는 함수의 정의 방식에 따라 다르게 동작한다.</p>
<p>특히 일반 함수와 화살표 함수의 this 바인딩이 어떻게 달라지는지에 대해 자세히 이해하는 것이 중요하다.</p>
<p>일반함수는 호출될 때 this가 동적으로 결정된다. 이는 함수 호출 패턴에 따라 달라지는데,</p>
<p>객체의 메서드로 정의된 함수가 호출될 때 그 메서드의 내부의 일반 함수는 기본적으로 전역 객체를 this로 참조하게 된다.</p>
<pre><code class="language-jsx">// 중첩된 객체의 일반함수에서의 this
const cat = {
  name: 'meow',
  foo1: function() {
    const foo2 = function() {
      console.log(this.name);
    };
    foo2();
  }
};

cat.foo1(); // undefined</code></pre>
<p>위 코드에서 foo2 함수는 foo1 함수의 내부에서 정의되었지만, 일반 함수로 호출됐기 때문에 this는 전역 객체를 가리킨다. 전역에 name이라는 속성값이 없으므로 this.name은 undefined가 된다.</p>
<pre><code class="language-jsx">const cat = {
  name: 'meow',
  foo1: function() {
    const foo2 = () =&gt; {
      console.log(this.name);
    };
    foo2();
  }
};

cat.foo1(); // meow</code></pre>
<p>위의 foo2 함수는 화살표 함수로 정의되었기 때문에 foo1 함수의 this를 그대로 사용한다. 따라서 this.name은 cat 객체의 name 속성인 meow가 된다.</p>
<hr />
<h3 id="화살표-함수에서의-this">화살표 함수에서의 <code>this</code></h3>
<p>일반 함수와 화살표 함수의 <code>this</code>는 다르게 동작한다. </p>
<p>화살표 함수는 함수를 선언할 때, <code>this</code>에 바인딩할 객체가 정적으로 결정된다. </p>
<p>따라서 화살표 함수의 <code>this</code>는 언제나 상위 스코프의 <code>this</code>를 가리킨다. </p>
<p>또한, <code>call</code>, <code>apply</code>, <code>bind</code> 메서드를 사용해 <code>this</code>를 변경할 수 없다.</p>
<pre><code class="language-jsx">function fun() {
  this.name = &quot;하이&quot;;
  return {
    name: &quot;바이&quot;,
    speak: function () {
      console.log(this.name);
    },
  };
}

function arrFun() {
  this.name = &quot;하이&quot;;
  return {
    name: &quot;바이&quot;,
    speak: () =&gt; {
      console.log(this.name);
    },
  };
}

const fun1 = new fun();
fun1.speak(); // 바이

const fun2 = new arrFun();
fun2.speak(); // 하이</code></pre>
<p>일반 함수로 사용했을 때는 자신이 종속된 객체를 <code>this</code>로 가리키고, 화살표 함수는 자신이 종속된 인스턴스를 가리킨다.</p>
<pre><code class="language-jsx">const cat = {
  name: 'meow',
  foo1: function() {
    const foo2 = function() {
      console.log(this.name);
    };
    foo2();
  }
};

cat.foo1(); // undefined</code></pre>
<pre><code class="language-jsx">const cat = {
  name: 'meow',
  foo1: function() {
    const foo2 = () =&gt; {
      console.log(this.name);
    };
    foo2();
  }
};

cat.foo1(); // meow</code></pre>
