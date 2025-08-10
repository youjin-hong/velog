# 📌 Velog 글 요약

| 항목   | 내용 |
|--------|------|
| **제목** | [스무디 한 잔 마시며 끝내는 리액트 + TDD] 7, 8장 - 상태 관리와 라이프사이클 이해 |
| **날짜** | Sun, 10 Aug 2025 01:00:59 GMT |
| **링크** | [https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-7-8%EC%9E%A5-%EC%83%81%ED%83%9C-%EA%B4%80%EB%A6%AC%EC%99%80-%EB%9D%BC%EC%9D%B4%ED%94%84%EC%82%AC%EC%9D%B4%ED%81%B4-%EC%9D%B4%ED%95%B4](https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-7-8%EC%9E%A5-%EC%83%81%ED%83%9C-%EA%B4%80%EB%A6%AC%EC%99%80-%EB%9D%BC%EC%9D%B4%ED%94%84%EC%82%AC%EC%9D%B4%ED%81%B4-%EC%9D%B4%ED%95%B4) |

---

<p>지난 시간에 리액트 프로젝트 설치와 react-testing-library에 대해 알아보았습니다. 오늘은 본격적으로 리액트 테스트를 하기에 앞서 클래스 컴포넌트 사용 방법과 상태관리(localStorage, Context API)에 대해 살펴보겠습니다. </p>
<p><a href="https://github.com/youjin-hong/TDD_study">TDD 실습 Github Repo</a>
<a href="https://ko.react.dev/reference/react/Component">클래스 컴포넌트</a>
<a href="https://ko.legacy.reactjs.org/docs/context.html#gatsby-focus-wrapper">Context API</a>
<a href="https://developer.mozilla.org/ko/docs/Web/API/Window/localStorage">로컬스토리지</a></p>
<hr />
<h2 id="✨-7-클래스-컴포넌트">✨ 7. 클래스 컴포넌트</h2>
<p>리액트는 v16.8부터 함수 컴포넌트를 권장하고 있지만 그 전에는 클래스 컴포넌트를 기본 컴포넌트로 사용했는데요. 이 긴 시간동안 클래스 컴포넌트가 사용됐기 때문에 클래스 컴포넌트로 제작된 많은 예제와 라이브러리들이 여전히 존재하고 있습니다. 그래서 클래스 컴포넌트 사용 방법을 어느 정도는 이해를 하면 좋을 것 같습니다. </p>
<h3 id="span-stylebackground-colorlavender클래스-컴포넌트span"><span style="background-color: lavender;">클래스 컴포넌트</span></h3>
<p><strong>리액트 훅</strong>이 나오기 전까지는 리액트는 클래스 컴포넌트를 주로 사용했습니다. 그 이유는 함수 컴포넌트에서는 컴포넌트의 상태를 관리하기 위한 State를 사용할 수 없었기 때문인입니다. </p>
<blockquote>
<p><strong>&lt;리액트 훅 이전&gt;</strong></p>
</blockquote>
<ul>
<li>State를 갖는 컴포넌트: 클래스 컴포넌트로 제작</li>
<li>단순히 Props 받아 화면에 표시하는 컴포넌트: 함수 컴포넌트로 제작</li>
</ul>
<p>그러나 리액트 훅이 등장하면서 함수 컴포넌트에도 State를 사용할 수 있게 되었고, 이때부터 클래스컴포넌트보다 이해하기 쉽고 사용하기 쉬운 함수 컴포넌트를 더 많이 사용하기 시작했습니다. </p>
<p>앞서 6장에서 사용했던 useState도 리액트 훅의 일종인데요. 리액트 훅이란 이를 포함해 useEffect, useContext 등을 사용해 함수 컴포넌트에서도 클래스 컴포넌트의 상태 관리, 생명주기(LifeCycle) 함수를 사용할 수 있게 해주는 방법을 말합니다. </p>
<p><img alt="리액트 클래스 컴포넌트 공식문서" src="https://velog.velcdn.com/images/so356hot/post/81a09c7c-b485-4432-804c-d667aec3925e/image.png" />
공식문서 상단에 대문짝만하게 리액트에서 함수형 컴포넌트를 권장하고 있지만, 제거할 계획을 하고 있지 않아보이고, 이는 개발을 하면서 언젠간 클래스 컴포넌트를 만나게 될 것임을 어쩌면 암시를 하고 있는 것 같습니다. 그래서 클래스 컴포넌트로 주로 개발을 하지 않더라도 방법 정도는 익혀두는 게 좋을 것 같다는 생각이 듭니다.  </p>
<br />

<h3 id="span-stylebackground-colorlavender프로젝트-준비span"><span style="background-color: lavender;">프로젝트 준비</span></h3>
<p>책에서는 프로젝트 생성을 연습하기 위해 새 프로젝트를 만들었지만, 저는 6장에서 CRA로 만든 프로젝트를 VITE로 마이그레이션을 방금 했기 때문에 그대로 사용하려 합니다. </p>
<p>CRA → VITE, jest → vitest로 마이그레이션을 했으니 chap_7의 프로젝트만 참고하시면 될 것 같습니다. </p>
  <br />

<h3 id="span-stylebackground-colorlavender개발span"><span style="background-color: lavender;">개발</span></h3>
<p>함수 컴포넌트를 클래스 컴포넌트로 리팩토링을 해보겠습니다. </p>
<p>typescript를 사용하는 경우, 부모 컴포넌트로부터 전달받을 Props와 컴포넌트 안에서 사용할 State의 타입을 미리 interface로 지정해야 하지만, 이 Button 컴포넌트는 아직 State를 사용하지 않으므로 생략했습니다. </p>
<p>수정 후 로컬에서 컴포넌트가 잘 렌더링 되는 걸 확인합니다. </p>
<p><strong><span style="background-color: yellow;">Button 컴포넌트</span></strong></p>
<pre><code class="language-jsx">// ./src/Components/Button/index.tsx
import React, {Component} from &quot;react&quot;;
import Styled from &quot;styled-components&quot;;

interface ContainerProps {
  readonly backgroundColor: string; // 대소문자 수정
  readonly hoverColor: string;      // 대소문자 수정
}

interface Props {
  readonly label: string;
  readonly backgroundColor?: string;  // 대소문자 수정
  readonly hoverColor?: string;       // 대소문자 수정
  readonly onClick?: () =&gt; void;
}

const Container = Styled.button&lt;ContainerProps&gt;`
  text-align: center;
  background-color: ${(props) =&gt; props.backgroundColor};  // 스타일로 변환됨
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  &amp;:hover {
    background-color: ${(props) =&gt; props.hoverColor};  // 스타일로 변환됨
  }
  &amp;:active {
    box-shadow: inset 5px 5px 10px rgba(0, 0, 0, 0.2);
  }
`;

const Label = Styled.div`
  color: #FFFFFF;
  font-size: 16px;
`;

export class Button extends Component&lt;Props&gt; {
  render() {
    const {
      label, backgroundColor = '#304FFE', hoverColor='#1E40FF', onClick
    } = this.props;

    return (
      &lt;Container backgroundColor={backgroundColor} hoverColor={hoverColor} onClick={onClick}&gt;
      &lt;label&gt;{label}&lt;/label&gt;
      &lt;/Container&gt;
    )
  }
}</code></pre>
<blockquote>
<p>클래스 컴포넌트 속성</p>
</blockquote>
<ul>
<li><code>render()</code> 함수: 화면에 표시되는 부분</li>
<li>함수의 매개변수 전달 방식: <code>this.props</code>로 부모 컴포넌트로부터 전달받은 Props에 접근 후, 자바스크립트의 구조분해할당을 통해 데이터 할당해 사용</li>
</ul>
<br />

<p><strong><span style="background-color: yellow;">Input 컴포넌트</span></strong></p>
<pre><code class="language-jsx">// ./src/Components/Input/index.tsx
import React, { Component } from &quot;react&quot;;
import Styled from &quot;styled-components&quot;;

interface Props {
  readonly placeholder?: string;
  readonly value?: string;
  readonly onChange?: (text: string) =&gt; void;
}

const InputBox = Styled.input`
  flex: 1;
  font-size: 16px;
  padding: 10px 10px;
  border-radius: 8px;
  border: 1px solid #BDBDBD;
  outline: none;
`;

