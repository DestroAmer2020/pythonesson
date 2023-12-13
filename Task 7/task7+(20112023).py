def setup_charivna_kulka(additional_answers):
    """
    Налаштовує чарівну кульку, додаючи додаткові відповіді.

    Параметри:
    - additional_answers (list): Список додаткових відповідей для додавання.

    Повертає:
    None

    Приклад використання:
    >>> setup_charivna_kulka(["Зовсім невідомо", "Запитайте пізніше"])
    """
    global possible_answers
    possible_answers.extend(additional_answers)

# Тести
def test_setup_charivna_kulka():
    initial_possible_answers = ["Так", "Ні", "Можливо", "Не зовсім впевнений", "Спробуйте ще раз пізніше"]

    # Перевірка додавання додаткових відповідей
    setup_charivna_kulka(["Зовсім невідомо", "Запитайте пізніше"])
    assert len(possible_answers) == len(initial_possible_answers) + 2, "Некоректне додавання додаткових відповідей"

    # Перевірка, що функція setup_charivna_kulka не змінює вихідний список відповідей
    assert possible_answers[:len(initial_possible_answers)] == initial_possible_answers, "Вихідний список відповідей був змінений"

    # Перевірка додавання порожнього списку відповідей
    setup_charivna_kulka([])
    assert len(possible_answers) == len(initial_possible_answers) + 2, "Некоректна реакція на порожній список відповідей"

    print("Тести пройдено успішно.")

# Запуск тестів для setup_charivna_kulka
test_setup_charivna_kulka()
