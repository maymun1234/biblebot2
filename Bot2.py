import csv
import random
import requests

# --- 1. CSV dosyasını oku ve ayetleri listele
verses = []
with open("turkish.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Örnek CSV: 8,"Yaratılış ",1,1,8,"Kubbeye ""Gök"" adını verdi..."
        # ayet metni 5. index'te (row[5])
        if len(row) > 5:
            verses.append(row[5].strip('"'))

# --- 2. Rastgele bir ayet seç
if not verses:
    print("CSV dosyasında ayet bulunamadı!")
    exit()

verse = random.choice(verses)

# --- 3. MiniBlog API bilgileri
API_URL = "https://bercan.blog/pages/api/minipost_create.php"
API_KEY = "6f81a9c5c8e6b92d01f89a33d6b5a7d3c9eacb90dcd33c0b89b5cfa22bffb510"

payload = {
    "content": verse,
    "is_miniblog": True
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# --- 4. POST isteği gönder
try:
    r = requests.post(API_URL, json=payload, headers=headers, timeout=10)
    print("Gönderilen Ayet:", verse)
    print("Status:", r.status_code)
    print("Response:", r.text)
except Exception as e:
    print("İstek gönderilirken hata oluştu:", e)
