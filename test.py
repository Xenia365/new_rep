# class MyPoint:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'<MyPoint(x={self.x}, y={self.y})>'
#
# p = MyPoint(1, 1)
# print(p)        # <MyPoint(x=1, y=1)>
# print(str(p))   # <MyPoint(x=1, y=1)>
# print(repr(p))
# print(eval('repr(p)'))
#from socket import send_fds
#from tkinter.font import names
from contextlib import suppress
from platform import processor
from statistics import quantiles


#
# class Commuter5:
#     def __init__(self, val) :
#         self.val = val
#  # Распространение типа класса на результаты
#     def __add__(self, other) :
#         if isinstance(other, Commuter5):
#             other = other.val #Commuter5: 99, как sefl, но для другого экземпляра
#         return Commuter5 (self.val + other)
#     def __radd__(self, other):
#         return Commuter5(other + self.val)
#     def __str__(self) :
#         return '<Commuter5: %s>' % self.val
#
# x = Commuter5(88)
# y = Commuter5(99)
#
#
#
# print(x + 10)
# print(10 + y)
# z = x + y
# print(z)
#
# class Truth:
#     def __bool__(self):
#         return self != 0
#
#
#
#
# x = Truth()
#
# print(bool(x))

#
#
#
# class Listinstance:
#
#  #Подмешиваемый класс, который предоставляет форматированную функцию
# #print() или str () для экземпляров через наследование реализованного
# #в нем метода __str__; отображает только атрибуты экземпляра; self
# # является экземпляром самого нижнего класса;
# # имена __X предотвращают конфликты с атрибутами клиента
#     def __attrnames(self):
#         result = ''
#         for attr in sorted(self.__dict__) :
#             result += '\t%s=%s\n' % (attr, self.__dict__[attr])
#         return result
#     def __str__(self) :
#         return '<Instance of %s, address %s:\n%s>' % (
#             self.__class__.__name__,
#             id(self),
#             self.__attrnames())
#
#
# class Spam(Listinstance):
# # Наследует метод__str__
#     def __init__(self, name):
#         self.data1 = name
#
#
# x = Spam('bob')
# print(x)
#
# display = str(x)
# print(display)
#

# class Set:
#     def __init__(self, value = []) :
#         self.data = []
#         self.concat(value)
#     def intersect(self, other):
#         res = []
#         for x in self.data:
#             if x in other:
#                 res.append(x)
#         return Set(res)
#     def union(self, other):
#         res = self.data[:]
#         for x in other:
#             if not x in res:
#                 res.append(x)
#         return Set(res)
#     def concat(self, value):
#         for x in value:
#             if not x in self.data:
#                 self.data.append(x)
#     def __len__(self): return len(self.data)
#     def __getitem__(self, key): return self.data[key]
#
#     def __and__(self, other): return self.intersect(other)
#     def __or__ (self, other): return self.union(other)
#     def __repr__(self): return 'Set:' + repr(self.data)
#     def __iter__(self) : return iter(self.data)
#
#
# x = Set( [1, 3, 3, 5, 7])
# print(x.union(Set( [1, 4, 7])))
# print(x | Set([1, 4, 6]))
#
# print(x.data, x.concat)
#
# for i in x:
#     print(i)

# class C(object):
#     data = 'spam'
#     def __getattr__(self, name) :
#         print ('getattr: ' + name)
#         return getattr(self.data, name)
#     def __getitem__ (self, i):
#         print ('getitem: ' + str(i))
#         return self.data[i]
#     def __add__(self, other):
#         print('add: ' + other)
#         return getattr (self .data, '__add__') (other)
#
#
# X = C()
# print(X.upper())
# print(X[1])
# print(X.__getitem__(1))
# print(X + 'eggs')
# print(X.__add__('eggs'))

#
# class C(object): pass
# X = C()
# print(type(X) , type (C))
#
# print(isinstance(X, object))
#
# print(type('spam'), type(str))
#
# print(C.__bases__, C.__class__)
#
# print(dir(object))
# class D: pass
#
# print(D.__class__, D.__bases__)
#
# print(str.__class__, str.__bases__)
#
# print(dir(C.__setattr__, C.__get__))

# Ex1

# class Adder:
#     def __init__(self):
#         self.list_add = []
#         self.dict_add = {}
#
#     def __add__(self, х, у):
#         print('Not Implemented')
#
#
#
# class ListAdder(Adder):
#     def __add__(self, other):
#         self.list_add.append(other)
#         return self.list_add
#
#
# class DictAdder(Adder):
#     def __add__(self, x):
#         self.dict_add[x] = 1
#         return self.dict_add
#
#
# x = ListAdder()
# print(x + 2)
#
# y = DictAdder()
# print(y + 2)