export class Input extends Component&lt;Props&gt; {
  render() {
    const {placeholder, value, onChange} = this.props;
    return (
      &lt;InputBox
      placeholder={placeholder}
      value={value}
      onChange={(event) =&gt; {
        if (onChange) {
          onChange(event.target.value)
        }
      }}
      /&gt;
    )
  }
}</code></pre>
<br />

<p><strong><span style="background-color: yellow;">ToDoItem 컴포넌트</span></strong></p>
<pre><code class="language-jsx">// ./src/Components/ToDoItem/index.tsx
import React, { Component } from &quot;react&quot;;
import Styled from &quot;styled-components&quot;;

import { Button } from &quot;Components/Button&quot;;

interface Props {
  readonly label: string;
  readonly onDelete?: () =&gt; void;
}

const Container = Styled.div`
  display: flex;
  border-bottom: 1px sold #BDBDBD;
  align-items: center;
  margin: 10px;
  padding: 10px;
`;

const Label = Styled.div`
  flex: 1;
  font-size: 16px;
  margin-right: 20px;
`;

export class TodoItem extends Component&lt;Props&gt; {
  render() {
    const {label, onDelete} = this.props;
    return (
      &lt;Container&gt;
        &lt;label&gt;{label}&lt;/label&gt;
        &lt;Button label=&quot;삭제&quot; backgroundColor=&quot;#FF1744&quot; hoverColor=&quot;#F01440&quot; onClick={onDelete} /&gt;
      &lt;/Container&gt;
    )
  }
}</code></pre>
<br />

<p><strong><span style="background-color: yellow;">App 컴포넌트</span></strong></p>
<p>위에서 Button, Input, ToDoItem 컴포넌트들은 state 없이 props만 전달받아 클래스 컴포넌트로 변경해주었는데요. App 컴포넌트에서는 State를 사용하는 클래스 컴포넌트로 리팩토링 해보겠습니다. </p>
<p>App은 부모 컴포넌트로 받는 Props는 없지만, 클래스 컴포넌트를 만들기 위해 빈 Props를 선언해주었고 함수 컴포넌트에서 useState를 사용해 만든 State 데이터에 관한 타입을 정의했습니다. </p>
<pre><code class="language-jsx">// ./src/App.tsx
import { Button, Input, ToDoItem } from &quot;Components/index&quot;;
import React, { Component, useState } from &quot;react&quot;;
import Styled from &quot;styled-components&quot;;


const Container = Styled.div`
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
`;

const Contents = Styled.div`
  display: flex;
  background-color: #FFFFFF;
  flex-direction: column;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2);
`;

const ToDoListContainer = Styled.div`
  min-width: 350px;
  height: 400px;
  overflow-y: scroll;
  border: 1px solid #BDBDBD;
  margin-bottom: 20px;
`;

interface Props {};
interface State {
  readonly toDo: string;
  readonly toDoList: string[];
}

class App extends Component&lt;Props, State&gt; {
  constructor(props:Props) {
    super(props)

    this.state = {
      toDo: '',
      toDoList: []
    }
  }

// 클래스 컴포넌트 내부에서 `addToDo`, 'deleteToDo` 같이 함수를 정의할 때는 클래스 함수로 정의해야 하고, 특별한 이유가 없다면 private으로 설정합니다. 
  private addToDo = (): void =&gt; {
// Props에 있는 변수에 접근할 때 this를 사용했듯이 State로 동일하게 State에 할당된 변수에 접근할 때 this를 사용합니다. 
    const {toDo, toDoList} = this.state;
    if(toDo) {
 // State는 불변 데이터이기 때문에 State값을 변경하려면 Set함수를 이용해야 합니다. 다만 useState와 다르게 함수명을 임의로 설정할 수 없고, `this.setState` 함수만을 사용합니다. 
      this.setState({
        toDo: '',
        toDoList: [...toDoList, toDo]
      })
    }
  }


    private deleteToDo = (index: number): void =&gt; {
      let list = [...this.state.toDoList];
      list.splice(index, 1)
      this.setState({
        toDoList: list,
      })
  }

  render() {
    const {toDo, toDoList} = this.state;

    return (
      &lt;Container&gt;
        &lt;Contents&gt;
          &lt;ToDoListContainer data-testid=&quot;toDoList&quot;&gt;
            {toDoList.map((item, index) =&gt; (
              &lt;ToDoItem key={item} label={item} onDelete={() =&gt; this.deleteToDo(index)} /&gt;
            ))}
          &lt;/ToDoListContainer&gt;
          &lt;Input
          placeholder=&quot;할 일을 입력해 주세요.&quot;
          value={toDo}
          onChange={(text) =&gt; this.setState({ toDo: text})} /&gt;
{* 이렇게 정의한 클래스 함수는 클래스 내에서 사용할 수 있고, 사용할 때도 `this`를 사용해 호출합니다. *}
          &lt;Button label=&quot;추가&quot; onClick={this.addToDo} /&gt;
        &lt;/Contents&gt;
      &lt;/Container&gt;
    )
  }
}

export default App;</code></pre>
<blockquote>
<p><strong>함수형 useState와 클래스 State 차이</strong></p>
</blockquote>
<ul>
<li>함수 컴포넌트: <code>useState</code>로 필요할 때마다 정의</li>
<li>클래스 컴포넌트: 컴포넌트에서 사용하는 모든 State를 하나의 State로 관리 </li>
</ul>
<br />

<h3 id="span-stylebackground-colorlavender라이프-사이클-함수span"><span style="background-color: lavender;">라이프 사이클 함수</span></h3>
<p>클래스 컴포넌트는 함수 컴포넌트와 다르게 <strong>라이프 사이클 함수</strong>들을 갖고 있습니다. 이 라이프 사이클 함수를 잘 이해하면 클래스 컴포넌트를 좀 더 효율적으로 활용할 수 있다는데요. 리액트의 모든 라이프 사이클 함수를 App 컴포넌트에 적용한 예제를 살펴보겠습니다. </p>
<pre><code class="language-jsx">// src/App.tsx
import { Button, Input, ToDoItem } from &quot;Components/index&quot;;
import React, { Component } from &quot;react&quot;;
import Styled from &quot;styled-components&quot;;
import type { IScriptSnapshot } from &quot;typescript&quot;;


const Container = Styled.div`
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
`;

const Contents = Styled.div`
  display: flex;
  background-color: #FFFFFF;
  flex-direction: column;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2);
`;

const ToDoListContainer = Styled.div`
  min-width: 350px;
  height: 400px;
  overflow-y: scroll;
  border: 1px solid #BDBDBD;
  margin-bottom: 20px;
`;

interface Props {};
interface State {
  readonly toDo: string;
  readonly toDoList: string[];
}

class App extends Component&lt;Props, State&gt; {
  /** constructor 함수
   * 클래스 컴포넌트는 클래스이므로 생성자 함수 존재
   * 그러나 클래스 컴포넌트에서 State를 사용하지 않아 상태 초기값이 필요하지 않다면 생성자 함수 생략 가능
   * 생성자 함수를 사용할 땐 반드시 super(props) 함수를 호출해서 부모 클래스의 생성자를 호출해야 함
   * 생성자 함수는 해당 컴포넌트가 생성될 때 한 번만 호출됨
   */
  constructor(props:Props) {
    super(props)

    this.state = {
      toDo: '',
      toDoList: []
    }
  }

  private addToDo = (): void =&gt; {
    const {toDo, toDoList} = this.state;
    if(toDo) {
      this.setState({
        toDo: '',
        toDoList: [...toDoList, toDo]
      })
    }
  }


    private deleteToDo = (index: number): void =&gt; {
      let list = [...this.state.toDoList];
      list.splice(index, 1)
      this.setState({
        toDoList: list,
      })
  }

