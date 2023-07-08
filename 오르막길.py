def solution(arr):
	answer = 0
	cnt = []
	length = len(arr)
	for i in range(length):
		if i > 0 and arr[i -1] < arr[i]:
			answer += 1
			cnt.append(answer)
		else:
			answer = 0
			cnt.append(answer)
	answer = max(cnt) + 1
	return answer


arr = [3, 1, 2, 4, 5, 6, 1, 2, 2, 3, 4, 7, 8, 10]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")