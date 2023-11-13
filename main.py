from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import IntEnum
from enum import Enum
import random

app = FastAPI()

class Weapon(Enum):
    """Enumeration representing the available weapons."""
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

    def __new__(cls, value):
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str):
            for member in cls:
                if member.name == value.upper():
                    return member
        return super()._missing_(value)


class Outcome(IntEnum):
    """Enumeration representing possible outcomes of the game."""

    YOU_WIN = 0
    DRAW = 1
    COMPUTER_WINS = 2


class PlayRequest(BaseModel):
    """Model for incoming play requests containing player's weapon choice."""

    choice: Weapon


class PlayResponse(BaseModel):
    """Model for responses of play endpoint showing the game result."""

    your_weapon: str
    computer_weapon: str
    winner: str


@app.post("/api/play", response_model=PlayResponse)
async def play(req: PlayRequest) -> PlayResponse:
    """
    Endpoint to play rock-paper-scissors against the computer.

    Args:
    - req (PlayRequest): Contains the player's choice of weapon.

    Returns:
    - PlayResponse: The result of the game including player's choice, computer's choice, and the winner.
    """

    computer_choice = random.choice(list(Weapon))

    if req.choice == computer_choice:
        winner = Outcome.DRAW
    elif (req.choice == Weapon.ROCK and computer_choice == Weapon.SCISSOR) or \
            (req.choice == Weapon.PAPER and computer_choice == Weapon.ROCK) or \
            (req.choice == Weapon.SCISSOR and computer_choice == Weapon.PAPER):
        winner = Outcome.YOU_WIN
    else:
        winner = Outcome.COMPUTER_WINS

    return {
        "your_weapon": req.choice.name,
        "computer_weapon": computer_choice.name,
        "winner": winner.name
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
