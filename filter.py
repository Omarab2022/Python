freinds =[ ("nancy",19),
           ("omar",20),
           ("anas",21),
           ("jamal",22),
           ("wassim",23),
           ("youssef",24),
           ("wiam",25),
           ("brahim",26)]

age = lambda x:x[1] >= 22

new_freind = filter(age,freinds)

for i in new_freind:
    print(i)


