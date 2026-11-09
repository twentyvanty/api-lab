
import pytest

@pytest.mark.parametrize("stars, expected_status, expected_stars", [
    (0, 400, 3),
    (1, 200, 1),
    (5, 200, 5),
    (6, 400, 3),
])
def test_update_rating_boundaries(
    api, auth, rating, stars, expected_status, expected_stars
):
    new = {"stars": stars}

    res = api.put(
        f"/api/ratings/{rating['id']}",
        json=new,
        headers=auth
    )

    assert res.status_code == expected_status

    # Read the rating again to check whether it was saved.
    check = api.get(
        f"/api/ratings/{rating['id']}",
        headers=auth
    )

    assert check.status_code == 200
    assert check.json()["stars"] == expected_stars