  /** render 함수
   * 이 함수는 클래스 함수가 렌ㄷ링되는 부분 (화면에 표시되는 부분)을 정의
   * 즉, 이 render 함수의 반환값이 화면에 표시됨
   * render함수는 부모 컴포넌트로부터 받는 Props값이 변경, 또는 this.setState에 의해 State 값이
   * 변경되어 화면 갱신 필요가 있을 때마다 호출됨
   * 
   * 따라서 render함수에서 this.setState를 사용해 직접 상태값을 바꿀 경우 무한 루프에 빠질 위험 주의
   * 이 예제에서는 클릭 이벤트와 연결하여 클릭 이벤트가 발생할 때만 this.setState가 호출되므로 무한루프 가능성 제거
   */
  render() {
    const {toDo, toDoList} = this.state;

    return (
      &lt;Container&gt;
        &lt;Contents&gt;
          &lt;ToDoListContainer data-testid=&quot;toDoList&quot;&gt;
            {toDoList.map((item, index) =&gt; (
              &lt;ToDoItem key={item} label={item} onDelete={() =&gt; this.deleteToDo(index)} /&gt;
            ))}
          &lt;/ToDoListContainer&gt;
          &lt;Input
          placeholder=&quot;할 일을 입력해 주세요.&quot;
          value={toDo}
          onChange={(text) =&gt; this.setState({ toDo: text})} /&gt;
          &lt;Button label=&quot;추가&quot; onClick={this.addToDo} /&gt;
        &lt;/Contents&gt;
      &lt;/Container&gt;
    )
  }

  /** getDerivedStateFromProps 함수
   * 이 함수는 부모로부터 받은 Props와 State를 동기화할 때 사용됨
   * 부모로부터 받은 Props로 State에 값을 설정하거나, State값이 Props에 의존하여 결정될 때 사용
   * 
   * State에 설정하고 싶은 값을 반환해주고, 동기화할 State가 없으면 null을 반환하면 됨
   */
  static getDerivedStateFromProps(nextProps: Props, prevState: State) {
    console.log('getDerivedStateFromProps')

    return null
  }

  /** componentDidMount 함수
   * 클래스 컴포넌트가 처음으로 화면에 표시된 이후에 호출됨
   * 즉, render 함수가 처음 한 번 호출된 후 이 함수가 호출됨
   * 
   * 컴포넌트가 화면에 처음 표시된 후 한 번만 호출되므로 ajax를 통한 데이터 습득이나 js 라이브러리와의 연동 수행할 때 주로 사용
   * 
   * Props나 this.setState로 State값이 바뀌어도 다시 호출 x
   * 
   * 따라서 render 함수와는 다르게 이 함수에 this.setState를 직접 호출할 수 있으며 
   * ajax를 통해 서버로부터 전달받은 데이터를 this.setState를 사용해 State에 설정하기 가장 적합
   */
  componentDidMount() {
    console.log('componentDidMount');
  }

  /** getSnapshotBeforeUpdate 함수
   * Props, State가 변경돼 화면을 다시 그리기 위해 render 함수가 호출된 후 
   * 실제로 화면이 갱신되기 직전에 이 함수가 호출됨
   * 
   * 반환값은 다음 함수인 componentDidUpdate의 세번째 매개변수로 전달됨
   * 
   * 자주는 사용 x, 화면 갱신 중 수동으로 스크롤 위치 고정하는 경우 등에 사용
   */
  getSnapshotBeforeUpdate(prevProps: Props, prevState: State) {
    console.log('getSnapshotBeforeUpdate');

    return {
      testData: true,
    }
  }

  /** componentDidUpdate 함수
   * componentDidMount 함수는 컴포넌트가 처음 화면에 표시된 후 실행되고 두 번 다시 호출되지 않는다고 했는데,
   * 반대로 이 함수는 컴포넌트가 처음 화면에 표시될 땐 실행이 안되지만, Props나 State가 변경돼 
   * 화면에 갱신될 때마다 render 함수가 호출된 후 호출됨 
   * 
   * 얘도 자주 사용은 안되지만 스크롤을 수동으로 고정할 때 getSnapshotBeforeUpdate랑 같이 쓰임
  */
  componentDidUpdate(prevProps: Props, prevState: State, snapshot: IScriptSnapshot) {
    console.log('componentDidUpdate');
  }

  /** shouldComponentUpdate 함수
   * 클래스 컴포넌트를 기본적으로 부모 컴포넌트로부터 받은 Props, State 변경 시 리렌더링돼 화면을 다시 그리는데, 
   * 값은 변경돼도 화면을 다시 그리고 싶지 않을 때 이 함수 사용하여 렌더링 제어
   * 
   * return false를 해주면 리렌더링을 방지
   * 
   * ※ 리렌더링 방지 이유: 렌더링 최적화를 위함
   */
  shouldComponentUpdate(nextProps: Props, nextState: State) {
    console.log('shouldComponentUpdate');
    return true    
  }

  /** componentWillUnmount 함수
   * 해당 컴포넌트가 화면에서 완전히 사라진 후 호출되는 함수
   * 보통 componentDidMount에서 연동한 자바스크립트 라이브러리를 해지하거나 setTimeout, setInterval 등의
   * 타이머를 clearTimeout, clearInterval을 사용해 해제할 때 사용됨
   */
  componentWillUnmount() {
    console.log('componentWillUnmount');
  }

  /** componentDidCatch 함수
   * render 함수에서 jsx 문법을 사용해 컴포넌트 렌더링 하는 부분에선 try-catch를 ㅅ용할 수 없음
   * 그래서 render 함수의 jsx에서 발생하는 에러의 예외처리할 수 있게 도와주는 라이프사이클 함수가 이 함수임
   * 
   * render 함수의 return 부분에서 에러 발생 시, 이 함수 실행됨
   */
  componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
    // this.setState({
    // error: true,
    // })
  }
}

export default App;</code></pre>
<blockquote>
<p><strong>호출 순서</strong></p>
</blockquote>
<ul>
<li><strong>컴포넌트가 생성될 때</strong>
<code>constructor</code> → <code>getDerivedStateFromProps</code> → <code>render</code> → <code>componentDidMount</code></li>
<li><strong>컴포넌트의 Props가 변경될 때</strong>
<code>getDerivedStateFromProps</code> → <code>shouldComponentUpdate</code> → <code>render</code> → <code>getSnapshotBeforeUpdate</code> → <code>componentDidUpdate</code></li>
<li><strong>컴포넌트의 State가 변경될 때</strong>
<code>shouldComponentUpdate</code> → <code>render</code> → <code>getSnapshotBeforeUpdate</code> → <code>componentDidUpdate</code></li>
<li><strong>컴포넌트 렌더링 중 에러 발생할 때</strong>
<code>componentDidCatch</code></li>
<li><strong>컴포넌트가 화면에서 제거될 때</strong>
<code>componentWillUnmount</code></li>
</ul>
<br />

<h3 id="span-stylebackground-colorlavender테스트-해보기span"><span style="background-color: lavender;">테스트 해보기</span></h3>
<p>우선 지금까지 작성한 할 일 목록 앱을 클래스 컴포넌트로 리팩토링 해보았는데요. 이를 테스트 하기 위해 아래 코드는 잠시 주석처리를 해줍니다. 
그리고 저는 jest 대신 vitest를 쓰고 있으므로 <code>npx vitest --update</code>로 스냅샷 업데이트를 해주었습니다. </p>
<pre><code class="language-jsx">  // static getDerivedStateFromProps(nextProps: Props, prevState: State) {
  //   console.log('getDerivedStateFromProps')

  //   return null
  // }

  // componentDidMount() {
  //   console.log('componentDidMount');
  // }

  // getSnapshotBeforeUpdate(prevProps: Props, prevState: State) {
  //   console.log('getSnapshotBeforeUpdate');

  //   return {
  //     testData: true,
  //   }
  // }

  // componentDidUpdate(prevProps: Props, prevState: State, snapshot: IScriptSnapshot) {
  //   console.log('componentDidUpdate');
  // }

  // shouldComponentUpdate(nextProps: Props, nextState: State) {
  //   console.log('shouldComponentUpdate');
  //   return true    
  // }

  // componentWillUnmount() {
  //   console.log('componentWillUnmount');
  // }

  // componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
    // this.setState({
    // error: true,
    // })
  // }</code></pre>
