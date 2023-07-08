def solution(arr, K):
    answer = 0
    length = len(arr)
    
    for i in range(length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                print(arr[i], arr[j], arr[k])
                if (arr[i] + arr[j] + arr[k]) % K == 0:
                    answer += 1
    return answer


arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)

print("solution 함수의 반환 값은", ret, "입니다.")