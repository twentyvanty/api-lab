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
1.
2.
3.
4.
5.
6.
7.
8.