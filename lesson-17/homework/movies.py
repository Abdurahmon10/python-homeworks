import pandas as pd

import csv

#merging and joining

df_general=pd.read_csv("movie.csv")

df_color=df_general.filter(items=["director_name","color"])

df_critic=df_general.filter(items=["director_name","num_critic_for_reviews"])

# print(df_color)
# print(df_critic)

df_left=pd.merge(df_color,df_critic,on="director_name",how="left")
df_outer=pd.merge(df_color,df_critic,on="director_name",how="outer")

print(df_left)
print(df_outer)

print(df_left.shape)
print(df_outer.shape)

#multilevel grouping

df_color_director_critic_sum=df_general.groupby(["director_name","color"])["num_critic_for_reviews"].sum().reset_index()
df_color_director_critic_sum.columns=["director_name","color","num_critic_for_reviews_total"]

df_color_director_duration_average=df_general.groupby(["director_name","color"])["duration"].mean().reset_index()
df_color_director_duration_average.columns=["director_name","color","duration_mean"]

print(df_color_director_critic_sum)
print(df_color_director_duration_average)


#applying functions

def how_long(i):
    if(pd.isna(i)):
        return "unknown"

    if(i<60):
        return "short"
    elif i<=120:
        return "medium"
    else:
        return "hard"

df_general["how_long"]=df_general["duration"].apply(how_long)
df_duration=df_general[["movie_title","duration","how_long"]]
print(df_duration)

