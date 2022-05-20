import pytest
from funcy import compact, select

# Создаем фикстуру
# Запускается перед каждым тестом


@pytest.fixture
def coll():  # имя фикстуры выбирается произвольно
    return ['One', True, 3, [1, 'hexlet', [0]], 'cat', {}, '', [], False, 'hi']

# Pytest сам прокидывает результат вызова функции там, где она указана в аргументе.
# Имя параметра совпадает с именем фикстуры


def test_compact(coll):
    result = compact(coll)    
    assert result == ['One', True, 3, [1, 'hexlet', [0]], 'cat', 'hi']

# Не важно, что предыдущий тест сделал с коллекцией.
# Здесь она будет новая, так как pytest вызывает coll() заново


def test_select(coll):
    result = select(lambda x: x, coll)
    assert result == ['One', True, 3, [1, 'hexlet', [0]], 'cat', 'hi']
