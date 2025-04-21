import json
import sys
import readchar
import os

# Define category constants
ALIMENTACAO = "ALIMENTACAO"
MORADIA = "MORADIA"
SUPERMERCADO = "SUPERMERCADO"
FARMACIA = "FARMACIA"
TRANSPORTE = "TRANSPORTE"
LAZER_HOBBY = "LAZER/HOBBY"
JUROS_MULTAS_TAXAS = "JUROS/MULTAS/TAXAS"
SAUDE = "SAÚDE"
FILHOS = "FILHOS"
PRESENTES_DOACOES = "PRESENTES/DOACOES"
PESSOAIS = "PESSOAIS"
VIAGENS = "VIAGENS"
DESCONHECIDO = "DESCONHECIDO"
OUTROS = "OUTROS"

categories = {
    ALIMENTACAO: ALIMENTACAO, #1
    MORADIA: MORADIA, #2 
    SUPERMERCADO: SUPERMERCADO, #3
    FARMACIA: FARMACIA, #4
    TRANSPORTE: TRANSPORTE, #5
    LAZER_HOBBY: LAZER_HOBBY, #q
    JUROS_MULTAS_TAXAS: JUROS_MULTAS_TAXAS, #w
    SAUDE: SAUDE, #e
    FILHOS: FILHOS, #r
    PRESENTES_DOACOES: PRESENTES_DOACOES, #a
    PESSOAIS: PESSOAIS, #s
    VIAGENS: VIAGENS, #d
    DESCONHECIDO: DESCONHECIDO, #f
    OUTROS: OUTROS, #z
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
    print(f"{index+1}/{len(expenses)} | {expense['date']} | {expense['description']} | R$ {expense['price']} | {expense['category']}{category_str}")


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

keymap = {
    '1': categories[ALIMENTACAO],
    '2': categories[MORADIA],
    '3': categories[SUPERMERCADO],
    '4': categories[FARMACIA],
    'q': categories[TRANSPORTE],
    'w': categories[LAZER_HOBBY],
    'e': categories[JUROS_MULTAS_TAXAS],
    'r': categories[SAUDE],
    'a': categories[FILHOS],
    's': categories[PRESENTES_DOACOES],
    'd': categories[PESSOAIS],
    'f': categories[VIAGENS],
    'z': categories[DESCONHECIDO],
    'x': categories[OUTROS],
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
        if index > 0:
            index -= 1
    elif key == readchar.key.DOWN:
        if index < len(expenses) - 1:
            index += 1
    elif key in keymap:
        action = keymap[key]
        if index < len(expenses) - 1:
            index += 1
        if action == "Quit":
            break
        else:
            current_expense['manual_category'] = action
            dirname = os.path.dirname(sys.argv[1])
            filename_without_extension = os.path.splitext(os.path.basename(sys.argv[1]))[0]
            with open(dirname + f"/{filename_without_extension}.json", 'w', encoding='utf-8') as file:
                json.dump(expenses, file, indent=4, ensure_ascii=False)
                print("Categoria salva!")