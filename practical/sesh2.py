number_of_elements = int(input("Enter the number of elements: "))
list_of_elements = []
for i in range(number_of_elements):
    num = int(input("Enter element : "))
    list_of_elements.append(num)
print("List of elements:", list_of_elements)
list_of_elements.sort()
print("the min and max is: ", list_of_elements[0], "and", list_of_elements[-1])


#swap
list1 = [1, 2, 3]
list1[0], list1[-1] = list1[-1], list1[0]
print("List after swapping first and last elements:", list1)


tuple1 = ("math", "java", "python", "physics", "chemistry")
for i in tuple1:
    print(i, end="\n")