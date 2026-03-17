# [ML] 비지도학습

- Date: 2026-03-17 03:58:09 UTC
- Velog: https://velog.io/@yura103/ML-%EB%B9%84%EC%A7%80%EB%8F%84%ED%95%99%EC%8A%B5

---

<h3 id="1-비지도학습">1. 비지도학습</h3>
<p>: 정답(label)없이 데이터의 구조, 패턴, 관계를 학습하는 방법</p>
<table>
<thead>
<tr>
<th>구분</th>
<th>지도학습</th>
<th>비지도학습</th>
</tr>
</thead>
<tbody><tr>
<td>정답(y)</td>
<td>있음</td>
<td>없음</td>
</tr>
<tr>
<td>목표</td>
<td>예측</td>
<td>구조 발견</td>
</tr>
<tr>
<td>평가</td>
<td>정확도, RMSE 등</td>
<td>명확하지 않음</td>
</tr>
<tr>
<td>예시</td>
<td>분류, 회귀</td>
<td>군집, 차원축소</td>
</tr>
</tbody></table>
<h3 id="2-군집clustering">2. 군집(Clustering)</h3>
<p>: 비슷한 데이터끼리 자동으로 묶는 것
정답은 없지만 데이터 내부의 자연스러운 그룹 구조를 찾는 것이 목적!</p>
<h4 id="1-거리-기반---k-means">1) 거리 기반 - K-Means</h4>
<p>: 각 클러스터의 중심(centroid)을 기준으로 데이터를 나누는 모델
<img alt="" src="https://velog.velcdn.com/images/yura103/post/bcc64b60-acf2-42e1-b0a2-69963f3e0be1/image.png" /></p>
<ul>
<li>동작 과정<ol>
<li>클러스터 개수 K 지정</li>
<li>랜덤하게 K개의 중심점 초기화</li>
<li>각 데이터를 가장 가까운 중심에 할당</li>
<li>중심을 해당 클러스터 평균으로 업데이트</li>
<li>3~4번 반복</li>
</ol>
</li>
<li>수식: 각 점과 해당 클러스터 중심 간 거리 제곱합(MSE) 최소화
<img alt="" src="https://velog.velcdn.com/images/yura103/post/91d7540e-8fef-42f1-b3ac-41738801d84b/image.png" /></li>
<li>장점: 빠르고 구현하기 쉬우며 대용량에 적합함.</li>
<li>단점: K를 미리 정해야하고 구형(원형) 클러스터에만 잘 맞으며 이상치에 민감함.<br />

</li>
</ul>
<h4 id="2-계층-기반---hierarchical-clustering">2) 계층 기반 - Hierarchical Clustering</h4>
<p>: 데이터를 트리 구조로 묶는 모델
<img alt="" src="https://velog.velcdn.com/images/yura103/post/baea8b1c-019b-478a-b3d6-702c3ec75467/image.png" /></p>
<ul>
<li><p><strong>Agglomerative(Bottom-up)</strong> -&gt; 실무에서 주로 사용</p>
<ul>
<li>처음엔 모든 점이 개별 클러스터</li>
<li>가장 가까운 것끼리 계속 병합</li>
</ul>
</li>
<li><p><strong>Divisive(Top-down)</strong></p>
<ul>
<li>하나의 큰 클러스터에서 시작</li>
<li>계속 쪼갬.</li>
</ul>
</li>
<li><p>거리 기준(Linkage 방식)</p>
<ul>
<li>Single linkage -&gt; 최소 거리</li>
<li>Complete linkage -&gt; 최대 거리</li>
<li>Average linkage -&gt; 평균 거리</li>
<li>Ward -&gt; 분산 증가 최소화</li>
</ul>
</li>
<li><p>K를 미리 정하지 않아도 되고 덴드로그램으로 시각화 가능
<img alt="" src="https://velog.velcdn.com/images/yura103/post/113ebd46-2363-4b9a-9abd-f6996732c09e/image.png" /></p>
</li>
<li><p>계산량이 크고 큰 데이터에 비효율적임</p>
</li>
<li><p>데이터가 많지 않고 계층 구조를 보고 싶을 때 주로 사용</p>
<br />

