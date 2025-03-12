Students_name=[]
Students_Scores=[]
numbers_of_students=int(input("Enter the number of students:"))
for i in range(numbers_of_students):
    names=input("Enter the name of the student")
    scores=int(input("Enter the scores of the student"))
    Students_name.append(names)
    Students_Scores.append(scores)
print("STUDENTS=:",Students_name)
print(" SCORES=:",Students_Scores)
print("STUDENTS AND THEIR SCORES ARE")
for i in range(len(Students_name)):
    print(f"{Students_name[i]}-{Students_Scores[i]}")

total_scores=0
i=0
while(i<len(Students_Scores)):
    total_scores=total_scores+Students_Scores[i]
    i=i+1
print("TOTAL SCORES ARE->",total_scores)
print("AVERAGE=",total_scores/len(Students_Scores))
Upper_CASE=[]
for i in Students_name:
    Upper_CASE.append(i.upper())
print(Upper_CASE)
count=0
for i in Students_Scores:
    if i>75:
        count=count+1
        print(i)
print("The number of students scored above 75 are->",count)
