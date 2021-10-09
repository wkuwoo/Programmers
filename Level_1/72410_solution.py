# 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환한다.
    new_id = new_id.lower() # lower()는 대문자를 소문자로 변경한다.

    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거한다.
    answer = ''
    for word in new_id:
        if word.isalnum() or word in '-_.': # isalnum()는 특수문자를 제외한 한글,영어,숫자만 True로 Return 한다.
            answer += word # 위 조건에 만족한 word들만 answer에 추가한다.

    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환한다.
    while '..' in answer:
        answer = answer.replace('..','.') # replace 함수로 '.'이 두개 이상 있는 '..'을 '.'으로 변경한다.

    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거한다.
    if answer[0] == '.' and len(answer) > 1: # 해당 부분 이해 못함
        answer = answer[1:]
    else: answer
    if answer[-1] == '.':
        answer = answer[:-1]
    else: answer

    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입한다.
    if answer == '': 
        answer =  'a'
    else: answer

    #if answer == '':
    #     answer = 'a'

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거한다.
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거한다.
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙인다.
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3-len(answer))

    return answer
