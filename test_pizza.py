import requests
SITE = "https://quickpizza.grafana.com"
AUTH = {"Authorization": "token abcdef0123456789"}
VEGETARIAN = {"mustBeVegetarian": True}
# A vegetarian request gets a named pizza with vegetarian ingredients only.
def test_vegetarian_pizza():
 res = requests.post(SITE + "/api/pizza", json=VEGETARIAN, headers=AUTH)
 assert res.status_code == 200
 body = res.json()
 assert body["pizza"]["name"] != ""
 for ingredient in body["pizza"]["ingredients"]:
  assert ingredient["vegetarian"] is True, ingredient["name"]