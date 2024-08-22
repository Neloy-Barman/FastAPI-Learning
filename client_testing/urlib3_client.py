import json
import urllib3

body = {
    "name": "Neloy Barman",
    "email": "neloycareer018@gmail.com"
}

client = urllib3.PoolManager()

try:
    response = client.request(
        method="POST",
        url="http://127.0.0.1:8000",
        body= json.dumps(body),
        # json=body
    )

    status = response.status

    decoded_response_data = json.loads(response.data.decode('utf-8'))

    print(f"Response Status: {status}")
    print(f"Decoded response data: {decoded_response_data}")
    print(f"Response Message: {decoded_response_data['message']}")
except (Exception) as e:
    print(f"An error has occured: {e}")

# print(type(response.data))

print("Everything worked so far")