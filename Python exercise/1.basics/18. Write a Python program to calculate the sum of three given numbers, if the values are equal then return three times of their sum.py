numbers = list()
print("enter 3 numbers---------------|")
for num in range(3):
    numbers.append(float(input("enter a number: ")))
if numbers[0] == numbers[1] == numbers[2]:
    print(sum(numbers) * 3)
else:
    print(sum(numbers))
