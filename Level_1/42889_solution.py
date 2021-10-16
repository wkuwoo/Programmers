def solution(N, stages):
    fail = {}
    users = len(stages)

    for stage in range(1, N+1):
        if users != 0:
            fail_user = stages.count(stage)
            fail[stage] = fail_user / users
            users -= fail_user
        else: fail[stage] = 0
            
    return sorted(fail, key=lambda x: fail[x], reverse=True)