<p>그럼 아래와 같이 테스트가 잘 통과하는 것을 볼 수 있습니다. 
<img alt="클래스 컴포넌트 리팩토링 후 테스트" src="https://velog.velcdn.com/images/so356hot/post/41095487-dc2f-4838-9019-2fa1481d552c/image.png" /></p>
<hr />
<h2 id="✨-8-context-api와-localstorage">✨ 8. Context API와 localStorage</h2>
<p>리액트에서 데이터를 다루는 방법으로는 크게</p>
<blockquote>
<ul>
<li>Props</li>
</ul>
</blockquote>
<ul>
<li>State</li>
<li><strong>Context</strong></li>
</ul>
<p>가 존재합니다. 이번엔 <strong>Context API</strong>를 통해 컨텍스트를 다루는 방법에 대해 알아보려 합니다. </p>
<p>또한 보통 웹 서비스에서 데이터는 DB에 저장하기 때문에 데이터를 저장하는 <strong>타이밍</strong>이나 <strong>데이터를 저장하는 방법</strong>에 대해서 공부할 필요가 있기 때문에 <strong>localStorage</strong>를 사용해 서버에 데이터를 저장하듯이 브라우저에 데이터를 저장하고 가져오는 방법에 대해 알아보겠습니다.</p>
<h3 id="span-stylebackground-colorlavendercontext-apispan"><span style="background-color: lavender;">Context API</span></h3>
<p>리액트에서 Props와 State는 부모 컴포넌트와 자식 컴포넌트, 또는 한 컴포넌트 안에서 데이터를 다루기 위해 사용됩니다. 이 Props와 State는 부모 컴포넌트 → 자식 컴포넌트. 즉, 위에서 아래로 단방향으로 데이터가 흐르게 됩니다. 
<img alt="Props와 State" src="https://velog.velcdn.com/images/so356hot/post/58edf04f-d948-4358-aa2c-589cd3657fb0/image.png" /></p>
<p>그런데 말입니다. 만약 다른 컴포넌트에서 한쪽으로 흐르고 있는 데이터를 사용하고 싶은 상황이 발생한다면 어떻게 될까요?
<img alt="다른 컴포넌트에서 데이터 사용" src="https://velog.velcdn.com/images/so356hot/post/dd991abd-d301-4fb1-bd61-a8cb06c3b85a/image.png" /></p>
<p>데이터는 위 → 아래, 한쪽으로 흐르기 때문에 데이터를 사용할 위치에 공통 부모 컴포넌트에 State를 만들고 Props로 전달하여야 합니다. </p>
<p>그러나 매번 이 과정을 거치게 되면 매우 비효율적일 것 같은데요. 이 문제를 해결하기 위해 리액트에서는 <strong>Flux</strong>라는 개념을 도입하였고, 그에 걸맞는 <strong>Context API</strong>를 제공하기 시작했습니다. </p>
<p><img alt="Context API" src="https://velog.velcdn.com/images/so356hot/post/d4ad52b9-d6d2-4af5-b157-c9eff71c6667/image.png" /></p>
<p>컨텍스트는 부모 컴포넌트로부터 자식 컴포넌트로 전달되는 데이터 흐름과는 상관없이 &quot;전역적으로&quot; 데이터를 다룹니다. 전역 데이터를 컨텍스트에 저장한 후, 필요한 컴포넌트에서 해당 데이터를 불러와 사용할 수 있는 것이죠.</p>
<p>컨텍스트를 사용하기 위해선 Context API를 사용해 컨텍스트의 <strong>프로바이더(Provider)</strong>와 <strong>컨슈머(Consumer)</strong>를 생성해야 합니다. 
컨텍스트에 저장된 데이터를 사용하기 위해선 공통 부모 컴포넌트에 컨텍스트 프로바이더를 사용해 데이터를 제공해야 하고, 데이터를 사용하려는 컴포넌트에 컨슈머를 사용해 실제 데이터를 사용합니다. </p>
<p><img alt="Context의 Provider, Consumer" src="https://velog.velcdn.com/images/so356hot/post/401ab77d-ee62-4b53-aee6-bcf31c55d037/image.png" /></p>
<p>지금부터 앞에서 만든 할 일 목록 앱에 Context API를 적용하여 전역 데이터를 다루는 컨텍스트를 생성하고 활용해 봅시다.</p>
<br />

<h3 id="span-stylebackground-colorlavender프로젝트-준비span-1"><span style="background-color: lavender;">프로젝트 준비</span></h3>
<p>책에서는 새 프로젝트를 만들고 있지만, 저는 chap_7을 복사해서 그대로 사용하되, 클래스 컴포넌트 대신 함수 컴포넌트로 바꾸어 프로젝트를 실행하겠습니다.</p>
<p>함수 컴포넌트로 바꾼 후, 터미널에 <code>npx vitest --update</code>을 입력하여 테스트가 문제없이 통과되는 걸 확인해줍니다. </p>
<br />

<h3 id="span-stylebackground-colorlavender개발span-1"><span style="background-color: lavender;">개발</span></h3>
<p>준비가 다 되었다면 컨텍스트를 사용할 수 있도록 할 일 목록 앱을 조금 수정해 줍니다. 
그림으로 목록의 구조를 살펴보겠습니다. </p>
<p><img alt="할 일 목록 앱 구조" src="https://velog.velcdn.com/images/so356hot/post/f244fdfa-7964-43af-b1fa-34710a11b95b/image.png" /></p>
<p>현재의 목록 앱은 App 컴포넌트 안에 ToDo 데이터와 ToDoList 데이터가 존재하며, Input 컴포넌트와 Button 컴포넌트, ToDoItem 컴포넌트를 사용해 할 일을 추가하거나 목록을 표시하고 있습니다. </p>
<p>이제 컨텍스트를 프로바이더, 컨슈머를 사용하여 Context API 사용법을 확인하기 위해 구조를 아래와 같이 바꿔줍니다. </p>
<p><img alt="할 일 목록 앱 구조 변경" src="https://velog.velcdn.com/images/so356hot/post/0ced1fee-7f51-49ba-b3e2-a138bdf7b644/image.png" /></p>
<p><img alt="할 일 목록 앱에 컨텍스트 추가" src="https://velog.velcdn.com/images/so356hot/post/c6e8943b-6d3b-4407-8266-b1e771c11bef/image.png" /></p>
<p><strong><span style="background-color: yellow;">InputContainer 컴포넌트</span></strong>
<code>./src/Components/InputContainer.tsx</code> 파일을 생성해줍니다. </p>
<pre><code class="language-jsx">import React from 'react'
import styled from 'styled-components';

import { Button } from 'Components/Button'
import { Input } from 'Components/Input'


const Container = styled.div`
  display: flex;
`

interface Props {
  readonly toDo?: string;
  readonly onChange?: (text: string) =&gt; void;
  readonly onAdd?: () =&gt; void;
}

export const InputContainer = ({ toDo, onChange, onAdd}: Props) =&gt; {
  return (
    &lt;Container&gt;
    &lt;Input placeholder='할 일을 입력해 주세요.' value={toDo} onChange={onChange} /&gt;
    &lt;Button label='추가' onClick={onAdd} /&gt;
    &lt;/Container&gt;
  )
}</code></pre>
<br />

<p><strong><span style="background-color: yellow;">ToDoList 컴포넌트</span></strong>
<code>./src/Components/ToDoList.index.tsx</code> 파일을 만들어줍니다. </p>
<pre><code class="language-jsx">import React from &quot;react&quot;;
import styled from &quot;styled-components&quot;;

import { ToDoItem } from &quot;Components/ToDoItem&quot;;

const Container = styled.div`
  min-height: 350px;
  height: 400px;
  overflow-y: scroll;
  border: 1px solid #BDBDBD;
  margin-bottom: 20px;
`

interface Props {
  readonly toDoList: string[];
  readonly deleteToDo: (index: number) =&gt; void;
}

export const ToDoList = ({ toDoList, deleteToDo}: Props) =&gt; {
  return (
    &lt;Container data-testid=&quot;toDoList&quot;&gt;
      {toDoList.map((item, index) =&gt; (
        &lt;ToDoItem key={item} label={item} onDelete={() =&gt; deleteToDo(index)} /&gt;
      ))}
    &lt;/Container&gt;
  )
}</code></pre>
<br />

<p><strong><span style="background-color: yellow;">ToDoList 컨텍스트</span></strong>
<code>./src/Contexts/ToDoList/index.tsx</code>를 만들어줍니다. </p>
<pre><code class="language-jsx">// 컨텍스트를 만들기 위해 리액트에서 `createContext`와
// 데이터를 동적으로 다루기 위한 `useState`를 불러옵니다.
import React, {createContext, JSX, useState} from 'react'

// 컨텍스트로 공유할 데이터&amp;함수들을 인터페이스로 정의하고,
// 정의한 인터페이스로 컨텍스트를 생성합니다.
interface Context {
  readonly toDoList: string[];
  readonly addToDo: (toDo: string) =&gt; void;
  readonly deleteToDo: (index: number) =&gt; void;
}

