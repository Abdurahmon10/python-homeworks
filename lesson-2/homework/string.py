# #1
# name=input()
# by=int(input())
# print(name,", your age is:",2025-by)

# #2

# s = 'LMaasleitbtui'

# print(s[::2])
# print(s[1::2])

# #3
# s=input()
# print(s.len())
# print(s.upper())
# print(s.lower())

# #4
# s=input()
# ss=s[::-1]
# print(ss)

# #5
# s=input()
# vovel=0
# consonant=0
# for i in s:
#     if i in "aeiou":
#         vovel+=1
#     elif i in "qwrtypsdfghjklzxcvbnm":
#         consonant+=1
# print("vovel: ",vovel,"consonant :",consonant)

# #6
# s=input()
# ss=input()
# if(s in ss):
#     print(s,"is in",ss)
# if(ss in s):
#     print(ss,"is in",s)

# #7

# sentence=input()
# replaced=input()
# replacer=input()

# sentence.replace(replaced,replacer)

# print(sentence)

# #8
# s=input()
# print(s[0:0])
# print(s[s.len():s.len()])

# #9
# s=input()
# print(s[::-1])

# #10
# s=input()
# print(s.count(" ")+1)

# #11
# s=input()
# print(any(1 for i in s if i in '1234567890'))

# #12
# print(','.join([input().split()]))

# #13
# print(input().replace(" ",""))

# #14
# s=input()
# ss=input()
# if(s==ss):
#     print("they are equal.")
# else:
#     print("they are not equal.")

# #15
# s="".join(i[0].upper() for i in [input().split()])
# print(s)


# #16
# s=input()
# ch=(input())
# print(s.replace(ch,""))

#17
s=input()
print("".join('*' if i.lower() in  "aoiue" else i for i in s))

#18
sentence=input()
start=input()
ends=input()
if(sentence.startswith(start) and sentence.endswith(ends)):
    print(" the given sentence starts and ends with the given words.")
else:
    print(" the given sentence does not start and ends with the given words.")


