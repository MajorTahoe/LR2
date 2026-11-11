import json
from pathlib import Path

FILE = Path("data/links.json")

def read_links():
    if not FILE.exists():
        FILE.parent.mkdir(exist_ok=True)
        FILE.write_text("[]", encoding="utf-8")

    return json.loads(FILE.read_text(encoding="utf-8"))


# Сохранение ссылок в JSON-файл
def save_links(links):
    FILE.parent.mkdir(exist_ok=True)
    FILE.write_text(
        json.dumps(links, ensure_ascii=False, indent=4),
        encoding="utf-8"
    )
