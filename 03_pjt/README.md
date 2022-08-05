## pjt_03

### nav_footer

- 새로 얻은 개념
 > (bootstrap) modal 과 button 연결하기 - button(data-bs-target) = #modal(id)
 > fixed top을 사용하면 헤더쪽이 일부분 가려진다. 그때는 stick top을 대신 사용한다
 > img 넣을 때 width="" height="" 형식으로 크기 지정 가능 (img-fluid  필수)
 
-  어려웠던 점
 > Login을 modal과 연결하기 위해 button으로 바꾸었더니 라인이 옆과 일치 X
 > 패딩값을 조정해서 위치를 맞춤


### home

- 새로 얻은 개념
 > 한줄로 row 선언하기 - row row-cols-1 row-cols-sm-3 g-3
 > row 밑에 선언되어 column 한줄에 1개(col-12)  -  sm이 지날시  column 한줄에 3개(col-4, col-4 , col4)  , g-3 -> 그리드간 간격 


- 어려웠던 점
 > 처음 row 밑에 바로 article 박스에 class="col="을 선언했지만 적용 X
 > article을 div 박스로 감싸준 후 div에 class="col="을 선언하니 적용 O


### community

- 새로 얻은 개념
 > d-none d-block 개념 : none이 보이지 않는 시작점 , block이 보이는 시작점 - ex) d-none d-lg-block - 보이지 않다가 lg를 넘어갈시 보이게 처리. 

- 어려웠던 점
 > nesting 하는 과정이 어려웠다. 전체를 먼저 나누고 그 다음에 세부적인 부분을 나누자
 > aling-self-center를 통해서 pagination을 가운데로 보내려 했지만 적용 X   이 부분 역시 div를 감싸고 div에 적용했더니 해결했다