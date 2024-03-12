
students = ["omar","anas","jamal","wassim","youssef","wiam","brahim"]

students.sort(reverse=True)

for i in students:
    print(i)

students2 = [("omar","A",50),
             ("anas","C",35),
             ("jamal","B",40),
             ("wassim","A",45),
             ("youssef","B",30),
             ("wiam","A",35),
             ("brahim","B",40)]

grade = lambda grades:grades[1]

students2.sort(key=grade)
for i in students2:
    print(i)