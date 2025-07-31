---
        title: "Socket.IO 개념부터 실시간 채팅 기능까지 알아보기
        date: Thu, 07 Nov 2024 08:03:26 GMT
        link: https://velog.io/@so356hot/Socket.IO-%EA%B0%9C%EB%85%90%EB%B6%80%ED%84%B0-%EC%8B%A4%EC%8B%9C%EA%B0%84-%EC%B1%84%ED%8C%85-%EA%B8%B0%EB%8A%A5%EA%B9%8C%EC%A7%80-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0
        ---
        <h3 id="socket을-사용하게-된-배경">socket을 사용하게 된 배경</h3>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/178f5f0e-bdca-49b0-96b9-92811364b4cf/image.png" /></p>
<p>이번에 Socket.IO를 이용해 각 post 글마다 실시간 채팅 댓글(예를 들면 예전에 있었던 네이버 실시간 댓글..?)을 구현하게 되어 공부하게 되었다. </p>
<p>우선 Socket.IO에 대해 들어가기 전에 소켓이라는 것이 왜 등장하게 된건지부터 알아보면 좋을 것 같아서 기존의 HTTP 방식과 웹소켓을 비교하며, 실시간 데이터 전달의 필요성과 해결 방안부터 살펴보자.</p>
<p><strong>HTTP의 특징과 Polling의 한계</strong>
우선 웹은 HTTP로 server와 client가 통신을 한다. 지난 시간에도 다뤘지만 HTTP 프로토콜에서는 server가 1개의 요청을 받으면 1개의 응답을 하고 연결을 끊어버린다. 그렇게 되면 서버에서는 client의 이전 요청에 대한 정보가 없어 무엇이 변경되었는지 알 수 없다. 
또한 server의 데이터가 업데이트 되더라도 client가 server로 요청을 보내지 않으면 변경된 데이터를 받아올 수 없음을 의미하기도 한다. 
이러한 기존의 전통적인 HTTP 방식을 <strong>“Polling”</strong>이라고 하한다.</p>
<p>그렇다면 주식 시세나 화상/음성 통화, 게임 등 실시간으로 데이터를 전달해야 하는 경우에는 어떻게 해야 할까? 주식 같은 경우 초 단위로 시세가 계속 바뀔 텐데 기존의 방식인 polling을 이용하게 되면 클라이언트는 서버에게 밀리초 단위로 요청을 계속 보내고 응답 받아야 할 것이다. 이런 경우에는 서버가 클라이언트에게 지속적으로 데이터를 전송할 수 있어야 한다. 이를 위해 웹소켓 프로토콜이 등장했다.</p>
<p>그런데 여기서 궁금한 것은 polling을 사용할 때, 서버에 부담이 가게 될 것인데, 서버의 어디에 부담이 가는 것일까?</p>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/3f8087e7-a173-4d80-bd49-1560d17e07d9/image.png" /></p>
<figcaption style="text-align: center; font-size: 15px; color: #808080; margin-top: 40px;">
    메모리의 구조 - disk로 갈수록 저렴하지만 속도가 매우 느려진다.
</figcaption>


