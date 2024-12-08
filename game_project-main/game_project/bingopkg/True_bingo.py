import os
from Cube import *
import random

class TrueBingo:
    def __init__(self,difficulty):
        self.player = Cube.create_bingo_board(1, 9)
        self.enemy = Cube.create_bingo_board(1, 9)
        self.hidden_board = [["?" for _ in row] for row in self.enemy[0]]
        self.difficulty = difficulty

    def hide_print(self):
        #적의 숨겨진 빙고판 출력
        print("적:")
        for row in self.hidden_board:
            print("  ".join(map(str, row)))

    def hide_bingo(self, original_board, hidden_board, selected_number):
        #선택된 숫자를 원래 빙고판과 숨겨진 빙고판에서 'X'로 변경
        for i in range(len(original_board)):
            for j in range(len(original_board[i])):
                if original_board[i][j] == selected_number:
                    original_board[i][j] = "X"
                    hidden_board[i][j] = "X"
                    return original_board

    def coordinates(self, board, number):
        #숫자의 좌표를 반환
        for i, row in enumerate(board[0]):
            for j, cell in enumerate(row):
                if cell == number:
                    return (i, j)
        return None

    def mark_number(self,board, number):
            for row in range(3):
                for col in range(3):
                    if board[row][col] == number:
                        board[row][col] = "X"
                        print(f"숫자 {number}이 빙고판에 적용되었습니다!")
                        return board

    def player_turn(self,board1,board2):
        #플레이어의 턴 진행
        Cube.print_board(board1)
        self.hide_print()
        try:
            num = int(input("1~9 사이의 제시할 숫자를 고르시오: "))
            real_num = int(input("사용할 숫자를 고르시오: "))
        except ValueError:
            print("잘못된 입력입니다. 턴을 건너뜁니다.")
            return

        opponent_truth = random.choice([True, False])
        coordinates = self.coordinates(board1, real_num)

        if coordinates is None:
            print(f"숫자 {real_num}는 빙고판에 없습니다. 턴을 종료합니다.")
            return

        if opponent_truth:
            print("적: 진실!")
            if num == real_num:
                print("적 승리!")
                self.hide_bingo(board2[0], self.hidden_board, real_num)
            else:
                print("적 패배!")
                self.mark_number(board1[0],real_num)
        else:
            print("적: 거짓!")
            if num != real_num:
                print("적 승리!")
                self.hide_bingo(board2[0], self.hidden_board, real_num)
            else:
                print("적 패배!")
                self.mark_number(board1[0],real_num)

    def enemy_turn(self,board1,board2):
        #적의 턴 진행
        Cube.print_board(board1)
        self.hide_print()

        num = random.choice(range(1, 10))
        enemy_numbers = [cell for row in board2[0] for cell in row if isinstance(cell, int)]
        real_num = random.choice(enemy_numbers)

        print(f"적이 제시한 숫자: {num}")
        player_truth = input("진실, 거짓, 건너뛰기 중 선택하시오: ").strip()

        coordinates = self.coordinates(board2, real_num)

        if coordinates is None:
            print(f"숫자 {real_num}는 빙고판에 없습니다. 턴을 종료합니다.")
            return

        if player_truth == "진실":
            if num == real_num:
                print("승리")
                self.mark_number(board1[0],real_num)
            else:
                print("패배")
                self.hide_bingo(board2[0], self.hidden_board, real_num)
        elif player_truth == "거짓":
            if num != real_num:
                print("승리")
                self.mark_number(board1[0],real_num)
            else:
                print("패배")
                self.hide_bingo(board2[0], self.hidden_board, real_num)
        elif player_truth == "건너뛰기":
            print('건너뛰었습니다.')
            self.mark_number(board1[0],real_num)
            self.hide_bingo(board2[0], self.hidden_board, real_num)
        else:
            print("진실, 거짓, 건너뛰기 중 선택하시오.")
            return

    def true_play_game(self):
        #게임 전체 진행
        os.system("cls")
        board1 = self.player
        board2 = self.enemy
        print("=== 진실 빙고 (PvE) ===")
        turn = 1

        while True:
            print(f"=== 턴 {turn} ===")
            self.player_turn(board1,board2)
            total_bingo1 = 0
            total_bingo1 += Cube.check_bingo(board1[0])
            print(f"나의 현재 빙고 개수: {total_bingo1}")
            if Cube.victory(self.difficulty,total_bingo1,turn) == 1:
                print('승리하셨습니다.')
                break
            total_bingo2 = 0
            total_bingo2 += Cube.check_bingo(board2[0])
            print(f"적의 현재 빙고 개수: {total_bingo2}")
            if Cube.victory(self.difficulty,total_bingo2,turn) == 1:
                print('패배하셨습니다.')
                break
            print(f"=== 턴 {turn + 1} ===")
            self.enemy_turn(board1,board2)
            total_bingo1 = 0
            total_bingo1 += Cube.check_bingo(board1[0])
            print(f"나의 현재 빙고 개수: {total_bingo1}")
            if Cube.victory(self.difficulty,total_bingo1,turn) == 1:
                print('승리하셨습니다.')
                break
            total_bingo2 = 0
            total_bingo2 += Cube.check_bingo(board2[0])
            print(f"적의 현재 빙고 개수: {total_bingo2}")
            if Cube.victory(self.difficulty,total_bingo2,turn) == 1:
                print('패배하셨습니다.')
                break
            turn += 2