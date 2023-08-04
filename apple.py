# A형 문제
T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 보드의 크기
    board = [list(map(int, input().split())) for _ in range(N)]
    targets = {}  # 사과의 위치
    direction = 1 # 출발하여 1번 사과에 도착하였을 때의 방향(하)
    result = 1  # 우회전의 횟수

    num = 0  # 사과의 개수
    for i in range(N):  # 사과의 개수와 위치 파악하기
        for j in range(N):
            if board[i][j] != 0:
                num += 1
                targets.setdefault(board[i][j], (i, j))


    cnt = 1  # 사과를 먹을 때마다 카운트
    dir_x, dir_y = targets[1]  # 기준점을 1번 사과의 위치로 초기화
    while cnt < num:
        a, b = targets[cnt + 1]  # 다음 사과의 위치
        if dir_x > a and dir_y < b:  # 제 1사분면에 다음사과가 위치
            if direction % 4 == 0:  # 현재 방향이 우인 경우
                result += 3  # 다음 사과에 도착했을 때의 누적 우회전 횟수
                direction += 3  # 다음사과에 도착했을 때의 방향
            elif direction % 4 == 1:  # 현재 방향이 하인 경우
                result += 3
                direction += 3
            elif direction % 4 == 2:  # 현재 방향이 좌인 경우
                result += 2
                direction += 2
            else:  # 현재 방향이 상인 경우
                result += 1
                direction += 1
        elif dir_x < a and dir_y < b:  # 제 2사분면에
            if direction % 4 == 0:
                result += 1
                direction += 1
            elif direction % 4 == 1:
                result += 3
                direction += 3
            elif direction % 4 == 2:
                result += 3
                direction += 3
            else:
                result += 2
                direction += 2
        elif dir_x < a and dir_y > b:  # 제 3사분면에
            if direction % 4 == 0:
                result += 2
                direction += 2
            elif direction % 4 == 1:
                result += 1
                direction += 1
            elif direction % 4 == 2:
                result += 3
                direction += 3
            else:
                result += 3
                direction += 3
        else:  # 제 4사분면에
            if direction % 4 == 0:
                result += 3
                direction += 3
            elif direction % 4 == 1:
                result += 2
                direction += 2
            elif direction % 4 == 2:
                result += 1
                direction += 1
            else:
                result += 3
                direction += 3
        cnt += 1
        dir_x, dir_y = a, b


    print(f'#{tc} {result}')


