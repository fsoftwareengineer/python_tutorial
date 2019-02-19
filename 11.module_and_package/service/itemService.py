items = []


class Item:
    id = ""
    name = ""


def insert_item(item_id, item_name):
    item = Item()
    item.id = item_id
    item.name = item_name
    items.append(item)


def print_items():
    for item in items:
        print("[" + item.id + "] " + item.name)
