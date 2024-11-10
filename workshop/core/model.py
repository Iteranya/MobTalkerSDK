from dataclasses import dataclass
# Feel free to expand these base classes~

@dataclass
class Character:
    id:str|None=None
    name: str|None = "unknown"
    description: str|None = None
    thoughts:str|None = None
    spriteFolder:list|None = "default"
    outfit: list|None = "male"
    outfit: str|None = "default"
    states: list|None = None
    maxhealth: int = 40
    traits: list|None = None
