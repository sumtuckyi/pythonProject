# 크로스워드
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # cnt = 1
    # # 행 우선 순회
    # for i in range(N):
    #     for j in range(N-1):
    #         if board[i][j] == board[i][j + 1] == 1:
    #             cnt += 1
    #             if cnt == K:
    #                 if j + 2 < N:
    #                     board[i][j + 2] == 0
    #                     result += 1
    #                 else:
    #                     result += 1
    #         else:
    #             cnt = 1
    for i in range(N):
        cnt = 0
        for j in range(N):
            if board[i][j]:  # 빈칸이면
                cnt += 1
            if j == N - 1 or board[i][j] == 0:  # 각 행의 마지막열 탐색을 마쳤거나 탐색 중 0을 만나면
                if cnt == K:  # 카운트를 확인
                    result += 1
                cnt = 0  # 빈칸이 끝났으므로 초기화
    # 열 우선 순회
    for i in range(N):
        cnt = 0
        for j in range(N):
            if board[j][i]:
                cnt += 1
            if j == N - 1 or board[j][i] == 0:
                if cnt == K:
                    result += 1
                cnt = 0

    print(f'#{tc} {result}')