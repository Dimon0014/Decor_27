# coding=utf-8
# Декораторы - это просто функции
def my_decorator(func):
    print "Я обычная  функция"

    def wrapper():
        print "Я - функция, возвращаемая декоратором сюда добавляется функционал"
        func()

    return wrapper


# Так что, мы можем вызывать её, не используя "@"-синтаксис:

def lazy_function():
    print "я функция которая декорируется zzzzzzzz"


decorated_function = my_decorator(lazy_function) # то есть так передается уже готовая не редактируемая функция
# выведет первый раз: Я обычная функция
# Данный код выводит "Я обычная функция", потому что это ровно то, что мы сделали:
# вызвали функцию. Ничего сверхъестественного

print '001'
@my_decorator
def lazy_function():   # получается мы здесь переопределяем старую функцию - lazy_function()
    print "А я nnnnnnn"
# выведет второй раз: Я обычная функция
print '002'

decorated_function()
print '003'
lazy_function()