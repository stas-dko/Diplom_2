# data.py

class Endpoints:
    MAIN_URL = 'https://stellarburgers.education-services.ru/' 

    INGREDIENTS_URL = f'{MAIN_URL}api/ingredients'           
    CREATE_ORDER_URL = f'{MAIN_URL}api/orders'               # url для создания заказа
    RESET_PASSWORD_URL = f'{MAIN_URL}api/password-reset'     # url для сброса пароля
    USER_REGISTER_URL = f'{MAIN_URL}api/auth/register'       # url для регистрации
    USER_LOGIN_URL = f'{MAIN_URL}api/auth/login'             # url для авторизации
    USER_LOGOUT_URL = f'{MAIN_URL}api/auth/logout'           # url для выхода
    TOKEN_URL = f'{MAIN_URL}api/auth/token'                  # url для получения токена
    USER_INFO_URL = f'{MAIN_URL}api/auth/user'               # url для получения информации о пользователе
    USER_UPDATE_URL = f'{MAIN_URL}api/auth/user'             # url для изменения данных о пользователе
    USER_DELETE_URL = f'{MAIN_URL}api/auth/user'             # url для удаления пользователя
    ALL_ORDERS_URL = f'{MAIN_URL}api/orders/all'             # url для получения информации о всех заказах
    USER_ORDER_INFO_URL = f'{MAIN_URL}api/orders'            # url для получения информации о конкретном заказе


class Message:
    # сообщения об ошибках при создании заказа без ингредиентов
    ERROR_MESSAGE_INGREDIENT = 'Ingredient ids must be provided'

    # сообщения об ошибках при создании существующего пользователя
    ERROR_MESSAGE_CREATE_DUPLICATE = '{"success":false,"message":"User already exists"}'

    # сообщения об ошибках при создании пользователя без данных
    ERROR_MESSAGE_CREATE_DATA_INCORRECT = 'Email, password and name are required fields'

    # сообщения об ошибках при авторизации пользователя
    ERROR_MESSAGE_AUTHORIZE_AND_LOGIN_INCORRECT = 'email or password are incorrect'

    # сообщения об ошибках при получении/обновлении информации о пользователе
    ERROR_MESSAGE_EMAIL_EXIST = 'User with such email already exists'

    # сообщения об ошибках при получении заказа без авторизации
    ERROR_MESSAGE_NOT_AUTHORIZE = 'You should be authorised'