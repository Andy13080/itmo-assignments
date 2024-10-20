# 1. ФЛАГ Финляндия
blue = '\x1b[48;5;21m'
white = '\x1b[48;5;15m'
stop = '\033[0m'


def draw_pix(row, size):
    vertical_stripe_start = size // 3
    vertical_stripe_end = 2 * size // 3
    horizontal_stripe_start = size // 3
    horizontal_stripe_end = 2 * size // 3

    for col in range(size * 2):

        if (horizontal_stripe_start <= row < horizontal_stripe_end) or (
                vertical_stripe_start <= col < vertical_stripe_end):
            print(blue + '  ', end='')
        else:
            print(white + '  ', end='')
    print(stop)


def finland_flag(size):
    for row in range(size):
        draw_pix(row, size)



finland_flag(15)

# 2. График функции y = x / 2

def graph_y_equals_x_div_2():
    width = 20
    height = 10
    for y in range(height, -1, -1):
        for x in range(width + 1):
            if x == 0 and y == 0:
                print('+', end=' ')
            elif x == 0:
                print('|', end=' ')
            elif y == 0:  
                print('-', end=' ')
            elif y == x // 1:
                print(' *', end=' ')
            else:
                print('   ', end=' ')



        print()

graph_y_equals_x_div_2()



# 3 задание чарт

white = '\x1b[48;5;15m'
stop = '\033[0m'
file = open("sequence.txt")
file_ms = [float(i) for i in file]
cor_dig = [i for i in file_ms if ((i <= 5) and (i >= -5))]
print(cor_dig)
print(len(cor_dig))
less_0 = len([i for i in cor_dig if (i > 0)])
more_0 = len(cor_dig) - less_0

def draw_line(count):
    print(white*(count < less_0), '  ', stop, ' ',white*(count < more_0), '  ', stop,)

def chart():
    for i in range(max(less_0, more_0), 0, -1):
        draw_line(i)
chart()
print(' <0     >0')

white = '\x1b[48;5;15m'
stop = '\033[0m'



# 4 задание фигурa

def process_numbers():
    with open('sequence.txt') as file:
        numbers = [float(line.strip()) for line in file]

    group_1 = [n for n in numbers if 5 <= n <= 10]
    group_2 = [n for n in numbers if -10 <= n <= -5]

    total = len(group_1) + len(group_2)

   
    percent_group_1 = len(group_1) / total * 100 if total > 0 else 0
    percent_group_2 = len(group_2) / total * 100 if total > 0 else 0

    print(f"Числа от 5 до 10: {percent_group_1:.2f}%")
    print(f"Числа от -5 до -10: {percent_group_2:.2f}%")


    max_height = 10
    group_1_height = int(max_height * percent_group_1 / 100)
    group_2_height = int(max_height * percent_group_2 / 100)




process_numbers()





white = '\x1b[48;5;15m'
stop = '\033[0m'


def draw_pix(st1, en1, st2, en2):
    ln1 = ' '*(st1 - 1) + white + ' '*(en1 - st1 + 1) + stop
    ln2 = ' '*(st2 - en1 - 1) + white + ' '*(en2 - st2 + 1) + stop
    print(ln1 + ln2)


def fig(size):
    width_of_place = size * 4 + 1
    height_of_place = size * 2 + 1

    first1 = ((width_of_place // 2) + 1) // 2 + 1
    first2 = first1 + size * 2 + 2

    for i in range(first1):
        draw_pix(first1 - i, first1 + i, first2 - i, first2 + i)

    for i in range(first1, 0, -1):
        draw_pix(first1 - i, first1 + i, first2 - i, first2 + i)

    draw_pix(first1, first1, first2, first2)

fig(5)