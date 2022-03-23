import requests

response = requests.get("https://opentdb.com/api.php?amount=20&difficulty=hard&type=boolean")
response.raise_for_status()
data = response.json()["results"]

question_data = data
