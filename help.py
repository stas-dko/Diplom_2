import requests
import allure
from faker import Faker
from data import Endpoints


class CreateRandomUser:
    @staticmethod
    @allure.step("Создание случайного пользователя")
    def create_random_user():
        faker = Faker('ru_RU')
        user = {
            'email': faker.email(),
            'password': faker.password(),
            'name': faker.name()
        }
        return user

    @staticmethod
    @allure.step("Создание случайного пользователя без email")
    def create_random_user_without_email():
        faker = Faker('ru_RU')
        user = {
            'email': '',
            'password': faker.password(),
            'name': faker.name()
        }
        return user

    @staticmethod
    @allure.step("Создание случайного пользователя без пароля")
    def create_random_user_without_password():
        faker = Faker('ru_RU')
        user = {
            'email': faker.email(),
            'password': '',
            'name': faker.name()
        }
        return user

    @staticmethod
    @allure.step("Создание случайного пользователя без имени")
    def create_random_user_without_name():
        faker = Faker('ru_RU')
        user = {
            'email': faker.email(),
            'password': faker.password(),
            'name': ''
        }
        return user

    @staticmethod
    @allure.step("Создание случайного пользователя без данных")
    def create_random_user_without_data():
        user = {
            'email': '',
            'password': '',
            'name': ''
        }
        return user


class User:
    valid_user = CreateRandomUser.create_random_user()
    invalid_user_without_email = CreateRandomUser.create_random_user_without_email()
    invalid_user_without_password = CreateRandomUser.create_random_user_without_password()
    invalid_user_without_name = CreateRandomUser.create_random_user_without_name()
    invalid_user_without_data = CreateRandomUser.create_random_user_without_data()


class RegisterLoginDeleteUser:
    @staticmethod
    @allure.step("Регистрация пользователя")
    def register_user():
        valid_user = User.valid_user
        response = requests.post(f'{Endpoints.USER_REGISTER_URL}', data=valid_user)
        return {'response_text': response.text, 'status_code': response.status_code, 'data_user': valid_user}


class LaiUser:
    lai_user = {
        'email': 'akkakiy@gmailcom',
        'password': 'Zaq12wsxcde34rfv',
        'name': 'Maximka'
    }


class GetIngredients:
    @staticmethod
    @allure.step("Получение списка ингредиентов")
    def get_ingredients(limit=4):
        response = requests.get(f'{Endpoints.INGREDIENTS_URL}')
        ingredients = response.json()['data']
        ingredients_list = []
        for i in ingredients:
            ingredients_list.append(i['_id'])
            if len(ingredients_list) == limit:
                break
        return ingredients_list