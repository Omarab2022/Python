

def double(x):
    print(x*2)

double(4)


double = lambda x:x*2
print(double(6))

multiply = lambda x,y:x*y
print(multiply(9,9))

hello = lambda text : print("hello Mr." + text)
hello("omar")

age_check = lambda x : True if x > 18 else False

print(age_check(22))