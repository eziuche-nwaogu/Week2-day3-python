ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")
stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(
        next_one
    )  # This expression could be written as append(stuff, next_one)
    print(f"There are {len(stuff)} items now.")
print("There we go: ", stuff)
print("Let's do some things with stuff.")
print(stuff[1])
print(stuff[-1])  # whoa! fancy
print(stuff.pop())
print(" ".join(stuff))  # This could be written as join(' ', stuff)
print(
    "#".join(stuff[3:5])
)  # This expression could also be written as join('#', stuff[3: 5])
print(", ".join(stuff))  # WE can aso do seperate the individual words and add a comma
print(f'The items on the list are: {", ".join(stuff)}')  # This will also work
