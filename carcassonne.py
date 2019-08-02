# -*- coding:utf-8 -*-
import pygame
import random
import tiles
from pygame.locals import *
import sys

#class deck_class:
#    def __init__(self):
#        self = [tiles.tile[0],tiles.tile[1]]
#        #random.shuffle(self)

def main():
    pygame.init()  # Pygameの初期化
    screen = pygame.display.set_mode((500, 600))  # 大きさ500*600の画面を生成
    pygame.display.set_caption("Carcassonne")  # タイトルバーに表示する文字
    turn = 1
    font = pygame.font.Font(None, 20)
    board_size = 5
    board = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
    #tile = [tiles.tile[8].image, 90]
    (x, y) = (2, 2)  # スタートタイル座標
    (x0, y0) = (0, 5) # ネクストタイル座標

    # デッキ作成
    deck = tiles.tile[1:10]
    random.shuffle(deck)
    deck.insert(0,tiles.tile[0]) # スタートタイルのみ先頭に追加
    board[x][y] = [deck[0], 90]

    while (1):
        screen.fill((0, 0, 0))  # 画面を黒色に塗りつぶし
        mpos = pygame.mouse.get_pos() #マウス座標取得
        text = font.render("TURN:" + str(turn), True, (255, 255, 255))  # 描画する文字列の設定
        screen.blit(text, [400, 500])  # 文字列の表示位置

        for i in range(0, board_size):
            for j in range(0, board_size):
                rect_board = pygame.draw.rect(screen, (100, 100, 100), Rect(100 * i, 100 * j, 100, 100), 2)  # グリッド表示
                if (rect_board.collidepoint(mpos)) and (pygame.mouse.get_focused()): #マウスがグリッド上にある＆ウィンドウ上の場合
                    pygame.draw.rect(screen, (200, 200, 200), Rect(100 * i, 100 * j, 100, 100)) #グリッド塗りつぶし

        # ボード全体表示
        for i in range(0, board_size):
            for j in range(0, board_size):
                if board[i][j] is not 0:
                    board_tile = pygame.image.load(board[i][j][0].image).convert_alpha()
                    rect_board_tile = board_tile.get_rect()
                    rect_board_tile.center = (100 * i + 50, 100 * j + 50)
                    board_tile = pygame.transform.rotate(board_tile, board[i][j][1])
                    screen.blit(board_tile, rect_board_tile)

        # ネクストタイル
        next_tile = pygame.image.load(deck[turn].image).convert_alpha()  # タイル画像読み込み
        rect_next_tile = next_tile.get_rect()
        rect_next_tile.center = (100 * x0 + 50, 100 * y0 + 50)  # 座標からタイル位置補正
        screen.blit(next_tile, rect_next_tile)  # プレイヤー画像の描画

        pygame.display.update()  # 画面を更新

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(画面閉じられる)
                sys.exit()

            rect_start_tile = pygame.image.load(board[x][y][0].image).convert_alpha().get_rect()
            rect_start_tile.center = (100 * x + 50, 100 * y + 50)
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):  # クリックイベント取得
                if rect_start_tile.collidepoint(event.pos):  # タイルの領域であれば回転
                    board[x][y][1] += 90
                    # print("hit")
                else:
                    for i in range(0, 5):
                        for j in range(0, 5):  # グリッド探索
                            rect_board = pygame.draw.rect(screen, (100, 100, 100), Rect(100 * i, 100 * j, 100, 100),
                                                          2)  # グリッド表示
                            if rect_board.collidepoint(event.pos):
                                board[i][j] = [deck[1],0]
                                turn += 1


if __name__ == "__main__":
    main()