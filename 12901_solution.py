# 2016년
# https://programmers.co.kr/learn/courses/30/lessons/12901
def solution(a, b):
    answer = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    day = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    over = sum(day[:a]) + b
    return answer[over % 7]
