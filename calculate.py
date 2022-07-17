import sys
first = int(sys.argv[1])
second = int(sys.argv[2])
print(f"{first} + {second} = {first + second }")
print(f"{first} - {second } = {first - second }")
print(f"{first} * {second } = {first * second }")
print(f"{first} / {second } = {first / second }")

# Для запуску потрібно використати команду в терміналі:
# python calculate.py та два аргументи.
# Наприклад, 
# python calculate.py 2 2
# python calculate.py 25 200
# python calculate.py 5 -10
# Перше число - це перший аргумент (first) 
# Друге число - це другий аргумент (second)