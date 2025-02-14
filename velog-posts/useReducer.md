<p>useReducer은 React의 컴포넌트의 상태 관리를 위한 훅 중 하나로, 복잡하고 긴 상태 로직을 관리할 때 useState보다 적합하며 모든 useState는 useReducer로 대체 가능하다. 
useState와 useReducer의 차이점은 상태 관리 코드를 <strong>컴포넌트 외부로 분리</strong>할 수 있다는 것이다. 즉 다른 파일에 작성 후 불러와 사용이 가능하다.</p>
<p>아래 코드를 통해 useReducer의 사용법을 살펴보자.</p>
<pre><code class="language-javascript">// useReducer 연습
// 카운터 기능을 만들어 볼 것임

import { useReducer } from &quot;react&quot;;

// reducer: 변환기
//-&gt; 상태를 실제로 변화시키는 변환기 역할
// 컴포넌트 외부로 상태를 분리함으로써 컴포넌트 내부를 간결하게 유지할 수 있다는 장점이 있음
function reducer(state, action) {
  // 인수로 넘어온 state는 상태, action은 dispatch에 적어준 액션객체를 뜻함
  console.log(state, action);
  switch (action.type) {
    case &quot;INCREASE&quot;:
      return state + action.data;
    case &quot;DECREASE&quot;:
      return state - action.data;
    default:
      return state;
  }
}

const Exam = () =&gt; {
  // state는 useState처럼 배열의 첫번째 요소로 받아서 반환해주는 역할을 함
  // dispatch는 상태변화를 요청하기만 해주는 함수를 반환해주는 역할을 함
  // dispatch는 '발송하다'라는 뜻을 갖고 있어, 한마디로 &quot;상태변화가 있어야 한다는 사실을 알리는, 발송하는 함수&quot;
  // 0은 설정한 초기값을 말한다.
  const [state, dispatch] = useReducer(reducer, 0);

  const onClickPlus = () =&gt; {
    // 인수로 상태가 어떻게 변화되길 원하는지 넣어줘야 함
    // 여기서는 객체로 넣어줄 것임 -&gt; 이것을 '액션객체'라고 함
    dispatch({
      type: &quot;INCREASE&quot;, // 버튼을 눌러 상태가 변화되면 INCREASE라고 적어줄 것임
      data: 1, // 버튼을 누를 때마다 1씩 증가시켜줄것임
    });
  };

  const onClickMinus = () =&gt; {
    dispatch({
      type: &quot;DECREASE&quot;,
      data: +1,
    });
  };

  return (
    &lt;&gt;
      &lt;h1&gt;{state}&lt;/h1&gt;
      &lt;button onClick={onClickPlus}&gt;+&lt;/button&gt;
      &lt;button onClick={onClickMinus}&gt;-&lt;/button&gt;
    &lt;/&gt;
  );
};

