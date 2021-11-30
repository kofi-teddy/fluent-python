# Using json


import json

data = {'name':'Raju', 'subjects':['phy', 'che', 'maths'], 'marks':[50,60,70]}   

#dumps() converts Python object to JSON
json_data = json.dumps(data, indent=2)


#loads() converts JSON string back to Python object
py_data = json.loads(json_data)

print(json_data)
print(py_data)



