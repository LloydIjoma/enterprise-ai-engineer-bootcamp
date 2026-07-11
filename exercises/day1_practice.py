# Day 1 - Python Practice
# Enterprise AI Engineer Bootcamp

# =========================
# 1. Variables
# =========================
name = "Lloyd"
age = 30
salary = 5000.0
print(name, age, salary)

# =========================
# 2. Strings
# =========================
greeting = f"Hello, {name}!"
print(greeting.upper())
print(greeting.lower())
print(greeting[0:5])  # slicing

# =========================
# 3. Lists
# =========================
tools = ["TensorFlow", "PyTorch", "Scikit-learn"]
tools.append("Keras")
print(tools)
tools.remove("Scikit-learn")
print(tools)

# =========================
# 4. Tuples
# =========================
coordinates = (10, 20)
x, y = coordinates
print(f"x={x}, y={y}")

# =========================
# 5. Sets
# =========================
ai_set = {"Python", "TensorFlow", "PyTorch"}
ml_set = {"Python", "Scikit-learn", "PyTorch"}
print(ai_set.intersection(ml_set))
print(ai_set.union(ml_set))

# =========================
# 6. Dictionaries
# =========================
employee = {"name": "Lloyd", "role": "AI Engineer", "experience": 5}
print(employee["role"])
employee["experience"] = 6
print(employee)

# =========================
# 7. Loops
# =========================
projects = ["CCTV Deployment", "Cloud Migration", "Safe City"]
for project in projects:
    print(f"Project: {project}")

# =========================
# 8. Functions
# =========================
def project_cost(hours, rate):
    return hours * rate

print(project_cost(40, 50))
