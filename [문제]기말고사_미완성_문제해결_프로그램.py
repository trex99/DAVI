# -*- coding: utf-8 -*-
"""[문제]기말고사_미완성_문제해결_프로그램.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OxyfMrXMaGEl7o-0ei_6870M0jqb_iBl

# 👍 [문제]기말고사 - 미완성 문제해결 프로그램

## [시험문제]
- 주석의 안내에 따라 미완성 프로그램을 완성하고, 기말고사 시험문제의 질문에 답하세요.

## [문제상황 - 해결할 문제 정의]

- 경상남도 밀양시 지역의 주택가격을 예측하는 모델을 만들기 위하여 데이터를 분석하고자 한다.
- 모델생성은 설명 가능한 회귀분석 방법을 이용할 예정이며, 분석과정 중간에 시각화를 진행하려고 한다.
- 이러한 과정을 수행하는 분석 프로그램을 완성하세요.

- 사용데이터 : 학기 중 실습코드와 함께 제공되는 data 폴더에 있는 houseprice.csv 파일

- 데이터 컬럼 설명
  - price : 주택가격
  - tax	: 세금
  - ground : 대지 평수
  - floor : 건물 평수
  - year : 건축 경과 년도

## [분석 프로그램]

### 필수 패키지 로드

#### <font color=red>[문제 - 1]</font>
#### 전체 프로그램이 문제없이 실행되기 위해 필요한 필수 패키지를 import 하세요. 
#### import 하는 패키지의 갯수 제한은 없지만, 필수가 아닌 패키지를 import하는 경우 하나 당 -0.1점이 감점됩니다.
"""

import ?
import ?
import ?
 ...
 ...
 ...
import ?

"""### 데이터 로드"""

# 파일 데이터 로드
data = pd.read_csv('houseprice.csv')

data

"""#### <font color=red>[문제 - 2]</font>
#### 데이터 컬럼명, 자료구조, Null 갯수, 데이타 타입 등을 볼 수 있도록 Cell 을 완성하세요.
"""

# 데이터 컬럼명, 자료구조, Null 갯수, 데이타 타입
?

# 상위 10개 데이터 출력
data.head(10)

# 데이터 구조(dimension, 크기, 길이) 확인
data.shape

"""### 데이터 분석

#### <font color=red>[문제 - 3]</font>
#### 각 변수의 기초 통계량을 볼 수 있는 프로그램 코드는 무엇인가 ? tax의 표준편차는 ground 표준편차보다 얼마나 큰가 ?
#### (결과 예시와 동일하게 출력하는 코드로 작성할 것)
"""

# 기초 통계량 확인
?

"""- 결과 예시

![image.png](data:image/png;base64,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)

#### <font color=red>[문제 - 4]</font>
#### 각 변수의 결측치를 확인하는 프로그램 코드는 무엇인가 ? price와 결측치와 floor의 결측치 합은 얼마인가 ?
#### (결과 예시와 동일하게 출력하는 코드로 작성할 것)
"""

# 결측치 확인
?

