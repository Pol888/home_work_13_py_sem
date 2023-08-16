import json
from task_4 import User
from task_6 import LevelError, AccessError


class Project:

    def __init__(self, file_name, sys_access_level=1):
        self.file_name = file_name
        self.lots_of_users: set = self.__loading_data()
        self.sys_access_level = sys_access_level
        self.system_users: list = []

    def __loading_data(self) -> set:
        with open(self.file_name, 'r', encoding='utf-8') as f:
            res_f: list = json.load(f)
            result: set[User] = set()
            for i in res_f:
                result.add(User(i['name'], i['id'], i['access_level']))
            return result

    def log_in_to_the_system(self):
        f = False
        while not f:
            print("Вход в систему....\n")
            name = input("Введите имя пользователя: ")
            i_d = input("Введите id пользователя: ")
            user_sys = None
            for i in self.lots_of_users:
                if i == User(name, i_d):
                    user_sys = i
            if isinstance(user_sys, User):
                self.__to_add_a_user(user_sys)
                f = True
            else:
                raise AccessError(name, i_d)

    def __to_add_a_user(self, user: User):
        if int(user.access_level) < self.sys_access_level:
            raise LevelError(user.access_level, self.sys_access_level)
        else:
            print("Пользователь в системе")
            self.system_users.append(user)


h = Project('file_name_id_al.json', 6)
h.log_in_to_the_system()
