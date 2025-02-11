import re

try:
    sample=open("sample.txt","r")
    sample.close()
except FileNotFoundError:
    sample=open("sample.txt","a")
    content_sample=input("Enter the something:\n")
    sample.write(content_sample)
    sample.close()


sample=open("sample.txt","r")

sample_content=sample.read()


list_words=re.split(r'[,\s\-_!?.]+',sample_content)

word_frequency=dict()

for i in list_words:
    i.lower()
    try:
        word_frequency[i]+=1
    except KeyError:
        word_frequency[i]=1

word_frequency=dict(sorted(word_frequency.items(), key=lambda item: item[1],reverse=True))
word_frequency.pop("")

top_words=int(input("Input the number of most frequent words you want to see in this document:\n"))
top_words=min(top_words,len(word_frequency.keys()))

print("Total number of words:",len(word_frequency.keys()))
print("Top",top_words,"most commong words:")
for words, count in word_frequency.items():
    if(count==1):
        print(words,"-",count,"time")
    else:
        print(words,"-",count,"times")
    top_words-=1
    if top_words==0:
        break

sample.close()

top_words=min(5,len(word_frequency.keys()))
word_count_report=open("word_cout_report.txt","w")
word_count_report.write("Word Count Report\nTotal Words: "+str(len(word_frequency.keys()))+"\n")
word_count_report.write("Top "+str(top_words)+" words:\n")
for words, count in word_frequency.items():
    if(count==1):
        word_count_report.write(words+" - "+str(count)+"\n")
    else:
        word_count_report.write(words+" - "+str(count)+"\n")
    top_words-=1
    if top_words==0:
        break
word_count_report.close()
word_count_report=open("word_cout_report.txt","r")
print(word_count_report.read())
word_count_report.close()