const ToDoListContext = createContext&lt;Context&gt;({
  toDoList: [],
  addToDo: (): void =&gt; {},
  deleteToDo: (): void =&gt; {}
})

// 컨텍스트를 사용하기 위해서는 데이터를 공유하는 컴포넌트들의 공통 부모 컴포넌트에
// 컨텍스트 Provider를 제공해야 합니다. 
// 여기서 &quot;제공&quot;의 의미는 공통 부모 컴포넌트를 컨텍스트의 Provider 안에서 렌더링되도록 하는 것을 의미합니다. 
interface Props {
  children: JSX.Element | JSX.Element[];
}

// 컨텍스트도 하나의 리액트 컴포넌트이므로
// 렌더링해야 하는 공통 부모 컴포넌트를 Props로 전달 받고, 
// 컨텍스트의 Provider 안에서 전달받은 컴포넌트를 렌더링하도록 합니다. 
const ToDoListProvider = ({ children}: Props)=&gt; {
  // 거듭 말하지만, 컨텍스트도 컴포넌트이기 때문에
  // 동적인 데이터를 다루기 위해서는 State를 사용해야 합니다.
  const [toDoList, setToDoList] = useState&lt;string[]&gt;([])

  const addToDo = (toDo: string): void =&gt; {
    if (toDo) {
      setToDoList([...toDoList, toDo])
    }
  }

  const deleteToDo = (index: number): void =&gt; {
    let list = [...toDoList]
    list.splice(index, 1)
    setToDoList(list)
  }

  // 프로바이더를 설정할 땐 value라는 Provider의 컨텍스트로 제공할 내용을 작성해야 합니다. 
  return (
    &lt;ToDoListContext.Provider value={{ toDoList, addToDo, deleteToDo}}&gt;
      {children}
    &lt;/ToDoListContext.Provider&gt;
  )
}

export {ToDoListContext, ToDoListProvider}</code></pre>
<p>리액트에서 <strong>컨텍스트도 하나의 컴포넌트</strong>로 취급을 하기 때문에 컴포넌트를 만드는 것과 유사합니다. </p>
<br />

<p><strong><span style="background-color: yellow;">App 컴포넌트에 프로바이더 적용</span></strong>
이렇게 Context API를 사용해 전역적으로 사용할 데이터와 함수를 정의해주었습니다. </p>
<ul>
<li>할 일 목록 데이터 생성</li>
<li>할 일 목록 데이터에 데이터를 추가/삭제하기 위한 함수 정의</li>
</ul>
<p>그 다음 변경된 컴포넌트와 프로바이더를 적용하기 위해 App 컴포넌트를 다음과 같이 수정해줍니다. </p>
<pre><code class="language-jsx">import { InputContainer } from &quot;Components/InputContainer&quot;;
import { ToDoList } from &quot;Components/ToDoList&quot;;
import { ToDoListProvider } from &quot;src/Contexts/ToDoList&quot;;
import Styled from &quot;styled-components&quot;;


const Container = Styled.div`
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
`;

const Contents = Styled.div`
  display: flex;
  background-color: #FFFFFF;
  flex-direction: column;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2);
`;


function App() {
  return (
  &lt;ToDoListProvider&gt;
    &lt;Container&gt;
      &lt;Contents&gt;
        &lt;ToDoList /&gt;
        &lt;InputContainer /&gt;
      &lt;/Contents&gt;
    &lt;/Container&gt;
&lt;/ToDoListProvider&gt;
  );
}

export default App;</code></pre>
<p>ToDoList, InputContainer 컴포넌트는 더 이상 App으로부터 데이터를 전달 받는 것이 아니라, 컨텍스트 안에 있는 <strong>전역 데이터</strong>를 <strong>직접 참조</strong>할 예정이기 때문에 이 둘 컴포넌트로 전달하던 모든 Props를 제거합니다. </p>
<p>현재는 이 두 컴포넌트를 리팩토링 하지 않았으므로 에러가 발생할 것입니다. 이제부터 두 컴포넌트를 리팩토링하여 에러를 제거하고 컨텍스트의 데이터를 직접 사용해보도록 하겠습니다. </p>
<br />

<p><strong><span style="background-color: yellow;">InputContainer 컴포넌트에 컨슈머 적용</span></strong>
InputContainer는 사용자가 입력한 데이터를 다루기 위해 useState를 사용해줘야 하고, 컨텍스트를 사용하기 위해 useContext를 불러와야 합니다. </p>
<p>그리고 컨텍스트를 사용하기 위해 ToDoListContext를 가지고 왔는데, 여기서 App과는 다르게 ToDoListProvider가 아닌 ToDoListContext를 가져 왔음을 주의합니다. </p>
<blockquote>
<p>✔️ 컨텍스트 제공, 사용할 때</p>
</blockquote>
<ul>
<li>컨텍스트를 제공한다: Provider 사용</li>
<li>컨텍스트를 사용한다: Context를 직접 사용</li>
</ul>
<pre><code class="language-jsx">import React, { useContext, useState } from 'react'
import styled from 'styled-components';

import { Button } from 'Components/Button'
import { Input } from 'Components/Input'

import { ToDoListContext } from 'src/Contexts/ToDoList';

const Container = styled.div`
  display: flex;
`

export const InputContainer = () =&gt; {
  const [toDo, setToDo] = useState('')
  const { addToDo} = useContext(ToDoListContext)

  return (
    &lt;Container&gt;
    &lt;Input placeholder='할 일을 입력해 주세요.' value={toDo} onChange={setToDo} /&gt;
    &lt;Button label='추가' onClick={() =&gt; {addToDo(toDo); setToDo('');}} /&gt; 
    &lt;/Container&gt;
  )
}</code></pre>
<br />

<p><strong><span style="background-color: yellow;">ToDoList 컴포넌트에 컨슈머 적용</span></strong>
이 컴포넌트도 마찬가지로 앞으로 App 컴포넌트에서 Props로 데이터를 받지 않고 컨텍스트 데이터를 직접 참조할 것이기 때문에 아래와 같이 수정해줍니다. </p>
<pre><code class="language-jsx">import React, { useContext } from &quot;react&quot;;
import styled from &quot;styled-components&quot;;

import { ToDoItem } from &quot;Components/ToDoItem&quot;;

import { ToDoListContext } from &quot;src/Contexts/ToDoList&quot;;

const Container = styled.div`
  min-height: 350px;
  height: 400px;
  overflow-y: scroll;
  border: 1px solid #BDBDBD;
  margin-bottom: 20px;
`

export const ToDoList = () =&gt; {
  const { toDoList, deleteToDo} = useContext(ToDoListContext);

  return (
    &lt;Container data-testid=&quot;toDoList&quot;&gt;
      {toDoList.map((item, index) =&gt; (
        &lt;ToDoItem key={item} label={item} onDelete={() =&gt; deleteToDo(index)} /&gt;
      ))}
    &lt;/Container&gt;
  )
}</code></pre>
<br />

<h3 id="span-stylebackground-colorlavenderlocalstoragespan"><span style="background-color: lavender;">localStorage</span></h3>
<p>위에서 Context API로 데이터를 전역으로 관리하는 방법에 대해서 알아보았습니다. 이제 이 전역으로 관리되는 데이터를 외부에 저장하는 방법에 대해 알아보겠습니다. </p>
<p>보통의 웹 서비스에서는 데이터를 API를 이용해 서버에 저장하고 가져오는데요. localStorage에 데이터를 저장하고 가져오는 타이밍과, API를 통해 서버에 데이터를 저장하고 가져오는 타이밍이 갖기 때문에 API로 서버에 저장하고 가져오는 것을 연습할 수 있습니다. </p>
<p>localStorage를 사용해 할 일 리스트 데이터를 브라우저에 저장하고 가져오기 위해 <code>./src/Contexts/ToDoList/index.tsx</code> 파일을 수정해줍니다. </p>
<pre><code class="language-jsx">import React, {createContext, JSX, useEffect, useState} from 'react'

interface Context {
  readonly toDoList: string[];
  readonly addToDo: (toDo: string) =&gt; void;
  readonly deleteToDo: (index: number) =&gt; void;
}

const ToDoListContext = createContext&lt;Context&gt;({
  toDoList: [],
  addToDo: (): void =&gt; {},
  deleteToDo: (): void =&gt; {}
})

