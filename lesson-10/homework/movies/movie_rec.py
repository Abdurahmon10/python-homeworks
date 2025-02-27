import requests

import os
import random


url="https://api.themoviedb.org/3/"

api_key=os.getenv("MOV_API_KEY")
token=os.getenv("MOV_TOKEN")

# print(token,api_key)



headers={
    "accept":"application/json",
    "Authorization": f"Bearer {token}"
}

genres=requests.get(url+'genre/movie/list?language=en',headers=headers).json()['genres']

# print(genres)

g=input("Input a genre that you want to watch:\n")

g=g.lower()

g_idl=[i["id"] for i in genres if i["name"].lower()==g]
if not(g_idl):
    print("genre not found")
    exit(0)
g_id=g_idl[0]


movies=requests.get(url+f"discover/movie?with_genres={g_id}",headers=headers).json()



movie=random.choice(movies["results"])



print("Title in eng: ",movie["title"])
print("Original title: ",movie["original_title"])
print("Overview: ",movie["overview"])
if(movie["adult"]):
    print("18+")
else:
    print("for everyone")

#print(movie)