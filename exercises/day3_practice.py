# from utilities import string_utils, file_utils
# import math_utils
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# main.py
import math_utils
print(math_utils.add(2, 3))
print(math_utils.multiply(4, 5))

# 2. Packages
# utilities/string_utils.py
def to_upper(text):
    return text.upper()

# utilities/file_utils.py
def save_text(filename, content):
    with open(filename, "w") as f:
        f.write(content)

# main.py
from utilities import string_utils, file_utils
print(string_utils.to_upper("hello"))
file_utils.save_text("sample.txt", "Enterprise AI Bootcamp")

# 3. JSON
import json
employee = {"name": "Lloyd", "role": "AI Engineer", "experience": 5}
with open("employee.json", "w") as f:
    json.dump(employee, f)

with open("employee.json", "r") as f:
    data = json.load(f)
    print(data)

# 4. API Requests
import requests
response = requests.get("https://api.github.com/users/LloydIjoma")
if response.status_code == 200:
    user_data = response.json()
    print(user_data["login"], user_data["public_repos"])
else:
    print("API request failed")
