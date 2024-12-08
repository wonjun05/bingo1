import random
class Cube:
    def __init__(difficulty):
        self.difficulty = difficulty

    def create_bingo_board(difficulty, num_range):
    #빙고판 생성
        all_numbers = list(range(1, num_range + 1))
        random.shuffle(all_numbers)
    
        boards = []
        for _ in range(difficulty):
            board_numbers = all_numbers[:9]  # 각 판에 9개의 숫자 할당
            all_numbers = all_numbers[9:]    # 사용한 숫자 제거
            boards.append([board_numbers[i:i + 3] for i in range(0, 9, 3)])
        return boards

    def print_board(boards):
        #빙고판 출력
        for i, board in enumerate(boards, 1):
            print(f"보드 {i}:")
            for row in board:
                print(row)
            print("-" * 11)

    def check_bingo(board):
    #빙고 줄 개수 확인
        size = len(board)
        bingo_count = 0

    # 가로 빙고
        for row in board:
            if all(isinstance(cell, str) for cell in row):
                bingo_count += 1

    # 세로 빙고
        for col in range(size):
            if all(isinstance(board[row][col], str) for row in range(size)):
                bingo_count += 1

    # 대각선 빙고
        if all(isinstance(board[i][i], str) for i in range(size)):
            bingo_count += 1
        if all(isinstance(board[i][size - 1 - i], str) for i in range(size)):
            bingo_count += 1

        return bingo_count

    def victory(difficulty,bingo_count,turn):
        if difficulty==1:
            winning=3
            if bingo_count==winning:
                print("빙고! 총 {} 줄 완성되었습니다. 총 {}턴 소요.".format(bingo_count,turn))
                return 1
        else:
            winning = {2: 5, 3: 8, 4: 11}[difficulty]
        if bingo_count==winning:
            print("빙고! 총 {} 줄 완성되었습니다. 총 {}턴 소요.".format(bingo_count,turn))
            return 1