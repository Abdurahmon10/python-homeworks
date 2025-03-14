import pandas as pd

df=pd.read_excel("titanic.xlsx")

#grouping and ggregation

df_pclass_age=df.groupby("Pclass")["Age"].agg("mean")
print(df_pclass_age)

df_pclass_fare=df.groupby("Pclass")["Fare"].agg("sum")
print(df_pclass_fare)

df_pclass_passenger=df.groupby("Pclass")["PassengerId"].agg("count")
print(df_pclass_passenger)


#pipelining

def survival(df):
    df_survived=df.filter(items=["Name","PassengerId","Survived"])[df["Survived"]==1]
    return df_survived

df_survived=df.pipe(survival)
print(df_survived)
print(df_survived.shape)



def nan(df):
    mean_age=df["Age"].mean()
    def filter_nan(x):
        if(pd.isna(x)):
            return mean_age
        else:
            return x
    df["Age"]=df["Age"].apply(filter_nan)
    return df
df=df.pipe(nan)
print(df[["Name","Age"]].head(20))

#apply functions


def is_child(age):
    if(pd.isna(age)):
        return "unknown"
    if(age<18):
        return "child"
    else:
        return "adult"

df["Age_Group"]=df["Age"].apply(is_child)
df_is_child=df[["Name","Age","Age_Group"]]
print(df_is_child)