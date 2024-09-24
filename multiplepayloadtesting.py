import requests

TARGET_URL = 'http://www.payloadtobetestedagainsthewebsite.com'

payloads = [
    "Payload 1",
    "Payload 2",
    "Payload 3",
    "Payload 4",
    "Payload 5"
]
def test_payloads(url, payloads):
    """Tests a list of payloads against a specified URL."""
    for payload in payloads:
        try:
            response = requests.post(url, data={'input': payload})

            if response.status_code == 200:
                print(
                    f"Payload: {payload} - Response: {response.text[:100]}")
            else:
                print(f"Payload: {payload} - Status Code: {response.status_code}")

        except requests.RequestException as e:
            print(f"Error testing payload {payload}: {e}")

def main():
    print(f"Testing payloads against {TARGET_URL}...")
    test_payloads(TARGET_URL, payloads)

if __name__ == "__main__":
    main()
