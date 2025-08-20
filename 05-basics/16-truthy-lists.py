inventory = ["Sword", None, None]
# inventory = ["Sword", "Shield", "Gold"]
# inventory = [None, None, None]

if all(inventory):
    print("The inventory is full! :3")
elif any(inventory):
    print("Okay, the inventory has some items")
else:
    print("Uh oh.. the inventory is empty :/")
