# Our first GUI
pictures = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
for i in pictures:
    for j in i:
        if j == 0:
            print(' ', end='')
        else:
            print('*', end='')
    print('')