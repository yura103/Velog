# [ML] Machine Learning

- Date: 2026-01-27 13:49:52 UTC
- Velog: https://velog.io/@yura103/ML-Machine-Learning

---

<h3 id="1-머신러닝machine-learning이란">1. 머신러닝(Machine Learning)이란?</h3>
<p>-&gt; 입력과 출력을 통해 규칙을 찾고, 새로운 입력이 들어왔을 때도 출력을 잘 예측하도록 하는 방법</p>
<blockquote>
<p>머신러닝 모델은 입력과 출력 사이의 관계를 내부적으로 학습하지만, 그 과정이 사람이 이해하기 쉬운 규칙 형태로 드러나지 않는 경우가 많음.
이 때문에 머신러닝은 종종 <strong>블랙박스(Black Box)</strong> 로 불림.</p>
<p>특히 트리 앙상블이나 딥러닝과 같은 복잡한 모델은 높은 예측 성능을 보이는 대신, 왜 그런 예측이 나왔는지 직관적으로 설명하기 어렵다는 한계를 가짐.</p>
</blockquote>
<h3 id="2-전통적인-프로그래밍-vs-머신러닝">2. 전통적인 프로그래밍 VS 머신러닝</h3>
<p><img alt="TravsML" src="https://velog.velcdn.com/images/yura103/post/8c548457-2ccb-45cc-9558-a4ebb3c6a369/image.png" /></p>
<table>
  <thead>
    <tr>
      <th>구분</th>
      <th>전통적인 프로그래밍</th>
      <th>머신러닝</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>기본 개념</td>
      <td>사람이 명시적인 규칙을 직접 작성</td>
      <td>데이터로부터 규칙을 자동 학습</td>
    </tr>
    <tr>
      <td>문제 유형</td>
      <td>규칙이 명확한 문제에 강함</td>
      <td>규칙을 명시하기 어려운 문제에 강함</td>
    </tr>
    <tr>
      <td>예시</td>
      <td>90점 이상 → A<br />80점 이상 → B</td>
      <td>이메일 → 스팸/정상 예측<br />거래 → 사기 확률 예측</td>
    </tr>
    <tr>
      <td>규칙 변화</td>
      <td>규칙이 바뀌면 코드를 직접 수정해야 함</td>
      <td>새 데이터로 재학습하여 대응 가능</td>
    </tr>
    <tr>
      <td>예외 처리</td>
      <td>예외가 많아지면 로직이 깨지기 쉬움</td>
      <td>예외도 패턴으로 흡수 가능</td>
    </tr>
    <tr>
      <td>성능 평가</td>
      <td>정답/오답 정도로만 판단</td>
      <td>Accuracy, F1, AUC 등 수치로 성능 측정</td>
    </tr>
    <tr>
      <td>확장성</td>
      <td>문제 복잡해질수록 유지보수 어려움</td>
      <td>데이터가 쌓일수록 성능 개선 가능</td>
    </tr>
    <tr>
      <td>주요 리스크</td>
      <td>규칙 누락, 하드코딩</td>
      <td>과적합, 편향, 데이터 누수</td>
    </tr>
    <tr>
      <td>해석 가능성</td>
      <td>로직이 명확하여 설명 쉬움</td>
      <td>복잡한 모델은 블랙박스가 되기 쉬움</td>
    </tr>
    <tr>
      <td>대표 사용처</td>
      <td>계산 로직, 정책 규칙, 단순 판별</td>
      <td>추천, 검색, 사기 탐지, 예측 문제</td>
    </tr>
  </tbody>
</table>
<br />


<h3 id="3-머신러닝-종류">3. 머신러닝 종류</h3>
<p><img alt="머신러닝 종류" src="https://velog.velcdn.com/images/yura103/post/d2f335ed-fd49-42d1-a4e3-6531ace2e1f9/image.png" width="60%" /></p>
<table>
  <thead>
    <tr>
      <th>구분</th>
      <th>지도학습<br />(Supervised Learning)</th>
      <th>비지도학습<br />(Unsupervised Learning)</th>
      <th>준지도학습<br />(Semi-supervised Learning)</th>
      <th>강화학습<br />(Reinforcement Learning)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>정답(Label)</td>
      <td>있음</td>
      <td>없음</td>
      <td>일부만 있음</td>
      <td>없음 (보상만 존재)</td>
    </tr>
    <tr>
      <td>목적</td>
      <td>입력에 대한 정답 예측</td>
      <td>데이터의 구조·패턴 발견</td>
      <td>적은 정답으로 학습 성능 향상</td>
      <td>누적 보상을 최대화하는 행동 학습</td>
    </tr>
    <tr>
      <td>대표 문제 유형</td>
      <td>분류, 회귀</td>
      <td>클러스터링, 차원 축소, 이상 탐지</td>
      <td>라벨 부족 문제</td>
      <td>의사결정, 정책 학습</td>
    </tr>
    <tr>
      <td>주요 기법</td>
      <td>
        로지스틱 회귀<br />
        결정 트리<br />
        랜덤 포레스트<br />
        XGBoost
      </td>
      <td>
        K-means<br />
        DBSCAN<br />
        PCA<br />
        Isolation Forest
      </td>
      <td>
        Pseudo-labeling<br />
        Self-training<br />
        Label Propagation
      </td>
      <td>
        Q-Learning<br />
        SARSA<br />
        Policy Gradient<br />
        DQN
      </td>
    </tr>
    <tr>
      <td>데이터 예시</td>
      <td>
        이메일 + 스팸 여부<br />
        집 정보 + 가격
      </td>
      <td>
        고객 행동 로그<br />
        사용자 특성 데이터
      </td>
      <td>
        일부 라벨된 데이터<br />
        다수의 미라벨 데이터
      </td>
      <td>
        환경 상태<br />
        행동과 보상
      </td>
    </tr>
    <tr>
      <td>활용 예시</td>
      <td>
        스팸 분류<br />
        사기 거래 예측<br />
        가격 예측
      </td>
      <td>
        고객 세그먼트 분석<br />
        데이터 탐색(EDA)
      </td>
      <td>
        의료 데이터 분류<br />
        이미지 분류
      </td>
      <td>
        게임 AI<br />
        로봇 제어<br />
        자율주행
      </td>
    </tr>
  </tbody>
