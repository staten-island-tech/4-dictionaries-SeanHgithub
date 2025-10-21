items = [
{
"name": "banana",
"price": 0.55,
"department": "fruit"},
{
"name": "apple",
"price": 0.50,
"department": "fruit"},
{
"name": "Table",
"price": 150,
"department": "Furniture"},
{
"name": "Couch",
"price": 1500,
"department": "Furniture"},
{
"name": "Salmon",
"price": 8,
"department": "Meat"},
{
"name": "Steak",
"price": 10,
"department": "Meat"},
{
"name": "Keyboard",
"price": 50,
"department": "Technology"},
{
"name": "PS5 Controller",
"price": 75,
"department": "Technology"},
    
]
cart = []
total = 0
for index, item in enumerate(items):
    print(index, ":", item["name"])
y = input("what do you want?")
for item in items:
    if item["name"] == y:
        cart.append(y)
        total += item["price"]
        break
z = input("anything else?")
while z == "yes":
    y = input("what do you want?")
    for item in items:
        if item["name"] == y:
            cart.append(y)
            total += item["price"]
            break
    z = input("anything else?")

print(cart)
print(total)




    
