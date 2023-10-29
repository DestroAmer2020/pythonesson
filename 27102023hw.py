import random

def charivna_kulka(question, custom_answers=None):
    """
    Генерує випадкову відповідь на поставлене питання.
    :param question: Рядок, який містить питання, на яке потрібно отримати відповідь.
    :param custom_answers: Список додаткових відповідей, які можна додати до базового списку відповідей кульки.
    :return: Рядок, який містить випадкову відповідь.
    """
    base_answers = ["Так", "Ні", "Можливо", "Не маю поняття"]
    
    if custom_answers:
        base_answers.extend(custom_answers)
    
    if not question or not isinstance(question, str):
        return "Будь ласка, введіть дійсне питання."
    
    return random.choice(base_answers)

# Тести для функції charivna_kulka
def test_charivna_kulka():
    # Перевірка на повернення одного з очікуваних значень
    response = charivna_kulka("Чи сьогодні буде дощ?")
    assert response in ["Так", "Ні", "Можливо", "Не маю поняття"]

    # Перевірка, що функція повертає значення типу str
    response = charivna_kulka("Це тестове питання.")
    assert isinstance(response, str)

    # Перевірка реакції на пусте питання або на введення, яке не є рядком
    response = charivna_kulka("")
    assert response == "Будь ласка, введіть дійсне питання."

    response = charivna_kulka(42)
    assert response == "Будь ласка, введіть дійсне питання."

# Функція для налаштування "чарівної кульки" з додатковими відповідями
def setup_charivna_kulka(custom_answers):
    """
    Налаштовує "чарівну кульку" додатковими відповідями.

    :param custom_answers: Список додаткових відповідей, які будуть додані до базового списку відповідей кульки.
    """
    if not isinstance(custom_answers, list):
        print("Список додаткових відповідей повинен бути типу list.")
        return
    
    global base_answers
    base_answers.extend(custom_answers)

# Тести для функції setup_charivna_kulka
def test_setup_charivna_kulka():
    setup_charivna_kulka(["Звісно!", "Спробуй ще раз", "Питай ще"])
    response = charivna_kulka("Чи все буде добре?")
    assert response in ["Так", "Ні", "Можливо", "Не маю поняття", "Звісно!", "Спробуй ще раз", "Питай ще"]

# Виконати тести для функцій charivna_kulka та setup_charivna_kulka
test_charivna_kulka()
test_setup_charivna_kulka()