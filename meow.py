def meow(n: int):
    for _ in range(n):
        print("meow")


# yeh apne aisa hints de sakte hai variable_name:datatype_youwanttostore
# aur isko pahele run karenge using mypy nameofthefile toh apne ko pata chalega errors and all.
number: int = int(input("Number: "))
meow(number)
