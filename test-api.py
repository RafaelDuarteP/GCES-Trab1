import pytest
import requests

base_url = 'http://localhost:80/api'  # Substitua pela URL correta da API


@pytest.fixture
def auth_token():

    register_user('username_example', 'example@example.com', 'example',
                  'example', 'password')

    login_response = login_user('username_example', 'password')
    token = login_response['token']
    return token


def register_user(username, email, first_name, last_name, password):
    url = f'{base_url}/auth/register'
    data = {
        'username': username,
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'password': password
    }
    response = requests.post(url, json=data)
    return response.json()


def login_user(username, password):
    url = f'{base_url}/auth/login'
    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)
    return response.json()


def test_get_books_unauthenticated():
    url = f'{base_url}/api/books'
    response = requests.get(url)
    assert response.status_code == 401


def test_get_books_authenticated(auth_token):
    url = f'{base_url}/api/books'
    headers = {'Authorization': f'Token {auth_token}'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert response.json() == []


def test_create_book(auth_token):
    url = f'{base_url}/api/books'
    headers = {'Authorization': f'Token {auth_token}'}
    data = {
        'title': 'Example Book',
        'author': 'Example Author',
        'release_year': 2023
    }
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 201
    assert 'id' in response.json()