interface Props {
  children: JSX.Element | JSX.Element[];
}

const ToDoListProvider = ({ children}: Props): JSX.Element=&gt; {
  const [toDoList, setToDoList] = useState&lt;string[]&gt;([])

  const addToDo = (toDo: string): void =&gt; {
    if (toDo) {
      const newList = [...toDoList, toDo]
      localStorage.setItem('ToDoList', JSON.stringify(newList))
      setToDoList([...toDoList, toDo])
    }
  }

  const deleteToDo = (index: number): void =&gt; {
    let list = [...toDoList]
    list.splice(index, 1)
    localStorage.setItem('ToDoList', JSON.stringify(list))
    setToDoList(list)
  }

  // 우선 localStorage에 저장된 데이터를 가져와 화면에 표시하기 위해선 useEffect 훅을 사용해야 합니다. 
  // 두 번째 매개변수엔 빈 배열을 전달하여 컴포넌트가 화면에 표시된 후 한 번만 호출되게 합니다. 
  useEffect(() =&gt; {
    const list = localStorage.getItem('ToDoList')
    if(list) {
      // localStorage에는 문자열 데이터만 저장할 수 있습니다.
      // 따라서 저장한 문자열을 우리가 원하는 배열 데이터로 변경하기 위해 JSON.parse를 사용해줍니다. 
      setToDoList(JSON.parse(list))
    }
  }, [])

  return (
    &lt;ToDoListContext.Provider value={{ toDoList, addToDo, deleteToDo}}&gt;
      {children}
    &lt;/ToDoListContext.Provider&gt;
  )
}

export {ToDoListContext, ToDoListProvider}</code></pre>
<br />

<h3 id="span-stylebackground-colorlavenderuseeffect-훅span"><span style="background-color: lavender;">useEffect 훅</span></h3>
<p>위에서 useEffect를 이용해서 컴포넌트의 생명 주기를 관리해주었는데요. 이 훅은 7장에서 다뤘던 클래스 컴포넌트 라이프 사이클 함수인 componentDidMount 함수와 비슷한 역할을 합니다. </p>
<p>리액트에서는 componentDidMount보다 useEffect 훅을 많이 쓰기 때문에 이 훅의 구조를 한 번 살펴보겠습니다. </p>
<h4 id="✔️-두-번째-매개변수-공간에-빈-배열-전달할-때">✔️ 두 번째 매개변수 공간에 빈 배열 전달할 때</h4>
<pre><code class="language-jsx">useEffect(() =&gt; {
  ...
}, [])</code></pre>
<p>첫 번째 매개변수 공간에는 콜백 함수를 설정해 useEffect의 역할을 정의합니다. 
두 번째 매개변수 공간에는 배열을 전달하는데, 우리가 앞서 사용한 것처럼 빈 배열을 전달하게 되면 componentDidMount와 같은 역할을 하여 <strong>컴포넌트가 처음 화면에 표시된 후</strong>에 이 useEffect는 <strong>한 번만</strong> 호출되게 됩니다. </p>
<br />

<h4 id="✔️-두-번째-매개변수-공간에-아무것도-설정하지-않을-때">✔️ 두 번째 매개변수 공간에 아무것도 설정하지 않을 때</h4>
<pre><code class="language-jsx">useEffect(() =&gt; {
  ...
});</code></pre>
<p>위의 코드처럼 useEffect의 두 번째 매개변수를 설정하지 않는 경우, componentDidMount와 componentDidUpdate의 역할을 동시에 수행하며, 이는 <strong>컴포넌트가 처음 화면에 표시된 후에도 실행</strong>되며, <strong>Props나 State의 변경으로 컴포넌트가 리렌더링된 후에도 실행</strong>됩니다. </p>
<br />

<h4 id="✔️-두-번째-매개변수-공간에-아무것도-설정하지-않고-첫-번째-매개변수-함수가-함수를-반환할-때">✔️ 두 번째 매개변수 공간에 아무것도 설정하지 않고, 첫 번째 매개변수 함수가 함수를 반환할 때</h4>
<pre><code class="language-jsx">useEffect(() =&gt; {
  ...
  return () =&gt; {
    ...
  };
});</code></pre>
<p>useEffect 함수의 역할을 정의하는 첫 번째 매개변수 함수는 <strong>함수를 반환</strong>할 수 있습니다. 이 반환하는 함수는 componentWillUnmount와 같은 역할을 하며, <strong>컴포넌트가 화면에서 사라진 후 이 함수가 호출</strong>되며, <strong>라이브러리와의 연동을 해제하거나, 타이머를 해제하는 데 사용</strong>됩니다. </p>
<br />

<h4 id="✔️-useeffect만의-고유한-기능">✔️ useEffect만의 고유한 기능</h4>
<pre><code class="language-jsx">useEffect(() =&gt; {
  ...
}, [toDoList]);</code></pre>
<p><strong>useEffect의 두 번째 매개변수로 배열을 전달</strong>할 수 있습니다. 두 번째 매개변수 배열에 특정 변수를 설정해 전달하면 모든 Props와 State 변경에 호출되는 componentDidUpdate와 다르게 <strong>전달된 변수가 변경될 때만</strong> 이 함수가 호출되도록 설정할 수 있습니다. </p>
<p>즉, 두 번째 매개변수로 toDoList를 전달하는 위의 useEffect는 컴포넌트가 화면에 표시된 후 한 번 호출되며, toDoList 값에 변경 사항이 발생하면, 이 변경 사항을 감지하고 useEffect의 콜백 함수를 실행하게 됩니다. </p>
<p>또한 useEffect는 클래스 컴포넌트의 라이프 사이클 함수와 다르게 <strong>한 컴포넌트 안에서 여러 번 정의</strong>해 사용할 수 있습니다.</p>
<br />

<h3 id="span-stylebackground-colorlavender테스트span"><span style="background-color: lavender;">테스트</span></h3>
<p>지금까지 Context API와 localStorage를 사용해 할 일 목록 앱을 리팩토링해 보았습니다. 이제 이 할 일 목록 앱을 테스트 하기 위한 <strong>테스트 명세</strong>를 작성해보도록 하겠습니다. </p>
<p>우선 현재 실행 중인 <code>npm start</code> 명령어를 취소하고 <code>npm run test</code>로 테스트 코드를 실행합니다. </p>
<p>스냅샷 업데이트가 안돼 에러가 발생한다면 <code>npx vitest --update</code>로 업데이트 해줍니다. </p>
<p>다 통과가 됐다면 이제 테스트 코드를 추가할 준비가 되었으니 새롭게 추가한 컴포넌트에 테스트 명세를 추가합니다.</p>
<p><strong><span style="background-color: yellow;">ToDoList 컨텍스트</span></strong>
<code>./src/Contexts/ToDoList/index.test.tsx</code> 파일을 만들어줍니다.</p>
<pre><code class="language-jsx">import React, { useContext } from 'react';
import { fireEvent, render, screen } from '@testing-library/react';

import { ToDoListContext, ToDoListProvider } from 'src/Contexts/ToDoList';

// beforeEach는 각각의 테스트 명세가 실행되기 전에 실행되는 함수로,
// 각 테스트 명세가 실행되기 전에 준비해야 할 내용을 작성할 때 사용합니다.
beforeEach(() =&gt; {
  // localStorage는 데이터를 영구적으로 저장하므로
  // 항상 깨끗이 지우지 않는다면 테스트가 의도된 바와 다르게 동작할 수 있습니다.
  localStorage.clear();
});