# Ex 2  Напишите класс по имени MyList, который скрывает
# (“помещает внутрь себя”) список Python: он должен перегружать большинство
# списковых операций, включая +, индексирование, итерацию, нарезание, а так
#  же списковые методы, такие как append и sort.
#
# class Mylist:
#     def __init__(self, x):
#         self.list_add = [x]
#         self.index = 0
#
#     def __add__(self, other):
#         self.list_add.append(other)
#         return self.list_add
#
#     def __getitem__(self, item):            #индексирование
#         if isinstance(item, slice):
#             return  self.list_add[item.start:item.stop:item.step]
#         else:
#             return self.list_add[item]
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.list_add):
#             raise StopIteration
#         else:
#             self.index += 1
#             return self.list_add[self.index - 1]
#
#
#     def __getattribute__(self, item):
#         if item == 'append':
#             return Mylist.__add__(self,item)
#         if item == 'sorted':
#             self.list_add = sorted(self.list_add)
#             return self.list_add
#         else:
#             return super().__getattribute__(item)
#
#
# g = Mylist(4)
#
# # for i in g:
# #     print(i)
#
# g.list_add.append(5)
#
#
# class MyListSub(Mylist):
#     counter = 0
#
#     def __add__(self, other):
#         MyListSub.counter += 1
#         return print(f'Обращение к операции +: {MyListSub.counter}, результат {super().__add__(other)}')
#
# h = MyListSub(6)
# h + 8


# class Lunch:
#     def __init__(self):
#         self.customer = Customer()
#         self.employee = Employee()
#         self.food = None
#
#     def order(self, foodName):
#         self.food = self.customer.placeOrder(foodName, self.employee)
#         return self.food
#
#     def result(self):
#         return self.food.name
#
#
# class Customer:
#     def __init__(self):
#         self.foodName = None
#
#     def placeOrder(self, foodName, employee):
#         self.foodName = foodName
#         return employee.takeOrder(foodName)
#
#     def printFood(self):
#         return self.foodName
#
#
# class Employee:
#     def takeOrder(self, foodName):
#         return Food(foodName)
#
#
# class Food:
#     def __init__(self, name):
#         self.name = name
#
#
# a = Lunch()
# a.order('potata')
# print(a.result())

#
# class Animal:
#     def speak(self):
#         return 'Animal class'
#     def reply(self):
#         return self.speak()
# class Mammal(Animal):
#     def speak(self):
#         return 'Mammal class'
# class Cat(Mammal):
#     def speak(self):
#         return 'Cat class'
# class Dog(Mammal):
#     def speak(self):
#         return 'Dog class'
# class Primate(Mammal):
#     def speak(self):
#         return 'Primate class'
# class Hacker(Primate): pass
#
#
#
# spot = Cat()
# data = Hacker()
# print(data.reply(), spot.reply())



# class Scene:
#     def __init__(self):
#         self.customer = Customer()
#         self.clerk = Clerk()
#         self.parrot = Parrot()
#     def action(self):
#         return self.customer.line(), self.clerk.line(), self.parrot.line()
#
# class Customer:
#     def line(self):
#         return 'customer: "that is one ex-bird!'
#
# class Clerk:
#     def line(self):
#         return 'clerk: "no it is not..."'
# class Parrot:
#     def line(self):
#         return 'parrot: None'
#
#
# a = Scene()
# print(a.action())

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self, name):
#         return f"{name} says woof!"
#
#     def get_human_age(self, age):
#         return age * 7
#

# class BankAccount:
#     def __init__(self, owner, balance = 0):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, dep):
#         self.balance += int(dep)
#         return self.balance
#
#     def withdraw(self, summa):
#         if self.balance > 0 and self.balance >= summa:
#             self.balance = self.balance - summa
#             return f"Остаток {self.balance}"
#         else:
#             return 'Недостаточно средств'
#
#     def get_balance(self):
#         return f"Текущий баланс счета {self.balance}"
#
#
#
# a = BankAccount("Ivanov")
# a.deposit(1000)
# a.withdraw(500)
# print(a.get_balance())


