import csv
import random
import requests

# --- CSV dosyasını oku
verses = []
with open("turkish.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) > 5:
            verses.append({
                "text": row[5].strip('"'),
                "book": row[1].strip('"'),
                "chapter": row[2],
                "verse": row[3]
            })

# --- Rastgele ayet seç
if not verses:
    print("CSV dosyasında ayet bulunamadı!")
    exit()

selected = random.choice(verses)
verse_text = selected["text"]
verse_ref = f"{selected['book']} {selected['chapter']}:{selected['verse']}"

# --- POST içeriğini oluştur (gerçek satır sonu ile)
content = f"{verse_text}\n\n-{verse_ref}"

# --- MiniBlog API bilgileri
API_URL = "https://bercan.blog/pages/api/minipost_create.php"
API_KEY = "6f81a9c5c8e6b92d01f89a33d6b5a7d3c9eacb90dcd33c0b89b5cfa22bffb510"

payload = {
    "content": content,
    "is_miniblog": True
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# --- POST isteği gönder
try:
    r = requests.post(API_URL, json=payload, headers=headers, timeout=10)
    print("Gönderilen Ayet:", content)
    print("Status:", r.status_code)
    print("Response:", r.text)
except Exception as e:
    print("İstek gönderilirken hata oluştu:", e)