describe('ToDoList Context', () =&gt; {
  it('renders component correctly', () =&gt; {
    // 우리가 만든 컨텍스트는 children이라는 필수 props를 갖고 있기 때문에 전달해야 합니다.
    const ChildComponent = () =&gt; {
      return &lt;div&gt;Child Component&lt;/div&gt;;
    };
    render(
      &lt;ToDoListProvider&gt;
        &lt;ChildComponent /&gt;
      &lt;/ToDoListProvider&gt;
    );

    // 컨텍스트와 함께 렌더링한 컴포넌트가 화면에 잘 표시되는지,
    // 아무 동작을 하지 않았으므로 localStorage가 비어있는지 등을 테스트합니다.
    const childComponent = screen.getByText('Child Component');
    expect(childComponent).toBeInTheDocument();
    expect(localStorage.getItem('ToDoList')).toBeNull();
  });

  // localStorage에 데이터가 존재할 때, 해당 데이터를 localStorage로부터 불러와서
  // 컨텍스트에 잘 저장하는지 테스트하는 테스트 명세를 작성합니다.
  it('loads localStorage data and sets it to state', () =&gt; {
    localStorage.setItem('ToDoList', '[&quot;ToDo 1&quot;, &quot;ToDo 2&quot;, &quot;ToDo 3&quot;]');

    const ChildComponent = () =&gt; {
      const { toDoList } = useContext(ToDoListContext);
      return (
        &lt;div&gt;
          {toDoList.map((toDo) =&gt; (
            &lt;div key={toDo}&gt;{toDo}&lt;/div&gt;
          ))}
        &lt;/div&gt;
      );
    };
    render(
      &lt;ToDoListProvider&gt;
        &lt;ChildComponent /&gt;
      &lt;/ToDoListProvider&gt;
    );

    expect(screen.getByText('ToDo 1')).toBeInTheDocument();
    expect(screen.getByText('ToDo 2')).toBeInTheDocument();
    expect(screen.getByText('ToDo 3')).toBeInTheDocument();
  });

  // 이제 컨텍스트에 데이터를 추가하거나 삭제하는 테스트 명세를 작성합니다.
  it('uses addToDo function', () =&gt; {
    const ChildComponent = () =&gt; {
      // 컨텍스트에 데이터를 추가하기 위해 addToDo 함수를 사용합니다.
      const { toDoList, addToDo } = useContext(ToDoListContext);
      return (
        &lt;div&gt;
          &lt;div onClick={() =&gt; addToDo('study react 1')}&gt;Add ToDo&lt;/div&gt;
          &lt;div&gt;
            {toDoList.map((toDo) =&gt; (
              &lt;div key={toDo}&gt;{toDo}&lt;/div&gt;
            ))}
          &lt;/div&gt;
        &lt;/div&gt;
      );
    };
    render(
      &lt;ToDoListProvider&gt;
        &lt;ChildComponent /&gt;
      &lt;/ToDoListProvider&gt;
    );

    // 마지막으로, localStorage가 비어있는지 확인하고,
    // addToDo 함수를 연결한 버튼을 클릭해 임의로 만든 할 일 데이터가 localStorage에
    // 잘 저장되고 화면에 잘 표시되는지 테스트합니다.
    expect(localStorage.getItem('ToDoList')).toBeNull();
    const button = screen.getByText('Add ToDo');
    fireEvent.click(button);
    expect(screen.getByText('study react 1')).toBeInTheDocument();
    expect(localStorage.getItem('ToDoList')).toBe('[&quot;study react 1&quot;]');
  });

  // 이제 추가된 데이터를 삭제하기 위한 deleteToDo 함수를 테스트합니다.
  it('uses deleteToDo function', () =&gt; {
    localStorage.setItem('ToDoList', '[&quot;ToDo 1&quot;, &quot;ToDo 2&quot;, &quot;ToDo 3&quot;]');

    const ChileComponent = () =&gt; {
      const { toDoList, deleteToDo } = useContext(ToDoListContext);
      return (
        &lt;div&gt;
          {toDoList.map((toDo, index) =&gt; (
            &lt;div key={toDo} onClick={() =&gt; deleteToDo(index)}&gt;
              {toDo}
            &lt;/div&gt;
          ))}
        &lt;/div&gt;
      );
    };
    render(
      &lt;ToDoListProvider&gt;
        &lt;ChileComponent /&gt;
      &lt;/ToDoListProvider&gt;
    );

    const toDoItem = screen.getByText('ToDo 2');
    expect(toDoItem).toBeInTheDocument();
    fireEvent.click(toDoItem);
    expect(toDoItem).not.toBeInTheDocument();
    expect(
      JSON.parse(localStorage.getItem('ToDoList') as string)
    ).not.toContain('ToDo 2');
  });
});</code></pre>
<br />

<p><strong><span style="background-color: yellow;">InputContainer 컴포넌트</span></strong>
위와 같이 <code>./src/Components/InputContainer/index.test.tsx</code> 파일을 만들어줍니다. </p>
<pre><code class="language-jsx">import { fireEvent, render, screen } from '@testing-library/react';

import { InputContainer } from 'Components/InputContainer';
import { ToDoListProvider } from 'src/Contexts/ToDoList';

describe('&lt;InputContainer /&gt;', () =&gt; {
  it('renders component correctly', () =&gt; {
    const { container } = render(&lt;InputContainer /&gt;);

    const input = screen.getByPlaceholderText('할 일을 입력해 주세요.');
    expect(input).toBeInTheDocument();
    const button = screen.getByText('추가');
    expect(button).toBeInTheDocument();

    expect(container).toMatchSnapshot();
  });

  // 이제 InputContainer 컴포넌트의 State를 테스트하는 명세를 추가해줍니다.
  it('empties data after adding data', () =&gt; {
    render(&lt;InputContainer /&gt;);

    const input = screen.getByPlaceholderText(
      '할 일을 입력해 주세요.'
    ) as HTMLInputElement;
    const button = screen.getByText('추가');

    expect(input.value).toBe('');
    fireEvent.change(input, { target: { value: 'study react 1' } });
    expect(input.value).toBe('study react 1');
    fireEvent.click(button);
    expect(input.value).toBe('');
  });

  // 마지막으로 컨텍스트를 사용하는 부분을 테스트합니다.
  it('adds input data to localStorage via Context', () =&gt; {
    render(
      &lt;ToDoListProvider&gt;
        &lt;InputContainer /&gt;
      &lt;/ToDoListProvider&gt;
    );

    const input = screen.getByPlaceholderText('할 일을 입력해 주세요.');
    const button = screen.getByText('추가');

    expect(localStorage.getItem('ToDoList')).toBeNull();

    fireEvent.change(input, { target: { value: 'study react 1' } });
    fireEvent.click(button);

    expect(localStorage.getItem('ToDoList')).toBe('[&quot;study react 1&quot;]');
  });
});</code></pre>
<br />

<p><strong><span style="background-color: yellow;">ToDoList 컴포넌트</span></strong>
마찬가지로 <code>./src/Components/ToDoList/index.test.tsx</code> 파일을 만들어줍니다. </p>
<pre><code class="language-jsx">import { fireEvent, render, screen } from '@testing-library/react';

import { ToDoListProvider } from 'src/Contexts/ToDoList';
import { ToDoList } from 'Components/ToDoList';

describe('&lt;ToDoList /&gt;', () =&gt; {
  // 우선 ToDoList 컴포넌트가 화면에 잘 표시되는 지 확인합니다.
  it('renders component correctly', () =&gt; {
    const { container } = render(
      &lt;ToDoListProvider&gt;
        &lt;ToDoList /&gt;
      &lt;/ToDoListProvider&gt;
    );

    const toDoList = screen.getByTestId('toDoList');
    expect(toDoList).toBeInTheDocument();
    expect(toDoList.firstChild).toBeNull();

    expect(container).toMatchSnapshot();
  });

  // 이제 데이터가 있는 경우, 화면에 할 일 목록이 잘 표시되는지 확인합니다.
  it('shows toDo list', () =&gt; {
    localStorage.setItem('ToDoList', '[&quot;ToDo 1&quot;, &quot;ToDo 2&quot;, &quot;ToDo 3&quot;]');

    render(
      &lt;ToDoListProvider&gt;
        &lt;ToDoList /&gt;
      &lt;/ToDoListProvider&gt;
    );

    expect(screen.getByText('ToDo 1')).toBeInTheDocument();
    expect(screen.getByText('ToDo 2')).toBeInTheDocument();
    expect(screen.getByText('ToDo 3')).toBeInTheDocument();
    expect(screen.getAllByText('삭제').length).toBe(3);
  });

  // 마지막으로, 표시된 할 일 목록 데이터를 삭제하는 테스트 명세를 작성합니다.
  it('deletes toDo item', () =&gt; {
    localStorage.setItem('ToDoList', '[&quot;ToDo 1&quot;, &quot;ToDo 2&quot;, &quot;ToDo 3&quot;]');

    render(
      &lt;ToDoListProvider&gt;
        &lt;ToDoList /&gt;
      &lt;/ToDoListProvider&gt;
    );

    const toDoItem = screen.getByText('ToDo 2');
    expect(toDoItem).toBeInTheDocument();
    fireEvent.click(toDoItem.nextElementSibling as HTMLElement);
    expect(toDoItem).not.toBeInTheDocument();
    expect(
      JSON.parse(localStorage.getItem('ToDoList') as string)
    ).not.toContain('ToDo 2');
  });
});</code></pre>
<br />