# class Vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#     def start_engine(self):
#         return f'Engine started'
#
# class Car(Vehicle):
#     def __init__(self, bramd, year, num_doors):
#         self.num_doors = num_doors
#
#     def start_engine(self):
#         return super().start_engine(), f'Engine started'
#
#     def honk(self):
#         return f"Beep beep!"
#
# car = Car("Toyota", 2020, 4)
# print(car.start_engine())
# print(car.honk())
#
# class Book:
#     def __init__(self, title, author, is_available=True):
#         self.title = title
#         self.author = author
#         self.is_available = is_available
#
#     def check_out(self):
#         if not self.is_available:
#             return 'Книга уже на руках'
#         else:
#             self.is_available = False
#             print(f'Книга "{self.title}" выдана')
#
#     def return_book(self):
#         if self.is_available:
#             return 'Книга уже в библиотеке'
#         else:
#             self.is_available = True
#             print(f'Книга "{self.title}" возвращена в библиотеку')
#
#     def print_book(self):
#         return f'Название: "{self.title}", автор: {self.author}, доступность: {self.is_available}'
#
#
# class Library:
#     def __init__(self):
#         self.books = []
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def find_book_by_title(self, title):
#         for book in self.books:
#             if book.title == title:
#                 return book.print_book()
#         return 'Книга не найдена'
#
#     def check_out_book(self, title):
#         for book in self.books:
#             if book.title == title:
#                 return book.check_out()
#         return 'Книга не найдена'
#
#     def return_book(self, title):
#         for book in self.books:
#             if book.title == title:
#                 return book.return_book()
#         return 'Книга не найдена'
#
#




# class Employee:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def calculate_bonus(self, bonus = 0.1):
#         return self.salary * bonus
#
#
# class Manager(Employee):
#
#     def __init__(self, name, salary):
#         self.employee = Employee(name, salary)
#         self.team = []
#
#     def add_team_member(self, employee):
#         self.team.append(employee)
#
#     def calculate_bonus(self, bonus = 0.2):
#          return Employee.calculate_bonus(self.employee, bonus)
#
#
# class Developer(Employee):
#
#     def __init__(self, name, salary, programming_language):
#         self.employee = Employee(name, salary)
#         self.programming_language = programming_language
#
#     def calculate_bonus(self, bonus = 0.15):
#         return Employee.calculate_bonus(self.employee, bonus)
#
#
#
# manager = Manager("Alice", 5000)
# developer1 = Developer("Bob", 4000, "Python")
# developer2 = Developer("Charlie", 4500, "Java")
#
# manager.add_team_member(developer1)
# manager.add_team_member(developer2)
#
# print(manager.calculate_bonus())  # Вывод: 1000 (20% от 5000)
# print(developer1.calculate_bonus())

#
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     def make_sound(self, sound="Some sound"):
#         return print(sound)
#
# class Lion(Animal):
#
#     def make_sound(self, sound="Roar!"):
#         return super().make_sound(sound)
#
# class Elephant(Animal):
#
#     def make_sound(self, sound="Trumpet!"):
#         return super().make_sound(sound)
#
# class Monkey(Animal):
#
#     def make_sound(self, sound="Ooh ooh!"):
#         return super().make_sound(sound)
#
# class Zoo:
#
#     def __init__(self):
#         self.animals = []
#
#     def add_animal(self, animal):
#         self.animals.append(animal)
#
#     def make_all_sounds(self):
#         for animal in self.animals:
#             animal.make_sound()
#
#
# zoo = Zoo()
# zoo.add_animal(Lion("Simba", "Lion"))
# zoo.add_animal(Elephant("Dumbo", "Elephant"))
# zoo.add_animal(Monkey("George", "Monkey"))
#
# zoo.make_all_sounds()

#
# class Product:
#     def  __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def get_total_price(self):
#         return self.price * self.quantity
#
#     def __str__(self):
#         return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
#
#
# class Store:
#
#     def __init__(self):
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def remove_product(self, product_name):
#         for product in self.products:
#             if product_name == product.name:
#                 self.products.remove(product)
#
#     def find_product_by_name(self, product_name):
#         for product in self.products:
#             if product_name == product.name:
#                 return product
#
#     def get_total_inventory_value(self):
#         summa = 0
#         for product in self.products:
#             summa += product.get_total_price()
#         return summa
#
#
# store = Store()
# store.add_product(Product("Apple", 1.5, 100))
# store.add_product(Product("Banana", 2.0, 50))
#
# print(store.find_product_by_name("Apple"))  # Вывод: Product: Apple, Price: 1.5, Quantity: 100
# print(store.get_total_inventory_value())

