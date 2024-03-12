
stores =[ ("shirts" ,60),
          ("pants",40),
          ("shoes",30),
          ("bags" ,20),
          ]

to_euros = lambda x:(x[0],x[1]*0.90)

new_store = map(to_euros,stores)

for i in new_store:
    print(i)