<p><strong><span style="background-color: yellow;">App 컴포넌트</span></strong></p>
<p>앞에서 App 컴포넌트의 내부 구조를 변경했으므로 App 컴포넌트에서 localStorage를 사용해 초기 데이터를 불러오는 부분에 대한 테스트 명세도 살짝 수정해줍니다. </p>
<pre><code class="language-jsx">import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

describe('&lt;App /&gt;', () =&gt; {
  it('renders component correctly', () =&gt; {
    const { container } = render(&lt;App /&gt;);

    const toDoList = screen.getByTestId('toDoList');
    expect(toDoList).toBeInTheDocument();
    expect(toDoList.firstChild).toBeNull();

    const input = screen.getByPlaceholderText('할 일을 입력해 주세요.');
    expect(input).toBeInTheDocument();
    const label = screen.getByText('추가');
    expect(label).toBeInTheDocument();

    expect(container).toMatchSnapshot();
  });

  it('adds and deletes ToDo items', () =&gt; {
    render(&lt;App /&gt;);

    const input = screen.getByPlaceholderText('할 일을 입력해 주세요.');
    const button = screen.getByText('추가');
    fireEvent.change(input, { target: { value: 'study react 1' } });
    fireEvent.click(button);

    const todoItem = screen.getByText('study react 1');
    expect(todoItem).toBeInTheDocument();
    const deleteButton = screen.getByText('삭제');
    expect(deleteButton).toBeInTheDocument();

    const toDoList = screen.getByTestId('toDoList');
    expect(toDoList.childElementCount).toBe(1);

    fireEvent.change(input, { target: { value: 'study react 2' } });
    fireEvent.click(button);

    const todoItem2 = screen.getByText('study react 2');
    expect(todoItem2).toBeInTheDocument();
    expect(toDoList.childElementCount).toBe(2);

    const deleteButtons = screen.getAllByText('삭제');
    fireEvent.click(deleteButtons[0]);

    expect(todoItem).not.toBeInTheDocument();
    expect(toDoList.childElementCount).toBe(1);
  });

  it('does not add empty ToDo', () =&gt; {
    render(&lt;App /&gt;);

    const toDoList = screen.getByTestId('toDoList');
    const length = toDoList.childElementCount;

    const button = screen.getByText('추가');
    fireEvent.click(button);

    expect(toDoList.childElementCount).toBe(length);
  });

  it('loads localStorage data', () =&gt; {
    localStorage.setItem('ToDoList', '[&quot;ToDo 1&quot;, &quot;ToDo 2&quot;, &quot;ToDo 3&quot;]');
    render(&lt;App /&gt;);

    expect(screen.getByText('ToDo 1')).toBeInTheDocument();
    expect(screen.getByText('ToDo 2')).toBeInTheDocument();
    expect(screen.getByText('ToDo 3')).toBeInTheDocument();
    expect(screen.getAllByText('삭제').length).toBe(3);
  });
});</code></pre>
<p>그 다음에 <code>npm run test -- --coverage</code> 명령어로 코드 커버리지를 확인해봅니다. 
<img alt="코드 커버리지" src="https://velog.velcdn.com/images/so356hot/post/8c985a07-f33d-4a54-8f0c-daaaa789963b/image.png" /></p>
<p>보면 컴포넌트들은 100%의 커버지리가 나오는데 reportWebVitals.ts, 엔트리 파일 등은 테스트 통과가 안되는 것을 확인할 수 있는데, 이 파일들은 단지 컴포넌트를 추가하기 편하게 만든 단순한 파일들이므로 특별히 테스트하지 않아도 됩니다. </p>
<p>이처럼 코드 커버리지를 통해 우리가 놓치고 있는 코드가 있는지, 없는지 확인할 수 있습니다. </p>
<br />


<hr />
<h2 id="💡-새롭게-알게-된-점">💡 새롭게 알게 된 점</h2>
<h3 id="span-stylebackground-colorlavender❗클래스-컴포넌트의-라이프-사이클-함수의-종류-vs-useeffect-span"><span style="background-color: lavender;">❗클래스 컴포넌트의 라이프 사이클 함수의 종류 vs useEffect </span></h3>
<p>그동안 useEffect를 사용하면서 생명주기에 대해 개념적으로만 이해하고 있었습니다. 언제 써야 하는지에 대한 체감이 부족했는데, 
클래스 컴포넌트의 라이프사이클 메서드들을 예시와 함께 학습하면서 컴포넌트의 <strong>마운트/업데이트/언마운트</strong>가 언제 어떤 상황에서 일어나는지 명확하게 이해할 수 있었습니다.
특히 useEffect의 두 번째 매개변수 사용법이 헷갈렸는데, 클래스 컴포넌트와 비교하며 공부하니 각 옵션의 의미를 완전히 이해할 수 있었습니다.</p>
<blockquote>
<p><strong>useEffect만의 고유한 기능</strong></p>
</blockquote>
<ul>
<li>의존성 배열을 통한 선택적 리렌더링</li>
<li>전체 컴포넌트가 아닌 변경된 props만 감지하여 최적화</li>
</ul>
<br />

<h3 id="span-stylebackground-colorlavender❗context-api-사용법span"><span style="background-color: lavender;">❗Context API 사용법</span></h3>
<p>예전에 프론트 공부를 시작한 지 얼마 안됐을 때 프로젝트에서 상태 관리를 해야할 일이 있어 찾아보다가 Context API의 존재를 알게 됐고, Consumer, Provider, Props, State에 대해 제대로 공부하지 않고 무턱대고 사용하려다가 이상한 라이브러리만 설치하고 폴더 구조도 꼬이고 결국 사용하지 못했던 경험이 있었습니다.
그래서 이번에 8장을 공부하며 Context API는 부모로부터 Props와 State를 직접 받지 않고 Context라는 곳에서 전역적으로 데이터를 관리하며 접근을 하게 된다는 개념을 확실하게 정립한 것 같고, 그래서 상태관리를 하는 것은 과도한 Props drilling을 막아준다는 말에 대해 이해할 수 있었습니다. 
또한 처음에 Provider와 Consumer에 대해 이해를 잘 못했는데, 이름 그대로 <strong>&quot;컨텍스트를 제공&quot;</strong>할 땐 <strong>Provider</strong>을, <strong>컨텍스트를 사용</strong>할 땐 <strong>Consumer</strong>을 사용하는, 즉 공통 부모 컴포넌트(eg. App.tsx)에 Provider을, useContext를 사용해 props 대신 데이터를 사용/저장해야하는 컴포넌트에 Consumer를 적용하면 되는 것이라는 걸 이해했고 이건 모든 상태관리 툴에서 동일한 개념으로 작용이 될 것 같다는 생각을 했습니다. </p>
<pre><code class="language-jsx">// 제공 (Provider) - 공통 부모 컴포넌트
&lt;ToDoListProvider&gt;
  &lt;App /&gt;
&lt;/ToDoListProvider&gt;

// 사용 (Consumer) - 데이터가 필요한 컴포넌트
const { toDoList, addToDo } = useContext(ToDoListContext);

## ❓ 어려웠던 점
테스트 돌리기 전 스냅샷 업데이트를 할 땐 책에서는 npm run test -u 명령어로 하라했지만, 이상하게 계속 업데이트가 안되고 테스트 실패가 뜨는 걸 확인했습니다. 
그래서 package.json을 비교해보았는데 6장부터 vite로 마이그레이션 하기도 했고, jest 대신 vitest 라이브러리를 쓰고 있기도 해서 명령어가 npx vitest --update 명령어로 해줘야 통과가 되는 걸 확인할 수 있었습니다. 

## 🙋‍ 궁금한 점 / 다음에 다루고 싶은 내용
useEffect, useState를 이 책에서 같이 클론코딩을 해보다가 리액트 훅의 도입 동기와 자주 쓰이는 리액트 훅들에는 어떤 것들이 있는지 궁금해져서 다음 포스트로 정리를 해보려 합니다. 
</code></pre>
