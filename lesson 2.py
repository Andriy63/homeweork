# 1
mylist = ['boy', 12, [], {}, 'year']
print(list(map(type, mylist)))
# 2
l = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, len(l), 2):
    old = l[i]
    l[i] = l[i + 1]
    l[i + 1] = old
print(l)
# 3
year = {1: 'january', 2: 'february', 3: ' march', 4: 'april', 5: 'may', 6: 'june',
        7: 'july', 8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}
a = print(year.keys())
if a == 1 or 2 or 12:
    print('Winter')
if a == 3 or 4 or 5:
    print('Sping')
if a == 6 or 7 or 8:
    print('Summer')
if a == 9 or 10 or 11:
    print('Autumn')
else:
    print('Error')
# второй вариант
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
if a == 1 or 2 or 12:
    print('Winter')
if a == 3 or 4 or 5:
    print('Sping')
if a == 6 or 7 or 8:
    print('Summer')
if a != 9 and not 10:
    print('Error')
else:
    print('Autumn')
# 4
my_str = 'зима весна лето осень тепло холодно жарко'
my_word = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word[el]}")
        num += 1
    else:
        print(f" {num} {my_word[el][0:10]}")
        num += 1
# 5
my_list = [9, 8, 7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input(6))
while digit != 10:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"текущий список - {my_list}")
    digit = int(input(6))
    print(my_list)
# 6

var = [
    (1, {'name': 'computer', 'price': 20000, 'amount': 5, 'units': 'one'}),
    (2, {'name': 'printer', 'price': 6000, 'amount': 2, 'units': 'one'}),
    (3, {'name': 'scanner', 'price': 2000, 'amount': 7, 'units': 'one'})
]

var = {
    'name' : [ 'computer', 'printer', 'scanner'],
    'price' : [20000, 6000, 2000],
    'amount' : [5, 2, 7],
    'units': 'one'

}
goods = []
features = {'name': '', 'price': '', ' amount': '', 'units': ''}
analytics = {'name': [], 'price': [], ' amount': [], 'units': []}
num = 0
feature_ = None
control = None
while True:
    control = input("For quit press 'Q', for continue press 'Enter', for analytics press 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Input feature "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == ' amount') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))


goods = int(input(3))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({ 'name': input("введите название "), 'price' : input("Введите цену "),
                     ' amount' : input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        { 'name' : my_dict.get('название'),  'price' : my_dict.get('цена'),  ' amount': my_dict.get('количество'),
         'units' : my_dict.get('ед')})
print(my_list)
print(my_analys)

