import requests

def fetch_data():
    url = "https://opensky-network.org/api/states/all"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['states']
        return [(
            state[0], state[1].strip(), state[2], state[3], state[4], state[5],
            state[6], state[7], state[8], state[9], state[10], state[11],
            state[12], state[13], state[14], state[15], state[16]
        ) for state in data]
    return None
