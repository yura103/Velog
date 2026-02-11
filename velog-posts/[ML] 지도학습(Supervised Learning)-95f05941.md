# [ML] 지도학습(Supervised Learning)

- Date: 2026-02-03 07:35:23 UTC
- Velog: https://velog.io/@yura103/ML-%EC%A7%80%EB%8F%84%ED%95%99%EC%8A%B5Supervised-Learning-dws6ylly

---

<h3 id="1-지도학습">1. 지도학습</h3>
<p>: 정답이 있는 데이터를 사용해 입력과 출력 사이의 관계를 학습하는 머신러닝 방법</p>
<ul>
<li>&quot;무엇을 예측하느냐&quot;에 따라 분류/회귀 등으로 나뉨</li>
</ul>
<h3 id="2-분류classification">2. 분류(Classification)</h3>
<ul>
<li>출력값: 범주형</li>
<li>예: 정상/비정상</li>
<li>확률을 예측한 뒤 <strong>임계값</strong>을 기준으로 최종 클래스 결정<blockquote>
<p><strong>임계값(Threshold)</strong>: 예측 확률을 양성/음성으로 나누는 기준</p>
</blockquote>
</li>
</ul>
<h3 id="3-회귀regression">3. 회귀(Regression)</h3>
<ul>
<li>출력값: 연속적인 수치</li>
<li>예: 집값, 매출, 온도</li>
<li>하나의 숫자를 직접 예측하며, 예측값과 실제값의 차이를 최소화하도록 학습</li>
</ul>
<h3 id="4-데이터-분할data-split">4. 데이터 분할(Data Split)</h3>
<ul>
<li><strong>train</strong>(훈련): 모델이 직접 학습하는 데이터</li>
<li><strong>validation</strong>(검증): 모델 선택 및 하이퍼파라미터 튜닝에 사용</li>
<li><strong>test</strong>(테스트): 최종 성능 평가용 데이터<p align="center">
<img alt="데이터 분할" src="https://velog.velcdn.com/images/yura103/post/65c5586b-abf3-4d87-9dd6-711db79d9b31/image.png" width="70%" />
</p>


</li>
</ul>
<h3 id="5-성능-평가">5. 성능 평가</h3>
<h4 id="1-혼동행렬confusion-matrix">1) 혼동행렬(Confusion Matrix)</h4>
<p>: 분류 성능 지표를 계산하기 위한 기초 구조
<img alt="혼동행렬" src="https://velog.velcdn.com/images/yura103/post/789eb979-4914-49b6-80b7-d0ef116ff24a/image.png" /></p>
<div align="center">
  <table>
    <thead>
      <tr>
        <th>지표</th>
        <th>영어</th>
        <th>한국어</th>
        <th>의미</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Sensitivity</td>
        <td>TPR, Recall</td>
        <td>민감도(재현율)</td>
        <td>실제 양성 중 맞춘 비율</td>
      </tr>
      <tr>
        <td>Specificity</td>
        <td>TNR</td>
        <td>특이도</td>
        <td>실제 음성 중 맞춘 비율</td>
      </tr>
      <tr>
        <td>Accuracy</td>
        <td>-</td>
        <td>정확도</td>
        <td>전체 중 맞춘 비율</td>
      </tr>
      <tr>
        <td>Precision</td>
        <td>PPV</td>
        <td>정밀도(양성 예측도)</td>
        <td>양성 예측 중 진짜 양성</td>
      </tr>
      <tr>
        <td>NPV</td>
        <td>-</td>
        <td>음성 예측도</td>
        <td>음성 예측 중 진짜 음성</td>
      </tr>
    </tbody>
  </table>
</div>

<br />

