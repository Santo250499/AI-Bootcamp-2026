employee = {
    "name": "Tanvir",
    "department": "ICT",
    "device": "Laptop",
    "skills": [
        "Python",
        "Microsoft 365",
        "AI"
    ]
}

print(employee)

print(employee["name"])
print(employee["department"])

for skill in employee["skills"]:
    print(skill)