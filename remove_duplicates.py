student_data = {'id1': {'name': 'Kevin'}, 'id1': {'name': 'Kevin'}, 'id2': {'name': "Sam"}, 'id2': {'name': "Sam"}}

result = {}

for key, value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)

