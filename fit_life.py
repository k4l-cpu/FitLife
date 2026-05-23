# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
ML_IN_LITER = 1000

# Ввод имени пользователя
user_name = input("Здравствуйте, давайте познакомимся, как вас зовут?  ")
# Ввод возраста
user_age = int(input("Сообщите ваш возраст?  "))
# Ввод веса
user_wegtht = float(input("Ваш вес в кг?  "))
# Ввод роста
try:
    user_height = float(input("Ваш рост в метрах?  "))
except ValueError:
    user_height = float(input("Вводить данные нужно через точку,\
например 1.75. Ваш рост в метрах?  "))

# Расчет ИМТ: вес разделить на (рост в квадрате)
bmi = user_wegtht / user_height**2

# Подсчет воды: вес * 30 мл
water_needed = user_wegtht * WATER_PER_KG

# Вывод результатов расчета
print()
print(f'Вот ваши показатели и рекомендации {user_name}:')
print()
print(f'Ваш возраст {user_age}, индекс массы тела {round(bmi, 1)}')
print(f'Норма потребления воды {water_needed / ML_IN_LITER:.1f} л. в день')
print()
print("Расчет окончен. Будьте здоровы!")
