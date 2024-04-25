#Tower Defense Game with Pygame
import pygame
import os
import sys
import random

# ゲーム画面の設定
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_TITLE = "Tower Defense Game"
FPS = 60

# 色の設定
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 初期化
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()

# ゲームのクラス
class Game:
    def __init__(self):
        # マップの設定
        self.map_width = SCREEN_WIDTH
        self.map_height = SCREEN_HEIGHT - 100
        self.map_rect = pygame.Rect(0, 0, self.map_width, self.map_height)
        self.map_image = pygame.Surface((self.map_width, self.map_height))
        self.map_image.fill(WHITE)
        self.enemies = []

        # 防衛設備と攻撃ユニットの設定
        self.defenders = []
        self.towers = []

    # マップを描画する関数
    def draw_map(self):
        screen.blit(self.map_image, self.map_rect)

    # 敵を描画する関数
    def draw_enemies(self):
        for enemy in self.enemies:
            pygame.draw.circle(screen, RED, (int(enemy.x), int(enemy.y)), 10)

    # 防衛設備を描画する関数
    def draw_defenders(self):
        for defender in self.defenders:
            pygame.draw.rect(screen, BLACK, defender.rect)

    # 攻撃ユニットを描画する関数
    def draw_towers(self):
        for tower in self.towers:
            pygame.draw.circle(screen, BLACK, (int(tower.x), int(tower.y)), 15, 1)

    # ゲームのメインループ
    def run(self):
        running = True
        while running:
            # イベントの処理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # 敵の生成
            if random.random() < 0.01:
                enemy = Enemy(random.randint(0, self.map_width), -20, 2)
                self.enemies.append(enemy)

            # 敵の移動
            for enemy in self.enemies:
                enemy.move()
                if enemy.y > self.map_height:
                    self.enemies.remove(enemy)

            # 描画
            screen.fill(WHITE)
            self.draw_map()
            self.draw_enemies()
            self.draw_defenders()
            self.draw_towers()
            pygame.display.update()

            # 時間の更新
            clock.tick(FPS)

        pygame.quit()


# 敵のクラス
class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.y += self.speed

# 防衛設備のクラス
class Defender:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


# 攻撃ユニットのクラス
class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 100

# ゲームのインスタンスを生成し、実行する
if __name__ == "__main__":
    game = Game()
    game.run()
