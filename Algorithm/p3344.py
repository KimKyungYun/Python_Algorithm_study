import sys

input = sys.stdin.readline

n = int(input())
board = [0] * n
def is_promising(x):
    for i in range(x):
        if board[x]==board[i] or abs(board[x]-board[i])==abs(x==i):
            return False
        return True

def n_queens(x):
    if x==n:
        return
    else:
        for i in range(x):
            board[x]=i
            if is_promising(x):
                n_queens(x+1)
n_queens(0)
for i in board: print(i)
