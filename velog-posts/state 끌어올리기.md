<p>연구실 스터디에서 새로운 프로젝트로 이번에 새롭게 리뉴얼한 교수님 연구실 페이지를 클론 코딩을 해보게 되었다. </p>
<p>바로 전 프로젝트에서도 교수님 연구실 페이지를 만드는 것이었지만, 그 땐 react로만 만들었는데 이번에는 nextJS로 만들어보게 되었다. </p>
<p>첫째 주에는 헤더를 반응형으로 만드는 것이 과제였다. 
먼저 nextjs 프로젝트를 만들기 위해 vscode 새 터미널에 아래와 같은 명령어를 입력해주었다. </p>
<pre><code class="language-javascript">npx create-next-app@latest</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/eadfe7ab-3351-42ef-b886-8ea42fd4687f/image.png" /></p>
<p>프로젝트를 생성해주었더니 react와는 다른 생소한 폴더구조를 볼 수 있었다. 
src/app에 생성하는 폴더구조가 바로 라우팅 주소로 설정되어 따로 라우팅 설정을 해주지 않아도 된다고 한다. 
react로 프로젝트를 만들 때는 react-router-dom으로 일일이 설정해줬던 기억이 있는데 너무 신기했다.</p>
<p>이렇게 따로 라우팅 설정을 해주지 않고 폴더이름으로 해줄 수 있는 이유는
nextJS는 <strong>파일 기반 라우팅 시스템</strong>을 사용하기 때문에 프로젝트의 &quot;app&quot; 디렉토리 안에 있는 파일과 폴더 구조를 기반으로 자동으로 라우트를 생성하기 때문이다. </p>
<p>이러한 파일 기반 라우팅의 주요 특징은 크게 5가지로 구분지을 수 있다고 한다. </p>
<ul>
<li><strong>1. 자동 라우트 매핑</strong>
: &quot;app&quot; 디렉토리 안에 있는 각 파일은 해당 파일 경로에 따른 URL에 자동으로 매핑된다. 
예를 들어, &quot;app/about/page.js&quot; 파일은 &quot;<a href="http://www.mysite.com/about&quot;%EC%9C%BC%EB%A1%9C">www.mysite.com/about&quot;으로</a> 접근할 수 있다. </li>
<li><strong>2. 동적 라우트</strong> 
: 대괄호([])를 사용해 파일이나 폴더 이름을 지정하여 동적 경로를 생성할 수 있다. 
예를 들어, &quot;app/about/[id].js&quot;는 &quot;<a href="http://www.mysite.com/1&quot;">www.mysite.com/1&quot;</a> 등과 같이 다양한 id에 대해 같은 페이지 구성을 사용할 수 있도록 한다. </li>
<li><strong>3. 중첩 라우트</strong>
: 폴더 구조를 사용해 중첩된 경로를 자연스럽게 만들 수 있다. 
예를 들어, &quot;app/about/first-page.js&quot;는 &quot;<a href="http://www.mysite.com/about/first-page&quot;%EB%A1%9C">www.mysite.com/about/first-page&quot;로</a> 라우트 된다고 한다.</li>
<li><strong>4. 특수 파일과 경로</strong>
: &quot;app&quot; 디렉토리 안에서 &quot;_app.js&quot;, &quot;_document.js&quot;, &quot;_error.js&quot;과 같은 특수 파일을 사용해 전체 애플리케이션 레벨의 커스텀 설정을 할 수 있다. 
예를 들어, &quot;_app.js&quot;는 모든 페이지에 공통으로 적용되는 레이아웃이나 상태를 관리할 때 사용될 수 있다. </li>
<li><strong>5. API 기반 라우트</strong>
: &quot;app/api&quot; 디렉토리를 사용해 <em>서버리스</em> 함수를 정의할 수 있다. 
이것은 next.js에서 제공하는 api 라우트 기능으로, 각 파일은 해당 파일 이름에 따른 api 엔드포인트가 된다. 
예를 들어 &quot;app/api/user.js&quot;는 &quot;<a href="http://www.mysite.com/api/user&quot;%EB%A1%9C">www.mysite.com/api/user&quot;로</a> 접근할 수 있는 api 엔드포인트를 생성한다. </li>
</ul>
<hr />
<p>그 다음 나는 src 폴더 아래에 components 폴더를 생성하여 그 안에 header 폴더를 생성하여 헤더를 만들어보았다. 
리액트로 반응형을 만들었을 땐, 프로젝트 디렉토리 안에 react-responsive 라이브러리를 이용해 useMediaQuery로 모바일, 데스크, 태블릿 크기만 지정해준 다음 
모든 폴더마다 모바일/태블릿/데스크탑 폴더를 만들어 css속성을 일일이 지정해줬는데 
이번에는 src폴더 아래에 hooks라는 폴더를 만들어 아래와 같이 코드를 작성해주었다. </p>
<pre><code class="language-javascript">import { useMediaQuery } from 'react-responsive';

