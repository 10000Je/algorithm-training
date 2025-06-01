import sys

def color_paper(paper, n, row, col, color=0):
    if n == 1:
        return paper[row][col] if color else 1 if not paper[row][col] else 0
    else:
        is_colored = True
        for i in range(row, row+n):
            for j in range(col, col+n):
                if (not color and paper[i][j]) or (color and not paper[i][j]):
                    is_colored = False
                    break
            else:
                continue
            break
        if is_colored:
            return 1
        else:
            pivot = n // 2
            result = [0 for i in range(4)]
            result[0] = color_paper(paper, pivot, row, col, color)
            result[1] = color_paper(paper, pivot, row, col+pivot, color)
            result[2] = color_paper(paper, pivot, row+pivot, col, color)
            result[3] = color_paper(paper, pivot, row+pivot, col+pivot, color)
            return sum(result)

n = int(sys.stdin.readline())
paper = [[color for color in map(int, sys.stdin.readline().split())] for i in range(n)]
print(color_paper(paper, n, 0, 0, color=0))
print(color_paper(paper, n, 0, 0, color=1))