# class Hero:
#     def __init__(self, name, health, attack_power):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power
#
#     def attack(self, enemy):
#         enemy.health -= self.attack_power
#
#     def is_alive(self):
#         return self.health > 0
#
#     def __str__(self):
#         return f'Hero: {self.name}, Health: {self.health}, Attack: {self.attack_power}'
#
#
# class Battle:
#
#     def __init__(self,hero1, hero2):
#         self.hero1 = hero1
#         self.hero2 = hero2
#
#     def start(self):
#         while self.hero1.is_alive() and self.hero2.is_alive():  # Пока оба героя живы
#             print(f"{self.hero1.name} attacks {self.hero2.name}!")
#             self.hero1.attack(self.hero2)  # Hero1 атакует Hero2
#             print(f"{self.hero2.name}'s health is now {self.hero2.health}")
#
#             if not self.hero2.is_alive():  # Проверяем, жив ли Hero2
#                 break
#
#             print(f"{self.hero2.name} attacks {self.hero1.name}!")
#             self.hero2.attack(self.hero1)  # Hero2 атакует Hero1
#             print(f"{self.hero1.name}'s health is now {self.hero1.health}")
#
#             if not self.hero1.is_alive():  # Проверяем, жив ли Hero1
#                 break
#
#
# hero1 = Hero("Aragorn", 100, 20)
# hero2 = Hero("Sauron", 120, 15)
#
# battle = Battle(hero1, hero2)
# battle.start()
# print(hero1, hero2)

# def safe(func, *pargs, **kargs):


# def decorator_without_arguments(func):
#     def wrapper(*args, **kwargs):
#         print('before decorator')
#         result = func(*args, **kwargs)
#         print('after decorator')
#         # return result here if needed
#         return result
#     return wrapper
#
# def decorator_with_arguments(some_arg):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             if some_arg == 10:
#                 print('before decorator')
#             result = func(*args, **kwargs)
#             print(result)
#             print('after decorator')
#             # return result here if needed
#             return result
#         return inner
#     return wrapper
#
# @decorator_with_arguments(5)
# def name(a):
#     return a
# #                            wrapper  inner
# # decorator_with_arguments(10)(name)   ("ggg")
#
# a = name("GGG")
# print(f"a = {a}")
#

#
# class Item:
#
#     def __init__(self, name, price):
#         self.name = name
#         self._quantity = 0
#         self._price = price
#         self.counter = None
#
#     def __str__(self):
#         return f'Item: {self.name}, quantity: {self._quantity}'
#
#     def take_item(self, n_quantity):
#         if n_quantity > self._quantity:
#             raise 'Not enough items in warehouse'
#         else:
#             self._quantity = self._quantity - n_quantity
#             return self._quantity
#
#
#     def check_quantity(self):
#         if self._quantity == 0:
#             return 0
#         else:
#             return self._quantity
#
#     def set_id(self, counter1):
#         self.counter = counter1
#
#     def del_id(self):
#         self.counter = None
#
#     def adding(self, n_quantity):
#         self._quantity += n_quantity
#         return self
#
#     def spisanie(self):
#         self._quantity = 0
#         return "Done! Quantity is 0!"
#
#     def _set_price(self, value):
#         if value > 0:
#             self._price = value
#         else:
#             print('Price must be more than 0')
#
#     def _get_price(self):
#         return self._price
#
#     price = property(fget=_get_price, fset=_set_price, fdel=None, doc='None')
#
#
#
#
# class Phone(Item):
#
#     def __init__(self,  name, category, price):
#         super().__init__(name, price)
#         self.category = category
#
#     def __str__(self):
#         return f'{super().__str__()}, Category: {self.category}'
#
#
#
#
# class Warehouse:
#
#     def __init__(self):
#         self.all_items = {}
#         self.counter = 1
#
#     def add(self, item, n_quantity): #добавить
#         if item.name in self.all_items.values(): #проверка если уже есть такой товар
#             return Item.adding(item, n_quantity)   #если есть, то меняет только количество
#         else:
#             self.all_items[self.counter] = Item.adding(item, n_quantity)
#             Item.set_id(item, self.counter)
#             with open('newfile.txt', 'w', encoding='utf-8') as g:
#                 g.write(f'Added: {item}')
#             self.counter += 1
#
#     def __str__(self):
#         for k in self.all_items.keys():
#             print(f'{self.all_items[k]}\n')
#
#     @staticmethod
#     def take_from_warehouse(n_item, n_quantity):
#         if Item.check_quantity(n_item):
#             return Item.take_item(n_item, n_quantity)
#         else:
#             return print('No such items in warehouse')
#
#     @staticmethod
#     def checker(n_item):
#         return Item.check_quantity(n_item)
#
#     @staticmethod
#     def spisat(n_item):
#         return Item.spisanie(n_item)
#
#     def delete_item(self, n_item):
#         assert n_item.counter != None, 'No such item in warehouse'
#         del self.all_items[n_item.counter]
#         Item.del_id(n_item)
#         with open('newfile.txt', 'w', encoding='utf-8') as g:
#             g.write(f'Deleted: {n_item}')
#
#
#
#
#
#
# mobile_1 = Phone('Iphone 16', 'Phones', 100000)
# mobile_2 = Phone('Iphone 1', 'Phones', 100000)
#
# mobile_1.price = -999999
# print(mobile_1.price)
#
#
#
#
# haus = Warehouse()
#
# haus.add(mobile_1, 10)
# haus.take_from_warehouse(mobile_1, 5)
#
# print(haus.all_items[1])
# print(mobile_1.counter)
# #haus.delete_item(mobile_1)



