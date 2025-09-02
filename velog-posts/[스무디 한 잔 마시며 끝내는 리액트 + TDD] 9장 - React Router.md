# 📌 Velog 글 요약

| 항목   | 내용 |
|--------|------|
| **제목** | [스무디 한 잔 마시며 끝내는 리액트 + TDD] 9장 - React Router |
| **날짜** | Tue, 02 Sep 2025 02:49:50 GMT |
| **링크** | [https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-9%EC%9E%A5-React-Router](https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-9%EC%9E%A5-React-Router) |

---

<blockquote>
<p><strong>참고자료</strong></p>
</blockquote>
<ul>
<li><a href="https://github.com/youjin-hong/TDD_study">TDD 실습 Github Repo</a></li>
<li><a href="https://velog.io/@so356hot/%EC%8A%A4%EB%AC%B4%EB%94%94-%ED%95%9C-%EC%9E%94-%EB%A7%88%EC%8B%9C%EB%A9%B0-%EB%81%9D%EB%82%B4%EB%8A%94-%EB%A6%AC%EC%95%A1%ED%8A%B8-TDD-8%EC%9E%A5-Context-API%EC%99%80-localStorage">8장 정리본</a></li>
<li><a href="https://reactrouter.com/">React-Router</a></li>
</ul>
<hr />
<h2 id="✨-9-react-router">✨ 9. react-router</h2>
<p>8장까지 직접 할 일 목록 앱을 개발하며 리액트 사용법에 대해 간단히 알아보았습니다. 8장까지는 나름 웹서비스임에도 불구하고 <strong>페이지 이동</strong>을 전혀 하지 않았는데요.</p>
<p>리액트는 사용자 UI를 만들기 위한 자바스크립트 라이브러리로, <strong>페이지 이동에 관한 부분은 지원하고 있지 않습니다.</strong> 따라서 웹 페이지 이동을 구현하기 위해서는 <strong>react-router</strong>라는 외부 라이브러리를 추가로 사용해야 합니다. </p>
<p>그래서 이번 9장에서는 react-router 라이브러리에 대해 살펴보려 합니다. </p>
<h3 id="span-stylebackground-colorlavenderreact-routerspan"><span style="background-color: lavender;">react-router</span></h3>
<p>우리가 일상에서 마주하는 보통의 웹 서비스는 <strong>URL 기준</strong>으로 화면을 표시합니다. 사용자가 URL로 웹 서버에 웹 페이지를 요청하면, 웹 서버는 사용자가 요청한 URL을 보고 그에 해당하는 웹 페이지를 응답하게 됩니다. </p>
<p>예로 <strong>유튜브에서 &quot;침착맨 음식 월드컵&quot;을 검색</strong>하는 것을 들 수 있습니다. </p>
<blockquote>
<p><img alt="유튜브" src="https://velog.velcdn.com/images/so356hot/post/d976dba8-3313-4439-8588-2dadb5cbd004/image.png" /></p>
</blockquote>
<blockquote>
<p><img alt="음식월드컵" src="https://velog.velcdn.com/images/so356hot/post/5396e97c-a209-41b6-a4ea-6ca1b4c5eba1/image.png" /></p>
</blockquote>
<p>이렇게 <code>https://www.youtube.com</code>에서 &quot;침착맨 음식 월드컵&quot; 검색어를 입력하게 되면,
<code>https://www.youtube.com/results?search_query=침착맨+음식+월드컵</code>으로 url이 서버에 전송되며, 서버는 url에 해당하는 결과인 침착맨의 음식 월드컵에 대한 동영상들을 응답해주게 되는 것이죠.</p>
<p>리액트는 SPA(Single Page Application)의 UI를 만드는 자바스크립트 라이브러리이기 때문에 보통의 웹 서비스와는 다르게 웹서버가 사용자 요청에 대한 모든 URL에 하나의 페이지만을 응답하게 되며, 응답 받은 하나의 페이지가 화면에 표시되게 됩니다. </p>
<blockquote>
<p>✔️ <strong>일반 웹사이트 동작 방식</strong></p>
</blockquote>
<ul>
<li>사용자: <code>https://www.youtube.com/results?search_query=침착맨</code> 요청</li>
<li>웹 서버: &quot;침착맨 검색 결과 페이지를 보내드릴게요!&quot;</li>
<li>브라우저: 검색 결과 화면 표시 🔍
➡️ 각 URL마다 서버에서 <strong>다른 HTML 파일</strong>을 응답하는 방식</li>
</ul>
<blockquote>
<p>✔️ <strong>SPA 동작 방식</strong></p>
</blockquote>
<ul>
<li>사용자: 어떤 URL로 요청하든</li>
<li>웹 서버: <strong>항상 같은 하나의 페이지(<code>index.html</code>)만 응답</strong></li>
<li>브라우저: 받은 페이지에서 URL을 보고 적절한 화면 표시
➡️ 서버는 <strong>하나의 페이지</strong>만 주고, 그 페이지가 URL을 보고 내용을 바꿔서 보여주는 방식</li>
</ul>
<p>이렇게 응답한 하나의 페이지에서 URL을 확인하고 특정 기능 또는 특정 컴포넌트(페이지)를 표시하는 것이 SPA의 기본 흐름입니다. 
<strong>SPA 프레임워크</strong>인 Angular와 Vue에서는 URL을 판단해 특정 컴포넌트를 보여주는 기능을 기본적으로 제공하고 있습니다. 
그러나 <strong>SPA UI 라이브러리</strong>인 리액트는 URL을 판단하고, 특정 컴포넌트를 보여주는 기능을 제공하지 않습니다. </p>
<p>그래서 <code>index.html</code>로 받은 URL에 해당하는 페이지를 사용자에게 보여주기 위해선 <strong>react-router</strong>라는 외부 라이브러리를 사용해야 합니다. </p>
<p>react-router 필요성에 대해 살펴보았으니 이제 8장에서 만든 할일 목록 앱에 react-router를 적용해보며 사용법에 대해 알아보겠습니다. </p>
<br />

