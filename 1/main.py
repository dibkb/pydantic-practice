from pydantic import BaseModel,field_validator
from typing import List,Optional
# custom validation
class User(BaseModel):
    id: int
    username:str
    @field_validator("username")
    @classmethod
    def validate_username(cls,v:str)->str:
        if " " in v:
            raise ValueError("Username must not contain spaces")
        return v.lower()

userOne = User(id=333,username="JohnDoe")
print(userOne.model_dump_json())

# Nested models
class Food(BaseModel):
    name: str
    price : float
    ingredients: Optional[List[str]] = None

class Restaurant(BaseModel):
    name:str
    location: str
    foods: List[Food]

food_egg_roll = Food(name="Egg Roll",price=34,ingredients=["egg"])

food_chicken_roll = Food(name="Chicken Roll",price=34,ingredients=["chicken"])

restaurant_one = Restaurant(
    name = "Nelu",
    location = "Lucknow",
    foods=[food_egg_roll]
)
print(restaurant_one.model_dump_json())



