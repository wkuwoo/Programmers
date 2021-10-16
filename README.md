# Programmers
## Level 1
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

#### 4. 12969_solution.py - 직사각형 별찍기
https://programmers.co.kr/learn/courses/30/lessons/12969
```python
# Best Solution
a, b = map(int, input().strip().split(' '))
print(('*'*a + '\n')*b)
```

#### 5. 12937_solution.py - 짝수와 홀수
https://programmers.co.kr/learn/courses/30/lessons/12937
```python
# Best Solution
```

#### 6. 12933_solution.py - 정수 내림차순으로 배치하기
https://programmers.co.kr/learn/courses/30/lessons/12933]
```python
# Best Solution
```

#### 7. 12948_solution.py - 핸드폰 번호 가리기
https://programmers.co.kr/learn/courses/30/lessons/12948
```python
# Best Solution
```

#### 8. 12901_solution.py - 2016년
https://programmers.co.kr/learn/courses/30/lessons/12901
```python
# Best Solution
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]
# 예술
def getDayName(a,b):
    answer = ""
    if a>=2:
        b+=31
        if a>=3:
            b+=29#2월
            if a>=4:
                b+=31#3월
                if a>=5:
                    b+=30#4월
                    if a>=6:
                        b+=31#5월
                        if a>=7:
                            b+=30#6월
                            if a>=8:
                                b+=31#7월
                                if a>=9:
                                    b+=31#8월
                                    if a>=10:
                                        b+=30#9월
                                        if a>=11:
                                            b+=31#10월
                                            if a==12:
                                                b+=30#11월
    b=b%7

    if b==1:answer="FRI"
    elif b==2:answer="SAT" 
    elif b==3:answer="SUN"
    elif b==4:answer="MON"
    elif b==5:answer="TUE"
    elif b==6:answer="WED"
    else:answer="THU"
    return answer
```

### 9. 12982_solution.py - 예산
https://programmers.co.kr/learn/courses/30/lessons/12982/solution_groups?language=python3

```python
# Best Solution
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
```
#### 10. 42889_solution.py - 실패율
https://programmers.co.kr/learn/courses/30/lessons/42889
```python
# Best Solution
```
