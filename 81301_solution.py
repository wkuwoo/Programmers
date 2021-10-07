# 숫자 문자열과 영어
# https://programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    answer = ''
    dict = {}
    info = ['zero', 'one', 'two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        dict[info[i]] = i
    print(dict)
    eng=''
    
    for i in s:
        if i.isdigit():
            answer = answer + i
        elif i.isalpha():
            eng = eng + i
            if eng in dict.keys():
                answer = answer + str(dict[eng])
                eng = ''
    return int(answer)
