number = int(input())
if number % 2 != 0:
    print("Weird")
if number % 2 == 0 and number in range(2, 6):
    print("Not Weird")
if number % 2 == 0 and number in range(6, 21):
    print("Weird")
if number % 2 == 0 and number > 20:
    print("Not Weird")
