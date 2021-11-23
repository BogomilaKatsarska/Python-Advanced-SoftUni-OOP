class Hero:
    username: str
    health: float
    damage: float
    level: int

    def __init__(self, username: str, level: int, health: float, damage: float):
        self.username = username
        self.level = level
        self.health = health
        self.damage = damage

    def battle(self, enemy_hero):
        if enemy_hero.username == self.username:
            raise Exception("You cannot fight yourself")

        if self.health <= 0:
            raise ValueError("Your health is lower than or equal to 0. You need to rest")

        if enemy_hero.health <= 0:
            raise ValueError(f"You cannot fight {enemy_hero.username}. He needs to rest")

        player_damage = self.damage * self.level
        enemy_hero_damage = enemy_hero.damage * enemy_hero.level

        self.health -= enemy_hero_damage
        enemy_hero.health -= player_damage

        if self.health <= 0 and enemy_hero.health <= 0:
            return "Draw"

        if enemy_hero.health <= 0:
            self.level += 1
            self.health += 5
            self.damage += 5
            return "You win"

        enemy_hero.level += 1
        enemy_hero.health += 5
        enemy_hero.damage += 5
        return "You lose"

    def __str__(self):
        return f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"

***************************************************************************************************

from project.hero import Hero

import unittest


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Harry", 100, 200, 300)
        self.enemy = Hero("Ron", 100, 200, 300)
        self.strong_hero = Hero("Strong Harry", 1000, 200000, 3000)

    def test_init(self):
        hero = Hero("Harry", 10, 100, 20)
        self.assertEqual(hero.username, "Harry")
        self.assertEqual(hero.level, 10)
        self.assertEqual(hero.health, 100)
        self.assertEqual(hero.damage, 20)

    def test_battle_yourself(self):
        with self.assertRaises(Exception) as e:
            self.hero.battle(self.hero)
        self.assertEqual(str(e.exception), "You cannot fight yourself")

    def test_battle_with_no_health(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as e:
            self.hero.battle(self.enemy)
        self.assertEqual(str(e.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_with_enemy_having_low_health(self):
        self.enemy.health = 0
        with self.assertRaises(Exception) as e:
            self.hero.battle(self.enemy)
        self.assertEqual(str(e.exception), f"You cannot fight {self.enemy.username}. He needs to rest")

    def test_battle_draw(self):
        res = self.hero.battle(self.enemy)
        self.assertEqual("Draw", res)

    def test_win_battle(self): #depending on which hero attacks the other one (strong -> enemy)
        res = self.strong_hero.battle(self.enemy)
        self.assertEqual(res, "You win")
        self.assertEqual(self.strong_hero.health, 170005)
        self.assertEqual(self.strong_hero.damage, 3005)
        self.assertEqual(self.strong_hero.level, 1001)
        self.assertEqual(self.enemy.health, -2999800)
        self.assertEqual(self.enemy.damage, 300)
        self.assertEqual(self.enemy.level, 100)

    def test_lose_battle(self): #depending on which hero attacks the other one (enemy -> strong)
        res = self.enemy.battle(self.strong_hero)
        self.assertEqual(res, "You lose")
        self.assertEqual(self.strong_hero.health, 170005)
        self.assertEqual(self.strong_hero.damage, 3005)
        self.assertEqual(self.strong_hero.level, 1001)
        self.assertEqual(self.enemy.health, -2999800)
        self.assertEqual(self.enemy.damage, 300)
        self.assertEqual(self.enemy.level, 100)

    def test_str(self):
        self.assertEqual("Hero Harry: 100 lvl\nHealth: 200\nDamage: 300\n", str(self.hero))