<h3 id="span-stylebackground-colorlavender프로젝트-준비span"><span style="background-color: lavender;">프로젝트 준비</span></h3>
<p>우선 8장 프로젝트를 루트 디렉토리에 복사+붙여넣기 한 뒤, <code>chap_9</code>로 폴더명을 변경해주겠습니다. </p>
<p>그 다음 <code>npm install</code> 후, 
<code>npm run test</code>하여 테스트가 다 통과되었다면 개발 환경 준비가 모두 끝났습니다. </p>
<p><img alt="개발준비" src="https://velog.velcdn.com/images/so356hot/post/817ff3a6-989f-42e8-9eed-aba456b0ba10/image.png" /></p>
<br />

<h3 id="span-stylebackground-colorlavender개발span"><span style="background-color: lavender;">개발</span></h3>
<p>이제 할 일 목록 앱에서 react-router를 사용해 페이지 이동 기능을 추가하기 위해 할 일 목록 페이지, 등록 페이지, 상세 페이지 이렇게 3개의 페이지로 나눠보겠습니다.</p>
<p><strong><span style="background-color: yellow;">react-router</span></strong>
우선 리액트와 타입스크립트를 위한 라이브러리들을 설치해줍니다. </p>
<pre><code class="language-bash">npm install --save react-router-dom
npm install --save-dev @types/react-router-dom</code></pre>
<p>설치했다면 이제 사용하기 위해 <code>./src/index.tsx</code> 파일을 수정해줍니다. 
이때 react-router가 제공하는 BrowserRouter를 사용해야합니다. 따라서 as를 이용해 Router로 이름을 변경하여 사용해주겠습니다. </p>
<pre><code class="language-jsx">// src/index.tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router } from 'react-router-dom';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  &lt;React.StrictMode&gt;
    &lt;Router&gt;
      &lt;App /&gt;
    &lt;/Router&gt;
  &lt;/React.StrictMode&gt;
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();</code></pre>
<p>이렇게 Router를 설정한 다음 URL에 해당하는 페이지를 정의하기 위해 <code>./src/App.tsx</code> 파일을 열어 수정해줍니다. </p>
<pre><code class="language-jsx">// src/App.tsx
import { InputContainer } from 'Components/InputContainer';
import { ToDoList } from 'Components/ToDoList';
import { Route, Routes } from 'react-router-dom';
import { ToDoListProvider } from 'src/Contexts/ToDoList';
import Styled from 'styled-components';

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
        &lt;Routes&gt;
          &lt;Route path=&quot;/&quot;&gt;
            &lt;Contents&gt;
              &lt;ToDoList /&gt;
              &lt;InputContainer /&gt;
            &lt;/Contents&gt;
          &lt;/Route&gt;
        &lt;/Routes&gt;
      &lt;/Container&gt;
    &lt;/ToDoListProvider&gt;
  );
}

