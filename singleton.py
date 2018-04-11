# coding: utf-8

"""
Одиночка (Singleton) - паттерн, создаюший объекты.
Паттерн нужен, чтобы создавать единственный экземпляр класса, а в дальнейшем давать доступ к первому и единственному экземпляру глобально.
Паттерн полезен тем, что не плодит дополнительные экземпляры в случаях, где онли не нужны, например для многократного подключения.
"""

class MyClass(object):
    __instance = None

    @staticmethod
    def get_instance():
        if MyClass.__instance == None:
            MyClass.__instance = MyClass()
        return MyClass.__instance

    # проверяем создается ли конструктор 1 раз при создании нескольких объектов
    def __init__(self):
        print("Конструктор вызван")


obj1 = MyClass.get_instance()
obj2 = MyClass.get_instance()
obj3 = MyClass.get_instance()
print(obj1 is obj2 is obj3) # True
