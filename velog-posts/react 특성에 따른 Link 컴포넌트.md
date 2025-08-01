---
title: react 특성에 따른 Link 컴포넌트
date: Thu, 28 Mar 2024 14:36:01 GMT
link: https://velog.io/@so356hot/%EC%95%8C%EA%B2%8C%EB%90%9C-%EC%A0%90
---

<ul>
<li>리액트에서는 a태그를 이용한 href 대신 Link 컴포넌트를 사용해야 한다. 
→ 상태값을 잃고 속도가 저하되기 때문이다. </li>
</ul>
<p>리액트는 단일 url을 가지고 SPA(Single Page Application)으로 사이트를 표현하는 프레임워크로, 
하나의 html 페이지와 애플리케이션 실행에 필요한 javascript와 css 같은 모든 자산을 로드하는 애플리케이션이다. </p>
<p>따라서 이러한 이유로 페이지를 새로 불러오게 되면 앱이 지니고 있는 상태가 초기화되고, 렌더링 된 컴포넌트도 모두 사라지고 새로 렌더링 해야 한다.</p>
<p>⇒ 상태 유지와 속도의 효율성을 위해 새로운 페이지를 불러오는 대신, 업데이트 하는 방식으로 구현해야 한다.</p>
<ul>
<li>a 태그의 href: 페이지를 이동시킬 때 페이지를 새로 불러오게 된다. 
→ 따라서 상태 값이 유지되지 못하고 속도도 저하된다.</li>
<li>Link 컴포넌트: html5 history api를 사용해 브라우저의 주소만 바꿀 뿐, 페이지를 새로 불러오진 않는다.</li>
</ul>
<p>→ a태그의 href를 Link 컴포넌트로 변경해준 뒤 테스트 해본 결과, href를 사용했을 때는 다른 페이지 이동 시 시간이 체감상 1초 정도 걸렸는데 Link 컴포넌트를 사용했을 때는 바로 바뀌는 것을 확인할 수 있었다. 이것으로 리액트에서 href 사용시 속도 저하를 직접 체감할 수 있었다. </p>
<ul>
<li><p>pathname, useLocation을 이용해 해당 경로에 스타일을 주려고 시도해보았다. 
isClickActive명을 정의해 현재 페이지 경로를 확인해 해당 경로에 맞는 메뉴 아이템에 현재 글씨에 볼드체로 굵게 표현하고 글씨 아래에 밑줄을 나타나게 만들어 보았다.</p>
</li>
<li><p>Outlet 컴포넌트는 자식 라우트를 렌더링하는 컴포넌트라고 한다. 
이는 각각의 페이지 컴포넌트를 적절히 표시하는 데 사용된다고 한다. 
이 컴포넌트는 추후에 나오지 않을 페이지도 만들 것까지 고려해 사용하는 것이라고 한다.</p>
</li>
<li><p>merge 후에 header가 상단에 고정되어 스크롤 시, 헤더가 안 보이거나 이미지에 겹쳐 보이는 issue가 발생했다
→ z-index를 10으로 주어 다른 컴포넌트보다 좀 더 위에 주어 해결할 수 있었다.</p>
</li>
</ul>
