import requests
import pytest
from config import API_TOKEN
from config import LOGIN
from config import PASSWORD

base_url = 'https://ru.yougile.com/api-v2'
token = API_TOKEN
login = LOGIN
password = PASSWORD

#авторизация
def test_auth():
    creds = {
        "login": LOGIN,
        "password": PASSWORD,
        "name": "QA 114.2"
        }
    resp = requests.post(base_url + '/auth/companies', json=creds)
    assert resp.status_code == 200

#позитивный
def test_get_projects():
    global token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    resp = requests.get(base_url + '/projects', headers=headers)
    assert resp.status_code == 200

#негативный
def test_get_projects_without_headears():
    global token
    resp = requests.get(base_url + '/projects')
    assert resp.status_code == 401
    
#позитивный
def test_create_project():
    global token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    project = {
    "title": "Новый проект",
    "users": {
        "056b9ac2-1235-46e0-8af8-3b1c5c9c03fa": "admin"
    }
    }
    resp = requests.post(base_url + '/projects', json=project, headers=headers)
    assert resp.status_code == 201

#негативный
def test_create_empty():
    global token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    project = {
        "title": "",
        "users": {
            "056b9ac2-1235-46e0-8af8-3b1c5c9c03fa": "admin"
        }
    }
    resp = requests.post(base_url + '/projects', json=project, headers=headers)
    assert resp.status_code == 400

#позитивный
def test_change_project():
    global token
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
    resp = requests.put(f"{base_url}/projects/{project_id}",json=update_data, headers=headers)
    assert resp.status_code == 200

#негативный
def test_change_project_wrong_id():
    global token
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
    resp = requests.put(f"{base_url}/projects/13",json=update_data, headers=headers)
    assert resp.status_code == 404





