# Programmers
#### 1. 77484_solution.py - 로또의 최고 순위와 최저 순위
https://programmers.co.kr/learn/courses/30/lessons/77484
```python
# Best Solution
def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    cnt_0 = lottos.count(0)
    ans = 0
    
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
```

#### 2. 72410_solution.py - 신규 아이디 추천
https://programmers.co.kr/learn/courses/30/lessons/72410
```python
# Best Solution
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
```

#### 3. 81301_solution.py - 숫자 문자열과 영어
https://programmers.co.kr/learn/courses/30/lessons/81301
```python
# Best Solution
def solution(s):
    answer = s
    num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
```

#### 4. 
