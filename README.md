# FallingSimulator



물리적 지식을 바탕으로 한 하위 개념 시뮬레이터 개발
 시뮬레이터 개발을 이용한 언어로는 Python을 이용하였다. C/C++을 이용해 실행시간을 대폭 줄일 수 있었으나, 시각화모듈 구현이 힘들다는 점이 단점으로 작용하였다. Python은 scipy, math, cmath, numpy 등의 각종 수학/과학 분야 모듈들이 존재했고 결정적으로 matplotlib과 pyplot 같은 데이터시각화 모델을 구현 없이 손쉽게 사용가능하다는 점이 선택한 큰 이유이다. 
 IDE는 PyCharm 4.5를 사용하였다.

 i) 기본 자유낙하

basic.py

 변수 및 상수 설정
deltaT 기본시간 간격
sStart 낙하 시작높이
s 높이
v 속도
g 중력가속도

9 ~ 12 각각 위치, 속도를 나타낸다. 다만 벡터인 속도는 스칼라로 표현했는데 이는 낙하는 좌우가 존재하지 않고 높이만 존재하므로 스칼라로 해도 무방하기 때문이다. 
13 시간이 50초가 되기 전까지 시뮬레이션을 실행한다. 만약 시간이 50초가 넘으면 그 즉시 시뮬레이션을 종료한다. 
15 속도를 지면 방향(-)으로 더해나가기 때문에 –부호를 붙인다
19 만약 real time으로 관찰하고 싶다면 모든 작업 후에 time.sleep(1/deltaT)를 실행해 딜레이를 준다. (이 때 계산시간은 0으로 가정한다.)

 이를 데이터 시각화 python 모듈인 matplotlib를 이용하면 위치와 속도 그래프를 확인할 수 있다. 


 i) 기본 자유낙하-2차원
 2차원 낙하는 기본적으로 x와 y, 두 개의 축으로 이루어진 2차원 공간에서의 낙하를 다룬다. 기본적으로 이 연구는 자유낙하에 집중하기 위해 항상 아래쪽으로 힘을 받는, 2차원이지만 1차원으로 가정하고 진행해도 문제가 없는 것이기 때문에 연구주제의 편리함과 심플함을 위해 1차원만 다루기로 했으나 기본 자유낙하 같은 부담이 없는 곳에서는 2차원 자유낙하를 시도해볼 수 있었다. 하지만 자유낙하를 2차원에서 하게 된다면 1차원과 다를 것이 없으므로 탄도계산 같은 좀 더 2차원에서 관찰하는 데에 적합한 주제를 하기로 했다.

 이에 대한 이론은 고등학교 물리2 과정에서 참고하였다. 

 두 개의 축을 잘 다루기 위해 새로운 클래스를 만들어 관리하기로 하였다. 사실상 이 내용은 이론보다는 설계적인 지식이 더 중요할 수 있으므로 이 내용에서는 언급 없이 넘어가기로 하겠다. 

util.py
main.py


ii) 중력이 변하는 자유낙하

gravity.py

실제 세계에서는 위 자유낙하 식과는 매우 다른 형태로 운동하게 된다. 중력은 높이에 종속되는 변수라는 점이다.

 계산된 결과값을 가지고 구현을 하면 이런 Python 코드가 나오게 된다.

 (떨어트리는 높이는 700km로 설정했으며 떨어지는 시간은 412.46으로 측정되었다. 
  대기마찰을 고려하지 않으면 지면에 닿는 순간의 속력은 약 3.616km/s이다.)


 iii) 대기마찰낙하 - (가변중력은 다루지 않는다)
 
 gravity_air.py
 
 실제 세계에서는 대기라는 것이 존재한다. 대기는 여러 가지 원소들로 이루어진 기체이며 대기 안에서 운동하는 물체는 저항을 받게 된다. 조금 더 현실에 가까운 환경을 만들기 위해 이 요소를 시뮬레이터에 추가하기 위해서 이론을 정리하자면.

먼저 대기마찰은 속도의 제곱에 비례한다고 가정한다면 낙하하고 있는 물체에 관한 힘의 식은

# F = -mg + kv^2


(이는 iiii) 가변대기마찰낙하를 위한 선행연구로 진행되어 시각화모듈화는 진행하지 않음)

