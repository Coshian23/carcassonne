# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys

def main():
    pygame.init()  # Pygameの初期化
    screen = pygame.display.set_mode((500, 500))  # 大きさ600*500の画面を生成
    pygame.display.set_caption("Carcassonne")  # タイトルバーに表示する文字
    board = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
    tile = ["d-tile.png", 90]

    while (1):
        screen.fill((0, 0, 0))  # 画面を黒色に塗りつぶし
        for i in range(0, 5):
            for j in range(0, 5):
                pygame.draw.rect(screen, (100, 100, 100), Rect(100 * i, 100 * j, 100, 100), 2)  # グリッド表示

        # pygame.draw.rect(screen,(0,200,0),Rect(200,200,100,100),2)   # 四角形を描画(塗りつぶしなし)
        # pygame.draw.rect(screen,(0,200,0),Rect(300,200,100,100),2)
        # pygame.draw.rect(screen,(0,200,0),Rect(200,300,100,100),2)
        # pygame.draw.rect(screen,(0,200,0),Rect(100,200,100,100),2)
        # pygame.draw.rect(screen,(0,200,0),Rect(200,100,100,100),2)
        # pygame.draw.rect(screen,(0,80,0),Rect(10,10,80,50))    # 四角形を描画(塗りつぶし)

        (x, y) = (2, 2)  # タイル座標
        board[x][y] = tile  # ボードへタイル格納
        player = pygame.image.load(tile[0]).convert_alpha()  # タイル画像読み込み
        # player = pygame.transform.smoothscale(player, (95,95))  #タイル拡大
        rect_player = player.get_rect()
        rect_player.center = (100 * x + 50, 100 * y + 50)  # 座標からタイル位置補正
        player = pygame.transform.rotate(player, tile[1])  # タイル回転
        screen.blit(player, rect_player)  # プレイヤー画像の描画

        pygame.display.update()  # 画面を更新

        mpos = pygame.mouse.get_pos()
        print(mpos)

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(画面閉じられる)
                sys.exit()

            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):  # クリックイベント取得
                if rect_player.collidepoint(event.pos):  # タイルの領域であれば回転
                    tile[1] += 90
                    # print("hit")
                else:
                    print("mekaabu")  # タイル外をクリック


if __name__ == "__main__":
    main()