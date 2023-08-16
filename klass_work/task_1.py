def fun_input_user():
    f = 1
    while f:
        try:
            t = float(input('дайте мне еды(особенную люблю): \n'))
            if str(t).split('.')[1] == '0':
                t = int(t)
                print(f'Это число {t}')

            else:
                print(f'Это число {t}')
            f = 0
        except ValueError:
            print('Другую еду давай')


fun_input_user()
