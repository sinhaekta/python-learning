def greet(name):
    return f"Hello, {name}!"    

result = greet("Alice")
print(result)
# o/p: Hello, Alice!    


def add(a, b):
    return a + b

sum_result = add(5, 3)
print("Sum:", sum_result)
# o/p: Sum: 8


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 

fact_result = factorial(5)
print("Factorial:", fact_result)
# o/p: Factorial: 120


def check_cpu(cpu_percent):
    if cpu_percent > 80:
        return "High CPU Usage"
    elif cpu_percent > 50:
        return "Moderate CPU Usage"
    else:
        return "Normal CPU Usage"

status = check_cpu(75)
print("CPU Status:", status)
# o/p: CPU Status: Moderate CPU Usage