export function useDeviceSize() {
    const isDesktop = useMediaQuery({ query: '(min-width: 1024px)' });
    const isTablet = useMediaQuery({ query: '(min-width:768px) and (max-width:1023px)' });
    const isMobile = useMediaQuery({ query: '(max-width:767px)' });

    return { isDesktop, isTablet, isMobile };
}

export function useHeaderSize() {
    const showSix = useMediaQuery({ query: '(min-width: 880px)' });
    const showFive = useMediaQuery({ query: '(min-width:874px) and (max-width:879px)' });
    const showFour = useMediaQuery({ query: '(min-width:779px) and (max-width:873px)' });
    const showThree = useMediaQuery({ query: '(min-width:768px) and (max-width:779px)' });

    const showHamburgerMenu = useMediaQuery({ query: '(max-width:767px)' });

    let showNumber = 6;
    if (showSix) showNumber = 6;
    if (showFive) showNumber = 5;
    if (showFour) showNumber = 4;
    if (showThree) showNumber = 3;
    if (showHamburgerMenu) showNumber = 0;

    const results = {
        isShowHamburgerMenu: showHamburgerMenu,
        showNumber: showNumber,
    };

    return results;
}</code></pre>
<p>데스크탑, 모바일, 태블릿 크기를 지정해준다음, 뷰 크기에 따라 헤더에 나타나는 메뉴 아이템의 개수를 직접 설정해주었다. 
이것은 뷰 너비에 따라 햄버거 버튼, 더보기 버튼을 구현하기 위한 밑작업이다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/374ca8ed-c12b-4ecb-8e2c-1755d447d85f/image.png" />
헤더 컴포넌트의 계층 구조는
Header -&gt; NavBar -&gt; SeeMoreMenu -&gt; SeeMoreBar 순이다. 
처음에 계층 구조를 생각하지 못하고 &quot;컴포넌트 분리&quot;에만 집중하다보니 props의 흐름을 잊고 SeeMoreMenu에 useState로 props를 관리했다. </p>
<p>처음에는 더보기 버튼 메뉴의 아이템을 클릭했을 때,
해당 메뉴에 경로를 표시하기 위해 해당 메뉴 아이템에 적용하려했던 bg-gray-400 속성이 적용되지 않고, 페이지 이동은 되지만 nav바에 그 전 메뉴 아이템에 css 속성이 적용된 상태가 유지되는 문제가 있었다. </p>
<p>이것은 더보기 버튼 클릭했을 때, 다른 이벤트 핸들러가 동작하지 않는 이유는 더보기 버튼을 누르면 메뉴가 삭제되며 unmount되기 때문이어서 useSelectedLayout()을 이용하면 된다는 피드백을 받았다. 
(이건 아직 이해를 못해서 적용시키지 못했다..)</p>
<p>그래서 코드를 갈아엎고 NavBar 밑에 SeeMoreMenu컴포넌트를 자식으로 두어 클릭했을 때의 로직까지 작성 후, 그 자식으로 SeeMoreBar 컴포넌트를 두어 메뉴를 펼쳤을 때 일어나는 로직을 작성하여 분리해주었다. </p>
<p>이 로직으로 작성했을 떄, 메뉴 아이템에 적용되는 bg-gray-400 속성이 nav바에도, SeeMoreMenu 총 2개가 적용되는 문제가 발생했다. </p>
<pre><code class="language-javascript">import React, { useState } from 'react';
import { useHeaderSize } from '@/hooks/useDeviceSize';
import { MenuItem } from '@/constants/MenuItem';
import Link from &quot;next/link&quot;;
import SeeMoreMenu from &quot;./SeeMoreMenu&quot;;
import SearchIcon from './_icons/SearchIcon';

type Props = {
    selectedItem: string | null;
    setSelectedItem: (item: string | null) =&gt; void;
};

