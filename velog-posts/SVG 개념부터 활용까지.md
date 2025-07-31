# 📌 Velog 글 요약

| 항목   | 내용 |
|--------|------|
| **제목** | SVG 개념부터 활용까지 |
| **날짜** | Fri, 06 Sep 2024 08:17:51 GMT |
| **링크** | [https://velog.io/@so356hot/SVG-%EA%B0%9C%EB%85%90%EB%B6%80%ED%84%B0-%ED%99%9C%EC%9A%A9%EA%B9%8C%EC%A7%80](https://velog.io/@so356hot/SVG-%EA%B0%9C%EB%85%90%EB%B6%80%ED%84%B0-%ED%99%9C%EC%9A%A9%EA%B9%8C%EC%A7%80) |

---

<h3 id="span-stylebackground-color-fff5b1svg-중요성-써야-하는-이유-래스터-파일의-한계-보완span"><span style="background-color: #fff5b1;">SVG 중요성: 써야 하는 이유, 래스터 파일의 한계 보완</span></h3>
<p>이미지 관리는 웹 성능을 결정 짓는 리소스 관리의 중요한 사항 중 하나라고 한다. 이에 svg가 많이 쓰인다고 한다.</p>
<p><code>svg</code>는 <code>png</code>, <code>jpg</code>보다 상대적으로 사용하기 전에 학습도 필요하기 때문에 쓰기가 꺼려질 수도 있으나,  <code>png</code>, <code>jpg</code> 같은 래스터 기반 포맷보다 이미지를 리사이징해도 깨지지 않는다는 장점과, 상대적으로 적은 용량으로 사용할 수 있다는 점, 애니메이션 추가가 가능하다는 점 등 다양한 장점을 갖고 있어 웹 개발에 자주 사용되는 <code>svg</code> 를 활용하는 다양한 방법에 대해 알아보고자 한다.</p>
<p>우선, <code>svg</code>의 주요 특징에 대해 살펴보자.</p>
<ol>
<li><p><span style="background-color: #eaeaea;"><strong>확장성</strong></span>
픽셀 기반이 아니기 때문에 크기를 조정해도 이미지가 깨지지 않는다. 모든 해상도에 대응할 수 있으며, 특히 반응형 웹 디자인에 적합하다</p>
</li>
<li><p><span style="background-color: #eaeaea;"><strong>파일 크기와 복잡도</strong></span>
<code>png</code>, <code>jpg</code>는 해상도가 높아질수록 파일 크기가 커진다. 이는 웹페이지 로드 시간을 길게 만들어 사용자 경험에 부정적인 영향을 줄 수 있다.
반면에, <code>svg</code>는 이미지의 <strong>복잡도</strong>가 파일 크기를 결정짓는 중요한 요소이다. <code>svg</code>는 코드로 이뤄져 있기 때문에 바이트도 안되는 크기로 이뤄져 있어 <code>png</code>, <code>jpg</code>보다 이미지 용량적인 측면에서 훨씬 적어 웹 사이트의 로딩 속도를 훨씬 빠르게 만들어준다. 
복잡도가 높은 <code>svg</code>도 최적화 토구를 통해 용량을 줄일 수 있어, 웹사이트 로딩 속도 측면에서 효율적이다.</p>
</li>
<li><p><span style="background-color: #eaeaea;"><strong>인터랙티브 요소 지원</strong></span>
<code>svg</code>는 단순히 정적인 이미지가 아니다. <code>css</code>를 사용하여 스타일을 지정할 수 있기 때문에, 실시간으로 디자인 변경이 가능하다.
예를 들어, 사용자가 버튼을 <code>hover</code>했을 때 색상에 바뀌거나 모양이 변하는 효과를 줄 수 있다.</p>
</li>
<li><p><span style="background-color: #eaeaea;"><strong>애니메이션 가능</strong></span>
<code>svg</code>는 <code>css</code>나 <code>JavaScript</code>를 통해 간단한 애니메이션을 추가할 수 있다. 복잡한 애니메이션 보다는, 아이콘의 움직임이나 색상 변화 등 가벼운 애니메이션을 구현하는 데 적합하다.</p>
</li>
<li><p><span style="background-color: #eaeaea;"><strong>가독성과 수정 용이성</strong></span>
<code>svg</code>코드는 HTML 코드와 마찬가지로 사람이 읽고 수정할 수 있는 코드로 작성된다. 아래 예시 코드는 간단한 <code>svg</code>코드이다.</p>
</li>
</ol>
<pre><code class="language-jsx">&lt;svg width=&quot;300&quot; height=&quot;300&quot;&gt;
  &lt;circle cx=&quot;150&quot; cy=&quot;50&quot; r=&quot;30&quot; /&gt;
  &lt;rect x=&quot;100&quot; y=&quot;100&quot; width=&quot;100&quot; height=&quot;100&quot; /&gt;
&lt;/svg&gt;</code></pre>
<p>반면에 <code>jpg</code>, <code>png</code>같은 래스터 포맷 이미지는 사람이 읽을 수 없는 데이터로 이뤄져 있기 때문에 수정이 필요할 땐 포토샵 같은 그래픽 소프트웨어가 필요하다.</p>
<pre><code class="language-jsx">ÿØÿàJFIF     d    dÿìd     ÿî&amp;          dÀ
    [ -&quot; ´
ÿÛ„ ÿÂd d ÿÄÌ                                      0 p!
          ! 01A&quot;2#$ aqBrQ‘¡b3Ss%5Cc4TÔU•μ&amp;6V</code></pre>
<h3 id="span-stylebackground-color-fff5b1svg의-기본-구조와-주요-구성-요소span"><span style="background-color: #fff5b1;">SVG의 기본 구조와 주요 구성 요소</span></h3>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/9340b73c-136f-4178-8b6d-11c2c30cb531/image.png" /></p>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;ko&quot;&gt;
  &lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot; /&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot; /&gt;
    &lt;title&gt;&lt;/title&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;svg
      width=&quot;200&quot;
      height=&quot;250&quot;
      version=&quot;1.1&quot;
      xmlns=&quot;http://www.w3.org/2000/svg&quot;
    &gt;
      &lt;!-- 정사각형 --&gt;
      &lt;rect
        x=&quot;10&quot;
        y=&quot;10&quot;
        width=&quot;30&quot;
        height=&quot;30&quot;
        stroke=&quot;black&quot;
        fill=&quot;transparent&quot;
        stroke-width=&quot;5&quot;
      /&gt;
      &lt;!-- 모서리가 둥근 사각형 --&gt;
      &lt;rect
        x=&quot;60&quot;
        y=&quot;10&quot;
        rx=&quot;10&quot;
        ry=&quot;10&quot;
        width=&quot;30&quot;
        height=&quot;30&quot;
        stroke=&quot;black&quot;
        fill=&quot;transparent&quot;
        stroke-width=&quot;5&quot;
      /&gt;
      &lt;!-- 원 --&gt;
      &lt;circle
        cx=&quot;25&quot;
        cy=&quot;75&quot;
        r=&quot;20&quot;
        stroke=&quot;red&quot;
        fill=&quot;transparent&quot;
        stroke-width=&quot;5&quot;
      /&gt;
      &lt;!-- 타원 --&gt;
      &lt;ellipse
        cx=&quot;75&quot;
        cy=&quot;75&quot;
        rx=&quot;20&quot;
        ry=&quot;5&quot;
        stroke=&quot;red&quot;
        fill=&quot;transparent&quot;
        stroke-width=&quot;5&quot;
      /&gt;
      &lt;!-- 1차 방정식 같은 직선 --&gt;
      &lt;line
        x1=&quot;10&quot;
        x2=&quot;50&quot;
        y1=&quot;110&quot;
        y2=&quot;150&quot;
        stroke=&quot;orange&quot;
        stroke-width=&quot;5&quot;
      /&gt;
      &lt;!-- 해리포터 흉터 같은 노란 선 --&gt;
      &lt;polyline
        points=&quot;60 110 65 120 70 115 75 130 80 125 85 140 90 135 95 150 100 145&quot;
        stroke=&quot;orange&quot;
        fill=&quot;transparent&quot;
        stroke-width=&quot;5&quot;
      /&gt;
      &lt;!-- 초록별 --&gt;
      &lt;polygon
        points=&quot;50 160 55 180 70 180 60 190 65 205 50 195 35 205 40 190 30 180 45 180&quot;
        stroke=&quot;green&quot;
        fill=&quot;transparent&quot;
        stroke-width=&quot;5&quot;
      /&gt;
      &lt;!-- 파란 곡선 --&gt;
      &lt;path
        d=&quot;M20,230 Q40,205 50,230 T90,230&quot;
        fill=&quot;none&quot;
        stroke=&quot;blue&quot;
        stroke-width=&quot;5&quot;
      /&gt;
    &lt;/svg&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>
<p>위 코드는 다양한 <code>svg</code>태그를 사용해 도형을 그린 것이다. 각 태그는 특정한 도형을 표현하며, 해당 속성을 이용해 위치와 크기 등을 조정할 수 있다.</p>
<blockquote>
<p><strong><code>&lt;rect&gt;</code> [사각형을 그리는 태그]</strong>
    사각형을 그리는 태그. 여기에는 사각형의 위치와 모양을 제어하는 6가지 속성이 있다. 
    ——<strong>속성——</strong>
     <code>x</code> : 사각형 좌측 상단의 x값
     <code>y</code> : 사각형 좌측 상단의 y값
     <code>width</code> : 사각형의 너비
     <code>height</code> : 사각형의 높이
     <code>rx</code> : 사각형의 가로 방향(x축)에서 둥글게 만드는 정도
     <code>ry</code> : 사각형의 세로 방향(y축)에서 둥글게 만드는 정도</p>
</blockquote>
<pre><code>&lt;rect x=&quot;10&quot; y=&quot;10&quot; width=&quot;30&quot; height=&quot;30&quot; /&gt;</code></pre><blockquote>
<p><strong><code>&lt;circle&gt;</code> [원을 그리는 태그]</strong>
    원을 그리는 태그.  원의 모양을 제어할 수 있는 요소는 3가지이다.
    ——<strong>속성——</strong>
     <code>r</code> : 원의 반지름
     <code>cx</code> : 원의 중심의 x값
     <code>cy</code> : 원의  중심의 y값</p>
</blockquote>
<pre><code>&lt;circle cx=&quot;50&quot; cy=&quot;50&quot; r=&quot;40&quot; /&gt;</code></pre><blockquote>
<p><strong><code>&lt;ellipse&gt;</code> [타원을 그리는 태그]</strong>
    타원을 그리는 태그. 원의 x와 y의 반경을 개별적으로 확장할 수 있는 좀 더 일반적인 형태라고 한다.
    ——<strong>속성——</strong>
     <code>rx</code> : 타원의 x 방향으로의 반지름 길이
     <code>ry</code> : 타원의 y 방향으로의 반지름 길이
     <code>cx</code> : 타원의 중심의 x값
     <code>cy</code> : 타원의 중심의 y값</p>
</blockquote>
<pre><code>&lt;ellipse cx=&quot;50&quot; cy=&quot;50&quot; rx=&quot;30&quot; ry=&quot;20&quot; /&gt;</code></pre><blockquote>
<p><strong><code>&lt;line&gt;</code> [직선을 그리는 태그]</strong>
    직선을 그리는 태그. 선의 시작, 끝 지점을 지정하는 두 점을 속성으로 갖는다.
    ——<strong>속성——</strong>
     <code>x1</code> : 점 1의 x값
     <code>y1</code> : 점 1의 y값
     <code>x2</code> : 점 2의 x값
     <code>y2</code> : 점 2의 y값</p>
</blockquote>
<pre><code>&lt;line x1=&quot;10&quot; y1=&quot;10&quot; x2=&quot;50&quot; y2=&quot;50&quot; /&gt;</code></pre><blockquote>
<p><strong><code>&lt;polyline&gt;</code> [직선들의 목록으로, 직선들을 이어붙여 새로운 선을 만드는 태그]</strong>
    직선들의 연결. 직선들은 꽤 길어질 수 있기 때문에 모든 포인트가 하나의 속성이 된다.
    ——<strong>속성——</strong></p>
</blockquote>
<ul>
<li><code>points</code><ul>
<li>포인트들의 목록을 의미<ul>
<li>각 숫자는 공백, 쉼표, 또는 줄바꿈 문자로 구분된다.</li>
<li>각 포인트는 반드시 x, y 좌표를 갖는다.
⇒ (0,0), (1,1)은 “0,0 1,1”이라고 쓸 수 있다.<pre><code>&lt;polyline points=&quot;10,10 20,20 30,10&quot; /&gt;</code></pre></li>
</ul>
</li>
</ul>
</li>
</ul>
<blockquote>
<p><strong><code>&lt;polygon&gt;</code> [다각형을 만드는 태그]</strong>
    점을 연결하는 직선으로 구성된다. (polyline과 유사) 다른 점이라면 자동으로 마지막 포인트로부터 첫 번째 포인트로 직선을 만들어서 닫힌 모양을 만든다.
    ——<strong>속성——</strong></p>
</blockquote>
<ul>
<li><code>points</code><ul>
<li>포인트들의 목록</li>
<li>각 숫자는 공백, 쉼표 또는 줄바꿈 문자로 구분된다.</li>
<li>각 포인트는 반드시 x,y 좌표를 가져야 한다.<ul>
<li>(0,0), (1,1), (2,2) ⇒ “0,0 1,1 2,2”로 쓸 수 있다
⇒ (2,2)에서 (0,0)으로 최종 직선이 그려져서 다각형이 완성된다.<pre><code>&lt;polygon points=&quot;10,10 20,20 30,10&quot; /&gt;</code></pre></li>
</ul>
</li>
</ul>
</li>
</ul>
<blockquote>
<p><strong><code>&lt;path&gt;</code> [패스] (가장 강력한 요소)</strong> ⭐⭐⭐
svg에서 사용할 수 있는 가장 일반적인 형태. 
    기본 도형에서 다뤘던 <code>x</code>, <code>y</code>, <code>fill</code>, <code>stroke</code>, <code>stroke-width</code> 등을 사용할 수 있고, 데이터 속성인 <code>d</code>를 통해 복잡한 도형을 그릴 수 있다.
    ——<strong>속성——</strong></p>
</blockquote>
<ul>
<li><code>d</code>: 경로를 그리기 위한 점과 기타 정보들의 목록입니다.<ul>
<li><strong>moveTo</strong> (이동): <code>M</code> (절대좌표), <code>m</code> (상대좌표)<br />→ 그림을 그리기 시작할 위치로 이동</li>
<li><strong>closePath</strong> (패스 닫기): <code>Z</code>, <code>z</code><br />→ 그리기 종료 (대소문자 구분 없음)</li>
<li><strong>lineTo</strong> (선 그리기)<ul>
<li>직선: <code>L</code> (절대), <code>l</code> (상대)</li>
<li>수평선: <code>H</code> (절대), <code>h</code> (상대)</li>
<li>수직선: <code>V</code> (절대), <code>v</code> (상대)</li>
</ul>
</li>
<li><strong>curve</strong> (커브 그리기)<ul>
<li>큐빅 베지어: <code>C</code>, <code>c</code>, <code>S</code>, <code>s</code></li>
<li>쿼드라틱 베지어: <code>Q</code>, <code>q</code>, <code>T</code>, <code>t</code></li>
<li>엘립티컬 아크: <code>A</code>, <code>a</code><br />→ 타원의 호(원, 타원의 일부분을 그린다)<pre><code>&lt;path d=&quot;M10 10 H 90 V 90 H 10 Z&quot; /&gt;</code></pre></li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="span-stylebackground-color-fff5b1svg-활용-사례-및-코드-예시span"><span style="background-color: #fff5b1;">SVG 활용 사례 및 코드 예시</span></h3>
<p><code>svg</code> 파일이 개발에 주로 사용되는 부분은 크게 로고/아이콘, 차트/그래프, 지도, 애니메이션이 있다. </p>
<ul>
<li><span style="background-color: #eaeaea;"><strong>로고 및 아이콘</strong></span>
: 해상도에 민감하기 때문이다</li>
<li><span style="background-color: #eaeaea;"><strong>차트 및 그래프</strong></span>
: 도형과 경로를 많이 사용하기 때문에 픽셀보다는 벡터가 적합하기 때문이다</li>
<li><span style="background-color: #eaeaea;"><strong>지도</strong></span>
: 지도 데이터는 다양한 크기에서 사용되기 때문에 벡터 그래픽이 필수이다.</li>
<li><span style="background-color: #eaeaea;"><strong>애니메이션</strong></span>
: svg는 SMIL(Synchronized Multimedia Integration Language)을 사용해 간단한 애니메이션을 만들 수 있다</li>
</ul>
<p><span style="background-color: #f5f0ff;"><strong><code>&lt;img&gt;</code>로 svg 사용하기</strong></span></p>
<p>원하는 이미지를 svg로 다운 받고 아래와 같이 <code>&lt;img&gt;</code> 태그를 html에 추가하여 <code>src</code> 속성이 <code>svg</code>이미지를 참조하도록 한다.
<img alt="" src="https://velog.velcdn.com/images/so356hot/post/869b9f50-02ea-4600-8180-5d5f2cd499c9/image.png" /></p>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;ko&quot;&gt;
  &lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot; /&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot; /&gt;
    &lt;title&gt;&lt;/title&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;img src=&quot;image.svg&quot; alt=&quot;test&quot; /&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/bb4be322-a73a-41fe-a365-f5dfc31a3fcf/image.png" /></p>
<p>크기를 지정하지 않는다면 원본 <code>svg</code>파일 크기로 상정된다. 만약, 원본 크기를 변경하고 싶다면 <code>css</code>를 사용해서 <code>width</code>와 <code>height</code>를 설정해줄 수 있다.</p>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;ko&quot;&gt;
  &lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot; /&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot; /&gt;
    &lt;title&gt;&lt;/title&gt;
    &lt;style&gt;
      img {
        height: 100px;
        width: 100px;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;img src=&quot;image.svg&quot; alt=&quot;test&quot; /&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/845c98a8-47da-4ab8-9914-226a7cdb2f47/image.png" /></p>
<p><span style="background-color: #f5f0ff;"><strong><code>background-image</code> 로 svg를 사용하기</strong></span></p>
<p>이 방법은 위의 <code>&lt;img&gt;</code> 태그를 이용해 svg를 추가하는 방법과 비슷하다. <code>css</code>백그라운드 이미지로 <code>svg</code>를 사용한다면, <code>&lt;img&gt;</code> 태그를 사용하는 것보다, <code>css</code>속성을 통해 좀 더 세밀하게 제어할 수 있다.</p>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;ko&quot;&gt;
  &lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot; /&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot; /&gt;
    &lt;title&gt;&lt;/title&gt;
    &lt;style&gt;
      img {
        height: 100px;
        width: 100px;
      }
      body {
        background: url(image.svg) no-repeat;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;!-- &lt;img src=&quot;image.svg&quot; alt=&quot;test&quot; /&gt; --&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/987be59c-0a08-45ee-a3d7-e06e0f82eb82/image.png" /></p>
<p><span style="background-color: #f5f0ff;"><strong>인라인(inline) svg 이미지 사용하는 방법</strong></span></p>
<p><code>svg</code> 이미지는 <code>&lt;svg&gt;</code> 태그로 직접 html 문서에 삽입해 작성할 수도 있다. vsCode나 IDE에서 svg 이미지를 열고, 코드를 복사해 html 문서 <code>&lt;body&gt;</code> 안에 붙여 넣으면 된다.</p>
<p><code>inline</code>방법을 사용하면 <code>&lt;img&gt;</code> 태그나 <code>background-image</code>를 사용하는 것보다 더 다양하게 이미지를 커스텀할 수 있다.</p>
<pre><code class="language-html">    &lt;svg width=&quot;500&quot; height=&quot;250&quot;&gt;
      &lt;rect
        width=&quot;200&quot;
        height=&quot;100&quot;
        fill=&quot;#3d87fb&quot;
        x=&quot;50%&quot;
        y=&quot;50%&quot;
        transform=&quot;translate(-100,-50)&quot;
      /&gt;
    &lt;/svg&gt;</code></pre>
<p><span style="background-color: #f5f0ff;"><strong><code>&lt;object&gt;</code> 로 svg 사용하는 방법</strong></span></p>
<p>이 코드 문법을 사용하면 html에 <code>&lt;object&gt;</code> 요소를 이용해 웹 페이지에 <code>svg</code> 이미지를 추가할 수 있다. <code>data</code>라는 속성에 <code>svg</code> 이미지를 넣어주면 된다.</p>
<pre><code class="language-html">    &lt;object data=&quot;image.svg&quot; width=&quot;300&quot; height=&quot;300&quot;&gt;&lt;/object&gt;</code></pre>
<p>이미지의 내부 조작이 크게 필요하지 않은 경우에는 <code>&lt;img&gt;</code>, <code>backgroud-image</code>를 사용하고, 
보다 복잡한 조작이 필요한 경우에는 <code>inline</code>, <code>&lt;object&gt;</code>를 이용하는 것이 좋다.</p>
