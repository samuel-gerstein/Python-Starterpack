from random import Random
from game.game_state import GameState
import game.character_class
import math

from game.item import Item

from game.position import Position
from strategy.strategy import Strategy

class StarterStrategy(Strategy):
    def strategy_initialize(self, my_player_index: int):
        return game.character_class.CharacterClass.WIZARD

    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        return game_state.player_state_list[my_player_index].position

    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        return Random().randint(0, 3)

    def buy_action_decision(self, game_state: GameState, my_player_index: int) -> Item:
        return Item.NONE

    def use_action_decision(self, game_state: GameState, my_player_index: int) -> bool:
        return False


class NewStrategy(Strategy):
    def strategy_initialize(self, my_player_index: int):
        return game.character_class.CharacterClass.WIZARD

    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        player = game_state.player_state_list[my_player_index]
        speed = player.stat_set.speed
        returnedposition = Position(player.position.x, player.position.y)
        xmovement = Random().randint(-3, 3)
        ymovement = Random().randint(-3 + abs(xmovement), 3 - abs(xmovement))
        returnedposition.x = returnedposition.x + xmovement
        returnedposition.y = returnedposition.y + ymovement
        return returnedposition

    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        player = game_state.player_state_list[my_player_index]
        player_range = player.stat_set.range
        for i in range(0, 4):
            if i != my_player_index:
                other_player = game_state.player_state_list[i]
                if (abs(player.position.x - other_player.position.x) <= player_range) or (abs(player.position.y - other_player.position.y) <= player_range):
                    return i;
        return Random().randint(0, 3)



    def buy_action_decision(self, game_state: GameState, my_player_index: int) -> Item:
        return Item.NONE

    def use_action_decision(self, game_state: GameState, my_player_index: int) -> bool:
        return False