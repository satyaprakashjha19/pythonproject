import sys
import json
import clipboard

def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_items(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
        return data



if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        
    elif command == "load":
        print("load")
    elif command == "list":
        print("list")
    else:
        print("unknown command")
else:
    print("please pass exatly one command.")