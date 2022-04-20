import pytest


def test_get_users(client):
    """
    Test for getting all users
    """
    response = client.get("/users/")
    assert response.status_code == 200


@pytest.mark.parametrize("name, age, email, password, expected_status_code",
                         [("User", 32, "user@example.com", "user1", 201),
                          ("User2", 26, "user@example.com", "user2", 409),
                          ("User3", 12, "", "user3", 400)])
def test_create_user(client, name, age, email, password, expected_status_code):
    """
    Test for creating a user
    """
    response = client.post("/new/", data={"name": name, "age": age, "email": email, "password": password})
    assert response.status_code == expected_status_code
