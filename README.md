# PCA
0610 PCA & Player 클래스 코드 작성 \
0611 Pitcher 클래스 & K-means 코드 추가 \
0612 최적 차원 분석 & list comprehension 이용 코드 수정 \
0613 2020년 진행되고 있는 데이터 이용 -->  각 player와 pitcher의 클래스 업데이트 가능하도록 수정
0624 클래스 변화로 생긴 에러 해결, arithmetic mean 함수 구현 완료(아마 p-value는 scipy 없이 구현 불가)

## 참고
0613 작업: 2020 데이터는 6월 24일 경기기록까지 데이터 사용
0613 작업: 동일한 인물 객체에 여러 해의 데이터 list로 부여

### 추가 제안 사항
- 2020년 진행되고 있는 데이터 이용 -->  각 player와 pitcher의 클래스 업데이트 가능하도록 수정 (done)
- 클래스 수정 후 pcatest_with_class1 line 82에서 error 발생. not solved yet. (done)
- PCA 완성 후 2, 3, 4차원 결과 도출 (결과에서 component 이름 확인)
- 그래프 보였을 때 팀별로 색상 다르게