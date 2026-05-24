# Проект FitLife - MVP версия 1.1

WATER_PER_KG = 30
ML_IN_LITER = 1000

user_name = input("Здравствуйте, давайте познакомимся,"
                  "как вас зовут?  ").title()
try:
    user_age = int(input("Сообщите ваш возраст?  "))
except ValueError:
    user_age = int(input("Введите количество полных лет "))

user_weight = float(input("Ваш вес в кг?  ").replace(',', '.', 1))

user_height = float(input("Ваш рост в метрах?  ").replace(',', '.', 1))


def calc_bmi(wegtht, height):
    """
        Возвращает индекс массы тела

    Параметры:
            weight (float): вес - число с плавающей точкой
            height (float): рост - число с плавающей точкойbdfy

    Возвращаемое значение:
            (float): имт - число с плавающей точкой
    """
    return wegtht / height**2


def calc_water_needed(weight):
    """
        Возвращает норму потребления воды

    Параметры:
            weight (float): вес - число с плавающей точкой

    Возвращаемое значение:
            (float): норма воды - число с плавающей точкой
    """
    return (weight * WATER_PER_KG) / ML_IN_LITER


bmi = round(calc_bmi(user_weight, user_height), 1)
water_needed = calc_water_needed(user_weight)

print()
print(f'Вот ваши показатели и рекомендации {user_name}:')
print()
print(f'Ваш возраст {user_age}, индекс массы тела {bmi}')
print(f'Норма потребления воды {water_needed:.1f} л. в день')
print()
print("Расчет окончен. Будьте здоровы!")
