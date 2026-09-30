import base64, hashlib, sqlite3, json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

peer = "fi-operator-73"
case_id = "FI-217"
kid = "chatapp-web-v2"
key = hashlib.sha256(f"{kid}|{peer}|{case_id}".encode()).digest()

conn = sqlite3.connect("/home/long/analysis/msg_cache.db")
rows = conn.execute("SELECT id, direction, body FROM messages ORDER BY id").fetchall()

lines = []
for msg_id, direction, body in rows:
    m = json.loads(body)
    iv = base64.b64decode(m["iv"])
    ct = base64.b64decode(m["ct"])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), 16).decode("utf-8")
    lines.append(pt)

# Xuất nhiều biến thể
with open("/home/long/analysis/chat_all.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

with open("/home/long/analysis/chat_concat.txt", "w", encoding="utf-8") as f:
    f.write("".join(lines))

with open("/home/long/analysis/chat_pipe.txt", "w", encoding="utf-8") as f:
    f.write("|".join(lines))

print("Done")
