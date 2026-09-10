fruits = ["apple","banana","grapes"]
vegetables =["carrot","brinjal","cabbage"]
beverages =["mrinda","pepsi","mountdew"]
fruits.append("strawberry")
print(fruits)
vegetables.insert(1,"onion")
print(vegetables)
beverages.pop()
print(beverages)
inventory = [fruits,vegetables, beverages]
print(inventory)
print(fruits[:2])
print(vegetables[-1])
length = [len(x) for x in fruits]
print(length)
print("Water" in beverages)
tup=(fruits[0],vegetables[0],beverages[0])
print(tup)

