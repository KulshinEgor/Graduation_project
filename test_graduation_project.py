import graduation_project
import pytest

# Егор Кульшин, 9-я когорта — Финальный проект. Инженер по тестированию плюс
def test_get_orders_success():
    actual = graduation_project.get_orders()
    expected = 200
    assert actual == expected
    if actual == expected:
        print('Тест пройден')
    else:
        print('Тест провален')