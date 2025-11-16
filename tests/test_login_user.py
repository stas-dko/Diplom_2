import allure
import requests

from data import Endpoints, Message
from help import LaiUser, User


@allure.suite('Проверки авторизации пользователя')
class TestLoginUser:
    @allure.title('Проверка авторизации пользователя')
    def test_login_user(self):
        requests.post(f'{Endpoints.USER_REGISTER_URL}', data=User.valid_user)
        login_user = requests.post(f'{Endpoints.USER_LOGIN_URL}',
                                   data=User.valid_user)
        requests.delete(f'{Endpoints.USER_DELETE_URL}', data=User.valid_user)
        assert login_user.status_code == 200
        assert login_user.json()['success'] is True

    @allure.title('Проверка авторизации несуществующего пользователя')
    def test_login_lai_user(self):
        response = requests.post(f'{Endpoints.USER_LOGIN_URL}', data=LaiUser.lai_user)
        assert response.status_code == 401
        assert response.json()['message'] == Message.ERROR_MESSAGE_AUTHORIZE_AND_LOGIN_INCORRECT