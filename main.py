import json
import sys
import readchar
import os

categories = {
    "SUPERMERCADO": "SUPERMERCADO", #1
    "ALIMENTACAO": "ALIMENTACAO", #2
    "SAUDE": "SAUDE", #3
    "ARTHUR": "ARTHUR", #4
    "ASSINATURAS": "ASSINATURAS", #5
    "HOBBY": "HOBBY", #q
    "CACHORROS": "CACHORROS", #w
    "PRESENTES": "PRESENTES", #e
    "DESCONHECIDO": "DESCONHECIDO", #r
    "TRANSPORTE": "TRANSPORTE", #a
    "CASA": "CASA", #s
    "VIAGEM": "VIAGEM", #d
    "TAXAS": "TAXAS", #f
    "OUTROS": "OUTROS", #z
}

def open_json_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at path: {path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file: {path}")
        return None


def print_expense(index, expense):
    print("=" * 100)
    category_str = f" | \033[32m{expense['manual_category']}\033[0m" if 'manual_category' in expense else ""
    print(f"{index+1}/{len(expenses)} | {expense['date']} | {expense['description']} | R$ {expense['price']}{category_str}")


def print_categories_prompt(selected_category):
    print(" ")
    print("\033[1m💰 Defina a categoria da despesa pressionando uma tecla:\033[0m")
    for key, value in keymap.items():
        if selected_category == value:
            print(f"[{key}] ✅ {value}")
        else:
            print(f"[{key}] {value}")
    print(" ")

expenses = open_json_file(sys.argv[1])
# Define your custom key mappings here
keymap = {
    '1': categories["SUPERMERCADO"],
    '2': categories["ALIMENTACAO"], 
    '3': categories["SAUDE"],
    '4': categories["ARTHUR"],
    'q': categories["ASSINATURAS"],
    'w': categories["HOBBY"],
    'e': categories["CACHORROS"],
    'r': categories["PRESENTES"], 
    'a': categories["DESCONHECIDO"],
    's': categories["TRANSPORTE"],
    'd': categories["CASA"],
    'f': categories["VIAGEM"],
    'z': categories["TAXAS"],
    'x': categories["OUTROS"],
    '/': "Quit"
}

index = 0
invalid_key = False
while True:
    print("\033c", end="")
    current_expense = expenses[index]
    for i in range(max(0, index-4), index):
        print_expense(i, expenses[i])
    print_expense(index, current_expense)
    print("-" * 100)
    print_categories_prompt(current_expense.get('manual_category', None))
    for i in range(index+1, min(index+5, len(expenses))):
        print_expense(i, expenses[i])
    key = readchar.readkey()

    if key == readchar.key.UP:
        index -= 1
    elif key == readchar.key.DOWN:
        index += 1
    elif key in keymap:
        action = keymap[key]
        index += 1
        if action == "Quit":
            break
        else:
            current_expense['manual_category'] = action
            dirname = os.path.dirname(sys.argv[1])
            with open(dirname + "/expenses.json", 'w', encoding='utf-8') as file:
                json.dump(expenses, file, indent=4, ensure_ascii=False)
                print("SAVED! ")