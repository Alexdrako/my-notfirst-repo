import json
a=10
b=15

myArray=[4, 4, 8, 3, 3, 3, 2, 4, 4]

# for element in myArray:
#     print(element)
# for i in range(0,3):
#     print(myArray[i])
# suma=sum(myArray)
# print(suma)
#
# сума = sum(число for число in myArray if число != 4)
# print(f"Сума чисел, що не дорівнюють 4: {сума}")

with open("List.json",'r') as json.file:
    data = json.load(json.file)
    for item in data['lists']:
        print(f"{item['id']}, {item['name']}")
