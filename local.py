import requests

# res = requests.get('http://127.0.0.1:5000/api/courses/0')
# res = requests.delete('http://127.0.0.1:5000/api/courses/2')
res = requests.put('http://127.0.0.1:5000/api/courses/3', json={'name': 'Unity', 'videos': 11})
# res = requests.post('http://127.0.0.1:5000/api/courses/4', json={'name': 'C++', 'videos': 20})
print(res.json())


