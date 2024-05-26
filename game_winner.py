# def game_winner(number_of_coins: int, current_player: str = "you") -> str:
#     """
#     Determine the winner of a game where players alternately take 1 or 2 coins from a 
#     pile and the player who takes the last coin wins.

#     Args:
#         number_of_coins (int): The number of coins in the pile.
#         current_player (str, optional): The player whose turn it is. Defaults to "you".

#     Returns:
#         str: The winner of the game.
#     """
#     if number_of_coins <= 0:
#         return current_player

#     next_player = "them" if current_player == "you" else "you"

#     if (game_winner(number_of_coins - 1, next_player) == current_player or \
#          game_winner(number_of_coins - 2, next_player) == current_player):
#         return current_player
#     else:
#         return next_player
    

def game_winner(number_of_coins: int) -> str:
    """
    Determine the winner of a game where players alternately take 1 or 2 coins from a pile and the player 
    who takes the last coin wins.

    Args:
        number_of_coins (int): The number of coins in the pile.

    Returns:
        str: The winner of the game.
    """
    if (number_of_coins - 1) % 3 == 0:
        return "them"
    else:
        return "you"