export default App;</code></pre>
<p>react-router 라이브러리가 v5까지는 Switch 컴포넌트와 exact 속성을 지원했지만 v6 이후부터는 Switch, exact는 지원하지 않으며 Switch 대신 Routes 컴포넌트를 지원하므로 버전에 맞게 바꿔줍니다. </p>
<br />

<p><strong><span style="background-color: yellow;">List 페이지 컴포넌트</span></strong>
지금 App 컴포넌트에 표시되고 있는 할 일 목록을 표시할 List 페이지를 만들기 위해 <code>./src/Pages/List/index.tsx</code> 파일을 만들고 작성해줍니다. </p>
<pre><code class="language-jsx">import { ToDoList } from 'Components/ToDoList';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

const Container = styled.div`
  display: flex;
  background-color: #ffffff;
  flex-direction: column;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2);
  position: relative;
  align-items: center;
`;

const AddButton = styled(Link)`
  font-size: 20px;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 60px;
  height: 60px;
  border-radius: 30px;
  cursor: pointer;
  position: absolute;
  bottom: -30px;
  background-color: #304ffe;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2);
  text-decoration: none;
  &amp;:hover {
    background-color: #1e40ff;
  }
  &amp;:active {
    box-shadow: inset 5px 5px 10px rgba(0, 0, 0, 0.2);
  }
`;

export const List = () =&gt; {
  return (
    &lt;Container&gt;
      &lt;ToDoList /&gt;
      &lt;AddButton to=&quot;/add&quot;&gt;+&lt;/AddButton&gt;
    &lt;/Container&gt;
  );
};</code></pre>
<p>그 다음 <code>./src/App.tsx</code>를 열어 다음과 같이 List 컴포넌트를 불러와줍니다. </p>
<pre><code class="language-jsx">// src/App.tsx
import { InputContainer } from 'Components/InputContainer';
import { ToDoList } from 'Components/ToDoList';
import { Route, Routes } from 'react-router-dom';
import { ToDoListProvider } from 'src/Contexts/ToDoList';
import { List } from 'src/Pages';
import Styled from 'styled-components';

const Container = Styled.div`
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
`;

function App() {
  return (
    &lt;ToDoListProvider&gt;
      &lt;Container&gt;
        &lt;Routes&gt;
          &lt;Route path=&quot;/&quot;&gt;
            &lt;List /&gt;
          &lt;/Route&gt;
        &lt;/Routes&gt;
      &lt;/Container&gt;
    &lt;/ToDoListProvider&gt;
  );
}

export default App;</code></pre>
<br />

<p><strong><span style="background-color: yellow;">Add 페이지 컴포넌트</span></strong>
<code>./src/Pages/Add/index.tsx</code> 파일을 만들고 다음과 같이 작성해줍니다.</p>
<pre><code class="language-jsx">import { InputContainer } from 'Components/InputContainer';
import styled from 'styled-components';

const Container = styled.div`
  display: flex;
  background-color: #ffffff;
  flex-direction: column;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2);
  position: relative;
  align-items: center;
`;

