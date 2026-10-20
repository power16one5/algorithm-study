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
P(A) = P(A | B) \\[1em]
P(B) = P(B | A) \\[2em]
P(A | B) = \frac {P(A \cap B)} {P(B)} \\[1em]
P(B) P(A | B) = P(A \cap B) = P(A) P(B | A)\\[1em]
= P(A)P(B)
$$






