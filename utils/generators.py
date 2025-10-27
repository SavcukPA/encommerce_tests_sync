import random
import string
from typing import Literal

def get_random_str(
        len: int = 5,
        use_latin: bool = True,
        use_cyrillic: bool = False,
        use_digits: bool = False,
        use_special: bool = False,
        case_type: Literal["lower", "upper", "mixed", "title", "capitalize"] = "mixed"
) -> str:
    """
    Генератор случайных строк с фиксированной длиной и разными регистрами.

    Args:
        len: Длина строки
        use_latin: Использовать латинские буквы
        use_cyrillic: Использовать кириллические буквы
        use_digits: Использовать цифры
        use_special: Использовать специальные символы
        case_type: Тип регистра:
            - "lower": все символы в нижнем регистре
            - "upper": все символы в верхнем регистре
            - "mixed": случайный регистр для каждого символа
            - "title": каждое слово с заглавной буквы
            - "capitalize": первая буква заглавная, остальные строчные

    Returns:
        Случайная строка
    """
    if len <= 0:
        raise ValueError("Длина должна быть положительным числом")

    chars = ""

    if use_latin:
        chars += string.ascii_letters
    if use_cyrillic:
        chars += "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if not chars:
        raise ValueError("Должен быть выбран хотя бы один тип символов")

    # Генерируем базовую строку
    result = "".join(random.choice(chars) for _ in range(len))

    # Применяем регистр в зависимости от case_type
    if case_type == "lower":
        result = result.lower()
    elif case_type == "upper":
        result = result.upper()
    elif case_type == "mixed":
        # Оставляем как есть - уже смешанный регистр из chars
        pass
    elif case_type == "title":
        result = result.title()
    elif case_type == "capitalize":
        result = result.capitalize()
    else:
        raise ValueError(f"Неизвестный тип регистра: {case_type}")

    return result