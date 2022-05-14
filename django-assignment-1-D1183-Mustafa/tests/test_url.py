import pytest


# @pytest.mark.urls("mysite.urls")
# def test_urls_client(client):
#     response = client.get("polls/")
#     assert response.content == b"Hello, world. You're at the polls index."


@pytest.mark.urls("mysite.urls")
def test_urls(client):
    assert b"Hello, world. You're at the polls index." in client.get("/polls/").content
