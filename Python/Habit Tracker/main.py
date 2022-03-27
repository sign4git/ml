import requests
import datetime as dt
from decouple import config

TODAYS_DATE = dt.datetime.now().strftime('%Y%m%d')
PIXELA_HOSTNAME = "https://pixe.la/v1/users"
USERNAME = config('USERNAME', default='')
TOKEN = config('TOKEN', default='')
headers = {
    "X-USER-TOKEN": TOKEN
}
GRAPHID = "walkid"
# PIXELA CREATE USER

# request_body = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response = requests.post(f"{PIXELA_HOSTNAME}", json=request_body)
# response.raise_for_status()
# print(response.text)


# CREATE GRAPHS
# request_body = {
#     "id": "walkid",
#     "name": "walkname",
#     "unit": "hours",
#     "type": "float",
#     "color": "sora"
# }
#
#
# create_graphs_response = requests.post(f"{PIXELA_HOSTNAME}/{USERNAME}/graphs", json=request_body, headers=headers)
# create_graphs_response.raise_for_status()
# print(create_graphs_response.url)
# print(create_graphs_response.text)

# GET GRAPHS
# get_graphs_response = requests.get(f"{PIXELA_HOSTNAME}/{USERNAME}/graphs", headers=headers)
# get_graphs_response.raise_for_status()
# print(get_graphs_response.url)
# print(get_graphs_response.text)

# POST PIXEL GRAPH BY ID
request_body = {
    # "date": "20220319",
    "quantity": "10.0"
}
# post_pixel_response = requests.post(f"{PIXELA_HOSTNAME}/{USERNAME}/graphs/{GRAPHID}", headers=headers,
#                                     json=request_body)
# post_pixel_response.raise_for_status()

# UPDATE PIXEL GRAPH BY ID AND DAY
# put_pixel_response = requests.put(f"{PIXELA_HOSTNAME}/{USERNAME}/graphs/{GRAPHID}/20220319", headers=headers,
#                                     json=request_body)
# put_pixel_response.raise_for_status()

# DELETE PIXEL GRAPH BY ID AND DAY
delete_pixel_response = requests.delete(f"{PIXELA_HOSTNAME}/{USERNAME}/graphs/{GRAPHID}/20220319", headers=headers)
delete_pixel_response.raise_for_status()
