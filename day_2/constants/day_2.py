from . import *

ME_LOSE = 'X'
ME_DRAW = 'Y'
ME_WIN = 'Z'
RULES = {
    (ELF_ROCK, ME_DRAW): DRAW + ROCK,
    (ELF_ROCK, ME_LOSE): LOSE + SCISSORS,
    (ELF_ROCK, ME_WIN): WIN + PAPER,
    (ELF_PAPER, ME_DRAW): DRAW + PAPER,
    (ELF_PAPER, ME_LOSE): LOSE + ROCK,
    (ELF_PAPER, ME_WIN): WIN + SCISSORS,
    (ELF_SCISSORS, ME_DRAW): DRAW + SCISSORS,
    (ELF_SCISSORS, ME_LOSE): LOSE + PAPER,
    (ELF_SCISSORS, ME_WIN): WIN + ROCK
}