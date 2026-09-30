#!/usr/bin/env python3

with open("/home/long/analysis/cache/f_000089", "rb") as f:
    data = f.read()

# Key bắt đầu bằng NSE1 — thử nhiều biến thể
keys = [
    b"NSE1842|confirmed|401|HanaRiverSide|DaNang",
    b"NSE1842|CONFIRMED|401|HanaRiverSide|DaNang",
    b"NSE1842|confirmed|401|HanaRiverSide|Da Nang",
    b"NSE1842|confirmed|401|Hana River Side|DaNang",
    b"NSE1|confirmed|401|HanaRiverSide|DaNang",
    b"NSE1|CONFIRMED|401|HanaRiverSide|DaNang",
    b"NSE1",
    b"NSE1842",
]

for key in keys:
    out = bytes(data[i] ^ key[i % len(key)] for i in range(len(data)))
    if out[:8] == b"\x89PNG\r\n\x1a\n":
        name = key.decode(errors='replace').replace('|','_').replace(' ','_')
        print(f"[+] MATCH: {key}")
        open(f"/home/long/analysis/proof_{name}.png", "wb").write(out)
        break
    else:
        print(f"[-] {key}: {out[:8].hex()}")
