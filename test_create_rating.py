import pytest

STARS_ERROR = "number of stars must be between 1 and 5 (inclusive)"

def test_base_choice_is_saved(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}
    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 201
    assert res.json()["stars"] == 3
    assert res.json()["pizza_id"] == pizza_id


@pytest.mark.parametrize("stars", [0, 6])
def test_stars_out_of_range(api, auth, pizza_id, stars):
    new = {"pizza_id": pizza_id, "stars": stars}
    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 400
    assert res.json() == {"error": STARS_ERROR}


def test_stars_decimal(api, auth, pizza_id):
    # C2: decimal
    pass


def test_stars_text(api, auth, pizza_id):
    # C2: text
    pass


def test_stars_missing(api, auth, pizza_id):
    # C2: missing
    pass


def test_pizza_not_found(api, auth):
    # C3: nonexistent pizza
    pass


def test_rating_without_token(api, pizza_id):
    # C4: no token
    pass


def test_rating_with_short_token(api, pizza_id):
    # C4: wrong-length token
    pass