export default Exam;</code></pre>
<p>사용할 때는 컴포넌트 최상단에서 호출하여 사용하며, reducer 함수와 초기 상태를 인자로 받는다. </p>
<p>reducer 함수는 상태가 어떻게 업데이트할 지 명시한 리듀서 함수로, 순수 함수여야 하며 현재 상태 state와 액션 객체 action을 받아 조건에 따라 새로운 다음 상태를 반환한다. 이 때 state와 action은 어떤 type도 가능하다. 
초기값 또한 어떤 type의 값도 가능하다.</p>
<p>useState처럼 const [state, dispatch] = useReducer(reducer, 0)을 만들어준다. 여기서 dispatch는 state를 다른 값으로 업데이트하고 리렌더링을 발생시키는 함수이다. 즉, action을 발생시키는 함수로, 이 함수를 통해 reducer에 action을 전달하고 state를 업데이트 시킬 수 있다. 컴포넌트 안에서는 dispatch 함수 안에 명령을 넣고 호출해주면 상태가 업데이트 된다. </p>
<p>또한 reducer 함수에서 switch default를 사용하여 정의를 해주었는데, 
default문보다 throw문을 두는 거이 더 낫다는 의견도 있다. 
action type이 case에 맞지 않는 것을 보낼 이유가 없기 때문에 이것은 사실상 <strong>오타 등에 의한 오류</strong>라고 봐야하기 때문이다. 참고하여 쓰면 좋을 것 같다. </p>
<p>두번째 인자에 들어가야할 초기값은 컴포넌트 밖으로 빼내어 정의해주어도 된다. 또한 action은 type의 객체를 지니고 있는 형태지만, 정해진 규칙은 없다. 
아래의 코드를 통해 확인할 수 있다. </p>
<pre><code class="language-javascript">// 카운터에 1을 더하는 액션
{
  type: 'INCREASE'
}
// 카운터에 1을 빼는 액션
{
  type: 'DECREASE'
}
// input 값을 바꾸는 액션
{
  type: 'CHANGE_INPUT',
  key: 'email',
  value: 'jinnieH@velog.com'
}
// 새 할 일을 등록하는 액션
{
  type: 'ADD_TODO',
  todo: {
    id: 1,
    text: 'useReducer 알기',
    done: false,
  }
}</code></pre>
<p>useReducer을 쓰는 이유는 몇가지가 있다. </p>
<p>1) 복잡한 상태 로직 관리
: 여러개의 상태값이 서로 의존적일 때, useReducer을 사용하면 상태 업데이트 로직을 한 곳에서 관리할 수 있어 코드를 깔끔하게 유지할 수 있다. </p>
<p>2) 성능 최적화
: 컴포넌트에서 발생하는 여러 상태 변화를 한 번에 처리할 수 있어서 불필요한 렌더링을 줄일 수 있다. </p>
<p>3) 재사용성
: reducer 함수와 로직을 다른 컴포넌트나 프로젝트에서 재사용할 수 있다. </p>
<p>4) 예측 가능한 상태 전이
: action을 통해 state가 어떻게 업데이트될 지 명시적으로 보여주기 때문에 상태 변화를 추적하기 쉽다. </p>
<p>이렇게 보면 useReducer가 useState보다 항상 나은 선택인 것처럼 보이지만 그렇지 않다. 각각 적합한 상황이 있는데 성능적인 문제보다는 <strong>상태 관리의 복잡성</strong>에 초점을 맞춰 선택하면 된다고 한다. </p>
<p>1) 코드의 크기
: 일반적인 경우에 useReducer은 reducer 함수와 dispatch 액션을 함께 작성해야하기 때문에 useState가 작성해야 하는 코드의 양이 훨씬 적다. 
그러나, 여러 이벤트 핸들러가 비슷한 방식으로 상태를 변경하고 있다면 상태 변경 로직을 useReducer의 reducer 내부로 옮김으로써 코드를 줄이는 데 도움이 된다. </p>
<p>2) 가독성
: useState는 상태 변경이 매우 간단할 때 읽기 쉽다. 그러나 상태 변경 로직이 복잡해지면 가독성이 떨어진다. 
이런 경우 useReducer를 사용해 상태 변경 로직을 reducer 내부로 옮겨 이벤트 핸들러와 상태 변경 로직을 완전히 분리할 수 있다.</p>
<p>3) 디버깅
: useState의 경우 상태 변경 도중 버그가 발생하면 어디서, 왜 잘못됐는지 알기 어렵다. 
useReducer을 사용하면 콘솔 로그를 확인하거나 에러를 발생시켜 디버깅할 수 있다. </p>
<p>4) 테스트
: reducer을 컴포넌트에 의존하지 않는 순수 함수이기 때문에 개별적으로 테스트할 수 있다. </p>
<p>5) 개인 선호도
: useState와 useReducer를 사용하는 것은 선호도 문제로, 사람마다 선호하는 것이 다르다. </p>
<p>지금까지 useReducer의 개념, 사용법, 언제 사용하면 좋을 지에 대해 살펴보았다. 
그동안 상태 관리는 useState만 써왔는데 앞으로 useReducer도 고려하여 써보는 연습을 계속 해봐야겠다. </p>