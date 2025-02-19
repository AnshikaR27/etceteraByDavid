students = [
    {"name":"Hermoine", "house":"Gryffindor"},
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Ron", "house":"Gryffindor"},
    {"name":"Draco", "house":"Slytherin"},
]

gryffindor = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]
