import pytest
from conftest import client


def test_1(client):
    rv = client.get('/ex1?X=1')
    assert rv.status_code == 400

def test_2(client):
    rv = client.get('/ex1?X=1a')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 1}

def test_3(client):
    rv = client.get('/ex1?X=1056da')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 2}

def test_4(client):
    rv = client.get('/ex1?X=20&Y=aaa')
    assert rv.status_code == 400

def test_5(client):
    rv = client.get('/ex1?X=!aaaa')
    assert rv.status_code == 400

def test_6(client):
    rv = client.get('/ex1?Y=aaaa')
    assert rv.status_code == 400
    
def test_7(client):
    rv = client.get('/ex1?X=1aaa1!..s')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 0.5}

def test_8(client):
    rv = client.get('/ex1?X=1234ciaociaociaociao')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 0.25}

def test_9(client):
    rv = client.get('/ex1?X=1234')
    assert rv.status_code == 400

def test_10(client):
    rv = client.get('/ex1?X=!ciao@22')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 0.5}