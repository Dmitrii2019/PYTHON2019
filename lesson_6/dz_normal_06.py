#__author__ = 'Гродзинский Дмитрий Александрович'
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Person:
    def __init__(self, name, surname, patronymic, class_room, subject):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.class_room = class_room
        self.subject = subject

class Students(Person): #Данные по студенту
    def __init__(self, name, surname, patronymic, mother, father, class_room, subject, teachers):
        Person.__init__(self, name, surname, patronymic, class_room, subject)
        self.mother = mother
        self.father = father
        self.teachers = teachers

    def fio(self):
        return f'{self.surname} {self.name[0]}.{self.patronymic[0]}.'

    def fio_parents(self):
        return f'{self.surname} {self.father} {self.surname} {self.mother}'

    def _subject(self):
        return f'{self.name} {self.class_room} {self.teachers} {self.subject}'

class Teachers(Person): #Данные по Учителю
    def __init__(self, name, surname, patronymic, class_room, subject):
        Person.__init__(self, name, surname, patronymic, class_room, subject)

class Classes: #№ классов
    def __init__(self, *args):
        self.class_room = args

    def classes(self):
        return self.class_room

    def students_num(self):
        if self.class_room == self.class_room:
            return Students.fio(self)

class Subject: # предметы математика и т,д
    def __init__(self, *args):
        self.subject = args

student1 = Students('Вася', 'Васильев', 'Васильевич', 'Аня', 'Василий', '7б', 'математика', 'Иванов')
student2 = Students('Петя', 'Петров', 'Олегович', 'Олга', 'Олег', '5б', 'русский', 'Иванов')
teachers = Teachers('Иван', 'Иванов', 'Иванович',  '5А', 'математика')

asd = Classes('5А', '5Б', '6А', '7Б')
print(asd.classes())
print(student1.fio())
print(student1._subject())
print(student1.fio_parents())

# Не успел доделать до конца, не все понял как делать.