# coding=utf-8
# Декоратор - это функция, ожидающая ДРУГУЮ функцию в качестве параметра
def my_shiny_new_decorator(a_function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку".
    # Она будет (что бы вы думали?..) обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.

    def the_wrapper_around_the_original_function():
        # Поместим здесь код, который мы хотим запускать ДО вызова
        # оригинальной функции
        print "Я - код, который отработает до вызова функции"

        # ВЫЗОВЕМ саму декорируемую функцию
        a_function_to_decorate()

        # А здесь поместим код, который мы хотим запускать ПОСЛЕ вызова
        # оригинальной функции
        print "А я - код, срабатывающий после"

    # На данный момент функция "a_function_to_decorate" НЕ ВЫЗЫВАЛАСЬ НИ РАЗУ
    #  так как это объявление декорирующей(которая обернута вокруг декорируемой) функции где
    # Теперь, вернём функцию-обёртку, которая содержит в себе
    # декорируемую функцию, и код, который необходимо выполнить до и после.ё
    # Всё просто!
    return the_wrapper_around_the_original_function


# Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
def a_stand_alone_function():
    print "Я простая одинокая функция, ты ведь не посмеешь меня изменять?.."


a_stand_alone_function()
# выведет: Я простая одинокая функция, ты ведь не посмеешь меня изменять?..

# Однако, чтобы изменить её поведение, мы можем декорировать её, то есть
# Просто передать декоратору, который обернет исходную функцию в любой код,
# который нам потребуется, и вернёт новую, готовую к использованию функцию:
print "  "
a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()
# выведет:
# Я - код, который отработает до вызова функции
# Я простая одинокая функция, ты ведь не посмеешь меня изменять?..
# А я - код, срабатывающий после
print " -----подменна имени ссылки------ "
a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()
#выведет:
# Я - код, который отработает до вызова функции
# Я простая одинокая функция, ты ведь не посмеешь меня изменять?..
# А я - код, срабатывающий после

@my_shiny_new_decorator             # то есть имя деоратора который применим к внвь создаваемой фонкции
def another_stand_alone_function2(): # определяем функцию которая пойдет на вход декоратору
    print "Оставь меня в покое2"


another_stand_alone_function2()     # вызываем функцию и она уже будет с декоратором
# выведет:
# Я - код, который отработает до вызова функции
# Оставь меня в покое
# А я - код, срабатывающий после