이 시뮬레이터에 있는 것처럼 공기 저항에 관련된 값들을 조금 극단적으로 넣어 살펴본 결과 예상하던 대로 속도의 변화율이 0에 근접하는 종단속도 현상이 일어났다.

낙하까지 걸리는 시간은 9.637초였고


지면에 닿는 순간의 속력은 11.318m/s이었다.

 iiii) 가변대기마찰낙하
 
 gravity_real_air.py
 
대기는 기본적으로 균질하지 않다. 이 이유는 지면에 작용하는 중력 때문인데, 대기는 기압경도력과 중력이 평형을 이루는 지점에서 정지한다. 이 때, 대기는 중력이 더 센 지면 쪽에서 정지하게 되고 밀도가 더 큰 경향을 보인다.
 대기마찰계수에서는 대기의 밀도에 따라 저항계수가 달라지므로 대기자유낙하를 계산할 시에는 이를 꼭 고려해야 한다. 
이를 위해 높이에 따른 밀도 를 구할 예정이다.

(실제와는 오차가 있겠지만 다른 샘플 초기값으로 시뮬레이터를 가동시켜본 결과, 15000m 부근에서 대기 밀도와 낙하물체의 속도가 상승하면서 공기 저항이 늘어나 속력이 급히 낮아지는 것을 확인할 수 있었다.)

 iiiii) 최종 시뮬레이터 작성
 마지막으로 할 일은 모든 개념학습 및 연구와 하위개념 시뮬레이터를 바탕으로 처음 목표로 제시했던 실제 상황과 비슷한 환경에서의 자유낙하를 구현해보는 것이다. 그 과정은 이미 진행해온 것에 개념을 추가하는 것만으로 가능하다.

 바로 전 iiii) 가변대기마찰낙하의 코드에서 가속도부분을 중력이 변하는 자유낙하를 적용시켜보자면 먼저

 Fd = getFdFromHeight(h)
    a = - (GM / (((0.001*h)+EarthR)**2))*1000 + ((Fd/m) * v**2)
    aList.append(a)
로 변환해서 중력가속도 g0부분을 가변중력으로 바꾸어준다.
또한 이를 위해 중력에 관한 상수와 변수를 선언해준다.

## 고유 파라미터
# 중력
g0 = 9.80665
GM = 398600.4418    # km^3/s^2 중력상수x지구질량
EarthR = 6378       # km       지구반지름

이렇게 된다면 가변중력, 가변대기마찰, 대기온도, 물체의 단면적 등 자유낙하에 관여하는 모든 변수를 통제해 모사하는 시뮬레이터를 만들 수 있다.

(3) 시뮬레이터를 통한 데이터 분석
 iiii)가변대기마찰낙하 와 최종 시뮬레이터의 신뢰성을 확인하기 위해 몇 가지 샘플 초기값을 넣어 실험하던 도중 예상치 못한 흥미로운 사실을 확인할 수 있었다.
 그것은 바로 초기 높이(떨어트리는 높이)가 일정 값 이상이 된다면 그 조건에서는 초기 높이에 상관없이 지면도달순간의 속도가 항상 일정한 값을 유지한다는 것이다. 이것은 며칠간 50번 이상의 다른 초기값을 넣어보아도 항상 같은 결과를 확인할 수 있었다.

정상적인 비교를 위해 height0(떨어트리는 높이)값을 제외한 모든 값을 고정 값으로 설정하고 height0값만을 바꾸어 각 샘플들을 대조해본다.

1번째 샘플
 m=40, Cd=0.3, A=1, height0=5000

그림  

2번째 샘플
 m=40, Cd=0.3, A=1, height0=10000

그림  

3번째 샘플
 m=40, Cd=0.3, A=1, height0=20000
 

(5) 이론과 실제 대조

 이 시뮬레이터를 바탕으로 2014년 10월 14일 미국에서 진행된 우주 스카이다이빙을 모사해보기로 한다.
 이 낙하의 주요 정보들을 토대로 변수들을 조절해보았다.
833.9 mph (1,342.8 km/hr) - highest speed (faster than speed of sound: 768 mph)
128,100 ft (39.045 km, 24.26 miles ) - highest altitude
4 minutes 20 seconds - total freefall time without parachute
119,846 ft (36,529 meters) - total freefall distance without parachute