<table>
  <thead>
    <tr>
      <th>상황</th>
      <th>TP (True Positive)</th>
      <th>TN (True Negative)</th>
      <th>FP (False Positive)</th>
      <th>FN (False Negative)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>스팸 필터</td>
      <td>스팸 메일을<br />스팸으로 차단</td>
      <td>정상 메일을<br />정상적으로 전달</td>
      <td><b>정상 메일을<br />스팸으로 차단</b></td>
      <td>스팸 메일이<br />받은편지함으로 전달</td>
    </tr>
    <tr>
      <td>사기 탐지</td>
      <td>사기 거래를<br />사기로 탐지</td>
      <td>정상 거래를<br />정상 처리</td>
      <td>정상 거래를<br />사기로 오탐</td>
      <td><b>사기 거래를<br />정상으로 통과</b></td>
    </tr>
    <tr>
      <td>의료 진단</td>
      <td>질병 환자를<br />정확히 진단</td>
      <td>건강한 사람을<br />정상 판정</td>
      <td>건강한 사람을<br />환자로 오진</td>
      <td><b>환자를<br />정상으로 판단</b></td>
    </tr>
    <tr>
      <td>추천 시스템</td>
      <td>관심 있는 상품을<br />추천</td>
      <td>관심 없는 상품을<br />추천하지 않음</td>
      <td><b>관심 없는 상품을<br />추천</b></td>
      <td>관심 있는 상품을<br />추천하지 않음</td>
    </tr>
  </tbody>
</table>