<p><strong>서버 부하 요인</strong></p>
<ol>
<li>연산량이 많아지기 때문에 <strong>CPU</strong>에 부담이 갈 것이다. 일반적인 웹서비스는 CPU가 부담을 많이 받는 서비스는 아니라고 한다. 그러나 수만명의 사람들이 요청을 하는 상황에서는 부하가 걸릴 수 있다. </li>
<li><strong>RAM</strong>(1차 메모리)에 부담이 갈 수 있다. 우리의 프로젝트로 치면 node.js, express가 해당된다. 이것들이 코드를 실행하며 돌다가 감당할 수 있는 메모리를 넘어서게 되면 부담이 된다. 이 경우 서버에 부하가 오게 되면 흔히 말하는 “메모리가 터졌다”라는 상황이 오게 된다. 
그러나 가상메모리(HDD, SSD)인 2차 메모리를 활용해 실제 사용할 수 있는 메모리 용량보다 크게 확장하여 쓸 수 있는데, 이 가상 메모리에 부하가 오게 되면 메모리가 터지진 않지만 속도가 많이 느려질 것이다. </li>
<li><strong>Disk</strong>(하드디스크)에 부담이 갈 수 있다. DB에 계속 요청을 보내고 응답을 하며 데이터를 저장하고 불러오는 과정이 반복되면 속도가 매우 느려질 것이다. </li>
</ol>
<p><strong>해결 방안: SSE와 WebSocket</strong></p>
<p>그래서 데이터를 계속 조금씩 쌓아두다가 한 번에 적재하고, DBMS로 insert 쿼리 요청을 보내면서 DB의 요청 횟수를 줄여 하드 디스크의 I/O 자체를 줄이는 거나 In-Memory DB(cache와 비슷한데 RAM임)에 영속적으로 존재해야 하는 데이터를 저장시켜놓아 Disk의  I/O를 줄이는 방법을 통해 서비스의 확장성을 높여 최적화할 수 있다. </p>
<p>그래서 SSE(Server Sent Events)라는 것이 나오게 되었다. 이것은 EventSource라는 객체를 사용하며, 처음에 한 번만 연결하면 서버가 클라이언트에 지속적으로 알아서 데이터를 보내준다. 그러나 클라이언트에서 서버로는 데이터를 보낼 수 없다. 이것은 쉽게 말해 양방향 데이터 전송이 안된다는 의미이다. </p>
<p>그러나 Web Socket(ws라고도 부름)이라고 하는 프로토콜은 클라이언트가 요청에 대한 응답을 지속적으로 받다가 또 한번 요청을 보낼 수도 있다. 이는 양방향으로 전송이 가능함을 의미한다. </p>
<h3 id="웹소켓-이해하기-→-socketio와의-차이까지">웹소켓 이해하기 → Socket.io와의 차이까지</h3>
<p>위에서 얘기했듯이 Web Socket은 실시간으로 양방향 데이터 전송이 가능한 기술이다. 이는 클라이언트 요청 없이도 서버에서 데이터 전송을 할 수 있다. 
Web Socket은 ws 프로토콜을 사용하는데, 최신 브라우저만 ws를 지원하고 있다. Node는 ws나 <a href="http://Socket.IO"><code>Socket.IO</code></a>같은 패키지를 통해 웹소켓을 사용할 수 있다. </p>
<p><strong>Socket.IO의 장점</strong></p>
<p>Socket.IO는 웹소켓을 기반으로 하지만, 웹소켓을 지원하지 않는 브라우저에서도 폴링 방식으로 실시간 통신을 가능하게 한다. 따라서 Socket.IO를 사용하면 브라우저 호환성을 높일 수 있다.</p>
<p>실무에서 실제로 웹소켓을 많이 활용하고 있다. </p>
<ul>
<li>지도<ul>
<li>eg. 카카오맵 버스 실시간 이동 현황</li>
<li>eg. 배달의 민족 라이더 위치</li>
</ul>
</li>
<li>대시보드<ul>
<li>회계팀이나 기업 내부에서 실시간 매출 지표, 성과 지표를 보여주어야 할 떄</li>
</ul>
</li>
<li>실시간 지표<ul>
<li>주식, 환율 등 실시간으로 변화하는 수치를 제공해야 하는 경우</li>
</ul>
</li>
<li>게임<ul>
<li>서버가 클라이언트 사이에서 중계하며 실시간으로 게임할 수 있게 해야 하는 경우</li>
</ul>
</li>
</ul>
<h3 id="간단한-채팅방-구현해보기">간단한 채팅방 구현해보기</h3>
<blockquote>
<p>간단한 채팅방 구현한 깃허브 주소: <a href="https://github.com/youjin-hong/socket_io_chat">https://github.com/youjin-hong/socket_io_chat</a></p>
</blockquote>
<blockquote>
<p><strong>[서버 코드 로직]</strong></p>
<ol>
<li>Express 서버와 Socket.IO 서버를 설정</li>
<li>소켓 이벤트를 처리하는 함수를 작성<ul>
<li>클라이언트 연결/연결 해제 이벤트</li>
<li>메시지 수신 및 broadcast 이벤트</li>
<li>특정 이벤트 발생 시 클라이언트 ID 반환 이벤트</li>
</ul>
</li>
</ol>
<p><strong>[클라이언트 코드 로직]</strong></p>
<ol>
<li>Socket.IO 클라이언트 라이브러리를 import</li>
<li>서버에 연결하고 이벤트를 처리<ul>
<li>서버로부터 메시지 수신 시 화면에 표시</li>
<li>사용자 입력 시 서버로 메시지 전송</li>
</ul>
</li>
</ol>
</blockquote>
<p><strong>[서버 기준]</strong></p>
<ol>
<li><strong>프로젝트 폴더 생성 후 <code>package.json</code> 만들기 (server)</strong></li>
</ol>
<pre><code class="language-bash">npm init -y</code></pre>
<ol>
<li><strong>필요한 모듈 설치해 기본 세팅하기(server)</strong></li>
</ol>
<pre><code class="language-bash">npm i express</code></pre>
<ol>
<li><strong>socket.io, http 설치(serv</strong></li>
</ol>
<pre><code class="language-bash">npm install socket.io http</code></pre>
<ol>
<li><strong><code>app.js</code> 생성(server) - express 서버, socket 서버 설정 &amp; 구동</strong></li>
</ol>
<pre><code class="language-jsx">const express = require(&quot;express&quot;);
const { createServer } = require(&quot;http&quot;);
const SocketHandler = require(&quot;./socketHandler&quot;);
const path = require(&quot;path&quot;);

const app = express();

const server = createServer(app);
const io = new SocketHandler(server);

app.locals.io = io;

app.get(&quot;/&quot;, (req, res) =&gt; {
  res.sendFile(path.join(__dirname, &quot;./index.html&quot;));
});

server.listen(8000, () =&gt; {
  console.log(&quot;http://localhost:8000 에서 서버 구동 중...&quot;);
});</code></pre>
<ol>
<li><strong><code>socketHandler.js</code> 생성(server) - socket의 이벤트 처리는 여기서 다 이뤄짐</strong></li>
</ol>
<pre><code class="language-jsx">const { Server } = require(&quot;socket.io&quot;);

const SocketHandler = (server) =&gt; {
  const io = new Server(server);

  // 사용자 저장소
  const users = {};

  // 소켓 연결 이벤트 처리
  io.on(&quot;connection&quot;, (socket) =&gt; {
    // 접속 시 서버에서 실행되는 코드
    const req = socket.request;
    const socketId = socket.id; // socket에 연결되면 아이디가 생성됨 -&gt; 겹치지 않는 해시함수로 만들어짐
    const clientIp =
      req.headers[&quot;x-forwarded-for&quot;] || req.connection.remoteAddress;

    console.log(&quot;connection!&quot;);
    console.log(&quot;socket ID : &quot;, socketId);
    console.log(&quot;client IP : &quot;, clientIp);

    // 접속 알림 전송
    io.emit(&quot;message&quot;, `${socketId} 님이 연결되었습니다.`);

    // 사용자 추가
    users[socketId] = { nickname: &quot;users nickname&quot;, point: 0 };

    // 메시지 수신 및 브로드캐스트
    socket.on(&quot;message&quot;, (msg) =&gt; {
      console.log(`${socketId}: ${msg}`);
      io.emit(&quot;message&quot;, `${socketId}: ${msg}`);
    });

    // 이벤트 핸들링: 특정 이벤트 발생 시 ID 반환
    socket.on(&quot;event1&quot;, (msg) =&gt; {
      console.log(msg);
      socket.emit(&quot;getID&quot;, socketId);
    });

    // 모든 클라이언트에게 메시지 전달
    socket.on(&quot;input&quot;, (data) =&gt; {
      io.emit(&quot;msg&quot;, { id: socketId, message: data });
      console.log(users);
    });

    // 본인을 제외한 모든 클라이언트에게 메시지 전달
    socket.on(&quot;inputWM&quot;, (data) =&gt; {
      socket.broadcast.emit(&quot;msg&quot;, { id: socketId, message: data });
    });

    // 특정 클라이언트에게 메시지 전달
    socket.on(&quot;private&quot;, (id, data) =&gt; {
      io.to(id).emit(&quot;msg&quot;, { id: socketId, message: data });
    });

    // 연결 해제 시 사용자 삭제
    socket.on(&quot;disconnect&quot;, () =&gt; {
      socket.broadcast.emit(&quot;message&quot;, `${socketId} 님의 연결이 끊어졌습니다.`);
      delete users[socketId];
    });
  });

  return io;
};

module.exports = SocketHandler;</code></pre>
<ul>
<li>이벤트 리스터 등록: <code>socket.on('이벤트명', () =&gt; {})</code></li>
<li>메세지 전달 (server가 client에게)<ul>
<li><code>io.emit('이벤트명', data)</code> : 접속된 모든 클라이언트로 메세지 전송</li>
<li><code>socket.emit('이벤트명', data)</code> : 메세지를 전송한 클라이언트에게만 메세지 전송</li>
<li><code>socket.broadcast.emit('이벤트명', data)</code> : 메세지를 전송한 클라이언트를 제외한 나머지 모든 클라이언트에게 메세지 전송</li>
<li><code>io.to(id).emit('이벤트명', data)</code> : 지정된 특정 클라이언트 ID에게만 메세지 전송</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/so356hot/post/09f859a5-4aab-4054-a444-9319ba7824de/image.png" /></p>
<p>server 코드를 (<code>nodemon app.js</code> )실행시켰을 때 위와 같이 ::1이라고 뜨는 것에 “::”은 클라이언트가 로컬호스트로부터 들어왔다는 것을 의미한다. </p>
<p><strong>[클라이언트 기준]</strong></p>
<ol>
<li><strong><code>index.html</code>을 생성한다.</strong></li>
</ol>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
  &lt;head&gt;
    &lt;-- viewport 메타태그: 모바일 기기에서 반응형 디자인을 위해 필요 --&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1.0&quot; /&gt;
    &lt;title&gt;Socket.IO chat&lt;/title&gt;
    &lt;link
      rel=&quot;stylesheet&quot;
      href=&quot;https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css&quot;
    /&gt;
    &lt;style&gt;
      main {
        display: flex;
        flex-direction: column;
        height: 100dvh;
      }
      article {
        flex-grow: 1;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;main class=&quot;container&quot;&gt;
      &lt;article&gt;
        &lt;ul&gt;&lt;/ul&gt;
        &lt;-- 채팅 메세지들이 표시될 리스트 --&gt;
      &lt;/article&gt;
      &lt;form&gt;
        &lt;-- 메시지 입력/전송을 위한 form --&gt;
        &lt;fieldset role=&quot;group&quot;&gt;
          &lt;input /&gt; &lt;-- 메세지 입력창 --&gt;
          &lt;button&gt;Send&lt;/button&gt;
        &lt;/fieldset&gt;
      &lt;/form&gt;
    &lt;/main&gt;

    &lt;script type=&quot;module&quot;&gt;
      // 프론트랑 백을 분리시켜서 구현하고 싶을 때 CDN으로 이렇게 삽입 해야 함
      import { io } from &quot;https://cdn.socket.io/4.7.5/socket.io.esm.min.js&quot;;

        // 웹소켓 연결
      const socket = io();

      const ul = document.querySelector(&quot;ul&quot;);

      // 서버로부터 이벤트 수신 시, 새 리스트 아이템 li 생성
      socket.on(&quot;message&quot;, (msg) =&gt; {
        const li = document.createElement(&quot;li&quot;);
        li.textContent = msg;
        ul.appendChild(li);

        // 스크롤을 항상 최신 메세지가 보이도록
        window.scrollTo(0, document.body.scrollHeight);
      });

      const form = document.querySelector(&quot;form&quot;);
      const input = document.querySelector(&quot;input&quot;);

      form.addEventListener(&quot;submit&quot;, (event) =&gt; {
        event.preventDefault();
        if (input.value) {
          socket.emit(&quot;message&quot;, input.value);
          input.value = &quot;&quot;;
        }
      });
    &lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>
<ul>
<li>메세지 전달 (client가 server에게)<ul>
<li><code>socket.emit('이벤트명', data)</code> : 서버로 data 전송</li>
</ul>
</li>
</ul>
<h3 id="실제-프로젝트에-적용해보기">실제 프로젝트에 적용해보기</h3>
<blockquote>
<p><a href="http://Socket.IO">Socket.</a>io 이벤트 연동 가이드 -  ‣ 
Socket.io 적용된 사이트 체험해보기 -  <a href="https://nfe-1-1-3-tech-log.vercel.app/">https://nfe-1-1-3-tech-log.vercel.app/</a></p>
</blockquote>
<ul>
<li><code>server.js</code> - 서버 진입점이자, express 애플리케이션과 Socket.IO를 결합해 HTTP와 웹소켓 서버를 설정하는 부분</li>
</ul>
<pre><code class="language-jsx">// ./server.js
const path = require('path');
const app = require(path.join(__dirname, './app'));
const http = require('http');
const SocketServer = require('./websocket/websocketServer');
const cors = require('cors'); // cors 미들웨어 추가

const PORT = process.env.PORT || 8000;

// CORS 미들웨어 적용
app.use(
  cors({
    origin: [
      'http://127.0.0.1:5500',
      'http://localhost:5500',
      'http://localhost:3000',
    ], // 테스트 HTML 파일이 실행되는 주소 추가
    credentials: true,
  })
);

// HTTP 서버 생성
const server = http.createServer(app);

// Socket.IO 서버 인스턴스 생성
const io = new SocketServer(server);

// app.locals에 Socket.IO 인스턴스 저장
app.locals.io = io;

server.listen(PORT, () =&gt; {
  console.log(`Server running on port ${PORT}`);
});</code></pre>
<ul>
<li><p><code>socketServer.js</code> - 서버에서 Socket.IO로 실시간 댓글 기능을 구현하는 구조로, 각 클라이언트가 특정 게시물에 연결하고, 해당 게시물에 새 댓글이 달릴 때 실시간으로 업데이트를 받도록 처리한다.</p>
<ul>
<li><p><strong>기본구조 설정</strong></p>
<pre><code class="language-jsx">// socket.io 생성하기 위해 Server 클래스 사용
const { Server } = require('socket.io');

// 파일 경로를 다루기 위한 Node.js 모듈
const path = require('path');

// MongoDB에 정의된 Comment 모델을 불러와 댓글 데이터 저장, 불러오는 데 사용
const Comment = require(path.join(__dirname, '../models/comment'));

// 댓글들을 DB에 저장하기 위해
const mongoose = require('mongoose');</code></pre>
</li>
<li><p><strong>클래스 정의 및 초기 설정</strong></p>
<pre><code class="language-jsx">// class SocketServer: 소켓 서버를 설정하고 관리하는 역할을 함
class SocketServer {
// constructor(server): 클래스가 생성될 때 호출되는 메서드 -&gt; HTTP 서버(server)를 인수로 받음
constructor(server) {
// this.io: Socket.IO 서버 인스턴스를 만들고, CORS 설정을 통해 클라이언트 연결을 허용
// origin: 프론트 도메인 연결 허용하도록 지정, credentials: 쿠키 같은 인증 정보 허용
  this.io = new Server(server, {
    cors: {
      origin: [
        'http://localhost:3000',
        'https://nfe-1-1-3-tech-log.vercel.app',
      ],
      credentials: true,
      methods: ['GET', 'POST'],
      allowedHeaders: ['my-custom-header'],
      transports: ['websocket', 'polling'],
    },
    pingTimeout: 60000,
    pingInterval: 25000,
    reconnection: true,
    reconnectionAttempts: 5,
    reconnectionDelay: 1000,
  });

      // setupEventHandlers: 소켓 이벤트를 설정하는 함수 -&gt; 각종 이벤트가 저장될 공간
  this.setupEventHandlers();
  this.setupRoomCleaner();
  return this.io;
}
}</code></pre>
</li>
<li><p><strong>이벤터 핸들러 설정</strong></p>
<pre><code class="language-jsx">setupRoomCleaner() {
setInterval(
  () =&gt; {
    const rooms = this.io.sockets.adapter.rooms;
    rooms.forEach((_, room) =&gt; {
      if (room.startsWith('post_')) {
        const clientCount =
          this.io.sockets.adapter.rooms.get(room)?.size || 0;
        if (clientCount === 0) {
          console.log(`Cleaning up empty room: ${room}`);
        }
      }
    });
  },
  30 * 60 * 1000
);
}</code></pre>
<pre><code class="language-jsx">setupEventHandlers() {
// 'connection': 클라이언트가 서버에 연결되면 해당 이벤트 발생 -&gt; 여기서 socket 객체 생성됨
// 각 socket: 연결된 클라이언트를 의미
// socket.id: 각 클라이언트를 식별할 수 있는 고유한 ID
 this.io.on('connection', socket =&gt; {
   console.log('Client connected:', socket.id);
  // 나머지 코드...
}</code></pre>
</li>
<li><p><strong>연결 에러 처리 &amp; 재연결 처리</strong></p>
<pre><code class="language-jsx">// 연결 에러 처리
socket.on('connect_error', error =&gt; {
console.error('Connection error:', error);
socket.emit('connection_error', {
  message: '서버 연결에 문제가 발생했습니다.',
});
});
// 재연결 시도 처리
socket.on('reconnect_attempt', attemptNumber =&gt; {
console.log(`Reconnection attempt ${attemptNumber}`);
});
// 재연결 성공 처리
socket.on('reconnect', attemptNumber =&gt; {
console.log(`Reconnected after ${attemptNumber} attempts`);
});</code></pre>
</li>
<li><p><strong>특정 게시물 방에 입장하기</strong></p>
<pre><code class="language-jsx">// 'join_post': 특정 게시물에 입장하기 위한 이벤트
// postId를 받아 해당 게시물의 고유한 방 이름을 생성
socket.on('join_post', postId =&gt; {
try {
  const cleanPostId = postId.replace(/&quot;/g, '');
  const roomName = `post_${cleanPostId}`;
  socket.join(roomName);  // 클라이언트(socket)은 해당 메서드로 방 입장
  console.log(`Client ${socket.id} joined ${roomName}`); // 입장한 방에만 메세지 전달
});

// 오름차순 정렬로 변경 (-1 → 1)
  const comments = await Comment.find({ postId: cleanPostId }).sort({
    createdAt: 1,
  }); // 오래된 순으로 정렬

  // 댓글 데이터 가공
  const processedComments = comments.map(comment =&gt; ({
     _id: comment._id,
     content: comment.content,
     userId: comment.userId,
     createdAt: comment.createdAt,
   }));
   socket.emit('load_comments', processedComments);
   } catch (error) {
   console.error('Error in join_post:', error);
   socket.emit('comment_error', {
     message: '댓글을 불러오는 중 오류가 발생했습니다.',
     error: error.message,
   });
 }
});</code></pre>
</li>
<li><p><strong>방 나가기 처리</strong></p>
<pre><code class="language-jsx">// 방 나가기 처리
socket.on('leave_post', postId =&gt; {
try {
  console.log('Leaving post:', postId);
  const roomName = `post_${postId}`;
  socket.leave(roomName);
  console.log(`Client ${socket.id} left ${roomName}`);
} catch (error) {
  console.error('Error in leave_post:', error);
}
});</code></pre>
</li>
<li><p><strong>새 댓글 생성 및 전송</strong></p>
<pre><code class="language-jsx">// 'new_comment': 클라이언트가 새로운 댓글을 보낼 때 발생하는 이벤트
// data: 댓글 데이터가 포함됨
    socket.on('new_comment', async data =&gt; {
      try {
        console.log('Received new comment data:', data);

        const commentData =
          typeof data === 'string' ? JSON.parse(data) : data;

        // 입력 데이터 검증
        if (
          !commentData.userId ||
          !commentData.postId ||
          !commentData.content
        ) {
          throw new Error('필수 입력 항목이 누락되었습니다.');
        }

        // ObjectId 검증은 postId에만 적용
        if (!mongoose.Types.ObjectId.isValid(commentData.postId)) {
          throw new Error('유효하지 않은 게시글 ID입니다.');
        }

        // 댓글 생성
        console.log('Creating new comment with data:', commentData);
        const comment = await Comment.create({
          userId: commentData.userId,
          postId: commentData.postId,
          content: commentData.content,
        });

        console.log('Created comment:', comment);

        // 응답 데이터 준비
        const responseComment = {
          _id: comment._id,
          content: comment.content,
          userId: comment.userId,
          createdAt: comment.createdAt,
        };

        const roomName = `post_${commentData.postId}`;

        // 댓글 생성 확인 메시지 송신자에게 전송
        socket.emit('comment_confirmed', {
          message: '댓글이 성공적으로 작성되었습니다.',
          comment: responseComment,
        });

        // 모든 클라이언트에게 새 댓글 전송
        this.io.to(roomName).emit('comment_added', responseComment);

        console.log(
          'Comment successfully processed and broadcast to room:',
          roomName
        );
      } catch (error) {
        console.error('Error in new_comment:', error);
        socket.emit('comment_error', {
          message: '댓글 작성 중 오류가 발생했습니다.',
          error: error.message,
        });
      }
    });</code></pre>
</li>
<li><p><strong>연결 해제</strong></p>
<pre><code class="language-jsx">// 'disconnect': 클라이언트가 서버와 연결을 끊으면 발생하는 이벤트
// 클라이언트 ID(socket.id)와 함께 연결 해제를 로그로 출력 
    socket.on('disconnect', () =&gt; {
      console.log('Client disconnected:', socket.id);
      Object.keys(socket.rooms).forEach(room =&gt; {
        if (room.startsWith('post_')) {
          socket.leave(room);
          console.log(`Left room on disconnect: ${room}`);
        }
      });
    });</code></pre>
</li>
</ul>
</li>
<li><p><code>/models/comment.js</code> - <strong>댓글에 대한 MongoDB 스키마 정의</strong></p>
</li>
</ul>
<pre><code class="language-jsx">const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const moment = require('moment-timezone');

const commentSchema = new Schema({
  // MongoDB의 ObjectId를 사용하여 User 모델 참조
  userId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true,
  },
  // MongoDB의 ObjectId를 사용하여 Post 모델 참조
  postId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Post',
    required: true,
  },
  content: {
    type: String,
    required: true,
  },
  //한국 시간으로 변경
  createdAt: {
    type: String,
    default: () =&gt; moment.tz('Asia/Seoul').format('YYYY-MM-DD HH:mm:ss'),
  },
});

const Comment = mongoose.model('Comment', commentSchema);
module.exports = Comment;</code></pre>
<h3 id="궁금했던-점">궁금했던 점</h3>
<ul>
<li><p>웹 애플리케이션은 클라이언트와 서버가 HTTP 프로토콜로 한다고 알고 있는데 소켓 연결할 때 왜 http 패키지로 http 서버를 또 만들어주는 건지?</p>
<p>  Socket.IO를 통해 실시간 통신을 할 때, HTTP 서버를 별도로 만들어주는 이유는 다음과 같다.</p>
<ol>
<li><strong>HTTP 프로토콜과 HTTP 서버의 차이</strong><ul>
<li><strong>HTTP 프로토콜</strong>은 클라이언트와 서버가 데이터를 주고받기 위한 일종의 통신 “규칙”이다. 
이를 통해 웹 브라우저와 서버 간의 요청-응답 방식의 통신이 이루어지며, 주로 HTML, 이미지, API 데이터 등 리소스를 요청하거나 전달할 때 사용된다.</li>
<li><strong>HTTP 서버</strong>는 이 <strong>HTTP 프로토콜에 따라 클라이언트 요청을 받고 응답을 보내는 역할</strong>을 하는 애플리케이션이다. 예를 들어, Node.js의 Express 서버, Apache, Nginx 등이 여기에 해당한다.</li>
</ul>
</li>
<li><strong>Socket.IO와 HTTP 서버의 역할</strong><ul>
<li>Socket.IO는 클라이언트와 서버 간 <strong>실시간 양방향 통신</strong>을 위한 라이브러리이다. 하지만 초기 연결은 HTTP 프로토콜을 통해 설정된다. 이 초기 연결 과정에서 HTTP 서버가 클라이언트와의 첫 연결을 담당한다.</li>
<li><strong>첫 연결 이후</strong> Socket.IO는 WebSocket 프로토콜로 전환하여 HTTP의 한계인 요청-응답을 벗어나 <strong>실시간 통신</strong>을 가능하게 한다.</li>
</ul>
</li>
<li><strong>HTTP 서버가 필요한 이유</strong><ul>
<li>Socket.IO를 사용하더라도 초기 연결 설정과 기본 웹 리소스 제공을 위해 <strong>HTTP 서버가 필요하다</strong>. 이 HTTP 서버가 클라이언트와의 첫 연결을 받아들이고, WebSocket으로 전환할 수 있는 기반을 마련해준다.</li>
<li>이후에는 WebSocket 프로토콜을 통해 양방향 통신을 수행하게 되므로 실시간 데이터를 주고받을 수 있다.</li>
</ul>
</li>
</ol>
<p>  <strong>결론적으로</strong>, HTTP 서버는 <strong>첫 연결을 설정하고 기본적인 HTTP 요청을 처리</strong>하는 역할을 하며, 이후에 Socket.IO를 통해 실시간 통신이 이뤄지기 때문에 http 서버가 필요한 것이다.</p>
</li>
</ul>
<br />

<blockquote>
</blockquote>
<h3 id="요약">요약</h3>
<ul>
<li><strong>Socket.IO 도입 배경 요약</strong><ul>
<li>기존의 HTTP 프로토콜은 서버가 한 번 응답하면 연결을 끊어버리기 때문에, 실시간 데이터 전송이 필요한 상황에 한계를 가짐.</li>
<li>Polling 방식으로 실시간성을 확보할 수 있지만, 이는 서버 CPU, RAM, 그리고 디스크에 큰 부담을 줌.</li>
<li>이에 따라 서버는 클라이언트의 데이터 변경 사항을 신속히 전송할 수 있어야 하며, WebSocket이 등장하여 양방향 실시간 데이터 전송을 가능하게 함.</li>
<li>WebSocket을 지원하지 않는 환경에서도 실시간 통신이 가능한 Socket.IO는 브라우저 호환성 확보의 장점이 있음.</li>
</ul>
</li>
<li><strong>Socket.IO 코드 예시 요약</strong><ul>
<li>서버에서 socketHandler.js 파일을 통해 소켓 연결을 설정하고 다양한 이벤트를 처리함. 이를 통해 연결된 모든 클라이언트에게 메시지를 브로드캐스트하거나 특정 클라이언트에게만 메시지를 전달 가능.</li>
<li>클라이언트 측에서는 Socket.IO 라이브러리를 사용하여 서버와의 연결을 수립하고, 이벤트 발생 시 서버로 메시지를 전송하거나 수신함.</li>
</ul>
</li>
<li><strong>서버 부하 감소 및 최적화 방안</strong><ul>
<li>RAM을 사용하는 In-Memory DB 또는 캐시를 활용하여 서버 부하를 줄이고 확장성을 높임.</li>
<li>서버가 클라이언트 요청을 지속적으로 수용하기 위해 WebSocket을 사용하여 실시간 통신을 효율적으로 지원.</li>
</ul>
</li>
</ul>
<hr />
<h3 id="참고-자료">참고 자료</h3>
<p><a href="https://socket.io/docs/v4/tutorial/step-4">https://socket.io/docs/v4/tutorial/step-4</a></p>
        