import requests

# Target URI looks like this (reference when framing parameters): https://opentdb.com/api.php?amount=10&type=boolean

QUESTION_AMOUNT = 10
QUESTION_TYPE = "boolean"

request_parameters = {
    "amount": QUESTION_AMOUNT,
    "type": QUESTION_TYPE,
}

response = requests.get("https://opentdb.com/api.php", params=request_parameters)
response.raise_for_status()
data = response.json()

question_data = data['results']