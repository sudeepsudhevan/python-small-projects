with open("file1.txt") as file1:
    list_one = file1.readlines()
with open("file2.txt") as file2:
    list_two = file2.readlines()    

result = [int(data) for data in list_one if data in list_two]

# Write your code above 👆

print(result)


