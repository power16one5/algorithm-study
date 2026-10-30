# Strategic Practice 2

## 1. Inclusion-Exclusion

### 1.

사람 7명의 생일이 4 계절에 적어도 한 번씩 나타날 확률을 구하시오.

$$
A_i = i \text {번째 계절에 생일이 없는 사건} \\[1em]

P(\text {모든 계절에 적어도 1명 생일이 있는 사건}) = 1 - P \left ( \bigcup _{i = 1} ^{4} A_i \right ) \\[1em]

P \left ( \bigcup _{i = 1} ^{4} A_i \right ) = \sum _{i = 1} ^{4} P(A_i) - \sum _{i = 1} ^{3} \sum _{j > i} P( A_i \cap A_j ) + \\[1em]
\sum _{i = 1} ^{2} \sum _{j > i} \sum _{k > j} P( A_i \cap A_j \cap A_k ) \\[1em]
$$

$4$ 계절 모두에 생일이 없는 사건, $A_i \cap A_j \cap A_k \cap A_n = \empty$이다. 

$$
P \left ( \bigcup _{i = 1} ^{4} A_i \right ) = \binom {4} {1} \left ( \frac {3} {4} \right ) ^ 7 - \binom {4} {2} \left ( \frac {2} {4} \right ) ^ 7 + \\[1em]
\binom {4} {3} \left ( \frac {1} {4} \right ) ^ 7 \\[1em]
P(\text {모든 계절에 적어도 1명 생일이 있는 사건}) = \boxed { 1 - \frac {4 \cdot 3 ^ 7 - 6 \cdot 2 ^ 7 + 4} {4 ^ 7} }
$$

### 2.

엘리스는 수업이 일주일에 한 번만 열리는 작은 대학에 다닙니다. 그녀는 서로 시간이 겹치지 않는 30개의 수업 중에 선택하려 하고, 월 ~ 금 각 날에는 6개의 선택할 수 있는 수업이 있습니다. 

앨리스는 무작위로 30개의 수업 중 7개를 선택합니다. 모든 선택의 확률은 동등하게 같습니다. 그녀가 월 ~ 금 모든 날에 수업이 있을 확률은 얼마나 될까요?

#### 포함 배제 방법

$$
A_i = i \text {번째 날에 수업이 없는 사건} \\[1em]

P(\text {모든 날에 수업이 있는 사건}) = 1 - P \left ( \bigcup _{i = 1} ^{5} A_i \right ) \\[1em]

P \left ( \bigcup _{i = 1} ^{5} A_i \right ) = \sum _{i = 1} ^{5} P(A_i) - \sum _{i = 1} ^{4} \sum _{j > i} P( A_i \cap A_j ) + \\[1em]
\sum _{i = 1} ^{3} \sum _{j > i} \sum _{k > j} P( A_i \cap A_j \cap A_k ) \\[1em]
$$

$4, 5$개의 날에 수업이 없는 사건은 $\empty$이다. 

$$
P(A_i)= \frac {\binom {24} {7}} {\binom {30} {7}} \\[1em]
P( A_i \cap A_j ) = \frac {\binom {18} {7}} {\binom {30} {7}} \\[1em]
P( A_i \cap A_j \cap A_k ) = \frac {\binom {12} {7}} {\binom {30} {7}} \\[1em]
P \left ( \bigcup _{i = 1} ^{5} A_i \right ) = \frac {\binom {5} {1} \cdot \binom {24} {7} - \binom {5} {2} \cdot \binom {18} {7} + \binom {5} {3} \cdot \binom {12} {7}} {\binom {30} {7}} \\[1em]
P(\text {모든 날에 수업이 있는 사건}) = \boxed {1 - \frac {\binom {5} {1} \cdot \binom {24} {7} - \binom {5} {2} \cdot \binom {18} {7} + \binom {5} {3} \cdot \binom {12} {7}} {\binom {30} {7}}} \\[1em]
$$

#### Naive Definition

