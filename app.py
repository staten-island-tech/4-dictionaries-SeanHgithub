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
total = 0
cart = []
for index, item in enumerate(items):
    print(index, ":", item["name"])
y = input("what do you want?")
cart.append(y)
total += [items][y]["price"]
z = input("anything else?")
while z == "yes":
    y = input("what do you want?")
    cart.append(y)
    total += [items][y]["price"]
    z = input("anything else?")
    break
print(cart, total)

    
