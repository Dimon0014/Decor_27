# coding=utf-8
def getTalk(type="whisper"):
    # Мы определяем функции прямо здесь
    def shout(word="да"):
        return word.capitalize() + "!"

    def whisper(word="да"):
        return word.lower() + "...";

    # Затем возвращаем необходимую
    if type == "shout":
        # Заметьте, что мы НЕ используем "()", нам нужно не вызвать функцию,
        # а вернуть объект функции
        return shout
    if type == "whisper":
        return whisper


# Как использовать это непонятное нечто?
# Возьмём функцию и свяжем её с переменной
print getTalk("whisper")()
talk = getTalk

# Как мы можем видеть, "talk" теперь - объект "function":
print talk
# выведет: <function shout at 0xb7ea817c>

# Который можно вызывать, как и функцию, определённую "обычным образом":
print talk("shout")()

# Если нам захочется - можно вызвать её напрямую из возвращаемого значения:
print getTalk("whisper")()
# выведет: да...