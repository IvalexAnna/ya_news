# test_example.py
def one_more(x):
    return x + 1


def test_correct():
    print('Правильный тест')  # Новая строка.
    assert one_more(4) == 5


def test_fail():
    print('Неправильный тест')  # Новая строка.
    assert one_more(3) == 5
