def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

# Для подтверждения того, что данный скрипт был запущен напрямую,
# а не вызван внутри другого файла в качестве модуля. Весь код написанный
# в теле этого условия будет выполнен только если пользователь запустил файл самостоятельно.
if __name__ == "__main__":
    test_abs1()
    print("All tests passed!")

