#Get data from the user
data = input("Enter data seperated by space: ").split()

#Convert the strings to integers
index = 0
while index < len(data):
    data[index] = int(data[index])
    index += 1

#Menu
print("\nChoose the operations:")
print("1. Mean")
print("2. Median")
print("3. Mode")

choice = input("Enter your choice(1/2/3): ")

#-------------CALCULATE MEAN-------------
if choice == "1":
    total = 0
    index = 0
    while index < len(data):
        total += data[index]
        index += 1

    mean = total / len(data)
    print("Mean is: ",mean)
    
#-------------CALCULATE MEDIAN------------
elif choice == "2":
    data.sort()
    n = len(data)

    if n % 2 != 0:
        median = data[n // 2]
    else:
        median = (data[n // 2 - 1] + data [n // 2]) / 2

    print("Median is: ",median)  

#-------------CALCULATE MODE------------ 
elif choice == "3":
    frequency = {}

    index = 0
    while index < len(data):
        num = data[index] 

        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

        index += 1

    # find max frequency
    max_count = 0
    mode = None

    for key in frequency:
        if frequency[key] > max_count:
            max_count = frequency[key]
            mode = key
    
    print("Mode is: ",mode)

#---------INVALID CASE---------
else:
    print("Invalid Choice!")
