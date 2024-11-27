def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
            else:
                shop_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
    return shop_list

cook_book = {
'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity':  1, 'measure': 'кг'},
    {'ingredient_name': 'Лук репчатый', 'quantity': 50, 'measure': 'г'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ],
  'Овощной салат': [
    {'ingredient_name': 'огурцы', 'quantity': 100, 'measure': 'г'},
    {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'г'},
    {'ingredient_name': 'лук репчатый', 'quantity': 30, 'measure': 'г'},
    {'ingredient_name': 'майонез', 'quantity': 15, 'measure': 'г'}
    ]
  }

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

