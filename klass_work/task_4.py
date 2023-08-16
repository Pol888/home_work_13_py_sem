import json


def user_factory_from_json_file(file_name: str) -> set:
    with open(file_name, 'r', encoding='utf-8') as f:
        res_f: list = json.load(f)
        result: set[User] = set()
        for i in res_f:
            result.add(User(i['name'], i['id'], i['access_level']))
        return result


class User:

    def __init__(self, name, i_d, access_level=None):
        self.name = name
        self.id = i_d
        self.access_level = access_level

    def __str__(self):
        return f'Имя - {self.name}, id - {self.id}, уровень доступа - {self.access_level}'

    def __eq__(self, other):
        return self.name == other.name and self.id == other.id

    def __hash__(self):
        return hash((self.name, self.id))

# user_factory_from_json_file('file_name_id_al.json')


# u = User('a', 2, 88)
# g = User('a', 2, 7)
# print(u == g)
