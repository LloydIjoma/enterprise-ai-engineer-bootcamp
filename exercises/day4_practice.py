# 1. Generators
def square_numbers(n):
    for i in range(n):
        yield i * i

for num in square_numbers(5):
    print(num)

# 2. Decorators
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@logger
def greet(name):
    print(f"Hello, {name}!")

greet("Lloyd")

# 3. Type Hints
def project_cost(hours: int, rate: float) -> float:
    return hours * rate

print(project_cost(40, 50.0))

# 4. Dataclasses
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    role: str
    experience: int

emp = Employee("Lloyd", "AI Engineer", 5)
print(emp)
