students = [
    {"name":"Hermoine", "house":"Gryffindor"},
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Ron", "house":"Gryffindor"},
    {"name":"Draco", "house":"Slytherin"},
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

# isme we have used a filter func; aur joh filter func hai uska first arg should be true ya false aur yeh arg iss case me jaa raha hai from the is_gryffindor func, and the second has to be an iterable. and isme it would return only the true waale outcomes
gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key= lamda s : s["name"]):
    print(gryffindor["name"])