export const Add = () =&gt; {
  return (
    &lt;Container&gt;
      &lt;InputContainer /&gt;
    &lt;/Container&gt;
  );
};</code></pre>
<p>그 다음 App 컴포넌트에도 다음과 같이 수정해줍니다.</p>
<pre><code class="language-jsx">import { Route, Routes } from 'react-router-dom';
...

function App() {
  return (
    &lt;ToDoListProvider&gt;
      &lt;Container&gt;
        &lt;Routes&gt;
          &lt;Route path=&quot;/&quot; element={&lt;List /&gt;} /&gt;
          &lt;Route path=&quot;/add&quot; element={&lt;Add /&gt;} /&gt;
        &lt;/Routes&gt;
      &lt;/Container&gt;
    &lt;/ToDoListProvider&gt;
  );
}

export default App;</code></pre>
<p>그럼 &quot;/add&quot; 페이지에서 입력한 할 일이 &quot;/&quot; 페이지에 리스트로 추가되는 것을 확인할 수 있습니다.</p>
<p>Add 페이지 컴포넌트의 InputContainer 컴포넌트에 할 일을 입력하고 추가하면 입력한 데이터는 앱의 전역 데이터를 다루는 ToDoList 컨텍스트에 저장됩니다. 
이렇게 저장된 전역 데이터는 브라우저의 페이지 뒤로 가기 버튼을 통해 List 페이지 컴포넌트로 이동해도 화면에 잘 표시되는 것을 확인할 수 있습니다.</p>
<p>하지만 지금 상태는 매번 뒤로가기 버튼을 눌러 리스트 업데이트를 확인을 해야하기 때문에 좋은UX가 아닙니다. &quot;/add&quot; 페이지에서 &quot;추가&quot; 버튼을 눌렀을 때 &quot;/&quot; 페이지로 이동하는 것이 좀 더 좋은 사용자 경험일 것입니다. 그래서 Add 컴포넌트를 아래와 같이 수정해줍니다. </p>
<pre><code class="language-jsx">import { InputContainer } from 'Components/InputContainer';
import { useNavigate } from 'react-router-dom';
import styled from 'styled-components';

const Container = styled.div`
  display: flex;
  background-color: #ffffff;
  flex-direction: column;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2);
  position: relative;
  align-items: center;
`;

export const Add = () =&gt; {
  const navigate = useNavigate();

  return (
    &lt;Container&gt;
      &lt;InputContainer onAdd={() =&gt; navigate('/')} /&gt;
    &lt;/Container&gt;
  );
};</code></pre>
<br />

<p><strong><span style="background-color: yellow;">InputContainer 컴포넌트</span></strong>
위에서 Add 컴포넌트에 onAdd 함수를 추가해주었는데, 아직 InputContainer에 onAdd 함수를 만들어주지 않았기 때문에 에러가 납니다. 
그래서 <code>./src/Components/InputContainer/index.tsx</code> 파일을 열어 수정해줍니다.</p>
<pre><code class="language-jsx">import React, { useContext, useState } from 'react';
import styled from 'styled-components';

import { Button } from 'Components/Button';
import { Input } from 'Components/Input';

import { ToDoListContext } from 'src/Contexts/ToDoList';

const Container = styled.div`
  display: flex;
`;

interface Props {
  readonly onAdd?: () =&gt; void;
}

export const InputContainer = ({ onAdd }: Props) =&gt; {
  const [toDo, setToDo] = useState('');
  const { addToDo } = useContext(ToDoListContext);

  return (
    &lt;Container&gt;
      &lt;Input
        placeholder=&quot;할 일을 입력해 주세요.&quot;
        value={toDo}
        onChange={setToDo}
      /&gt;
      &lt;Button
        label=&quot;추가&quot;
        onClick={() =&gt; {
          addToDo(toDo);
          setToDo('');
          if (toDo &amp;&amp; typeof onAdd === 'function') {
            onAdd();
          }
        }}
      /&gt;
    &lt;/Container&gt;
  );
};</code></pre>
<br />

