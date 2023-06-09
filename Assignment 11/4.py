def concentric(num, type_cr='emoji'):
    emoji = ['😀','😍','😎','👀','🎈','🍗','🍕','😆']
    center = (num-1) / 2
    if not center.is_integer() or center < 0:
        raise ValueError('input number have to odd and positive number (1,3,5,...) !!')
    CR_matrix = []
    for row in range(num):
        Temp_array = []
        for com in range(num):
            result = int(max(abs(com - center), abs(row - center)))
            if type_cr == 'emoji':
                Temp_array.append(emoji[result%(len(emoji))])
            else:
                Temp_array.append(result)
        CR_matrix.append(Temp_array)
    return CR_matrix

def print_concentric_rugs(CR_matrix):
    for row in CR_matrix:
        for char in row:
            print(char, end=' ')
        print()

number = int(input('Enter your nubmer to creat concentric rugs: '))
print_concentric(concentric_rugs(number))