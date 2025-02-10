universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    student_enrollment=[i[1] for i in universities]
    tuitions=[i[2] for i in universities]
    return student_enrollment,tuitions

def mean(num_list):
    total=sum(num_list)
    return "{:.2f}".format(round(total/len(num_list),2))
def meadian(numlist):
    numlist.sort()
    if(len(numlist)%2==1):
        return numlist[len(numlist)//2]
    return mean([numlist[len(numlist)/2],numlist[len(numlist)/2-1]])

student_num,tuitions=enrollment_stats(universities)


print("******************************")

print("Total students:",sum(student_num))
print("Total tuition: $",sum(tuitions))
print("\nStudent mean:",mean(student_num))
print("Student median:",meadian(student_num))
print("\nTuition mean: $",mean(tuitions))
print("Tuition median: $",meadian(tuitions))

print("******************************")