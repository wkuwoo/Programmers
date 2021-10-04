# 로또의 최 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3
# It hasn't been resolved yet.

def solution(lottos, win_nums):
    answer = [0,0]
    rank = [6,6,5,4,3,2,1]

    cnt = 0
    cntz = lottos.count(0)

    for i in lottos:
        if i in win_nums:
            cnt += 1
    
    answer[0], answer[1] = rank[cnt+cntz],rank[cnt]

    return answer