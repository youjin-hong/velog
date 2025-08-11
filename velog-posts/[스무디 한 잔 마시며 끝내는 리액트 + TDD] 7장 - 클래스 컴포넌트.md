# 📌 Velog 글 요약

| 항목   | 내용 |
|--------|------|
| **제목** | [스무디 한 잔 마시며 끝내는 리액트 + TDD] 7장 - 클래스 컴포넌트 |
| **날짜** | Mon, 11 Aug 2025 06:47:01 GMT |
| **링크** | [https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-7%EC%9E%A5-%ED%81%B4%EB%9E%98%EC%8A%A4-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8](https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-7%EC%9E%A5-%ED%81%B4%EB%9E%98%EC%8A%A4-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8) |

---

<blockquote>
<p><strong>참고자료</strong></p>
</blockquote>
<ul>
<li><a href="https://github.com/youjin-hong/TDD_study">TDD 실습 Github Repo</a></li>
<li><a href="https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-6%EC%9E%A5-Props%EC%99%80-State">6장 정리본</a></li>
<li><a href="https://ko.react.dev/reference/react/Component">클래스 컴포넌트</a></li>
</ul>
<p>지난 시간에 리액트 프로젝트 설치와 react-testing-library에 대해 알아보았습니다. 오늘은 본격적으로 리액트 테스트를 하기에 앞서 클래스 컴포넌트 사용 방법에 대해 살펴보겠습니다. </p>
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
<pre><code class="language-jsx">// 제공 (Provider) - 공통 부모 컴포넌트
&lt;ToDoListProvider&gt;
  &lt;App /&gt;
&lt;/ToDoListProvider&gt;

// 사용 (Consumer) - 데이터가 필요한 컴포넌트
const { toDoList, addToDo } = useContext(ToDoListContext);</code></pre>
<h2 id="❓-어려웠던-점">❓ 어려웠던 점</h2>
<p>테스트 돌리기 전 스냅샷 업데이트를 할 땐 책에서는 npm run test -u 명령어로 하라했지만, 이상하게 계속 업데이트가 안되고 테스트 실패가 뜨는 걸 확인했습니다. 
그래서 package.json을 비교해보았는데 6장부터 vite로 마이그레이션 하기도 했고, jest 대신 vitest 라이브러리를 쓰고 있기도 해서 명령어가 npx vitest --update 명령어로 해줘야 통과가 되는 걸 확인할 수 있었습니다. </p>
<h2 id="🙋-궁금한-점--다음에-다루고-싶은-내용">🙋‍ 궁금한 점 / 다음에 다루고 싶은 내용</h2>
<p>useEffect, useState를 이 책에서 같이 클론코딩을 해보다가 리액트 훅의 도입 동기와 자주 쓰이는 리액트 훅들에는 어떤 것들이 있는지 궁금해져서 다음 포스트로 정리를 해보려 합니다. </p>
