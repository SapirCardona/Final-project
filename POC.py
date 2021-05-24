




shopping_bag = []

Nike_store = dict(Categories=["Men", "Woman"], Items=["Shirt", "Pants"], Sizes=["S", "M", "L"])
Store_name = "Nike"
Categories = ["Men", "Woman"]
Items = ["Shirt", "Pants"]
Sizes = ["S", "M", "L"]

def add_to_shopping_bag(store_name, category, item, size):
    shopping_bag.append(store_name)
    shopping_bag.append(category)
    shopping_bag.append(item)
    shopping_bag.append(size)

add_to_shopping_bag("nike", "man", "shirt", "M")
print(shopping_bag)
print(Nike_store.values())