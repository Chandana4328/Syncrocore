animals=["Lion","Tiger","Cheetha","Elephant"]
b=['a','e','i','o','u']
for i in animals:
    for j in i:
        if j.lower() not in b:
            print(j,end=" ")

'''for i in animals:

        
new_even_list=[]
for i in animals:
    if len(i)%2==0:
        new_even_list.append(i)
print(new_even_list)
repeated_string=[]
for i in new_even_list:
    new=i*len(i)
    repeated_string.append(new)
print("the repeated string",repeated_string)'''


         