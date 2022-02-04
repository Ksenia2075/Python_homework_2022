from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = []
    for x in range(count):
        idx = randrange(len(nouns))
        ix = randrange(len(adverbs))
        dx = randrange(len(adjectives))
        list_out.append(f'{nouns[idx]} {adverbs[ix]} {adjectives[dx]}')
    return list_out
    return list_out