"""- 결과 예시

![image.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAABqCAYAAAB04VkvAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAQ0SURBVHhe7ZsBbuQgDEW7e6rep+fqWXdlqV/66zVMMhNjJv5PQkkwkIA/DqTTX5+fn38+RFt+/xxFU7aNAN/f3x9fX18/V/fC+sZU9lMRYDEQNicviJVsK4DKWdGJNAFA1XaMFH7UHoE6vgzne5uISY0A5oRZmGP7UbgOt+vz2SbGpArAnAAih7D9CHAyc7YN8S+3WgSaQDiJx9xKABYNfBJzbiUAcZ70RSCw81dnpNX3oX0W6vUaeEzal0A4HE7wzod9xMzOjuUynG/M2q9kp+dMF4DYG/01sDlaBDZHAmiOBNAcCaA5EkBztAsooMV3AEPfAv4nGpPKcdIroDlpAkCYsyPOGeR726isyCFNAAhpdhyFPCR2sL9GWZFDyStADt2HsjWAzWwkD6KAZn8+JQKAY5FEHWURYAYLJIoQ4jrKBSAH15L+JRAO9qGe8/15VNbnvTPoL6jsmz4FN2fLNYBYhwTQHAmgORJAcySA5rTdBVRuLXfaBioCLAbC4+QFsRIJoDnpAjB1Q+GsdM7jfBDlj8rhyCliZutKqgBssGdhju3Mo3ojUCeq92ybdydNABhwwOcgyovqveqwI8/SFa0BmiMBNCdNAD50vxrGRQ6pEQAi8O/gGZFwRnWPikpiHJO6CDRs8I86H8Bhlrgu53vbI0Ztrsb3ofp50v81jKnsqIjRL4Kao11AcySA5kgAzZEAmrNkEYjdgN8FVG+Bqthpd5QugJmTOwog6nPlOOgV0JxUASDU2RHnR5nVGdmQN6sr/iVVAAhrdjwT4sx5qOMdObMZbBeP2e4VAAcCdvTMBuT4c2gN0BwJoDkSQHO2E4B/r/N7f2YTz7HthyA4OrKPbO8iCDw/qHxm/R6gOVoDNEcCaI4E0BwJoDkSQHMkgOZoG1iAvgM0JvpYVfkBS6+A5qQJwIc5g/PsnBMzyjeQN7KLc5REAHOchTxO7Ngon+Ey4jXSBOCdB6c94qoy4hhlawATBCdmlC+uZ4kAzJF+1tq1TwbKcp7II1UA5kDN4r1ZEgGOzORIKBJPPmW/CPLO5TKwcQSBfdTeOzHr+2rSBOAdJ/ZEn4KbU7YNFHsgATRHAmiOBNCcpQLw25934erntvY4jbj6vhFlEWBF5yoZ9c/ybWvMKSq7anxavQKeHdTsbxnZ7c9IF4ANuh94XM9sDJfHcVSO01WcvReuI9sRrM4qUaQKAB3xYQ6dg+0MozY5P7Iblnclo3vhPrB5rCynStIEYB3jzkcDEWHleFBm7fiy74I9N6dZf7O51RrABo+TeMzWAjg7G3hWITG7i+Jsf69gSwHYIHSdwdZvJFxnkiYA78RnOhLNBt/mbMb4e66eXWex5+OEvExSI4A9vDkhchTbzjBqk/Mj+2pG/dvtObf7PQAGLBqU6sG6I/pBSHNutQ0U55EAmiMBNEcCaM3Hx1/VF1R5r+bLPQAAAABJRU5ErkJggg==)

#### <font color=red>[문제 - 5]</font>
#### boxplot에서 5개 변수 중 몇 개의 변수에 이상치가 있다고 생각할 수 있는가 ?
"""

# boxplot을 그려서 이상치 확인
?

"""#### <font color=red>[문제 - 6]</font>
#### floor와 price 변수간의 상관관계를 해석(설명)하세요.

"""

# 수치형 변수간의 상관계수 확인
data.corr()

# 수치형 변수간의 상관계수 시각화
sns.heatmap(data=data.corr(), annot=True)
plt.show()

"""## 상관계수 해석
- 상관계수는 상관분석에서 두 변수간의 선형적 관계를 –1에서 1 사이의 값으로 나타냅니다.
- 선형적 관계가 1에 가까우면 양의 상관관계, -1에 가까우면 음의 상관관계를 갖는다고 합니다. 0이면 관계가 없다고 합니다.
- 위의 상관계수 매트릭을 보면 price와 tax 간의 선형적 관계를 보면 상관계수가 0.915249이며 강한 양의 상관관계가 있다고 할 수 있습니다.
- 또한 floor와 year간의 선형적 관계를 보면 상관계수가 -0.178057이며 아주 약한 음의 상관관계가 있다고 할 수 있습니다.
"""

# price 와 tax 관계 확인
sns.scatterplot(data=data, x='tax', y='price')
plt.show()

# price 와 tax 상관계수 확인
print('')
print('상관계수 : ', data[['tax', 'price']].corr().values[0][1])

