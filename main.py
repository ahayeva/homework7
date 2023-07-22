def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    print(f"Прості числа в діапазоні від {start} до {end}:")
    for number in range(start, end + 1):
        if is_prime(number):
            print(number, end=' ')
    print()
if __name__ == "__main__":
 start_range = int(input("Введіть початок діапазону "))
end_range = int(input("Введіть кінець діапазону "))

  print_primes_in_range(start_range, end_range)
#EXERCISE 2
def print_multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i}*{j} = {i*j}", end=" ")
        print()

print(" множення від 1 до 10:")
print_multiplication_table()
#EXERCISE 3
def print_custom_multiplication_table(start, end):
    for i in range(start, end + 1):
        for j in range(1, 11):
            print(f"{i}*{j} = {i*j}", end=" ")
        print()

start_range = int(input(" початок діапазону: "))
end_range = int(input(" кінець діапазону: "))

print(f"Таблиця множення від {start_range} до {end_range}:")
print_custom_multiplication_table(start_range, end_range)