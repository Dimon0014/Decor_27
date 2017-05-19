# coding=utf-8
def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3  # действительно, дружелюбно - снизим возраст ещё сильней :-)
        return method_to_decorate(self, lie)

    return wrapper                                      # в начале объявляем декоратор, затем класс внутри класса
                                                        #  создаем функцию и декорируем ее.
                                                        # в принципе логика обратная есть класс с функцией внутри
class Lucy(object):                                     # сверху доптсывается(объявляется) декоратор и
    def __init__(self):                                # добавляется строкой с @(собакой) и названием к функции
        self.age = 32                                  # которой хотим добавить дополнительный функционал

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print "Мне %s, а ты бы сколько дал?" % (self.age + lie)


l = Lucy()
l.sayYourAge(-3)
# выведет: Мне 26, а ты бы сколько дал?