# 세금은 대지 평수와 선형적인지 분석결과를 설명
sns.scatterplot(data=data, x='ground', y='tax')
plt.show()

# 층수와 건축 경과 년도는 선형적인지 분석결과를 설명
sns.scatterplot(data=data, x='floor', y='year')
plt.show()

"""#### <font color=red>[문제 - 7]</font>
#### 출력 결과를 동일하게 재현할 수 있는 프로그램 코드를 완성하세요.
#### 정규분포로 변환하는 프로그램을 완성하는 것입니다.

"""

# 회귀분석은 정규 분포 가정한다.
# 정규분포로 변환하기 전/후를 하나의 figure에 출력
from sklearn.preprocessing import PowerTransformer, StandardScaler

# figure 준비
fig, ax = plt.subplots(nrows=1, ncols=2)

# 전
sns.kdeplot(data=data['price'], ax=ax[0])

# 후
scaler = ?
t = ?
sns.kdeplot(data=t, ax=ax[1])

plt.show()

# z-score 계산
score_price_original = data.price.values
score_price_mean = np.mean(score_price_original)
score_price_std = np.std(score_price_original)

print('평균 : ', score_price_mean)
print('표준편차 : ', score_price_std)
print('')

# 표준점수화한 데이터 (평균에서의 떨어진 정도)
z_score_price = (score_price_original - score_price_mean) / score_price_std
print('표준점수 합계 : ', z_score_price.sum())
print('표준점수 평균 : ', z_score_price.mean())
print('표준점수 표준편차 : ', z_score_price.std())

sns.lineplot(z_score_price)
plt.show()

# price 데이터에 대한 추정
# 점 추정 : 표본 평균
p_mean = data.price.mean()
print('표본평균 : ', p_mean)

# ground 데이터에 대한 구간 추정 : 표본 평균에 대한 신뢰구간
from statsmodels.stats import weightstats

stat = weightstats.DescrStatsW(data.ground)
s_result = stat.tconfint_mean(alpha=0.05)
print('95% 신뢰구간 : ', s_result)

# ground 데이터에 대해 barplot으로 95% 신뢰구간을 표시하여 검증
myplot = sns.barplot(data=data, y='ground', errorbar=('ci', 95))
myplot.axhline(s_result[1])
plt.show()

# 기초 통계량 확인
# 데이터 갯수, 평균, 분산, 표준편차, 최대값, 최소값, 중앙값
len(data.price), data.price.mean(), data.price.var(), data.price.std(), data.price.max(), data.price.min(), data.price.median()

len(data.tax), data.tax.mean(), data.tax.var(), data.tax.std(), data.tax.max(), data.tax.min(), data.tax.median()

len(data.ground), data.ground.mean(), data.ground.var(), data.ground.std(), data.ground.max(), data.ground.min(), data.ground.median()

len(data.floor), data.floor.mean(), data.floor.var(), data.floor.std(), data.floor.max(), data.floor.min(), data.floor.median()

len(data.year), data.year.mean(), data.year.var(), data.year.std(), data.year.max(), data.year.min(), data.year.median()

"""### 모델링

#### <font color=red>[문제 - 8]</font>
#### 출력 결과를 동일하게 재현할 수 있는 프로그램 코드를 완성하세요.
#### 회귀분석 프로그램을 완성하는 것입니다.
"""

# 회귀분석
?
?

res.summary()

"""## [분석결과의 해석]

#### <font color=red>[문제 - 9]</font>
#### 분석결과에 대한 모형적합도를 Adj.R-squared로 설명하세요.

#### <font color=red>[문제 - 10]</font>
#### 분석결과에서 회귀계수 tax에 대해 설명하세요.

#### <font color=red>[문제 - 11]</font>
#### 분석결과를 보고 회귀식을 작성하세요.

# End Of Program

### 이번 학기 수고 많이 하셨습니다. 
### 여러분을 만나서 행복한 한 학기를 보냈습니다. 
### 모두 건강하기 바라며, 소원하는 바 모든 것이 이루어길 바랍니다.
"""