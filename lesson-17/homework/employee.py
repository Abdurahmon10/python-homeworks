import pandas as pd

df=pd.read_csv("employee.csv")

#applying custom functions

def normalise(df):
    mean=df["BASE_SALARY"].mean()
    std=df["BASE_SALARY"].std()
    df["NORMAL_Z"]=(df["BASE_SALARY"]-mean)/std
    return df

df_salary_department=df.groupby("DEPARTMENT").apply(normalise)

print(df_salary_department[["DEPARTMENT","BASE_SALARY","NORMAL_Z"]])
