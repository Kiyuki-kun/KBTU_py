def calculate_running_average(numbers):
    running_average = []
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
        if count == 1:
            running_average.append(number)
        else:
            running_average.append(total / count)
    return running_average

numbers = [1, 2, 3, 4, 5]
print(calculate_running_average(numbers))