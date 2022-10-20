import pprint
cook_book = {}
with open ('recipes.txt', encoding='utf-8') as file:
    for str in file:
        dish = str.strip()
        compaund = []
        ingredient_count = file.readline()
        for i in range(int(ingredient_count)):
            ing = file.readline()
            name, amount, extent = ing.strip().split(' | ')
            compaund.append({'ingredient_name': name, 'quantity': amount, 'mesuare': extent})
        divide_line = file.readline()
        cook_book[dish] = compaund
pprint.pprint(cook_book)
print ()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for comp in cook_book[dish]:
                ingr_name = comp['ingredient_name']
                mes = comp['mesuare']
                quan = int(comp['quantity']) * person_count
                if ingr_name in shop_list_by_dishes.keys():
                    shop_list_by_dishes[ingr_name]['quantity'] += quan
                else:
                    shop_list_by_dishes[ingr_name] = {'mesuare': mes, 'quantity': quan}
        else:
            print(f'Блюда {dish} нет')
    return shop_list_by_dishes

pprint.pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))


file_name = ['1.txt', '2.txt', '3.txt']
all_text = {}
for file_n in file_name:
    with open (file_n, encoding='utf-8') as comp:
        text = comp.readlines()
        text_new = ''.join(text)
        len_f = len(text)
        all_text[file_n] = (f'{len_f}\n{text_new}\n')

sorted_dict = {}
sort_text = sorted(all_text, key=all_text.get)
for n in sort_text:
    sorted_dict[n] = all_text[n]

for clef, meaning in sorted_dict.items():
    with open('general.txt', 'a', encoding='utf-8') as fold:
        fold.writelines(f'{clef}\n{meaning}')