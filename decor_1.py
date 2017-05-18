# coding=utf-8
def shout(word="yes"):
    return word.capitalize() + "!"


print shout("нет")
# выведет: 'Да!'

# Так как функция - это объект, вы связать её с переменнной,
# как и любой другой объект
scream = shout

# Заметьте, что мы не используем скобок: мы НЕ вызываем функцию "shout",
# мы связываем её с переменной "scream". Это означает, что теперь мы
# можем вызывать "shout" через "scream":

print scream()
# выведет: 'Да!'

# Более того, это значит, что мы можем удалить "shout", и функция всё ещё
# будет доступна через переменную "scream"

del shout
try:
    print shout()
except NameError, e:
    print e
    # выведет: "name 'shout' is not defined"

print scream()


# выведет: 'Да!'
def doSomethingBefore(func):
    print "Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал"
    print func()


doSomethingBefore(scream)
# выведет:
# Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал
# Да!