5개의 날 중 7번 선택해야 하므로 2가지 경우가 될 수 있다.
- 2개 날은 2개 수업, 3개 날은 1개 수업
- 1개 날은 3개 수업, 4개 날은 1개 수업

곱의 법칙을 활용하면 

$$
\text {2개 날은 2개 수업, 3개 날은 1개 수업} = \binom {5} {2} \binom {6} {2} ^ 2 \binom {6} {1} ^ 3 \\[1em]
\text {1개 날은 3개 수업, 4개 날은 1개 수업} = \binom {5} {1} \binom {6} {3} \binom {6} {1} ^ 4 \\[1em]
\boxed {\frac {\binom {5} {2} \binom {6} {2} ^ 2 \binom {6} {1} ^ 3 + \binom {5} {1} \binom {6} {3} \binom {6} {1} ^ 4} {\binom {30} {7}}} \\[1em]
$$

## 2. Independence

### 1. 

사건이 자기 자신과 독립일 수 있나? 만약 그렇다면 언제 가능한가?

$$
A \cap A = A \\[1em]
P(A \cap A) = P(A) \\[1em]
$$

$A$와 $B$가 독립이라 가정하면 $P(A \cap B) = P(A)P(B)$이 성립한다. \
따라서

$$
P(A) = P(A \cap A) = P(A) ^ 2
$$

이 결론은 $P(A)$가 $0$ 또는 $1$일 경우에만 가능하다.

### 2.

$A$ 와 $B$가 독립이면 $A^c$와 $B^c$도 항상 독립인가? 증명 또는 반례를 보이시오

$$
P(A^c \cap B^c) = 1 - P(A \cup B) \\[1em]
= 1 - P(A) - P(B) + P(A \cap B) \\[1em]
= 1 - P(A) - P(B) + P(A) P(B) \\[1em]
= (1 - P(A))(1 - P(B)) = P(A ^ c) P(B ^ c)
$$

### 3.

3개의 사건이 쌍으로는 독립이지만 서로는 독립은 아닌 예를 드시오.

동전 2개를 던진다고 가정해보자.

$$
\text {첫 번째 동전이 앞면} = A \\[1em]
\text {두 번째 동전이 앞면} = B \\[1em]
\text {두 동전 모두 같은 면} = C \\[1em]
$$

이 사건들은 쌍으로 독립이다. \
$A, B$는 독립이고 \
$A, C$도 아래와 같이 독립이다.

$$
P(A \cap C) = P(A) P(C)
$$

$A, C$가 독립인 것과 같이 $B, C$도 똑같이 독립임을 알 수 있다.

하지만 $A, B, C$는 독립이 아니다.

$$
P(A \cap B \cap C) \ne P(A) P(B) P(C)
$$

$A, B$가 발생하면 당연히 $C$도 발생하기 때문이다.

### 4.

$A, B, C$가 상호 독립이 아니지만 $P(A \cap B \cap C) = P(A) P(B) P(C)$는 성립하는 $A, B, C$ 예시를 보여라. 힌트) 간단한하고 극단적 사례를 보이자.

세 사건이 상호 독립이 되려면 아래 4개의 조건을 모두 만족해야 한다.

$$
P(A \cap B) = P(A) P(B) \\[1em]
P(B \cap C) = P(B) P(C) \\[1em]
P(A \cap C) = P(A) P(C) \\[1em]
P(A \cap B \cap C) = P(A) P(B) P(C) \\[1em]
$$

여기서 $P(A \cap B \cap C) = P(A) P(B) P(C)$만 만족하고 다른 조건 중 적어도 1개 이상 만족하지 않으면 된다.

극단적 예시로 $P(A) = 0$인 경우를 생각해 보자. $P(A \cap B \cap C) = 0 = P(A) P(B) P(C)$이 되고 $B, C$는 서로 독립이 아닌 사례를 들면 된다. 간단히 $B = C$이고 $0 \lt P(B) \lt 1$.

## 3. 조건부

### 1.

