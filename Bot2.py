# --- CSV ile Rastgele ayet seçicimiz.

import csv
import random
import requests
import re  # 1. Regular expressions modülünü dahil et

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


if not verses:
    print("CSV dosyasında ayet bulunamadı!")
    exit()

selected = random.choice(verses)
verse_text = selected["text"]
verse_ref = f"{selected['book']} {selected['chapter']}:{selected['verse']}"


# --- İSTENEN DEĞİŞİKLİKLER BURADA ---

# 2. Kural: Küçük harften sonra büyük harf gelirse (örn: "SözRab'dir"),
# araya boşluk ekle. Türkçe karakterleri (Ç, Ğ, İ, Ö, Ş, Ü) de destekler.
# Bu yöntem "RAB" gibi tamamen büyük harfli kelimeleri "R A B" diye bölmez.
verse_text = re.sub(r"([a-zçğıöşü])([A-ZÇĞİÖŞÜ])", r"\1 \2", verse_text)

# 3. Kural: Bir virgülden sonra boşluk olmayan bir karakter gelirse (örn: "Söz,Rab"),
# araya boşluk ekle. (Eğer zaten boşluk varsa, örn: "Söz, Rab", dokunmaz.)
verse_text = re.sub(r",(\S)", r", \1", verse_text)

# --- DEĞİŞİKLİKLER BİTTİ ---


content = f"{verse_text}\n\n-{verse_ref}"

# --- Kodun geri kalanı (API isteği vb.) ---
# print(content) # Sonucu test etmek için bu satırı kullanabilirsiniz


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


try:
    r = requests.post(API_URL, json=payload, headers=headers, timeout=10)
    print("Gönderilen Ayet:", content)
    print("Status:", r.status_code)
    print("Response:", r.text)
except Exception as e:
    print("İstek gönderilirken hata oluştu:", e)
