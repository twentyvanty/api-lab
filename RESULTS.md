# API lab results
## Part 0
- Step 0.1, the number of pizza names:243
- Step 0.3, status code of the request without a token:401
- Step 0.4, the name of your pizza: The stupid marinara
- Step 0.12, results of the three runs without a session (optional):-
- Step 0.16, blocks of "how many of the three tools are excluded": 2
## Defect report
- Title:Impossible pizza request returns HTTP 500
- Request:POST /api/pizza with all three tools excluded.
- Expected result:HTTP 400 with a JSON error message.
- Actual result:HTTP 500 with an empty response body.
- Severity:Medium – The API returns an internal server error instead of handling an invalid request properly.
## Part A
- Step A4, status codes when the other user reads, changes and deletes:
## Part B
1. Actual API tests can find networks problems while Unit test cannot fully detects the problems for its not communicate with the real server. by the others hand, unit test still useful for it run faster and can test individual components. 
2. Each test creates a new user to avoid sharing data with other tests or users. Applying in project 2, follow the ways to create own test data and using my own account or credentials.
3.-
4.The block where all three tools were excluded revealed the defect. The API returned HTTP 500 with an empty response body instead of HTTP 400 with a useful error message.
5. 72 tests
6. Read rating: HTTP [insert actual code], Change rating: HTTP [insert actual code], Delete rating: HTTP [insert actual code] I expect all three attempts to be refused because only the owner should access or modify the rating. Different 4xx status codes are not necessarily defects, as long as the API consistently prevents unauthorized access and the behavior matches its intended design.
7. {"ratings":[{"id":1,"stars":5,"pizza_id":1},{"id":2,"stars":1,"pizza_id":2},{"id":3,"stars":1,"pizza_id":3},{"id":5,"stars":5,"pizza_id":11},{"id":6,"stars":2,"pizza_id":1},{"id":7,"stars":5,"pizza_id":14},{"id":8,"stars":5,"pizza_id":15},{"id":9,"stars":5,"pizza_id":20},{"id":11,"stars":5,"pizza_id":27},{"id":12,"stars":5,"pizza_id":33},{"id":13,"stars":5,"pizza_id":35},{"id":17,"stars":5,"pizza_id":55},{"id":18,"stars":5,"pizza_id":60},{"id":19,"stars":5,"pizza_id":61},{"id":23,"stars":5,"pizza_id":78},{"id":24,"stars":5,"pizza_id":79},{"id":26,"stars":5,"pizza_id":82},{"id":27,"stars":5,"pizza_id":87},{"id":28,"stars":5,"pizza_id":88},{"id":30,"stars":5,"pizza_id":97},{"id":42,"stars":5,"pizza_id":135},{"id":43,"stars":5,"pizza_id":136},{"id":47,"stars":5,"pizza_id":176},{"id":48,"stars":5,"pizza_id":177},{"id":50,"stars":5,"pizza_id":186},{"id":51,"stars":5,"pizza_id":190},{"id":54,"stars":5,"pizza_id":198},{"id":55,"stars":5,"pizza_id":200},{"id":56,"stars":5,"pizza_id":203},{"id":57,"stars":5,"pizza_id":204},{"id":59,"stars":2,"pizza_id":1},{"id":60,"stars":5,"pizza_id":212},{"id":61,"stars":5,"pizza_id":213},{"id":62,"stars":5,"pizza_id":215},{"id":84,"stars":2,"pizza_id":1},{"id":88,"stars":5,"pizza_id":296},{"id":89,"stars":5,"pizza_id":297},{"id":90,"stars":5,"pizza_id":307},{"id":110,"stars":5,"pizza_id":371},{"id":111,"stars":5,"pizza_id":373},{"id":112,"stars":5,"pizza_id":388},{"id":113,"stars":2,"pizza_id":1},{"id":114,"stars":5,"pizza_id":392},{"id":115,"stars":5,"pizza_id":393},{"id":116,"stars":5,"pizza_id":394},{"id":120,"stars":5,"pizza_id":405},{"id":121,"stars":5,"pizza_id":406},{"id":122,"stars":5,"pizza_id":407},{"id":125,"stars":5,"pizza_id":422},{"id":127,"stars":5,"pizza_id":435}]} 
This is a security defect because an unauthorized stranger could read ratings belonging to other users. This exposes information without proper authentication. The API should reject the invalid token instead of returning the ratings.
8. An API test checks response status codes, response data, and validation rules more directly than a web page test. A web page test can check things that an API test cannot easily verify, such as the visual layout, buttons, navigation, and whether the page displays correctly to users.