# coding: utf-8

"""
Заместитель (Proxy, Surrogate) - паттерн, котоый создает суррогат другого объекта и конторолиркет к нему доступ.
"""

class Proxy(object):
    def __init__(self, object_a):
        self._object_a = object_a

    def decorateEnterExit(self, obj, f):
        def inner(*args, **kwargs):
            with obj as _:
                return f(*args, **kwargs)
        return inner

    def __getattribute__(self, name):
        obj = object.__getattribute__(self, '_object_a')
        dee = object.__getattribute__(self, 'decorateEnterExit')
        return dee(obj, getattr(obj, name))