export default function NavBar({ selectedItem, setSelectedItem }: Props) {
    const { showNumber, isShowHamburgerMenu } = useHeaderSize();
    const [isScrolled, setIsScrolled] = useState(false);
    const iconColor = isScrolled ? &quot;black&quot; : &quot;white&quot;;

    const visibleItems = MenuItem.slice(0, showNumber);
    const subMenuItems = MenuItem.slice(showNumber);

    return (
        &lt;main className=&quot;mb-2.5&quot;&gt;
            &lt;div className=&quot;flex flex-1 justify-end mr-3&quot;&gt;
                &lt;nav className={`p-3 flex justify-center items-end ${isShowHamburgerMenu ? 'pr-10' : ''}`}&gt;
                    &lt;ul className=&quot;flex gap-4&quot;&gt;
                        {visibleItems.map((item, index) =&gt; (
                            &lt;li key={index}
                                className={`cursor-pointer ${selectedItem === item.name ? 'bg-gray-400' : 'bg-transparent'}`}
                                onClick={() =&gt; setSelectedItem(item.name)}&gt;
                                &lt;Link href={item.href}&gt;{item.name}&lt;/Link&gt;
                            &lt;/li&gt;
                        ))}
                        {!isShowHamburgerMenu &amp;&amp; subMenuItems.length &gt; 0 &amp;&amp; &lt;SeeMoreMenu subMenuItems={subMenuItems} selectedItem={selectedItem} setSelectedItem={setSelectedItem} /&gt;}
                    &lt;/ul&gt;
                &lt;/nav&gt;
                &lt;div className=&quot;mt-2.5&quot;&gt;
                    &lt;SearchIcon color={iconColor} /&gt;
                &lt;/div&gt;
            &lt;/div&gt;
        &lt;/main&gt;
    );
};</code></pre>
<p>컴포넌트의 위치도 바꿔보고, props의 타입도 설정해보고 이것저것 다 해보았는데 문제는 해결되지 않았다. 
그래서 결국 gpt의 도움을 받게 되었는데 이 문제는 <strong>state 끌어올리기</strong>로 해결할 수 있다는 답변을 받았다. </p>
<p>그래서 나는 놓치고 있던 header의 계층 구조를 살펴보았다. 
Header - NavBar - SeeMoreMenu - SeeMoreBar 순으로 부모-자식 관계가 이뤄지는데 나는 SeeMoreMenu에 props 설정을 해놓았던 것이다.
props는 부모에서 자식으로 전달되는 값이기 때문에 전달하려는 최상위 컴포넌트에 상태를 설정해줘야 한다는 것을 잊고 있었던 것이다.  </p>
<pre><code class="language-javascript">// Header.tsx
&quot;use client&quot;;
import { useScroll } from &quot;@/hooks/useScroll&quot;;
import HeaderIcon from &quot;./_icons/HeaderIcon&quot;;
import NavBar from &quot;./NavBar&quot;;
import Title from &quot;@/constants/Title&quot;;
import BackgroundImage from &quot;./_components/BackgroundImage&quot;;
import HamburgerMenu from &quot;./HamburgerMenu&quot;;
import { MenuItem } from &quot;@/constants/MenuItem&quot;;
import { useState } from &quot;react&quot;;

export default function Header() {
    const isScroll = useScroll();
    const [selectedItem, setSelectedItem] = useState&lt;string | null&gt;(null);

    return (
        &lt;div className=&quot;relative w-full&quot;&gt;
            &lt;BackgroundImage /&gt;
            &lt;div className=&quot;absolute top-0 left-0 right-0&quot;&gt;
                &lt;header className={`w-full flex justify-between items-center fixed z-20 ${isScroll ? 'bg-white text-black' : 'bg-transparent text-white'} transition-colors ease-in-out`}&gt;
                    &lt;HamburgerMenu subMenuItems={MenuItem} /&gt;
                    &lt;HeaderIcon /&gt;
                    &lt;NavBar selectedItem={selectedItem}
                        setSelectedItem={setSelectedItem} /&gt;
                &lt;/header&gt;
                &lt;Title /&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    );
};
</code></pre>
<pre><code class="language-javascript">// NavBar.tsx
import React, { useState } from 'react';
import { useHeaderSize } from '@/hooks/useDeviceSize';
import { MenuItem } from '@/constants/MenuItem';
import Link from &quot;next/link&quot;;
import SeeMoreMenu from &quot;./SeeMoreMenu&quot;;
import SearchIcon from './_icons/SearchIcon';

type Props = {
    selectedItem: string | null;
    setSelectedItem: (item: string | null) =&gt; void;
};

