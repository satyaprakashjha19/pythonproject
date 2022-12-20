import sys
import json
import clipboard

SAVED_DATA = "clipboard"


def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return{}



if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("enter a key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
        
    elif command == "load":
        key = input("enter a key:")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("key does not exist.")
        
    elif command == "list":
        print("data")
    else:
        print("unknown command")
else:
    print("please pass exatly one command.")