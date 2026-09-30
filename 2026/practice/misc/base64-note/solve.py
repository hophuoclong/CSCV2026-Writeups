"""Decode the bundled practice note. Python 3, standard library only."""

import base64
import binascii
from pathlib import Path


def main():
    source = Path(__file__).with_name("data.txt")
    try:
        encoded = source.read_text(encoding="ascii").strip()
        decoded = base64.b64decode(encoded, validate=True)
        print(decoded.decode("utf-8"))
    except (OSError, UnicodeError, binascii.Error, ValueError) as exc:
        raise SystemExit(f"Cannot decode the practice note: {exc}") from exc


if __name__ == "__main__":
    main()
