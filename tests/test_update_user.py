import allure
import pytest
import requests

from data import Endpoints, Message
from help import User, CreateRandomUser


@allure.suite('Проверки изменения данных пользователя')
class TestUpdateUser:
    @allure.title('Проверка изменения данных при авторизации')
    @pytest.mark.parametrize('field_to_update', ['email', 'password', 'name'])
    def test_update_user(self, field_to_update):
        new_user = CreateRandomUser.create_random_user()
        register_user = requests.post(f'{Endpoints.USER_REGISTER_URL}', data=new_user)
        get_token = register_user.json()['accessToken']
        update = requests.patch(f'{Endpoints.USER_UPDATE_URL}',
                                data=field_to_update, headers={'Authorization': f'{get_token}'})
        requests.delete(f'{Endpoints.USER_DELETE_URL}', data=new_user)
        assert update.status_code == 200 and update.json()['success'] is True

    @allure.title('Проверка изменения данных без авторизации')
    @pytest.mark.parametrize('field_to_update', ['email', 'password', 'name'])
    def test_update_user_without_login(self, field_to_update):
        requests.post(f'{Endpoints.USER_REGISTER_URL}', data=User.valid_user)
        get_token = None
        response = requests.patch(f'{Endpoints.USER_UPDATE_URL}',
                                  data=User.valid_user,
                                  headers={'Authorization': f'{get_token}'})
        assert response.status_code == 401
        assert response.json()['success'] is False
        assert response.json()['message'] == Message.ERROR_MESSAGE_NOT_AUTHORIZE