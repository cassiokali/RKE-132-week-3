n = int(input('Sisesta täisarv: 9'))

# if n % 2 == 0:
#     print('Arv on paaris')
# else:
#     print('Arv on paaritu')

# print('Arv on paaris' if n % 2 == 0 else 'Arv on paaritu')

match n % 2:
    case 0:
        print('Arv on paaris')
    case _:
        print('Arv on paaritu')