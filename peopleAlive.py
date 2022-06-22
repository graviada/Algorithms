from typing import List, Dict


def maxPeopleAlive(persons: List[int], startYear: int, endYear: int) -> Dict:
    aliveDeltas = dict.fromkeys(range(startYear, 2 + endYear), 0)

    for person in persons:
        birth = person[0] - startYear + 1990
        death = person[1] - startYear + 1990

        if birth <= 2 + endYear and death <= 2 + endYear:
            aliveDeltas[birth] += 1
            aliveDeltas[death] -= 1

    return aliveDeltas


def maxYear(aliveDeltas: Dict, startYear: int, endYear: int) -> int:
    maxAlive = currAlive = 0
    maxAliveYear = 0

    for year in range(startYear, endYear + 2):
        currAlive += aliveDeltas[year]

        if currAlive > maxAlive:
            maxAlive = currAlive
            maxAliveYear = year

    return maxAliveYear


def mainFunc(persons: List[int], startYear: int, endYear: int) -> int:
    alive = maxPeopleAlive(persons, startYear, endYear)
    return maxYear(alive, startYear, endYear)