</li>
</ul>
<h4 id="3-밀도-기반---dbscan">3) 밀도 기반 - DBSCAN</h4>
<p>: 밀도가 높은 영역을 하나의 클러스터로 보는 모델
<img alt="" src="https://velog.velcdn.com/images/yura103/post/36879de4-bc1e-40e7-b9a8-fb09cb702b2b/image.png" /></p>
<ul>
<li><p>ε (입실론): 반경, MinPts: 최소 이웃 개수</p>
</li>
<li><p>Core point: 이웃이 충분히 많음, Border point: 코어 근처, Noise: 어디에도 속하지 않음
  <img alt="" src="https://velog.velcdn.com/images/yura103/post/8b9aea63-f0a2-470f-9a9a-be020ce823e1/image.png" /></p>
</li>
<li><p>클러스터 개수 자동 결정, 이상치 자동 탐지, 비구형 클러스터 가능</p>
</li>
<li><p>입실론 선택 어려우며 밀도 차이가 큰 데이터에 약함</p>
</li>
<li><p>이상치 탐지가 중요할 때와 클러스터 모양이 복잡할 때 주로 사용</p>
<br />

</li>
</ul>
<h4 id="4-확률-기반---gaussian-mixture-modelgmm">4) 확률 기반 - Gaussian Mixture Model(GMM)</h4>
<p>: 각 클러스터가 &quot;가우시안 분포&quot;라고 가정
<img alt="" src="https://velog.velcdn.com/images/yura103/post/905777fa-f866-484d-a79d-85ef13e2ce1f/image.png" /></p>
<p>K-Means는 &quot;딱 잘라 나누는&quot;방식이라면 GMM은 각 점이 각 클러스터에 속할 확률을 가짐 -&gt; soft assignment(확률 기반 소속)</p>
<ul>
<li>학습 방식 (EM 알고리즘 사용)<ol>
<li>E-step: 각 점의 소속 확률 계산</li>
<li>M-step: 평균/공분산 업데이트</li>
<li>반복</li>
</ol>
</li>
<li>타원형 클러스터와 확률 해석 가능</li>
<li>K 필요하고 계산 비용이 크며 초기값...?<br />

</li>
</ul>
<h4 id="정리">정리</h4>
<table>
<thead>
<tr>
<th>알고리즘</th>
<th>기준</th>
<th>K 필요</th>
<th>이상치 처리</th>
<th>모양</th>
</tr>
</thead>
<tbody><tr>
<td>K-Means</td>
<td>거리</td>
<td>O</td>
<td>약함</td>
<td>원형</td>
</tr>
<tr>
<td>Hierarchical</td>
<td>거리</td>
<td>선택적</td>
<td>약함</td>
<td>다양</td>
</tr>
<tr>
<td>DBSCAN</td>
<td>밀도</td>
<td>X</td>
<td>강함</td>
<td>자유</td>
</tr>
<tr>
<td>GMM</td>
<td>확률</td>
<td>O</td>
<td>보통</td>
<td>타원형</td>
</tr>
</tbody></table>
<br />

