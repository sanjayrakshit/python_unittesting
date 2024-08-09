import pytest
import requests

import src.service as service
import unittest.mock as mock


@mock.patch("src.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)
    assert user_name == "Mocked Alice"


@mock.patch("requests.get")
def test_get_posts(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    expected_post = [
        {
            "userId": 1,
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
        }
    ]
    mock_response.json.return_value = expected_post
    mock_get.return_value = mock_response
    assert service.get_posts() == expected_post


@mock.patch("requests.get")
def test_get_posts_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_posts()