class Task:

    def __init__(self, name, priority):
        self.name = name
        if self.check_priority(priority):
            self._priority = priority
        self._status = 'Undone'
        self.task_id = None

    def add_id(self, todolist_id):
        self.task_id = todolist_id
        return print(f'New task added: {self}')

    def del_id(self):
        self.task_id = None
        return print('Task has been deleted')

    def c_status(self, new_status):
        self._status = new_status
        return self._status

    def get_priority(self):
        return self._priority

    @staticmethod
    def check_priority(x):
        if x not in (1, 2, 3, 4, 5):
            raise ValueError('You need to use priority 1 - 5')
        else:
            return True

    def c_priority(self, new_priority):
        if self.check_priority(new_priority):
            self._priority = new_priority
            return self._priority

    def get_status(self):
        return self._status

    @staticmethod
    def set_status(self, new_status):
        return print(f'You can not change {self._status} status to {new_status}')


    status = property(fget=get_status, fset=set_status)
    priority = property(fget=get_priority, fset=c_priority)



class DevelopersTask(Task):

    def __init__(self, name, priority, project_name,):
        super().__init__(name, priority)
        self.project_name = project_name



class ToDoList:

    def __init__(self):
        self.all_tasks = {}
        self.counter = 1

    def add_task(self, task):
        if task not in self.all_tasks.values():
            self.all_tasks[self.counter] = task
            task.add_id(self.counter)
            self.counter += 1
        else:
            print('This task is already in ToDoList')

    def delete_task(self, task):
        if task in self.all_tasks.values():
            del self.all_tasks[task.task_id]
            return task.del_id()
        else:
            print('No such task in ToDoList')


    @staticmethod
    def change_status(task, new_status):
        if task._status == new_status:
            print('Same status, you can not change it')
        else:
           return task.c_status(new_status)

    @staticmethod
    def change_priority(task, new_priority):
        if task._priority == new_priority:
            print('Same priority, you can not change it')
        else:
           return task.c_priority(new_priority)

    def filter(self, status):
        founded = {k: v for k, v in self.all_tasks.items() if status == v._status or status == v._priority}
        return f'Witn {status} were founded: {founded}'


first_list =  ToDoList()

first_task = DevelopersTask('To make a new repository for project', 1, 'Doodle')
first_task.status = 'Done'
print(first_task.status)

first_list.add_task(first_task)


first_task.priority = 3
print(first_task.priority)


print(first_list.filter(3))



def divide_numbers(x, y):
    try:
        return x / y
    except (ZeroDivisionError(), ValueError()):
        print('Use correct value')
    finally:
        print('Operation passed')


print(divide_numbers(5,10))



h = 22
print(h.__class__)


def calculate_discount(x, y):
    assert x >= 0, 'Wrong condition, arg x must be non negative'
    assert y in range(1, 101), 'Wrong condition, arg y not in range 1-100'
    return x - x * (y / 100)





def process_data(x):
    with x as file:
        try:
            for line in file:
                assert line.__class__ == 'dict', 'Line must be dictionary'
                line.read('\n')
        except (FileNotFoundError(), UnicodeDecodeError()):
            print('Exceptions found')

def check_even_number(number):
    try:
        if not isinstance(number, int):
            raise TypeError("Ожидается целое число")
        if number % 2 != 0:
            raise ValueError("Число нечетное")
    except TypeError as e:
        print(f"Ошибка: {e}")
    except ValueError as e:
        print(f"Ошибка: {e}")
    else:
        print(f"Число {number} четное")
    finally:
        print("Проверка завершена")