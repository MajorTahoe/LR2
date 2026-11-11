from fastapi import FastAPI, HTTPException
from app.utils import read_links, save_links
from app.schemas import LinkCreate

app = FastAPI()

@app.post("/links")
def add_link(link: LinkCreate):
    links = read_links()

    new_link = link.model_dump(mode="json")
    new_link["id"] = max(
        [item["id"] for item in links],
        default=0
    ) + 1

    links.append(new_link)
    save_links(links)

    return new_link


# Получение всех ссылок
@app.get("/links")
def get_links():
    return read_links()


# Получение ссылки по ID
@app.get("/links/{link_id}")
def get_link(link_id: int):
    for link in read_links():
        if link["id"] == link_id:
            return link

    raise HTTPException(
        status_code=404,
        detail="Ссылка не найдена"
    )


# Удаление ссылки по ID
@app.delete("/links/{link_id}")
def delete_link(link_id: int):
    links = read_links()

    for link in links:
        if link["id"] == link_id:
            links.remove(link)
            save_links(links)

            return {"message": "Ссылка удалена"}

    raise HTTPException(
        status_code=404,
        detail="Ссылка не найдена"
    )
