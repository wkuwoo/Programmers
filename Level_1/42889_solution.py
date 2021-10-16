def solution(N, stages):
    fail = {}
    users = len(stages)

    for stage in range(1, N+1):
        if users != 0:
            fail_user = stages.count(stage)
            print("1.",fail_user)
            fail[stage] = fail_user / users 
            print("2.",fail[stage])
            users -= fail_user
            print("3.",users)
        else: fail[stage] = 0
            
    return sorted(fail, key=lambda x: fail[x], reverse=True)
