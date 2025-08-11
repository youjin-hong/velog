# 📌 Velog 글 요약

| 항목   | 내용 |
|--------|------|
| **제목** | [스무디 한 잔 마시며 끝내는 리액트 + TDD] 6장 - Props와 State |
| **날짜** | Mon, 11 Aug 2025 06:41:46 GMT |
| **링크** | [https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-6%EC%9E%A5-Props%EC%99%80-State](https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-6%EC%9E%A5-Props%EC%99%80-State) |

---

<blockquote>
<p><strong>참고자료</strong></p>
</blockquote>
<ul>
<li><a href="https://github.com/youjin-hong/TDD_study">TDD 실습 Github Repo</a></li>
<li><a href="https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-5-React-Typescript-%EA%B0%9C%EB%B0%9C-%ED%99%98%EA%B2%BD-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0">5장 정리본</a></li>
</ul>
<hr />
<h2 id="✨-6-props와-state">✨ 6. Props와 State</h2>
<h3 id="span-stylebackground-colorlavenderprops와-state란span"><span style="background-color: lavender;">Props와 State란</span></h3>
<p><strong>Props (Properties)</strong>
부모 컴포넌트에서 자식 컴포넌트로 전달되는 데이터
자식 컴포넌트에서는 변경 불가능 (읽기 전용)
컴포넌트의 <strong>속성(Properties)</strong>을 의미</p>
<p><strong>State</strong>
한 컴포넌트 안에서 유동적인 데이터를 다룰 때 사용
컴포넌트 내부에서 변경 가능
컴포넌트의 <strong>상태(State)</strong>를 나타냄</p>
<br />

<h3 id="span-stylebackground-colorlavender프로젝트-설정span"><span style="background-color: lavender;">프로젝트 설정</span></h3>
<p><strong><span style="background-color: yellow;">프로젝트 생성</span></strong></p>
<pre><code class="language-bash">cd chap_6
npx create-react-app todo-list --template=typescript</code></pre>
<br />

<p><strong><span style="background-color: yellow;">필요한 라이브러리 설치</span></strong>. </p>
<pre><code class="language-bash">cd chap_6
npm install --save-dev styled-components
npm install --save-dev @types/styled-components jest-styled-components
npm install --save-dev husky lint-stated prettier</code></pre>
<br />

<p><strong><span style="background-color: yellow;">Prettier 설정(.prettierrc.js)</span></strong> </p>
<pre><code class="language-javascript">module.exports = {
  jsxBracketSameLine: true,
  singleQuote: true,
  tailingComma: 'all',
  printWidth: 100
}</code></pre>
<br />

<p><strong><span style="background-color: yellow;">package.json에 husky, lint-staged 설정</span></strong> </p>
<pre><code class="language-json">  &quot;scripts&quot;: {...},
  &quot;husky&quot;: {
    &quot;hooks&quot;: {
      &quot;pre-commit&quot;: &quot;lint-staged&quot;
    }
  },
  &quot;lint-staged&quot;: {
    &quot;src/**/*.{js,jsx,ts,tsx,css,scss,md}&quot;: [
      &quot;prettier --write&quot;
    ]
  },</code></pre>
<br />

<p><strong><span style="background-color: yellow;">절대 경로 설정(tsconfig.json)</span></strong>
마지막으로 lint-staged와 husky를 설정하기 위해 package.json 파일을 수정했다면 절대 경로를 추가하기 위해 tsconfig.json에 <code>&quot;baseUrl&quot;: &quot;src&quot;</code>를 추가해줍니다.</p>
<br />

<h3 id="span-stylebackground-colorlavender컴포넌트별-할일-목록-앱-개발하기span"><span style="background-color: lavender;">컴포넌트별 할일 목록 앱 개발하기</span></h3>
<p><strong><span style="background-color: yellow;">Button 컴포넌트</span></strong></p>
<pre><code class="language-jsx">import React from &quot;react&quot;;
import Styled from &quot;styled-components&quot;;

interface ContainerProps {
  readonly backgroundColor: string;
  readonly hoverColor: string;
}

interface Props {
  readonly label: string;
  readonly backgroundColor?: string;
  readonly hoverColor?: string;
  readonly onClick?: () =&gt; void;
}

const Container = Styled.button&lt;ContainerProps&gt;`
  text-align: center;
  background-color: ${(props) =&gt; props.backgroundColor};
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  &amp;:hover {
    background-color: ${(props) =&gt; props.hoverColor};
  }
  &amp;:active {
    box-shadow: inset 5px 5px 10px rgba(0, 0, 0, 0.2);
  }
`;

