squares =[]

for i in range(1,11):
    squares.append(i*i)

print(squares)

squares2 =[ i * i for i in range(1,11)]

print(squares2)

students =[10,30,50,60,70,80,90,100]

plus_50 = list(filter(lambda  x : x >30 , students))

print(plus_50)


passed_students = [i if i>40 else "failed" for i in students]
print(passed_students)
