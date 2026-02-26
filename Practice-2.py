#Create a program that counts the distinct words in a given text.

lines = int(input("Enter the number of lines: "))

setA = set()
for i in range(lines):
    setB = set(input(f"Enter the line {i + 1}: ").split())
    setA.update(setB)

print("The number of distinct words in the set is", len(setA))