const Label = Styled.div`
  color: #FFFFFF;
  font-size: 16px;
`;

export const Button = ({
  label,
  backgroundColor = &quot;#304FFE&quot;,
  hoverColor = &quot;#1E40FF&quot;,
  onClick,
}: Props) =&gt; {
  return (
    &lt;Container
      backgroundColor={backgroundColor}
      hoverColor={hoverColor}
      onClick={onClick}
    &gt;
      &lt;Label&gt;{label}&lt;/Label&gt;
    &lt;/Container&gt;
  );
};</code></pre>
<br />

<p><strong><span style="background-color: yellow;">Input 컴포넌트</span></strong></p>
<pre><code class="language-jsx">import React from &quot;react&quot;;
import Styled from &quot;styled-components&quot;;

interface Props {
  readonly placeholders?: string;
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

export const Input = ({ placeholders, value, onChange }: Props) =&gt; {
  return (
    &lt;InputBox
      placeholder={placeholders}
      value={value}
      onChange={(event) =&gt; {
        if (typeof onChange === &quot;function&quot;) {
          onChange(event.target.value);
        }
      }}
    /&gt;
  );
};</code></pre>
<br />

<p><strong><span style="background-color: yellow;">ToDoItem 컴포넌트</span></strong></p>
<pre><code class="language-jsx">import React from &quot;react&quot;;
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

export const ToDoItem = ({ label, onDelete }: Props) =&gt; {
  return (
    &lt;Container&gt;
      &lt;Label&gt;{label}&lt;/Label&gt;
      &lt;Button
        label=&quot;삭제&quot;
        backgroundColor=&quot;#FF1744&quot;
        hoverColor=&quot;#F01440&quot;
        onClick={onDelete}
      /&gt;
    &lt;/Container&gt;
  );
};</code></pre>
<br />

<h3 id="span-stylebackground-colorlavenderstate-활용하기span"><span style="background-color: lavender;">State 활용하기</span></h3>
<p><strong><span style="background-color: yellow;">App 컴포넌트 - useState Hook 사용</span></strong></p>
<pre><code class="language-jsx">import React, { useState } from &quot;react&quot;;
import Styled from &quot;styled-components&quot;;
import { Button, Input, ToDoItem } from &quot;Components&quot;;

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

function App() {
  const [toDo, setToDo] = useState(&quot;&quot;);
  const [toDoList, setToDoList] = useState&lt;string[]&gt;([]);

  const addToDo = (): void =&gt; {
    if (toDo) {
      setToDoList([...toDoList, toDo]);
      setToDo(&quot;&quot;);
    }
  };

  const deleteTodo = (index: number): void =&gt; {
    let list = [...toDoList];
    list.splice(index, 1);
    setToDoList(list);
  };

  return (
    &lt;Container&gt;
      &lt;Contents&gt;
        &lt;ToDoListContainer&gt;
          {toDoList.map((item, index) =&gt; (
            &lt;ToDoItem
              key={item}
              label={item}
              onDelete={() =&gt; deleteTodo(index)}
            /&gt;
          ))}
        &lt;/ToDoListContainer&gt;
        &lt;Input
          placeholders=&quot;할 일을 입력해 주세요.&quot;
          onChange={(text) =&gt; setToDo(text)}
        /&gt;
        &lt;Button label=&quot;추가&quot; onClick={addToDo} /&gt;
      &lt;/Contents&gt;
    &lt;/Container&gt;
  );
}

export default App;</code></pre>
<br />

<h3 id="span-stylebackground-colorlavender테스트-코드-작성span"><span style="background-color: lavender;">테스트 코드 작성</span></h3>
<p><strong><span style="background-color: yellow;">Button 컴포넌트 테스트 코드 작성</span></strong>
Button 컴포넌트 폴더 아래에 index.test.tsx 파일을 만들어 아래와 같이 작성해 줍니다. </p>
<pre><code class="language-javascript">describe('&lt;Button /&gt;', () =&gt; {
  it('renders component correctly and applies styles', () =&gt; {
    const { container } = render(&lt;Button label=&quot;Button Test&quot; /&gt;);

    const buttonElement = screen.getByRole('button', { name: 'Button Test' });
    expect(buttonElement).toBeInTheDocument();
    expect(buttonElement).toHaveStyleRule('background-color', '#304FFE');
  });

  it('clicks the button', () =&gt; {
    const handleClick = jest.fn();
    render(&lt;Button label=&quot;Button Test&quot; onClick={handleClick} /&gt;);

    const label = screen.getByText('Button Test');
    fireEvent.click(label);
    expect(handleClick).toHaveBeenCalledTimes(1);
  });
});</code></pre>
<br />

<p><strong><span style="background-color: yellow;">Input 컴포넌트 테스트 코드 작성</span></strong></p>
<pre><code class="language-jsx">import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import 'jest-styled-components';

import { Input } from 'Components/Input';

describe('&lt;Input /&gt;', () =&gt; {
  it('renders component correctly', () =&gt; {
    const { container } = render(&lt;Input value=&quot;default value&quot; /&gt;);

    const input = screen.getByDisplayValue('default value');
    expect(input).toBeInTheDocument();

    expect(container).toMatchSnapshot();
  });

  it('renders placeholder correctly', () =&gt; {
    render(&lt;Input placeholders=&quot;default placeholder&quot; /&gt;);

    const input = screen.getByPlaceholderText('default placeholder');
    expect(input).toBeInTheDocument();
  });

  it('changes the data', () =&gt; {
    render(&lt;Input placeholders=&quot;default placeholder&quot; /&gt;);

    const input = screen.getByPlaceholderText('default placeholder') as HTMLInputElement;
    fireEvent.change(input, { target: { value: 'study react' } });
    expect(input.value).toBe('study react');
  });
});</code></pre>
<br />

<p><strong><span style="background-color: yellow;">ToDoItem 컴포넌트 테스트 코드 작성</span></strong> </p>
<pre><code class="language-jsx">describe('&lt;Input /&gt;', () =&gt; {
  it('renders component correctly', () =&gt; {
    const { container } = render(&lt;ToDoItem label=&quot;default value&quot; /&gt;);

    const todoItem = screen.getByText('default value');
    expect(todoItem).toBeInTheDocument();

    const deleteButton = screen.getByText('삭제');
    expect(deleteButton).toBeInTheDocument();
    expect(container).toMatchSnapshot();
  });

  it('clicks the delete button', () =&gt; {
    const handleClick = jest.fn();
    render(&lt;ToDoItem label=&quot;default value&quot; onDelete={handleClick} /&gt;);

    const deleteButton = screen.getByText('삭제');
    expect(handleClick).toHaveBeenCalledTimes(0);
    fireEvent.click(deleteButton);
    expect(handleClick).toHaveBeenCalledTimes(1);
  });
});</code></pre>
<br />

<p><strong><span style="background-color: yellow;">App 컴포넌트 테스트 코드 작성</span></strong></p>
<pre><code class="language-jsx">describe('&lt;App /&gt;', () =&gt; {
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
});</code></pre>
<blockquote>
<p><strong>💡핵심 포인트</strong></p>
</blockquote>
<ul>
<li><strong>props와 state 비교</strong>: 아래 표 참조</li>
<li><strong>Typescript 인터페이스로 Props 타입 안전성 확보</strong></li>
<li><strong>선택적 Porps는 <code>?</code>와 기본값 활용</strong></li>
<li><strong>이벤트 핸들링은 Props로 전달</strong></li>
<li><strong>컴포넌트 재사용을 고려한 설계 in React</strong></li>
<li><strong>export와 export default의 차이</strong></li>
</ul>
<table>
<thead>
<tr>
<th>구분</th>
<th>Props</th>
<th>State</th>
</tr>
</thead>
<tbody><tr>
<td><strong>데이터 방향</strong></td>
<td>부모 → 자식</td>
<td>컴포넌트 내부</td>
</tr>
<tr>
<td><strong>변경 가능성</strong></td>
<td>불가능 (읽기 전용)</td>
<td>가능</td>
</tr>
<tr>
<td><strong>용도</strong></td>
<td>컴포넌트 속성 설정</td>
<td>동적 데이터 관리</td>
</tr>
<tr>
<td><strong>선언 방식</strong></td>
<td>인터페이스로 타입 정의</td>
<td>useState Hook 사용</td>
</tr>
</tbody></table>
<hr />
<h2 id="💡-새롭게-알게-된-점">💡 새롭게 알게 된 점</h2>
<h3 id="span-stylebackground-colorlavender❗dom을-다루는-게-왜-단순한-자바스크립트의-테스트로-정확한-오류를-잡아내기-어려운지span"><span style="background-color: lavender;">❗DOM을 다루는 게 왜 단순한 자바스크립트의 테스트로 정확한 오류를 잡아내기 어려운지?</span></h3>
<p>DOM은 브라우저 환경에서만 존재하는 객체이기 때문에, 단순히 자바스크립트 테스트 환경에서는 아래와 같은 이유들로 컴포넌트의 <strong>실제 동작</strong>과 <strong>테스트 환경</strong> 차이로 인해 정확한 오류 검출이 어려워집니다. </p>
<ul>
<li><strong>브라우저 API 부재</strong>
: <code>document</code>, <code>window</code> 등의 브라우저 전용 객체가 없다. </li>
<li><strong>이벤트 시스템 미지원</strong>
: 클릭, 입력 등의 실제 사용자 상호작용을 시뮬레이션하기 어렵다. </li>
<li><strong>렌더링 로직 부재</strong>
: 실제 화면에 어떻게 표시되는지 확인 불가</li>
<li><strong>스타일 적용 확인 불가</strong>
: CSS 스타일이나 레이아웃 변화를 테스트할 수 없다. </li>
</ul>
<br />

<h3 id="span-stylebackground-colorlavender❗react-testing-library는-실제-dom-노드에서-작동하므로-더-신뢰할-수-있는-테스트를-할-수-있다고-했는데-왜-더-신뢰할-수-있는-건지span"><span style="background-color: lavender;">❗react-testing-library는 실제 DOM 노드에서 작동하므로 더 신뢰할 수 있는 테스트를 할 수 있다고 했는데, 왜 더 신뢰할 수 있는 건지?</span></h3>
<p>다른 테스트 프레임워크는 인스턴스 기반으로 접근합니다. </p>
<pre><code class="language-javascript">// Enzyme 등의 접근 방식 (인스턴스 기반)
const wrapper = shallow(&lt;MyComponent /&gt;);
wrapper.instance().someMethod(); // 내부 구현에 의존</code></pre>
<p>반면 react-testing-library는 실제 DOM 노드에 접근하여 실제 사용자 행동과 유사한 테스트를 제공합니다.</p>
<pre><code class="language-javascript">// 실제 DOM 기반 테스트
render(&lt;MyComponent /&gt;);
const button = screen.getByRole('button');
fireEvent.click(button); // 실제 사용자 행동과 유사</code></pre>
<p><strong>신뢰할 수 있는 이유?</strong></p>
<ul>
<li><p><strong>실제 DOM 사용</strong></p>
<ul>
<li>브라우저에서 실행되는 것과 동일한 환경</li>
</ul>
</li>
<li><p><strong>사용자 중심 테스트</strong></p>
<ul>
<li>내부 구현이 아닌 사용자가 보는 화면 기준</li>
<li>접근성을 고려한 요소를 선택</li>
</ul>
</li>
<li><p><strong>통합 테스트 지향</strong></p>
<ul>
<li>컴포넌트 간의 상호작용까지 검증</li>
<li>실제 사용 시나리오와 유사한 테스트</li>
</ul>
</li>
<li><p><strong>구현 세부사항과 분리</strong></p>
<ul>
<li>내부 state나 props가 아닌 결과물에 집중</li>
<li>리팩토링 시에도 테스트가 깨지지 않음</li>
</ul>
</li>
</ul>
<h2 id="❓-어려웠던-점">❓ 어려웠던 점</h2>
<p>cra와 react 19 버전, 그리고 업그레이드된 react-testing-library 의 변경된 사항들 때문에 책을 클론코딩하면 테스트 실패가 뜨는 게 너무 번거로웠습니다. 직접 겪었던 사례를 몇 가지 들어보자면, 테스트 코드에서 container나 parentElement 등을 쓰면 &quot;직접적인 DOM 노드 사용을 피하라&quot;는 메세지가 많이 떴습니다. 어떤 코드는 이 메시지가 뜨면서도 테스트는 통과하기도 했지만 대부분은 fail이 떴습니다. 초반에는 버전 업그레이드에 따른 권장 방식에 맞춰 부모 요소에 직접 접근하지 않고 getByRole이나 testId로 접근하여 오류를 하나씩 해결하며 클론 코딩을 진행했는데, 작성해야 할 코드가 점점 길어질수록 번거로웠습니다. vite로 마이그레이션을 해야하나 싶었지만 이번 스터디의 내 목표는 testing-library의 사용법을 익히는 것이기 때문에 CRA에서 VITE로의 마이그레이션은 안할 것 같습니다. </p>
<h2 id="🙋-궁금한-점--다음에-다루고-싶은-내용">🙋‍ 궁금한 점 / 다음에 다루고 싶은 내용</h2>
<p>4, 5, 6장의 내용이 생각보다 많아서 한번에 공부하다 보니 제대로 개념 정립이 되지 않은 것 같습니다. 오류 메시지도 해결할 겸 다시 복기해보려고 합니다. </p>
