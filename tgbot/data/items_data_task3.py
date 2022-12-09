from dataclasses import dataclass


@dataclass
class Fruits:
    item_id: int
    name: str
    photo_link: str


Kiwi = Fruits(
    item_id=1,
    name="Kiwi",
    photo_link="https://bipbap.ru/wp-content/uploads/2018/04/267530-640x400.jpg"
)

Strawberry = Fruits(
    item_id=2,
    name="Strawberry",
    photo_link="https://bipbap.ru/wp-content/uploads/2018/04/10174-640x434.jpg"
)

fruits = (Kiwi, Strawberry)
