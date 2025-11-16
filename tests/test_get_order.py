import allure
import requests

from data import Endpoints, Message
from help import GetIngredients


@allure.suite('Проверки получения информации о заказе')
class TestGetOrder:
    @allure.title('Проверка получения информации о заказе с авторизацией')
    def test_get_order_with_login(self, user_full_cycle):
        token = user_full_cycle[1].json()['accessToken']
        data_ingredients = GetIngredients.get_ingredients()
        order = requests.post(f'{Endpoints.CREATE_ORDER_URL}', data={'ingredients': data_ingredients},
                              headers={'Authorization': f'{token}'})
        order_id = order.json()['order']['number']
        get_order = requests.get(f'{Endpoints.USER_ORDER_INFO_URL}/{order_id}', headers={'Authorization': f'{token}'})
        order_info = get_order.json()
        assert get_order.status_code == 200 and order_info['success'] is True and len(order_info['orders']) == 1
        assert len(order_info['orders'][0]['ingredients']) == len(data_ingredients)
        assert order_info['orders'][0]['ingredients'][0] == data_ingredients[0]

    @allure.title('Проверка получения информации о заказе без авторизации')
    def test_get_order_without_login(self):
        token = ''
        get_order = requests.get(f'{Endpoints.USER_ORDER_INFO_URL}/{""}', headers={'Authorization': f'{token}'})
        assert get_order.status_code == 401 and get_order.json()['message'] == Message.ERROR_MESSAGE_NOT_AUTHORIZE