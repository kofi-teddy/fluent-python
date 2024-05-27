from typing import Any, Dict, List


def find_multisport_athletes(array_1: List[Dict[str, Any]], array_2: List[Dict[str, Any]]) -> List[str]:
    """
    Find athletes who are in both arrays.

    Args:
        array_1 (List[Dict[str, Any]]): The first array of athletes.
        array_2 (List[Dict[str, Any]]): The second array of athletes.

    Returns:
        List[str]: The names of the athletes who are in both arrays.
    """
    hash_table = {}
    multisport_athletes = []

    for athlete in array_1:
        hash_table[athlete['first_name'] + " " + athlete['last_name']] = True

    for athlete in array_2:
        if hash_table.get(athlete['first_name'] + " " + athlete['last_name']):
            multisport_athletes.append(athlete['first_name'] + " " + athlete['last_name'])

    return multisport_athletes


basketball_players = [
      {"first_name": "Jill", "last_name": "Huang", "team": "Gators"},
      {"first_name": "Janko", "last_name": "Barton", "team": "Sharks"},
      {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Sharks"},
      {"first_name": "Jill", "last_name": "Moloney", "team": "Gators"},
      {"first_name": "Luuk", "last_name": "Watkins", "team": "Gators"}
]
football_players = [
      {"first_name": "Hanzla", "last_name": "Radosti", "team": "32ers"},
      {"first_name": "Tina", "last_name": "Watkins", "team": "Barleycorns"},
      {"first_name": "Alex", "last_name": "Patel", "team": "32ers"},
      {"first_name": "Jill", "last_name": "Huang", "team": "Barleycorns"},
      {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Barleycorns"}
]

find_multisport_athletes(basketball_players, football_players)