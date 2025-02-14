<h3 id="react-life-cycle">[react Life Cycle]</h3>
<p>React의 각 구성 요소에는 3가지 주요 단계동안 모니터링하고 조작할 수 있는 수명 주기가 있다. 수명주기는 초기화부터 시작해 DOM에서 언마운트 될 때 끝이 난다. </p>
<blockquote>
<p>Mount → Update → UnMount 의 생애주기를 갖는다.</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/e0bbdad4-1fa3-49a4-8cc8-603e50d990a5/image.png" /></p>
<ol>
<li><strong>Mount</strong></li>
</ol>
<ul>
<li>Like 탄생</li>
<li>Mount는 요소를 DOM에 넣는 것을 의미한다.</li>
<li>component가 탄생하는 순간
→ 즉, 화면에 처음 렌더링 되는 순간을 말한다
⇒ <strong>“a 컴포넌트가 마운트 되었다” = “a 컴포넌트가 화면에 처음으로 렌더링 되었다.”</strong></li>
</ul>
<ol start="2">
<li><p><strong>Update</strong></p>
<ul>
<li>Like 변화</li>
<li>컴포넌트가 다시 렌더링 되는 순간</li>
<li>리렌더링 될 때를 의미
⇒ <strong>“a 컴포넌트가 업데이트 되었다” = “a 컴포넌트가 리렌더링 되었다.”</strong></li>
</ul>
</li>
<li><p><strong>UnMount</strong></p>
<ul>
<li>Like 죽음</li>
<li>컴포넌트가 화면에서 사라지는 순간</li>
<li>렌더링에서 제외되는 순간을 의미
⇒ <strong>“a 컴포넌트가 언마운트 되었다” = “a 컴포넌트가 화면에서 사라졌다”</strong></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/96d359ec-8172-42bc-833d-d4b6b1d3f728/image.png" /></p>
</li>
</ol>
<p>이러한 컴포넌트의 라이프사이클을 잘 알고 있으면 우리가 원하는 타이밍에 컴포넌트에 어떤 작업을 실행시키도록 만들 수 있다. </p>
<p>위의 그림을 예를 들어, 컴포넌트가 화면에 처음 나타났을 때 
즉, <strong>mount</strong> 되었을 때 백엔드 서버에 네트워크 요청을 보내서 데이터를 불러오는 기능을 만들 수 있다. 
또는 컴포넌트가 <strong>update</strong>될 때 변경된 값이 무엇인지 console에 출력하는 기능을 만들 수도 있다. 
마지막으로 컴포넌트가 <strong>unmount</strong>될 때 즉, 화면에서 사라질 때 컴포넌트가 사용하던 여러 유형의 메모리들을 정리할 수도 있다. </p>
<p>이렇게 컴포넌트 라이프사이클의 단계별로 다른 작업을 수행하도록 하는 것을 
<strong>라이프사이클 제어</strong>라고 한다. </p>
<p>이 라이프사이클 제어는 <strong>useEffect Hook</strong>을 이용하면 손쉽게 이용할 수 있다.
아래에서 useEffect에 대해 알아본 후, useEffect Hook을 이용해 라이프 사이클을 제어하는 방법에 대해 알아보겠다. </p>
<hr />
<h3 id="useeffect">[useEffect]</h3>
<p>리액트 컴포넌트의 사이드 이펙트를 제어하는 새로운 React Hook을 말한다. </p>
<blockquote>
<p><strong>사이드 이펙트</strong>
우리 말로 “부작용”이라는 뜻으로, 
리액트에서는 <strong>컴포넌트의 어떠한 동작에 따라 “부수적인 효과”, “파생되는 효과”</strong>정도로 해석 가능하다.
<img alt="" src="https://velog.velcdn.com/images/so356hot/post/4fb23122-269a-4880-834a-469ba8fe1227/image.png" />
<img alt="" src="https://velog.velcdn.com/images/so356hot/post/970c947e-cf03-4566-baed-9364d8209cfb/image.png" /></p>
</blockquote>
<p>아래의 코드는 useEffect의 기본 형태이다. </p>
<pre><code class="language-javascript">import { useState, useEffect } from 'react';

