import pandas as pd
import numpy as np
series = pd.Series([1,2,3,4,5])
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64
print(series)

series = pd.Series([1,2,3,4,5], index=["a", "b", "c", "d", "c"])
# a    1
# b    2
# c    3
# d    4
# c    5
# dtype: int64
print(series)

print(series[2])
print(series.iloc[2])
print(series["c"])
print(series.loc["c"])
# 3
# c    3
# c    5
# dtype: int64

print(series[2:])   # 2~부터 행 시작
# c    3
# d    4
# c    5
# dtype: int64

print(series.iloc[2:])

dates1 = pd.date_range("20211001", periods=12)
print(dates1)

series = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12])
series.index = dates1
print(series)

print(list("ABCD"))
df = pd.DataFrame(np.random.randn(10, 4), columns=list("ABCD"))
# np.random.randn(m, n): 평균0, 표준편차1의 가우시안 표준정규분포 난수를 matrix array(m,n) 생성
print(df)

df.to_csv("data.csv", index=False)
df = pd.read_csv("data.csv")
days = pd.date_range("20211001", periods=10)
df.index = days
print(df)
print(df.index)
print(df.values)

print(df.describe())
#                A          B          C          D
# count  10.000000  10.000000  10.000000  10.000000
# mean   -0.344508   0.780379   0.180905   0.240138
# std     0.620870   0.847731   0.792800   0.948685
# min    -1.289562  -0.266698  -1.628819  -0.644666
# 25%    -0.771585   0.070761  -0.121060  -0.229310
# 50%    -0.287938   0.772007   0.164266  -0.049328
# 75%    -0.089082   1.221708   0.846309   0.431005
# max     0.950682   2.365403   0.950307   2.648980

print(df.mean(0))   # 열 기준 평균
print(df.mean(1))   # 행 기준 평균
print(df.head())
print(df.tail())

print(df["A"])
print(df.A)

print(df[["A", "B"]]) # 괄호 2개 들어감
print(df[2:4]) 
print(df.iloc[2:4])
print(df[(df.A < 0) & (df.B>0)]) # #check

data = {"name" : ["Janet", "Nad", "Timothy", "June", "Amy"],
        "year" : [2012, 2012, 2013, 2014, 2014],
        "reports" : [6, 13, 14, 1, 7]}

df = pd.DataFrame(data, index=["Singapore", "China", "Japan", "Sweden", "Norway"])
print(df)

schools = np.array(["Cambridge", "Oxford", "Oxford", "Cambridge", "Oxford"])

df["school"] = schools
print(df)

print(df.drop(["China", "Japan"]))  # 행
print(df[df.name != "Nad"]) # 행
print(df.drop("reports", axis=1))   # 열

df = pd.DataFrame(
    {
        "Gender" : ["m", "m", "f", "f", "f"],
        "Team" : [1,2,3,3,1]
    }
)
print(df)

print(pd.crosstab(df.Gender, df.Team)) # 첫 번째 파라미터 : index, 두 번째 파라미터 : column
print(pd.crosstab(df.Team, df.Gender)) # values는 count이다.

print(df["Gender"])