<p><strong><span style="background-color: yellow;">ToDoItem 컴포넌트</span></strong>
할 일을 선택했을 때, 할 일 상세 페이지로 이동할 수 있도록 수정할 것이기 때문에 <code>./src/Components/ToDoItem/index.tsx</code> 파일을 수정해줍ㄴ디ㅏ. </p>
<pre><code class="language-jsx">import Styled from 'styled-components';

import { Button } from 'Components/Button'; // Button 컴포넌트 import
import { Link } from 'react-router-dom';

interface Props {
  readonly label: string;
  readonly id: number;
  readonly onDelete?: () =&gt; void;
}

const Container = Styled.div`
  display: flex;
  border-bottom: 1px solid #BDBDBD;
  align-items: center;
  margin: 10px;
  padding: 10px;
`;

const Label = Styled(Link)`
  flex: 1;
  text-decoration: none;
  font-size: 16px;
  margin-right: 20px;
`;

export const ToDoItem = ({ id, label, onDelete }: Props) =&gt; {
  return (
    &lt;Container&gt;
      &lt;Label to={`/detail/${id}`}&gt;{label}&lt;/Label&gt;
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

<p><strong><span style="background-color: yellow;">ToDoList 컴포넌트</span></strong>
ToDoItem에 id라는 props를 추가함으로써 부모 컴포넌트 ToDoList 컴포넌트에 발생하고 있는 에러를 수정해줍니다. 수정할 파일은 <code>./src/Components/ToDoList/index.tsx</code>입니다. </p>
<pre><code class="language-jsx">...

export const ToDoList = () =&gt; {
  const { toDoList, deleteToDo } = useContext(ToDoListContext);

  return (
    &lt;Container data-testid=&quot;toDoList&quot;&gt;
      {toDoList.map((item, index) =&gt; (
        &lt;ToDoItem
          key={item}
          id={index}
          label={item}
          onDelete={() =&gt; deleteToDo(index)}
        /&gt;
      ))}
    &lt;/Container&gt;
  );
};</code></pre>
<p>부모 컴포넌트인 ToDoList 컴포넌트에서 자식 컴포넌트인 ToDoItem 컴포넌트에 props로 id를 넘겨줍니다. 그럼 에러가 사라진 것을 확인할 수 있습니다. </p>
<br />

<p><strong><span style="background-color: yellow;">Detail 페이지 컴포넌트</span></strong>
할 일 목록 페이지에서 하나의 할 일을 선택했을 때, 해당 할 일의 내용을 확인할 수 있는 상세 페이지를 만들어 줍니다. 이를 위해 <code>./src/Pages/Detail/index.tsx</code> 파일을 생성해줍니다. 
좀 더 강화된 타입 지정과, 리액트 저번 업그레이드에 따른 useHistory -&gt; useNavigate 라이브러리로 변경한 코드 수정본입니다.</p>
<pre><code class="language-jsx">import { Button } from 'Components/Button';
import { useContext } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { ToDoListContext } from 'src/Contexts/ToDoList';
import styled from 'styled-components';

const Container = styled.div`
  display: flex;
  background-color: #ffffff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2);
  align-items: center;
  flex-direction: column;
`;

const ToDo = styled.div`
  min-width: 350px;
  height: 350px;
  overflow-y: auto;
  border: 1px solid #bdbdbd;
  margin-bottom: 20px;
  padding: 10px;
`;

export const Detail = () =&gt; {
  const navigate = useNavigate();
  const { id } = useParams&lt;{ id: string }&gt;(); // ✅ 제네릭으로 id 타입 지정

  if (!id) {
    // 라우트 파라미터가 없을 때 처리
    navigate(-1);
    return null;
  }

  const index = Number.parseInt(id, 10);
  const { toDoList, deleteToDo } = useContext(ToDoListContext);
  const toDo = toDoList[index];

  return (
    &lt;Container&gt;
      &lt;ToDo&gt;{toDo}&lt;/ToDo&gt;
      &lt;Button
        label=&quot;삭제&quot;
        backgroundColor=&quot;#FF1744&quot;
        hoverColor=&quot;#F01440&quot;
        onClick={() =&gt; {
          deleteToDo(index);
          navigate(-1);
        }}
      /&gt;
    &lt;/Container&gt;
  );
};</code></pre>
<p>이렇게 만든 상세 페이지를 사용하기 위해 <code>./src/App.tsx</code> 파일에 다음을 추가해줍니다. </p>
<pre><code class="language-jsx">...

function App() {
  return (
    &lt;ToDoListProvider&gt;
      &lt;Container&gt;
        &lt;Routes&gt;
          ...
          &lt;Route path=&quot;/detail/:id&quot; element={&lt;Detail /&gt;} /&gt;
        &lt;/Routes&gt;
      &lt;/Container&gt;
    &lt;/ToDoListProvider&gt;
  );
}

export default App;</code></pre>
<br />

<p><strong><span style="background-color: yellow;">PageHeader 컴포넌트</span></strong>
현재 개발한 할 일 추가/할 일 상세 페이지에서 이전 페이지로 돌아가기 위해서는 브라우저의 뒤로 가기 버튼을 눌러야만 합니다. 
이런 불편함을 없애기 위해 페이지 헤더 컴포넌트를 만들고, 헤더 컴포넌트로 돌아가는 버튼을 추가해줍니다. 
<code>./src/Components/PageHeader/index.tsx</code>을 만들어줍니다. </p>
<pre><code class="language-jsx">import { Link, useLocation } from 'react-router-dom';
import styled from 'styled-components';

const Container = styled.div`
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #1e40ff;
`;

const Title = styled.div`
  padding: 20px;
  font-size: 20px;
  font-weight: 600;
`;

const GoBack = styled(Link)`
  padding: 20px;
  color: #ffffff;
  font-size: 16px;
  font-weight: 600;
  text-decoration: none;
  position: absolute;
  left: 20px;
`;

export const PageHeader = () =&gt; {
  const { pathname } = useLocation();
  let title = '에러';

  if (pathname === '/') {
    title = '할 일 목록';
  } else if (pathname === '/add') {
    title = '할 일 추가';
  } else if (pathname.startsWith('/detail')) {
    title = '할 일 상세';
  }

  return (
    &lt;Container&gt;
      &lt;Title&gt;{title}&lt;/Title&gt;
      {pathname !== '/' &amp;&amp; &lt;GoBack to=&quot;/&quot;&gt;돌아가기&lt;/GoBack&gt;}
    &lt;/Container&gt;
  );
};</code></pre>
<p>이렇게 추가한 PageHeader 컴포넌트를 사용하기 위해 <code>./src/App.tsx</code> 파일을 열어 수정해줍니다.</p>
<pre><code class="language-jsx">...

function App() {
  return (
    &lt;ToDoListProvider&gt;
      &lt;Container&gt;
        &lt;PageHeader /&gt;
        &lt;Routes&gt;
          ...
      &lt;/Container&gt;
    &lt;/ToDoListProvider&gt;
  );
}

export default App;</code></pre>
<br />

<p><strong><span style="background-color: yellow;">NotFound 페이지 컴포넌트</span></strong>
마지막으로, 사용자가 존재하지 않는 url을 입력했을 때 표시할 NotFound 페이지 컴포넌트를 만들기 위해 <code>./src/Pages/NotFound/index.tsx</code> 파일을 만들어줍니다. </p>
<pre><code class="language-jsx">import styled from 'styled-components';

const Container = styled.div`
  font-size: 20px;
`;

export const NotFound = () =&gt; {
  return &lt;Container&gt;Not Found 👤&lt;/Container&gt;;
};</code></pre>
<p>그 다음 <code>./src/App.tsx</code> 파일에 추가해줍니다. </p>
<pre><code class="language-jsx">...

function App() {
  return (
    &lt;ToDoListProvider&gt;
      &lt;Container&gt;
        &lt;PageHeader /&gt;
        &lt;Routes&gt;
          ...
        &lt;/Routes&gt;
      &lt;/Container&gt;
    &lt;/ToDoListProvider&gt;
  );
}

export default App;</code></pre>
