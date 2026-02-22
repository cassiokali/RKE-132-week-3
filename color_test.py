color = input('Sisesta oma lemmikvärv:').lower()


# if color == 'punane':
#     print('Sa oled energeline inimene!')
# elif color == 'roosa':
#     print('Sa oled romantik!')
# elif color == 'roheline':
#      print('Sa oled rahulik inimene!')
# elif color == 'sinine':
#     print('Sa oled keskendunud inimene!')
# else:
#     print('Sa oled imeline ükssarvik!')

match color:
    case 'punane':
        print('Sa oled energeline inimene!')
    case 'roosa':
        print('Sa oled romantik!')
    case 'roheline':
        print('Sa oled rahulik inimene!')
    case 'sinine':
        print('Sa oled keskendunud inimene!')
    case _:
        print('Sa oled imeline ükssarvik!')