주머니 안에 같은 확률로 파랑 또는 초록 구슬이 하나 있고, 초록 구슬이 있다(총 2개의 구슬). 주머니에서 무작위로 구슬 하나를 뽑고 초록 구슬이 나왔다. 이 때 남은 구슬이 초록색인 확률은?

$$
A = \text{공이 초록색으로 설정됨} \\[1em]
B = \text{첫 번째 공이 초록색} \\[1em]
C = \text{두 번째 공이 초록색} \\[1em]
$$

$P(C | B)$를 계산하고 싶다.

$$
\begin{split}
P(C | B) &= P(C | B, A) P(A | B) + P(C | B, A^c) P(A^c | B) \\[1em]
&= 1 \cdot P(A | B) + 0 \cdot P(A^c | B) \\[1em]
&= P(A | B) \\[1em]
\end{split}
$$

$P(A | B)$를 계산하기 위해 베이지안 룰을 사용해보자.

$$
\begin{split}
P(A | B) &= \frac {P(B | A) P(A)} {P(B)} \\[1em]
&= \frac {1/2} {P(B \cap A) + P(B \cap A^c)} \\[1em]
&= \frac {1/2} {P(B | A) P(A) + P(B | A^c) P(A^c)} \\[1em]
&= \frac {1/2} {1/2 + 1/4} \\[1em]
&= \frac {2} {2 + 1} \\[1em]
&= \frac {2} {3} \\[1em]
\end{split}
$$

그래서 $P(C | B) = \boxed {\frac {2} {3}}$

### 2.

스팸 필터는 스팸에 일반적으로 발생하는 문장을 감지하도록 디자인돼 있습니다. 이메일에 80%가 스팸이라고 가정해봅시다. "free money"라는 문장은 스팸 이메일에 10%의 사용하고, 스팸이 아닌 이메일에 1%가 사용합니다. \
새로운 이메일이 방금 도착했고 이메일에 "free money"가 언급됐을 때 스팸일 확률은 얼마나 될까?

$$
A = \text {그 이메일이 스팸} \\[1em]
B = \text {"free money"가 언급됌} \\[1em]
$$

알고 싶은 건 $P(A | B)$

$$
\begin{split}
P(A | B) &= \frac {P(B | A) P(A)} {P(B)} \\[1em]
&= \frac {0.1 \cdot 0.8} {P(B | A)P(A) + P(B | A^c)P(A^C)} \\[1em]
&= \frac {0.08} {0.1 \cdot 0.8 + 0.01 \cdot 0.2} \\[1em]
&= \frac {0.08} {0.08 + 0.002} \\[1em]
&= \frac {80} {80 + 2} = \boxed {\frac {40} {41} \approx 97.56\% } \\[1em]
\end{split}
$$

### 3.

어떤 개인이 어떤 강도 행위를 저질러 유죄 판결을 받는 사건을 $G$라고 하자. \
증거를 수집하면서 $E_1, E_2$ 사건이 발생했다는 게 밝혀졌다.

#### a.

발생한 사건 $E_1, E_2$이 각 $G$의 확률을 높이고 $(\ P(G | E_1) > P(G))$ 그리고 $P(G | E_2) > P(G)\ )$, 같이 발생하면 $G$ 확률이 낮아질 수 있나? $(\ P(G | E_2, E_1) < P(G)\ )$

사건이 오후 1시에서 3시 사이에 발생했다고 가정하자. \
$E_1$은 오후 1시부터 2시까지 사건 발생 지점 근처 카페에 있었던 사건, \
$E_2$은 오후 2시부터 3시까지 사건 발생 지점 근처 카페에 있었던 사건이다.

두 사건 모두 $G$ 사건의 확률을 높인다. $(\ P(G | E_1) > P(G),\ P(G | E_2) > P(G)\ )$ \
하지만 동시에 발생했다면 1시에서 3시 사이에 알리바이가 생기기에 $G$ 사건의 확률을 낮춘다.

#### b.

