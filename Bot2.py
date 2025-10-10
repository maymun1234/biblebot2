import json
import urllib.request

def lambda_handler(event=None, context=None):
    API_URL = "https://bercan.blog/pages/api/minipost_create.php"
API_KEY = "6f81a9c5c8e6b92d01f89a33d6b5a7d3c9eacb90dcd33c0b89b5cfa22bffb510"

    data = {
        "api_key": API_KEY,
        "icerik": "Bugünün otomatik paylaşımı 🌅",
        "is_miniblog": True
    }

    try:
        req = urllib.request.Request(
            API_URL,
            data=json.dumps(data).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req) as response:
            result = response.read().decode("utf-8")
            print("Response:", result)
        return {
            "statusCode": 200,
            "body": result
        }
    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "body": str(e)
        }

# Yerel test için:
if __name__ == "__main__":
    lambda_handler()
