import requests

API_URL = "https://bercan.blog/pages/api/minipost_create.php"
API_KEY = "6f81a9c5c8e6b92d01f89a33d6b5a7d3c9eacb90dcd33c0b89b5cfa22bffb510"


payload = {
    "content": "Merhaba! Bu bir bot tarafından gönderilen MiniBlog testi. Kısa ve öz.",
    "is_miniblog": True,
    # "author_username": "botuser"   # opsiyonel
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

r = requests.post(API_URL, json=payload, headers=headers, timeout=10)
print("Status:", r.status_code)
print("Response:", r.text)
