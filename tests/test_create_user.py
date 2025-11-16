import allure
import pytest
import requests

from data import Endpoints, Message
from help import User, RegisterLoginDeleteUser, CreateRandomUser


@allure.suite('Проверки регистрации пользователя')
class TestCreateUser:
    @allure.title('Проверка регистрации пользователя')
    def test_create_user(self):
        new_user = CreateRandomUser.create_random_user()
        register_user = requests.post(f'{Endpoints.USER_REGISTER_URL}', data=new_user)
        requests.delete(f'{Endpoints.USER_DELETE_URL}', data=new_user)
        assert register_user.status_code == 200
        assert register_user.json()['success'] is True

    @allure.title('Проверка регистрации пользователя без заполнения одного или всех обязательных полей')
    @pytest.mark.parametrize('user', [User.invalid_user_without_email,
                                      User.invalid_user_without_password,
                                      User.invalid_user_without_name,
                                      User.invalid_user_without_data])
    def test_create_user_without_fields(self, user):
        response = requests.post(f'{Endpoints.USER_REGISTER_URL}', data=user)
        assert response.status_code == 403 and response.json()['message'] == Message.ERROR_MESSAGE_CREATE_DATA_INCORRECT

    @allure.title('Проверка регистрации существующего пользователя')
    def test_create_duplicate_user(self):
        requests.post(f'{Endpoints.USER_REGISTER_URL}', data=User.valid_user)
        response = RegisterLoginDeleteUser.register_user()
        assert response['status_code'] == 403
        assert response['response_text'] == Message.ERROR_MESSAGE_CREATE_DUPLICATE