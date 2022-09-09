import sys
import clipboard
import json

SAVED_DATA = 'clipboard.json'

def save_items(filepath , data):
    with open(filepath , 'w') as f:
        json.dump(data , f)
        

def read_items(filepath):
    try:
        with open(filepath , 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = read_items(SAVED_DATA)

    if command == 'save':
        key = input('Ennter a key: ')
        data[key] = clipboard.paste()
        save_items(SAVED_DATA , data)
        print('Data Saved')
        
    elif command == 'load':
        key = input('Enter the key to load Data from: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard')
        else:
            print('Key not found')

    elif command == 'list':
        for x , y in data.items():
            print(x,'  ', y)
            
            
    else:
        print("Command  not found")
else:
    print('Please insert an existing command')
    
