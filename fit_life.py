# Проект FitLife - MVP версия 1.0


WATER_PER_KG = 30
ML_IN_L = 1000


def getting_info():
    """Сбор данных пользователя"""
    user_name = input('Как вас зовут? ')
    user_name = user_name.title()
    user_age = int(input('Сколько вам лет? '))
    user_weight = float(input('Сколько вы весите (в кг)? '))
    user_height = float(input('Каков ваш рост (в метрах, например, 1.75)? '))
    return user_name, user_age, user_weight, user_height


def calculate_bmi(user_weight, user_height):
    """Расчет ИМТ/bmi"""
    bmi = user_weight / (user_height ** 2)
    bmi = round(bmi, 1)
    return bmi


def calculate_water_recommendation(user_weight):
    """Расчет нормы воды"""
    water_ml = user_weight * WATER_PER_KG
    water_l = water_ml / ML_IN_L
    return water_l


def program():
    """Цепочка функций, выполняющая программу"""
    print('Привет, я бот, помогающий с фитнесом!')
    print('Хочу рассчитать ваш ИМТ и норму воды, для этого мне', end=' ')
    print('потребуются ваши данные.')
    user_name, user_age, user_weight, user_height = getting_info()
    print(f'Отчёт для пользователя: {user_name} ({user_age} г.)')
    bmi = calculate_bmi(user_weight, user_height)
    print(f'Твой индекс массы тела: {bmi}')
    water_l = calculate_water_recommendation(user_weight)
    print(f'Рекомендуемая норма воды: {water_l} л. в день')
    print('Расчет окончен. Будьте здоровы!')
