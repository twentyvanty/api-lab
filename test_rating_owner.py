
import uuid


def make_other_user(api):
    """Create and log in a second user."""
    name = "lab-" + uuid.uuid4().hex[:12]
    user = {"username": name, "password": "Pizza-2026"}

    res = api.post("/api/users", json=user)
    assert res.status_code == 201

    res = api.post("/api/users/token/login", json=user)
    assert res.status_code == 200

    return {"Authorization": "token " + res.json()["token"]}


def test_other_user_cannot_read_rating(api, auth, rating):
    other_auth = make_other_user(api)

    res = api.get(
        f"/api/ratings/{rating['id']}",
        headers=other_auth
    )

    assert 400 <= res.status_code <= 499

    # The owner can still read the original rating.
    owner_res = api.get(
        f"/api/ratings/{rating['id']}",
        headers=auth
    )
    assert owner_res.status_code == 200
    assert owner_res.json()["stars"] == 3


def test_other_user_cannot_change_rating(api, auth, rating):
    other_auth = make_other_user(api)

    res = api.put(
        f"/api/ratings/{rating['id']}",
        json={"stars": 5},
        headers=other_auth
    )

    assert 400 <= res.status_code <= 499

    # Check that the rating was not changed.
    owner_res = api.get(
        f"/api/ratings/{rating['id']}",
        headers=auth
    )
    assert owner_res.status_code == 200
    assert owner_res.json()["stars"] == 3


def test_other_user_cannot_delete_rating(api, auth, rating):
    other_auth = make_other_user(api)

    res = api.delete(
        f"/api/ratings/{rating['id']}",
        headers=other_auth
    )

    assert 400 <= res.status_code <= 499

    # Check that the owner can still read the rating.
    owner_res = api.get(
        f"/api/ratings/{rating['id']}",
        headers=auth
    )
    assert owner_res.status_code == 200
    assert owner_res.json()["stars"] == 3
