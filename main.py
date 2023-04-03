import requests
from random import choice
import json

import colors


def main() -> None:
    with open("qoutes.json", "r", encoding="utf-8") as f:
        qoutes: list = json.load(f)

    qoute: dict = choice(qoutes)

    print(f"{colors.blue}\"{colors.yellow}{qoute['q'].strip()}{colors.blue}\"\n\t{colors.reset}{colors.red}- {qoute['a']}")


if __name__ == "__main__":
    main()
