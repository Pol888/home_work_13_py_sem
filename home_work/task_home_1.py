import statistics


class StudentsNameErrors(Exception):
    pass


class IsTitleError(StudentsNameErrors):

    def __init__(self, name: str):
        self.name: str = name

    def __str__(self):
        return f'Значение которое вы ввели {self.name} не соответствует норме записи имени, ' \
               f'значение в норме = {self.name.title()}, первая буква печатается с большой буквы, ' \
               f'остальные с маленькой.'


class IsAlphaError(StudentsNameErrors):

    def __init__(self, name: str):
        self.name: str = name

    def __str__(self):
        mismatched_characters = []
        for i in self.name:
            if not i.isalpha():
                mismatched_characters.append(i)

        return f'Значение которое вы ввели {self.name} содержит в себе символы {mismatched_characters} ' \
               f'не соответствующие норме, значение должно иметь в себе только буквы'


class ValidationStudentsName:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: str):
        if value.istitle() and value.isalpha():
            setattr(instance, self.param_name, value)
        elif not value.istitle() and value.isalpha():
            raise IsTitleError(value)
        elif value.istitle() and not value.isalpha():
            raise IsAlphaError(value)


class Student:
    first_name = ValidationStudentsName()
    last_name = ValidationStudentsName()

    def __init__(self, first_name, last_name, grade_report=None):
        self.first_name = first_name
        self.last_name = last_name
        self.grade_report = grade_report

    def __str__(self):
        result = f'Student name - {self.first_name} {self.last_name}\n Grade_Report:\n' \
                 f'  Subject{" " * (max(map(lambda x: len(x[0]), self.grade_report)) - len("Subject"))}|' \
                 f'Marks{" " * (max(map(lambda x: len(x[1]) * 2, self.grade_report)) - len("Marks") - 1)}|' \
                 f'Test_result{" " * (max(map(lambda x: len(x[2]) * 2, self.grade_report)) - len("Test_result"))} ' \
                 f'|Average score for tests\n'
        for i in self.grade_report:
            result += '  ' + str(i[0]) + " " * (max(map(lambda x: len(x[0]), self.grade_report)) - len(str(i[0]))) \
                      + '|' \
                      + ' '.join(map(str, i[1])) + (' ' * (max(map(lambda x: len(x[1]) * 2 - 1, self.grade_report)) -
                                                           len(i[1]) * 2 + 1)) + '|' \
                      + ' '.join(map(str, i[2])) + (
                                  ' ' * ((max(map(lambda x: len(' '.join(map(str, x[2]))), self.grade_report))) -
                                         len(' '.join(map(str, i[2]))))) + '|' + str(
                round(statistics.mean(i[2]), 2)) + '\n'

        average_score_on_marks_list = []
        for i in self.grade_report:
            average_score_on_marks_list.extend(i[1])

        result += f'  Average_score_on_marks: {round(statistics.mean(average_score_on_marks_list), 2)}\n'
        return result


s = Student('Pol', 'mopy')