<blockquote>
<p>임계값을 조정하면 Precision과 Recall 사이의 균형이 바뀌며, 어떤 오류(FP 또는 FN)를 더 줄일지 선택할 수 있음.</p>
</blockquote>
<h4 id="2-성과-지표">2) 성과 지표</h4>
<table>
  <thead>
    <tr>
      <th>성과 지표</th>
      <th>수식</th>
      <th>문제 유형</th>
      <th>주 사용처</th>
      <th>언제 적합한가</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Accuracy</b></td>
      <td>(TP + TN) / (TP + TN + FP + FN)</td>
      <td>분류</td>
      <td>균형 데이터</td>
      <td>모든 클래스 비중이 비슷할 때</td>
    </tr>
    <tr>
      <td><b>Balanced Accuracy</b></td>
      <td>(Recall<sub>+</sub> + Recall<sub>-</sub>) / 2</td>
      <td>분류</td>
      <td>불균형 데이터</td>
      <td>다수 클래스 쏠림 방지</td>
    </tr>
    <tr>
      <td><b>Precision</b></td>
      <td>TP / (TP + FP)</td>
      <td>분류</td>
      <td>스팸, 추천</td>
      <td>오탐(FP)이 치명적일 때</td>
    </tr>
    <tr>
      <td><b>Recall</b></td>
      <td>TP / (TP + FN)</td>
      <td>분류</td>
      <td>사기, 의료</td>
      <td>미탐(FN)이 치명적일 때</td>
    </tr>
    <tr>
      <td><b>F1-score</b></td>
      <td>2 × (Precision × Recall) / (Precision + Recall)</td>
      <td>분류</td>
      <td>불균형 분류</td>
      <td>Precision·Recall 균형</td>
    </tr>
    <tr>
      <td><b>F1-macro</b></td>
      <td>(1 / C) × Σ F1<sub>c</sub></td>
      <td>분류</td>
      <td>다중 분류</td>
      <td>모든 클래스 동일 중요</td>
    </tr>
    <tr>
      <td><b>F1-weighted</b></td>
      <td>Σ (n<sub>c</sub> / N) × F1<sub>c</sub></td>
      <td>분류</td>
      <td>실무·대회</td>
      <td>클래스 비중 반영</td>
    </tr>
    <tr>
      <td><b>ROC-AUC</b></td>
      <td>ROC 곡선 아래 면적</td>
      <td>분류</td>
      <td>금융, 신용</td>
      <td>임계값과 무관한 순위 성능</td>
    </tr>
    <tr>
      <td><b>PR-AUC</b></td>
      <td>Precision–Recall 곡선 면적</td>
      <td>분류</td>
      <td>극불균형</td>
      <td>양성 클래스가 매우 적을 때</td>
    </tr>
    <tr>
      <td><b>Log Loss</b></td>
      <td>−Σ [ y·log(p) + (1−y)·log(1−p) ]</td>
      <td>분류</td>
      <td>금융·신용</td>
      <td>확률 예측 품질 평가</td>
    </tr>
    <tr>
      <td><b>Brier Score</b></td>
      <td>(1/N) × Σ (y − p)²</td>
      <td>분류</td>
      <td>리스크 모델</td>
      <td>확률 신뢰도(calibration)</td>
    </tr>
    <tr>
      <td><b>MCC</b></td>
      <td>(TP·TN − FP·FN) / √((TP+FP)(TP+FN)(TN+FP)(TN+FN))</td>
      <td>분류</td>
      <td>극불균형</td>
      <td>가장 안정적인 단일 지표</td>
    </tr>
    <tr>
      <td><b>MAE</b></td>
      <td>(1/N) × Σ |y − ŷ|</td>
      <td>회귀</td>
      <td>가격·수요</td>
      <td>직관적 오차 해석</td>
    </tr>
    <tr>
      <td><b>MSE</b></td>
      <td>(1/N) × Σ (y − ŷ)²</td>
      <td>회귀</td>
      <td>연구</td>
      <td>최적화·미분 용이</td>
    </tr>
    <tr>
      <td><b>RMSE</b></td>
      <td>√MSE</td>
      <td>회귀</td>
      <td>대회</td>
      <td>큰 오차에 강한 패널티</td>
    </tr>
    <tr>
      <td><b>R²</b></td>
      <td>1 − (Σ (y−ŷ)² / Σ (y−ȳ)²)</td>
      <td>회귀</td>
      <td>리포트</td>
      <td>평균 예측 대비 설명력</td>
    </tr>
    <tr>
      <td><b>MAPE</b></td>
      <td>(1/N) × Σ |(y−ŷ)/y|</td>
      <td>회귀</td>
      <td>매출·수요</td>
      <td>비율 해석이 중요할 때</td>
    </tr>
    <tr>
      <td><b>RMSLE</b></td>
      <td>√( (1/N) × Σ (log(ŷ+1) − log(y+1))² )</td>
      <td>회귀</td>
      <td>성장률</td>
      <td>큰 값 영향 완화</td>
    </tr>
    <tr>
      <td><b>NDCG@k</b></td>
      <td>DCG@k / IDCG@k</td>
      <td>랭킹/추천</td>
      <td>추천 시스템</td>
      <td>상위 결과가 중요할 때</td>
    </tr>
    <tr>
      <td><b>MAP</b></td>
      <td>(1/Q) × Σ AP</td>
      <td>랭킹/검색</td>
      <td>검색</td>
      <td>전체 랭킹 품질</td>
    </tr>
    <tr>
      <td><b>MRR</b></td>
      <td>(1/Q) × Σ (1 / rank)</td>
      <td>랭킹/QA</td>
      <td>검색·QA</td>
      <td>첫 정답이 중요할 때</td>
    </tr>
  </tbody>
</table>

<blockquote>
<p>머신러닝 모델의 성능은 하나의 지표로 모두 설명할 수 없으며,
문제의 목적과 데이터 특성에 따라 중요하게 봐야 할 오류의 종류가 달라진다.
대회 환경에서는 특정 성과 지표를 극대화하는 것이 목표가 되지만,
이는 검증 데이터에 대한 오버피팅으로 이어져 실제 서비스 환경에서는 일반화 성능과 신뢰도가 떨어질 수 있다.
예를 들어 Precision이 높더라도 RMSE가 크거나 ROC-AUC가 0.5 이하라면,
모델은 의미 있는 예측을 하지 못하는 상태에 가깝다.
결국 좋은 모델이란 단일 지표의 수치가 높은 모델이 아니라,
성능, 일반화, 신뢰도를 함께 고려했을 때 문제에 적합한 모델이다.</p>
</blockquote>
