nums_dict = {
    'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
    'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
}
def num_translate(value: str) -> str:
    """переводит числительное с английского на русский от 0 до 10"""
    str_out = nums_dict.get(value)
    return str_out


print(num_translate("nine"))
print(num_translate("eight"))
print(num_translate("one"))
print(num_translate("zero"))