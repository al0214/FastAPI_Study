from pydantic import BaseModel


class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str


thing = Creature(
    name="Yeti",
    country="CN",
    area="Himalayas",
    description="Hirsute Himalayan",
    aka="Abominable Snowman"
)
