def odd_nums(number: int) -> int:
    # создаем генератор для нечетных чисел в диапазоне от 1 до n без yield
    return (num for num in range(1, n + 1, 2))


n = 15
generator = odd_nums(n)
for _ in range(1, n+1, 2):
    print(next(generator))
#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration