# Проект FitLife - MVP версия 1.0


WATER_PER_KG = 30
ML_IN_L = 1000


def getting_user_name():
    """Сохранение имени пользователя"""
    user_name = input('Как вас зовут? ')
    return user_name.title().strip()


def getting_user_age():
    """Сохранение возраста пользователя"""
    return int(input('Сколько вам полных лет? '))


def getting_user_weight():
    """Сохранение веса пользователя"""
    while True:
        try:
            user_weight = float(input('Сколько вы весите (в кг)? '))
            break
        except ValueError:
            print('Извините, не получилось перевести число в', end=' ')
            print('необходимый формат. Пожалуйста, попробуйте ещё ра', end='')
            print('з введите ваш веc в кг, например, 69 или 72 или 91.')
    return user_weight


def getting_user_height():
    """Сохранение роста пользователя"""
    return float(input('Каков ваш рост (в метрах, например, 1.75)? '))


def calculate_bmi(user_weight, user_height):
    """Расчет ИМТ/bmi"""
    bmi = user_weight / (user_height ** 2)
    return round(bmi, 1)


def calculate_water_recommendation(user_weight):
    """Расчет нормы воды"""
    water_ml = user_weight * WATER_PER_KG
    return water_ml / ML_IN_L


def fit_life():
    """Цепочка функций, выполняющая программу"""
    print('Привет, я бот, помогающий с фитнесом! Хочу рассчитать ваш', end=' ')
    print('ИМТ и норму воды, для этого мне потребуются ваши данные.')
    user_name = getting_user_name()
    user_age = getting_user_age()
    user_weight = getting_user_weight()
    user_height = getting_user_height()
    print(f'Отчёт для пользователя: {user_name} ({user_age} г.)')
    bmi = calculate_bmi(user_weight, user_height)
    print(f'Твой индекс массы тела: {bmi}')
    water_l = calculate_water_recommendation(user_weight)
    print(f'Рекомендуемая норма воды: {water_l} л. в день')
    print('Расчет окончен. Будь здоров!')


fit_life()