</table>

<ul>
<li>추천시스템은 지도학습이나 비지도학습과 같이 특정 학습 방식이 아니라, 사용자에게 적절한 아이템을 추천하기 위한 응용 시스템이며, 실제로는 지도학습, 비지도학습, 협업 필터링 등 다양한 기법을 조합해 구현됨.<br />

</li>
</ul>
<h3 id="4-모델의-일반화">4. 모델의 일반화</h3>
<p><img alt="모델의 일반화1" src="https://velog.velcdn.com/images/yura103/post/8290f90b-387e-4852-b842-4a7fbc81bca7/image.png" width="80%" /></p>
<ul>
<li><strong>Overfitting(과적합)</strong>: 학습 데이터에 지나치게 맞춰진 상태<ul>
<li>새로운 데이터에 대해서는 성능이 떨어짐</li>
<li>일반적인 패턴뿐만 아니라 노이즈까지 학습함</li>
</ul>
</li>
<li><strong>Underfitting(과소적합)</strong>: 모델이 자나치게 단순하여 데이터의 패턴을 충분히 학습하지 못한 상태<ul>
<li>학습 데이터와 새로운 데이터 모두에서 성능이 낮게 나타남</li>
<li>데이터의 구조를 제대로 표현하지 못한 경우에 발생</li>
</ul>
</li>
<li>머신러닝의 목표: 과적합이나 과소적합에 치우치지 않고, 학습 데이터와 보지 못한 데이터 모두에서 안정적인 성능을 높이는 <strong>일반화(Generalization)</strong>가 잘 된 모델을 만드는 것
<img alt="모델의 일반화2" src="https://velog.velcdn.com/images/yura103/post/c1aad2bb-e175-4e2b-ae2d-9803a69cc0c0/image.png" /></li>
<li>위 그림은 모델의 복잡도에 따라 발생하는 편향(Bias)과 분산(Variance)의 관계를 나타냄.</li>
<li><strong>Bias(편향)</strong>: 모델이 실제 데이터의 패턴을 얼마나 단순하게 가정하고 있는지를 의미<ul>
<li>항상 비슷한 방향으로 틀리면 - 편향이 큼</li>
<li>정답 근처를 중심으로 맞추면 - 편향이 작음</li>
</ul>
</li>
<li><strong>Variance(분산)</strong>: 학습 데이터가 조금만 달라져도 모델의 예측 결과가 얼마나 크게 변하는지를 의미<ul>
<li>예측 결과들이 넓게 흩어져 있으면 - 분산이 큼</li>
<li>예측 결과들이 한곳에 모여 있으면 - 분산이 작음<blockquote>
<p>사격 비유로 보면,</p>
<ul>
<li>편향(Bias): 조준점이 어디를 향하고 있는가 (초점)</li>
<li>분산(Variance): 탄착이 얼마나 흩어지는가 (흔들림)</li>
</ul>
<p>편향이 큰 경우에는 초점만 조정하면 개선할 수 있어 더 많은 데이터나 모델 개선으로 성능을 높일 수 있음. 반면 분산이 큰 경우에는 예측이 들쭉날쭉해 새로운 데이터에 대한 일반화가 어려우며, 이는 오버피팅으로 이어짐.</p>
</blockquote>
</li>
</ul>
</li>
</ul>
<p>-&gt; 편향이 크면 <strong>언더피팅</strong>이 발생하고, 분산이 크면 <strong>오버피팅</strong>이 발생하기 때문에 편향과 분산이 적절히 균형을 이루는 지점에서 보지 못한 데이터에도 잘 동작하는 일반화된 모델을 찾는 것이 중요함!</p>
