# 1 задание
cook_book = {}
with open('1.txt', 'r', encoding='utf-8') as m:
        dish_name = None
        for n in m:
            n = n.strip()
            if n:
                if dish_name is None:
                    dish_name = n
                    cook_book[dish_name] = []
                else:
                    try:
                        quantiti = int(n)
                        for _ in range(quantiti):
                            ingredient_line = next(m).strip()
                            ingredient_name, quantity, measure = ingredient_line.split(' | ')
                            cook_book[dish_name].append({
                                'ingredient_name': ingredient_name,
                                'quantity': int(quantity),
                                'measure': measure
                            })
                    except ValueError:
                        print(f"Ошибка при обработке строки: {n}")
                    dish_name = None
for dish, ingredients in cook_book.items():
        print(f"{dish}:")
        for ingredient in ingredients:
            print(f"  {ingredient}")


# 2 задание
cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
}

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}

    return shop_list

dishes_to_prepare = ['Омлет',]
person_count = 2
shopping_list = get_shop_list_by_dishes(dishes_to_prepare, person_count)
print(shopping_list)

# 3 задание
import os
def merge_files(file_list, output_file):
    file_info = []
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.readlines()
            line_count = len(content)
            file_info.append((file, line_count, content))
    file_info.sort(key=lambda x: x[1])
    with open(output_file, 'w', encoding='utf-8') as out_f:
        for file_name, line_count, content in file_info:
            out_f.write(f"{file_name}\n{line_count}\n")
            out_f.writelines(content)
files_to_merge = ['2.txt', '3.txt', '4.txt']
output_file_name = '5.txt'
merge_files(files_to_merge, output_file_name)