export default function NavBar({ selectedItem, setSelectedItem }: Props) {
    const { showNumber, isShowHamburgerMenu } = useHeaderSize();
    const [isScrolled, setIsScrolled] = useState(false);
    const iconColor = isScrolled ? &quot;black&quot; : &quot;white&quot;;

    const visibleItems = MenuItem.slice(0, showNumber);
    const subMenuItems = MenuItem.slice(showNumber);

    return (
        &lt;main className=&quot;mb-2.5&quot;&gt;
            &lt;div className=&quot;flex flex-1 justify-end mr-3&quot;&gt;
                &lt;nav className={`p-3 flex justify-center items-end ${isShowHamburgerMenu ? 'pr-10' : ''}`}&gt;
                    &lt;ul className=&quot;flex gap-4&quot;&gt;
                        {visibleItems.map((item, index) =&gt; (
                            &lt;li key={index}
                                className={`cursor-pointer ${selectedItem === item.name ? 'bg-gray-400' : 'bg-transparent'}`}
                                onClick={() =&gt; setSelectedItem(item.name)}&gt;
                                &lt;Link href={item.href}&gt;{item.name}&lt;/Link&gt;
                            &lt;/li&gt;
                        ))}
                        {!isShowHamburgerMenu &amp;&amp; subMenuItems.length &gt; 0 &amp;&amp; &lt;SeeMoreMenu subMenuItems={subMenuItems} selectedItem={selectedItem} setSelectedItem={setSelectedItem} /&gt;}
                    &lt;/ul&gt;
                &lt;/nav&gt;
                &lt;div className=&quot;mt-2.5&quot;&gt;
                    &lt;SearchIcon color={iconColor} /&gt;
                &lt;/div&gt;
            &lt;/div&gt;
        &lt;/main&gt;
    );
};</code></pre>
<pre><code class="language-javascript">// SeeMoreMenu.tsx
import { useState } from &quot;react&quot;;
import { MenuItem } from &quot;@/constants/MenuItem&quot;;
import SeeMoreBar from &quot;./SeeMoreBar&quot;;

type Props = {
    subMenuItems: MenuItem[];
    selectedItem: string | null;
    setSelectedItem: (item: string | null) =&gt; void;
};
export default function SeeMoreMenu({ subMenuItems, selectedItem, setSelectedItem }: Props) {
    const [active, setActive] = useState(false);


    const onActiveMenu = () =&gt; {
        setActive(!active);
    };


    return (
        &lt;&gt;
            &lt;li className=&quot;flex relative&quot; onClick={onActiveMenu}&gt;
                &lt;p className=&quot;cursor-pointer&quot;&gt;더보기&lt;/p&gt;
                {active &amp;&amp; (
                    &lt;SeeMoreBar
                        menuItems={subMenuItems}
                        selectedItem={selectedItem}
                        setSelectedItem={setSelectedItem}
                    /&gt;
                )}
            &lt;/li&gt;
        &lt;/&gt;
    );
};</code></pre>
<pre><code class="language-javascript">// SeeMoreBar.tsx
import { MenuItem } from &quot;@/constants/MenuItem&quot;;
import Link from &quot;next/link&quot;;

type Props = {
    menuItems: MenuItem[];
    selectedItem: string | null;
    setSelectedItem: (name: string) =&gt; void;
};

export default function SeeMoreBar({ menuItems, selectedItem, setSelectedItem }: Props) {
    return (
        &lt;div className=&quot;submenu-container open border-2 border-black absolute top-8 -left-[85px] w-[180px] px-8 py-8 rounded-sm bg-white text-black&quot;&gt;
            &lt;ul className=&quot;flex flex-col&quot;&gt;
                {menuItems.map((item, index) =&gt; (
                    &lt;li key={index} 
                        className={`cursor-pointer ${selectedItem === item.name ? 'bg-gray-400' : 'bg-transparent'} p-2`}
                        onClick={() =&gt; setSelectedItem(item.name)}&gt;
                        &lt;Link href={item.href}&gt;{item.name}&lt;/Link&gt;
                    &lt;/li&gt;
                ))}
            &lt;/ul&gt;
        &lt;/div&gt;
    );
}</code></pre>
<p>그래서 Header 컴포넌트에 useState로 아래와 같이 상태값을 설정해준 뒤, 그 자식 컴포넌트 NavBar에 props를, 그 밑의 자식 컴포넌트에도 props를 전달해주어 문제를 해결하였다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/e74ee7a7-71d5-4a34-9167-beb524747261/image.png" /></p>
<p>이렇게 설정을 거치고 나니 props의 깊이가 좀 깊은 거 아닌가?라는 의문이 들었다. 
udemy에서 강의를 들었을 때, props의 깊이가 깊어지면 <strong>context</strong>를 이용해 props 관리를 해줄 수 있다고 하였는데 이것은 컴포넌트 분리를 깔끔하게 한 후에 시도를 해봐야겠다.</p>
<br />

<p><strong>헤더와 관련해서 앞으로의 과제</strong></p>
<ul>
<li>useSelectedLayoutSegments()로 useState 대신 적용해보기</li>
<li>context 사용해보기</li>
<li>컴포넌트 더 깔끔하게 분리해보기</li>
<li><blockquote>
<p>커스텀 훅을 쓰는 것이 중요 &amp; 레이아웃도 분리하여 컨테이너로 사용해보기</p>
</blockquote>
</li>
</ul>