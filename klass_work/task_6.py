class MyFavoriteErrors(Exception):
    pass


class LevelError(MyFavoriteErrors):
    def __new__(cls, user_level, allowed_level):
        cls.user_level = user_level
        cls.allowed_level = allowed_level
        return super().__new__(cls)

    def __str__(self):
        return f'Ваш уровень доступа {self.user_level} меньше разрешенного {self.allowed_level}'


class AccessError(MyFavoriteErrors):
    def __new__(cls, name, i_d):
        cls.name = name
        cls.i_d = i_d
        return super().__new__(cls)

    def __str__(self):
        return f'Пользователя с именем {self.name} с id {self.i_d} не существует в базе'
