#Get data from the user
values = input("Enter data seperated by space: ").split()

#Convert the strings to integers
index = 0
while index < len(values):
    values[index] = int(values[index])
    index += 1

#Menu
print("\nChoose the operations:")
print("1. Mean")
print("2. Median")
print("3. Mode")

choice = input("Enter your choice(1/2/3): ")

#-------------CALCULATE MEAN-------------
def calc_mean(data):
    total = 0
    index = 0
    while index < len(data):
        total += data[index]
        index += 1

    mean = total / len(data)
    return mean   

#-------------CALCULATE MEDIAN------------
def calc_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 != 0:
        median = sorted_data[n // 2]
    else:
        median = (sorted_data[n // 2 - 1] + sorted_data [n // 2]) / 2

    return median

#-------------CALCULATE MODE------------ 
def calc_mode(data):
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
    
    return mode

#---------PROCESS USER CHOICE---------
if choice == "1":
    print("Mean is: ", calc_mean(values))
elif choice == "2":
    print("Median is: ", calc_median(values))
elif choice == "3":
    print("Mode is: ", calc_mode(values))
else:
    print("Invalid Choice!")
