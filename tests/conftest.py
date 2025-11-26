import pytest
import requests

import help
from data import Endpoints
from help import User


@pytest.fixture
def user_registration_and_login():
    created_user = requests.post(f'{Endpoints.USER_REGISTER_URL}', data=User.valid_user)
    login_user = requests.post(f'{Endpoints.USER_LOGIN_URL}', data=User.valid_user)
    yield created_user, login_user


@pytest.fixture
def user_full_cycle(user_registration_and_login):
    created_user, login_user = user_registration_and_login
    yield created_user, login_user
    requests.delete(f'{Endpoints.USER_DELETE_URL}', data=User.valid_user)

