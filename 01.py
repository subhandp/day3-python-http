def Mode(List):
    number = max(set(List), key = List.count) 
    return number

numbers = [1,2,3,4,5,6,6,8,8,6,9]
grades = [87.5, 88.5, 60.5, 90.5, 88.5]

mostNumbers = Mode(numbers)
mostGrades = Mode(grades)

print('mostNumbers',mostNumbers)
print('mostGrades',mostGrades)

