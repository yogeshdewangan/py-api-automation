import json
import jsonpath

odics = '{"name":"Yogesh", "age":36}'

json_result= json.loads(odics)

print(json_result["name"])