function App() {
const [count, setCount] = useState(0);
useEffect(() =&gt; {}, [count]);

return (
&lt;&gt;
&lt;/&gt;
);
}
export default App;</code></pre>
<p>useEffect 함수에서 두번째 인자인 배열에 count state값을 넣어주게 되면 count state값이 바뀔 때마다 첫번째 인자인 콜백함수가 실행된다. </p>
<p>이 두번째 인자 배열에 들어가는 값에 따라 다르게 동작하기 때문에 이 배열을
&quot;의존성 배열&quot;이라고 하며 dependency array, deps라고 부른다. 
deps에는 여러개의 값을 넣을 수 있다. </p>
<p>여기서 꼭 useEffect를 써야 하는 것인가, console.log로 대체할 순 없을 것인가라는 의문이 들며 아래와 같은 코드를 작성할 수 있다. </p>
<pre><code class="language-javascript">import { useState, useEffect } from 'react';

function App() {
const [count, setCount] = useState(0);
useEffect(() =&gt; {
console.log(`count: ${count} / input: ${input});
}, [count]);

const onClickButton = (value) =&gt; {
setCount(count + value);
};

return (
&lt;&gt;
&lt;/&gt;
);
}
export default App;</code></pre>
<p>그러나 이 코드는 생각했던대로 작동하지 않는다. 즉, count값이 입력에 따라 바로 update되지 않는 것을 확인할 수 있다. 
그 이유는 useState의 setCount함수가 <strong>비동기적</strong>으로 처리되기 때문이다. 
그래서 값을 바로 update하여 사이드 이펙트와 같은 부수효과들을 진행하려면 useEffect를 사용해야 한다. 
그래야 변경된 state값을 바로바로 이용할 수가 있기 때문이다. </p>
<hr />
<h3 id="life-cycle-제어">[Life Cycle 제어]</h3>
<p>useEffect의 개념, 동작 원리까지 알아보았다. 이제 카운터앱의 코드를 이용해 생애주기별로 useEffect를 이용한 라이프사이클 제어 방법에 대해 알아보자.</p>
<pre><code class="language-javascript">// App.jsx
import { useState, useEffect, useRef } from 'react';

function App() {
const [count, setCount] = useState(0);
const [input, setInput] useState('');

// 새로운 레퍼런스 객체 생성, 초기값은 아직 mount되지 않았다는 의미로 false
const isMount = useRef(false);

// 1. useEffect로 마운트(탄생) 제어하는 방법
// : useEffect를 호출하고 빈 배열을 넣으면 처음 렌더링 될 때만 호출된다
useEffect(() =&gt; {
    console.log('mount');
    }, []);

// 2. useEffect로 업데이트(변화, 리렌더링) 제어하는 방법
// : 두번째 인자인 배열을 제거해주면 된다
// mount될 때 update가 뜨지 않고 진짜 update를 했을 때만 코드를 실행시키고 싶다면
// useRef를 이용해서 App이 지금 mount가 되었는지 체크하는 변수를 만들면 된다
// (일종의 flag 역할을 하는 것이다)
useEffect(() =&gt; {
    if (!isMount.currnet) {
        isMount.current = true;
        return;
        }
    console.log('update');
    });

// 3. useEffect로 언마운트(죽음)을 제어하는 방법: Even.jsx에서 확인하기

const onClickButton = (value) =&gt; {
setCount(count + value);
};

return (
&lt;&gt;
&lt;/&gt;
);
}
export default App;</code></pre>
<pre><code class="language-javascript">// Even.jsx
import { useEffect } from &quot;react&quot;;

const Even = () =&gt; {
  useEffect(() =&gt; {
    // 함수 안에 또 return 문 함수가 있는 것을 확인할 수 있다
    // 이것을 클린업, 정리함수라고 하며,
    // 이 정리함수는 useEffect가 끝날 때 실행된다
    return () =&gt; {
      console.log(&quot;unmount&quot;);
    };
  }, []);
  // 의존성 배열을 빈 배열로 작성해주면 useEffect가 mount될 때 실행되고,
  // 반대로 정리함수(return () =&gt; {})는 unmount될 때 실행된다
  return &lt;&gt;짝수입니다.&lt;/&gt;;
};

export default Even;</code></pre>