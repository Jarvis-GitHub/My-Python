people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should use the cars.")
elif cars < people:
    print("We can't decide.")

if trucks > cars:
    print("This too many trucks.")
elif trucks < cars:
    print("Maybe we could use the trucks.")
else:
    print("We still can't decide.")