초기값 
h0 = 39045, m=80
표준대기
Cd=0.5
A=1
약 250초 후 낙하산 펼침
	A=30
	Cd=0.5
데이터들을 가지고 시뮬레이터를 기동시킨 결과

실제 낙하산 펼친 순간(t=260)의 고도 약 2500m
시뮬레이션 상 t=250일 때 약2800m
시뮬레이션 상 t=255일 때 약2500m
시뮬레이션 상 최고속도 400m/s 이상(실제 스카이다이빙에서는 약 380m/s)
시뮬레이션 상 총 8~9분정도(실제는 글라이딩을 포함해 약간 더 긺)

 어림잡은 초기값으로 설정한 결과 실제와 비슷한 결과를 보임으로써 기본적으로 구현한 기능들이 잘 작동하고 있고 대략적인 기능들은 신뢰성에 큰 문제가 없는 것으로 보인다.

3. 연구리뷰

 A. 부족한 점
 일단 가변대기마찰자유낙하 시뮬레이터를 바탕으로 하는 시뮬레이터(최종 시뮬레이터 포함)에서 발견된 문제점인 형 변환문제가 있다. 내부적으로 개발언어로 사용한 Python은 따로 자료 형을 명시적으로 정하지 않고 내부적으로 처리한다. 이 때, 계산과정에서 내부적으로 정한 자료형의 범위를 넘는 계산 값이 나와 자동 형 변환이 일어나고 이 과정에서 복소수에 해당하는 자료 형으로의 자동 변환이 일어나서 연산 불가능한 상황이 되어버리고 만다. 이 오류는 초기 값 50000m이상의 특정 값 이상에서 일어나는 것으로 확인되었다.
 또한 가변대기마찰자유낙하 시뮬레이터와 최종 시뮬레이터 사이의 엄청난 오차이다. 사실 최종 시뮬레이터는 가변대기마찰자유낙하 시뮬레이터에서 가변중력을 고려하여 작성되었는데 50000m이상의 고고도가 아니면 중력가속도의 절댓값은 9 이하로 내려가지 않는다. 따라서 실제 결과는 그렇게 크지 않을 것으로 예상하나 실제로는 엄청난 오차가 발생한다. 같은 높이, 같은 환경에서 시행하였을 때, 총 낙하시간이 60초 정도 차이나는 것으로 나왔다. 별도로 디버깅해본 결과, 중력 계산이 잘못된 것은 아닌 걸로 보이며, 설계적 이상이 아닌 실제 결과로 해석할 수 있을지는 아직도 의문이다. 이 점에 관해서는 추후 계속 살펴볼 계획이다.
 Python언어의 대표적인 문제점인 실행속도도 예상하던 대로 문제점으로 제기되었다. 대기마찰인 경우 계산 양이 급격하게 많아지면서 기존의 dt=0.0001인 경우를 정상적으로 기동시키기 어려워지면서 dt=0.01까지 높이게 되었다. 시간 간격이 넓으면 넓어질수록 원래 함수와 오차가 생기고 특히 수치해석의 방법인 오일러 방법 특성상 오차는 더 큰 오차를 초래할 수 있으므로 이는 시뮬레이터의 신뢰성에 문제가 된다. 이 문제점은 첫 번째 문제점인 가변대기마찰자유낙하 시뮬레이터와 최종 시뮬레이터의 오차문제의 원인이 될 가능성이 있다고 생각한다.
 그리고 또한 초기값 문제이다. 상수의 단위 계산법을 잘못 계산한 탓인지 초기 해면기압인 1013.25hPa를 표준단위인 Pa로 바꿀 경우 101325Pa인데 이 값을 넣어서 계산하면 공기저항이 너무 커져 금방 종단속도에 도달하게 된다. 이를 kPa단위에 해당하는 101.325를 넣으면 그때서야 실제에 가까운 값을 갖게 된다. 이 점에 관해서는 단위에 관한 이해를 제대로 하지 않은 점 등이 원인으로 추측된다. 이 문제점은 개발 도중 중력가속도 계산에서도 일어난 적이 있으며 기본적인 원인임에도 불구하고 아직까지 특별히 고칠 점을 찾지 못했다는 점에서 조금 더 반성해야할 문제점이라고 생각한다.
