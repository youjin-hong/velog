<p>이수증 신청을 했는데 신청 취소를 할 경우, 이수증 관리 페이지에서 취소하고자 하는 행의 ‘신청 취소’ 버튼을 누르면 해당 행이 삭제가 되어야 하는데, 새로고침을 해야만 삭제가 표시되는 문제가 발생했다. </p>
<p>그래서 네트워크탭을 열어보니, tableBody에 key={moduleName}으로만 되어있어 같은 모듈명을 가진 행들이 많아서 구분을 못한다는 뜻의 메세지가 담겨있었다. </p>
<p>그래서 <code>${row.moduleName}-${row.date}</code>로 변경을 해주었으나, 무언가 찝찝했다. date 초단위까지 구분을 하기 때문에 겹칠 일이 없으나 나중에 서비스가 배포된 후에 date가 분 단위로 축소가 되거나 사라질 수도 있기 때문에 map(row, index)를 추가하여 key={<code>${row.moduleName}-${index}</code>}로 바꿔주었다. </p>
<p>테스트 결과 삭제하고자 하는 행은 바로 삭제가 되는 것을 확인할 수 있었는데, 다시 보니 이수증 승인 거절당한 행도 같이 사라졌다가 새로고침하면 거절당한 행들이 다시 뜨는 문제를 발견했다. </p>
<p>처음에는 백엔드에서 body에 moduleName만을 담아서 보내고 받기 때문에 프론트에서 행 구분을 못해서 일어나는 일이라고 생각하고 api 쿼리 엔드포인트에 ${setRows}도 담아보고, </p>
<p>moduleName 대신에 id도 담아봤는데 (이건 안되는 거 알면서 그냥 해봤음..) 계속 같은 모듈명을 가진 행들이 테이블에서 같이 사라지는 문제가 발생했다. </p>
<p>백엔드에서 moduleName과 함께 행을 구분하는 id도 넘겨달라고 할까 생각하다가 정확한 논리는 모르겠지만 강한 feel로 이건 아닌 것 같다 생각해서 그만 뒀다. </p>
<p>결국 혼자 끙끙 앓다가 결국 gpt를 호출했는데 바로 답을 알려줬다. </p>
<p>현재 내 코드는 아래와 같았다. </p>
<pre><code class="language-jsx">  const handleCancel = async (confirmed) =&gt; {
    const token = sessionStorage.getItem('token');
    const headers = {
      Authorization: `Bearer ${token}`
    };
    if (confirmed) {
      try {
        const response = await axios({
          url: '',
          method: 'DELETE',
          headers: headers,
          data: { moduleName: selectedRow.moduleName }
        });
        console.log('Response:', response);
        setRows(rows.filter((item) =&gt; item.moduleName !== selectedRow.moduleName));
      } catch (error) {
        console.error('이수증 삭제 실패:', error);
      }
    }
    handleCloseCancelDialog();
  };
</code></pre>
<p>여기서 setRows를 호출하는 방식을 조금만 바꾸면 된다고 하는 것이다.</p>
<p>백엔드에서 moduleName 외에 식별할 고유 id를 주지 않는 경우라면, 프론트엔드에서는 이를 기준으로 특정 행을 구분하기는 어려우나 <strong>상태관리</strong>를 통해 해결할 수 있었다. </p>
<p>현재 사용자가 특정 행의 삭제 버튼을 클릭했을 때, 그 행의 전체 객체를 selectedRows 상태에 저장하고 있기 때문에 이 객체의 참조 자체가 고유하다는 점을 이용하라고 하였다. </p>
<p>그리고 이건 스터디 때 배운 건데, react는 객체를 참조에 의해 비교하므로 같은 속성값(moduleName)을 가진 두 객체라 할 지라도, 그것들이 서로 다른 메모리 주소를 가리킨다면, 즉 서로 다른 참조를 가지면 ‘다른 객체’로 간주할 수 있다는 것이 떠올랐다. </p>
<p>따라서 setRows의 호출 방식을 setRows((item) ⇒ item !== selectedRow)); 로 변경하여 rows 배열에서 selectedRow와 동일한 참조를 가진 객체 (즉, 사용자가 삭제하기로 선택한 특정 행)을 제외하고 나머지 행들을 새로운 배열로 만들었다. </p>
<p>이렇게 고쳐서 테스트를 해보았더니, 같은 moduleName 값을 가진 행들이 영향을 받지 않고, 정확하게 내가 삭제를 원하는 행 만이 제거가 되는 것을 확인했다. </p>
<p>이 방법은 selectedRow에 저장된 객체와 rows 배열 내의 객체들이 정확히 같은 참조를 갖고 있을 때만 작동한다고 한다. </p>
<p>따라서 handleClick 함수에서 setSelectedRow(row)를 호출할 때 전달되는 row 객체와, 나중에 rows 배열을 순회하며 비교하는 객체가 메모리상에서 동일한 참조를 갖고 있어야 한다고 한다. </p>
<p>이것은 일반적으로 react의 상태 관리 패턴을 따르는 경우에 자연스럽게 보장된다고 한다.</p>