<h3 id="3-차원축소dimensionality-reduction">3. 차원축소(Dimensionality Reduction)</h3>
<ul>
<li>압축: 정보를 최대한 유지하며 차원을 줄이는 과정 -&gt; 모델 학습/저장/노이즈 제거</li>
<li>시각화(2D/3D 구조 보기) -&gt; 군집/이상치/구조 탐색<h4 id="1-pcaprincipal-component-analysis">1) PCA(Principal Component Analysis)</h4>
: 데이터를 가장 많이 퍼져있는 방향(분산 최대)로 회전시켜, 중요한 축부터 남기는 선형 차원축소
<img alt="" src="https://velog.velcdn.com/images/yura103/post/7628e588-7aff-43a5-b5df-4ecc4b521d5c/image.png" /></li>
<li>분산이 가장 큰 방향을 찾기 -&gt; 직교하는 다음 방향 찾기 -&gt; 상위 몇 개 축만 남기기</li>
<li>노이즈를 제거하고 다중공산성을 완화하며 차원 줄여서 모델 안정화시키고 빠른 압축</li>
<li>선형 구조만 잡고 곡선/비선형 구조는 못 잡고 스케일에 민감하여 표준화 필수</li>
<li>수치형 tabular 데이터, 모델 전처리, 노이즈 제거, 속도 개선에서 주로 사용<h4 id="2-t-sne">2) t-SNE</h4>
: 가까운 점은 2D에서도 가깝게 만들도록, 국소 이웃 구조를 보존하는 시각화 특화 비선형 차원축소
<img alt="" src="https://velog.velcdn.com/images/yura103/post/cbae0f18-7af4-4a18-8edb-6068e72bb0b0/image.png" /></li>
<li>전역 구조보다 로컬 구조에 집중</li>
<li>가까운 점끼리는 확률적으로 높은 유사도를 가지며 이 확률을 저차원에서도 유지</li>
<li>클러스터 간 거리가 진짜 거리가 아니고 전역 구조 왜곡 가능하기 때문에 시각화용으로 자주 쓰임(모델 전처리X)</li>
<li>군집 구조 탐색하고 임베딩 시각화하고 라벨 품질 점검할 때 주로 쓰임<h4 id="3-umap">3) UMAP</h4>
: t-SNE처럼 이웃 구조를 보존하면서도, 더 빠르고 전역 구조도 어느 정도 유지하는 비선형 차원축소</li>
<li>데이터가 어떤 &quot;곡면&quot; 위에 있다고 가정</li>
<li>핵심 파라미터<ul>
<li>n_neighbors -&gt; 로컬 vs 전역 균형</li>
<li>min_dist -&gt; 군집이 얼마나 뭉칠지</li>
</ul>
</li>
<li>대규모 데이터 시각화하고 임베딩 생성하고 클러스터링 전 단계에서 주로 사용 
<img alt="" src="https://velog.velcdn.com/images/yura103/post/b84345b6-364a-42ac-ac59-2e0223ec92e5/image.png" /></li>
</ul>
<table>
<thead>
<tr>
<th>항목</th>
<th>t-SNE</th>
<th>UMAP</th>
</tr>
</thead>
<tbody><tr>
<td>속도</td>
<td>느림</td>
<td>빠름</td>
</tr>
<tr>
<td>전역 구조</td>
<td>약함</td>
<td>조금 더 유지</td>
</tr>
<tr>
<td>transform</td>
<td>약함</td>
<td>지원 좋음</td>
</tr>
<tr>
<td>실무 활용</td>
<td>시각화 중심</td>
<td>임베딩/클러스터링</td>
</tr>
</tbody></table>
<h4 id="4-autoencoder">4) AutoEncoder</h4>
<p>: 신경망으로 입력 -&gt; 압축 -&gt; 복원을 학습해서, 압축 공간(latent)을 차원축소 표현으로 쓰는 방식
입력 x -&gt; Encoder -&gt; 압축된 표현 z(latent) -&gt; Decoder -&gt; 복원</p>
<ul>
<li>복잡한 비선형 구조 학습이 가능하며 이미지/텍스트가 강력하고 임베딩 생성에 좋음.</li>
<li>과적합 위험이 있고 튜닝이 필요하며 학습 비용이 크다는 단점이 있음.</li>
<li>이미지, 고차원 임베딩, 비선형 구조가 강한 데이터, 재구성 오차 기반 이상치 탐지에서 주로 사용</li>
</ul>
<table>
<thead>
<tr>
<th>항목</th>
<th>PCA</th>
<th>AutoEncoder</th>
</tr>
</thead>
<tbody><tr>
<td>구조</td>
<td>선형</td>
<td>비선형 가능</td>
</tr>
<tr>
<td>학습</td>
<td>고유값분해</td>
<td>신경망 학습</td>
</tr>
<tr>
<td>복잡성</td>
<td>낮음</td>
<td>높음</td>
</tr>
<tr>
<td>데이터 요구량</td>
<td>적어도 됨</td>
<td>많을수록 좋음</td>
</tr>
</tbody></table>
<h4 id="정리-1">정리</h4>
<table>
<thead>
<tr>
<th>방법</th>
<th>선형</th>
<th>목적</th>
<th>빠름</th>
<th>시각화</th>
<th>전처리</th>
</tr>
</thead>
<tbody><tr>
<td>PCA</td>
<td>O</td>
<td>압축</td>
<td>매우 빠름</td>
<td>보통</td>
<td>좋음</td>
</tr>
<tr>
<td>t-SNE</td>
<td>X</td>
<td>시각화</td>
<td>느림</td>
<td>매우 좋음</td>
<td>거의 안 씀</td>
</tr>
<tr>
<td>UMAP</td>
<td>X</td>
<td>시각화/임베딩</td>
<td>빠름</td>
<td>매우 좋음</td>
<td>가능</td>
</tr>
<tr>
<td>AutoEncoder</td>
<td>X</td>
<td>압축/임베딩</td>
<td>느림</td>
<td>보통</td>
<td>가능</td>
</tr>
</tbody></table>
<h3 id="4-밀도추정이상치-탐지">4. 밀도추정/이상치 탐지</h3>
<p><strong>이상치 탐지란?</strong>
: 데이터의 일반적인 패턴에서 벗어난 &quot;비정상적인 관측치&quot;를 찾는 문제</p>
<ul>
<li>이상치를 정의하는 3가지 관점<ul>
<li>고립되기 쉬운 점 (Isolation)</li>
<li>정상 영역 밖에 있는 점 (Boundary)</li>
<li>주변보다 밀도가 낮은 점 (Density)<h4 id="1-isolation-forest">1) Isolation Forest</h4>
정상 데이터는 뭉쳐있고 랜덤하게 분기해도 쉽게 혼자 남지 않는 반면, 이상치는 외딴 곳에 있고 몇 번만 나눠도 혼자 떨어짐 -&gt; 분리 경로가 짧음</li>
</ul>
</li>
<li>동작 원리<ul>
<li>랜덤으로 feature 선택</li>
<li>랜덤으로 split value 선택</li>
<li>데이터를 분리</li>
<li>이 과정을 트리 형태로 반복</li>
<li>어떤 점이 고립되기까지의 깊이(path length) 계산</li>
<li><blockquote>
<p>평균 path length가 짧으면 이상치</p>
</blockquote>
</li>
</ul>
</li>
<li>장점: 빠르고 고차원에서도 비교적 잘 작동하고 스케일 크게 문제 안 되고 기본 baseline으로 좋음.</li>
<li>단점: contamination(이상치 비율) 설정이 필요하고 아주 복잡한 경계 표현은 어려움.</li>
<li>대규모 tabular 데이터, 빠른 이상치 후보 추출, baseline 모델에 주로 사용<h4 id="2-one-class-svm">2) One-Class SVM</h4>
: &quot;정상 데이터만 감싸는 경계를 학습하고 그 밖은 이상치다.&quot;</li>
<li>커널 공간에서 정상 데이터 대부분을 포함하는 최대 마진 경계 찾기</li>
<li>핵심 파라미터<ul>
<li>ν (nu): 이상치 비율 상한</li>
<li>gamma: 커널 복잡도 조절</li>
<li>유연한 비선형 경계 가능하고 정상 분포가 명확할 때 강력</li>
<li>느리고 스케일링 필수고 파라미터 민감하고 대용량 부적합함.</li>
</ul>
</li>
<li>데이터 크지 않고 정상 패턴이 명확하고 경계 기반 탐지 필요할 때 주로 쓰임<h4 id="3-lof">3) LOF</h4>
: &quot;내 주변보다 밀도가 낮으면 이상치&quot; -&gt; 로컬 밀도 비교</li>
<li>동작 방식<ol>
<li>k개 이웃 찾기</li>
<li>이웃들의 밀도 계산</li>
<li>나의 밀도와 이웃 밀도 비교</li>
<li>비율이 크면 이상치</li>
</ol>
</li>
<li>로컬 이상치 탐지에 강하고 복잡한 분포에서도 유리</li>
<li>KNN 기반으로 느리고 고차원에서 거리 의미 약해지고 새 데이터에 대해 transform 불편</li>
<li>군집 여러 개 존재하고 특정 클러스터 내부에서 튀는 점 탐지할 때 주로 사용</li>
</ul>
<h4 id="정리-2">정리</h4>
<table>
<thead>
<tr>
<th>항목</th>
<th>Isolation Forest</th>
<th>One-Class SVM</th>
<th>LOF</th>
</tr>
</thead>
<tbody><tr>
<td>철학</td>
<td>고립</td>
<td>경계</td>
<td>밀도</td>
</tr>
<tr>
<td>속도</td>
<td>빠름</td>
<td>느림</td>
<td>중간</td>
</tr>
<tr>
<td>대규모</td>
<td>가능</td>
<td>어려움</td>
<td>어려움</td>
</tr>
<tr>
<td>고차원</td>
<td>비교적 강함</td>
<td>민감</td>
<td>약함</td>
</tr>
<tr>
<td>이상치 종류</td>
<td>전역</td>
<td>경계 밖</td>
<td>로컬</td>
</tr>
<tr>
<td>baseline 추천</td>
<td>⭐⭐⭐</td>
<td>⭐</td>
<td>⭐⭐</td>
</tr>
</tbody></table>
<h3 id="5-연관규칙">5. 연관규칙</h3>
<p>: 거래(transaction) 데이터에서 &quot;A가 있으면 B도 같이 있다&quot; 같은 패턴을 찾는 것</p>
<table>
<thead>
<tr>
<th>거래 ID</th>
<th>상품 목록</th>
</tr>
</thead>
<tbody><tr>
<td>T1</td>
<td>{우유, 빵, 버터}</td>
</tr>
<tr>
<td>T2</td>
<td>{우유, 기저귀}</td>
</tr>
<tr>
<td>T3</td>
<td>{빵, 버터}</td>
</tr>
<tr>
<td>T4</td>
<td>{우유, 빵}</td>
</tr>
<tr>
<td>이렇게 집합 형태가 기본 구조임</td>
<td></td>
</tr>
<tr>
<td>- Support(지지도): 전체 거래 중 해당 아이템셋이 등장한 비율</td>
<td></td>
</tr>
<tr>
<td><img alt="" src="https://velog.velcdn.com/images/yura103/post/a05b4d42-f1ef-4722-8fcc-db07a8f6dc14/image.png" /></td>
<td></td>
</tr>
<tr>
<td>- Confidence(신뢰도): A를 사면 B도 살 확률</td>
<td></td>
</tr>
<tr>
<td><img alt="" src="https://velog.velcdn.com/images/yura103/post/61a4075e-eb71-49f8-a117-56cb5c4f3642/image.png" /></td>
<td></td>
</tr>
<tr>
<td>- Lift(향상도): 원래 B가 많이 팔리는 상품이라서 그런 건 아닌지 보정</td>
<td></td>
</tr>
<tr>
<td><img alt="" src="https://velog.velcdn.com/images/yura103/post/64d7a3c4-c980-401f-b648-65e6259a37b9/image.png" /></td>
<td></td>
</tr>
<tr>
<td>#### 1) Apriori</td>
<td></td>
</tr>
<tr>
<td>: 자주 등장하는 아이템셋의 부분집합도 자주 등장</td>
<td></td>
</tr>
<tr>
<td><img alt="" src="https://velog.velcdn.com/images/yura103/post/b3eb5d40-9b24-4bc7-ac5e-058eaed6ae28/image.png" /></td>
<td></td>
</tr>
</tbody></table>
<ul>
<li>동작 과정<ol>
<li>1-아이템셋 중 support &gt;= min_support인 것 찾기</li>
<li>이들을 조합해 2-아이템 후보 생성</li>
<li>support 검사 -&gt; 살아남은 것만 유지</li>
<li>3-아이템 후보 생성</li>
<li>반복</li>
</ol>
</li>
<li>개념 이해가 쉽고 구현이 직관적</li>
<li>후보가 폭발적으로 증가 가능하고 min_support가 낮으면 계산량 폭증하고 아이템 종류 많으면 매우 느림</li>
<li>데이터가 크지 않고 이해 목적의 baseline에서 주로 사용<h4 id="2-fp-growth">2) FP-Growth</h4>
: 후보를 만들지 않고 거래를 트리 구조로 압축해 빈발 패턴을 찾는 과정
<img alt="" src="https://velog.velcdn.com/images/yura103/post/472e9153-1228-4f44-b57c-fab725957022/image.png" /></li>
</ul>
<p>Apriori는 후보를 생성하고 후보 하나하나 support 검사를 하는 반면, FP-Growth는 전체 거래를 FP-tree로 압축하고 공통 prefix를 공유하고 후보 폭발을 줄임</p>
<ul>
<li>Apriori보다 빠르고 대규모 데이터에 적합하고 후보 폭발을 방지</li>
<li>구현 복잡하고 이해 난이도 높음<h4 id="정리-3">정리</h4>
<table>
<thead>
<tr>
<th><strong>Apriori (후보 만들고 검사)</strong></th>
<th><strong>FP-Growth (압축해서 탐색)</strong></th>
</tr>
</thead>
<tbody><tr>
<td>1️⃣ 1개짜리부터 개수 세기</td>
<td>1️⃣ 1개짜리 개수 세기 (같음)</td>
</tr>
<tr>
<td>우유4, 빵4, 버터2, 기저귀2</td>
<td>우유4, 빵4, 버터2, 기저귀2</td>
</tr>
<tr>
<td>--------------------------------</td>
<td>--------------------------------</td>
</tr>
<tr>
<td>2️⃣ 2개 조합 전부 만들기</td>
<td>2️⃣ 거래를 빈도순으로 정렬</td>
</tr>
<tr>
<td>우유-빵, 우유-버터, 우유-기저귀, 빵-버터, 빵-기저귀…</td>
<td>예: 우유→빵→버터</td>
</tr>
<tr>
<td>--------------------------------</td>
<td>--------------------------------</td>
</tr>
<tr>
<td>3️⃣ 각 조합마다 등장 횟수 전부 다시 계산</td>
<td>3️⃣ 공통 prefix를 하나의 경로로 압축</td>
</tr>
<tr>
<td>우유-빵(3) ✔</td>
<td>우유(4)</td>
</tr>
<tr>
<td>우유-기저귀(2) ✔</td>
<td>└─ 빵(3)</td>
</tr>
<tr>
<td>빵-버터(2) ✔</td>
<td>├─ 버터(1)</td>
</tr>
<tr>
<td>나머지 탈락</td>
<td>└─ 기저귀(1)</td>
</tr>
<tr>
<td>--------------------------------</td>
<td>--------------------------------</td>
</tr>
<tr>
<td>4️⃣ 3개 조합 다시 생성하고 검사</td>
<td>4️⃣ 트리에서 조건부 패턴 바로 추출</td>
</tr>
<tr>
<td>우유-빵-기저귀(1) 탈락</td>
<td>우유-빵(3), 우유-기저귀(2), 빵-버터(2) 바로 계산</td>
</tr>
<tr>
<td>--------------------------------</td>
<td>--------------------------------</td>
</tr>
<tr>
<td>핵심: <strong>후보를 계속 만들어서 검사</strong></td>
<td>핵심: <strong>트리로 압축해서 후보 폭발 방지</strong></td>
</tr>
<tr>
<td><br /></td>
<td></td>
</tr>
</tbody></table>
</li>
</ul>
<table>
<thead>
<tr>
<th>항목</th>
<th>Apriori</th>
<th>FP-Growth</th>
</tr>
</thead>
<tbody><tr>
<td>방식</td>
<td>후보 생성 후 검사</td>
<td>트리 압축</td>
</tr>
<tr>
<td>속도</td>
<td>느릴 수 있음</td>
<td>빠름</td>
</tr>
<tr>
<td>후보 폭발</td>
<td>있음</td>
<td>거의 없음</td>
</tr>
<tr>
<td>구현 난이도</td>
<td>쉬움</td>
<td>어려움</td>
</tr>
<tr>
<td>실무 사용</td>
<td>적음</td>
<td>많음</td>
</tr>
</tbody></table>
<blockquote>
<p><strong>연관규칙의 한계</strong>
인과관계가 아니고 단순 동시 발생 패턴일 뿐임!
lift 해석 주의가 필요하고 너무 낮은 support는 노이즈일 수 있음!</p>
</blockquote>
