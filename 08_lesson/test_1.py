import requests
from config import API_TOKEN
from config import LOGIN
from config import PASSWORD

base_url = 'https://ru.yougile.com/api-v2'
token = API_TOKEN
login = LOGIN
password = PASSWORD


def test_auth():
    '#авторизация'
    creds = {
        "login": LOGIN,
        "password": PASSWORD
        }
    resp = requests.post(base_url + '/auth/companies', json=creds)
    assert resp.status_code == 200


def test_get_projects():
    '#позитивный'
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    resp = requests.get(base_url + '/projects', headers=headers)
    assert resp.status_code == 200


def test_get_projects_without_headears():
    '#негативный'
    resp = requests.get(base_url + '/projects')
    assert resp.status_code == 401


def test_create_project():
    '#позитивный'
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    project = {"title": "Новый проект"}
    resp = requests.post(base_url + '/projects', json=project, headers=headers)
    assert resp.status_code == 201


def test_create_empty():
    '#негативный'
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    project = {"title": ""}
    resp = requests.post(base_url + '/projects', json=project, headers=headers)
    assert resp.status_code == 400


def test_change_project():
    '#позитивный'
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    create_resp = requests.post(
        base_url + '/projects',
        json={"title": "Временный проект"},
        headers=headers
        )
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]
    update_data = {
        "title": "Новый проект - моей компании"
    }
    resp = requests.put(f"{base_url}/projects/{project_id}",
                        json=update_data, headers=headers)
    assert resp.status_code == 200


def test_change_project_wrong_id():
    '#негативный'
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    create_resp = requests.post(
        base_url + '/projects',
        json={"title": "Временный проект"},
        headers=headers
        )
    assert create_resp.status_code == 201
    create_resp.json()["id"]
    update_data = {
        "title": "Новый проект - моей компании"
    }
    resp = requests.put(f"{base_url}/projects/13",
                        json=update_data, headers=headers)
    assert resp.status_code == 404
