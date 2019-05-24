# My solution to the practise problem in https://automatetheboringstuff.com/chapter5/

def displayInventory(Inventory):
    displayString = "Inventory:\n"
    displayString += "\n".join([str(Inventory[x]) + " " + x for x in Inventory.keys()])
    displayString += "\n\nTotal number of items: " + str(sum(Inventory.values()))
    print(displayString)

def addToInventory(inventory, addedItems):
    # The line below should work but doesn't TODO: Learn why
    #uniqueItems = {x: addedItems.count(x) if x not in inventory.keys() else x: inventory[x] + addedItems.count(x) for x in addedItems}
    uniqueItems = dict([(x, addedItems.count(x)) if x not in inventory.keys() else (x, inventory[x] + addedItems.count(x)) for x in addedItems])
    return {**inventory, **uniqueItems}


if __name__ == "__main__":
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)
