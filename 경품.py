"""
1. 게시글 번호를 1 증가시키고 자릿수를 구합니다.
2. 만약 자릿수가 짝수가 아니라면 1로 돌아갑니다.
3. 만약 구한 자릿수가 짝수라면 다음을 수행합니다.
  3-1. 앞 자릿수 절반과 뒷 자릿수 절반을 분리합니다.
  3-2. 앞 자릿수 절반의 자릿수 합과 뒷 자릿수 절반의 자릿수 합을 구합니다.
  3-3. 위에서 구한 합이 서로 같으면 4로 가고, 같지 않으면 1로 돌아갑니다.
4. (3에서 구한 수 - 처음에 매개변수로 주어진 수)를 return 합니다.

"""

def func_a(n): # n에 자릿수가 매개변수가 입력될 것으로 예상
	ret = 1 # ret = 1, 10, 100, 1000
	while n > 0:
		ret *= 10
		n -= 1
	return ret 

#n이 367이라면
def func_b(n):
	ret = 0
	while n > 0:
		ret += 1
		n //= 10 #자릿수 구하는 함수
	return ret

def func_c(n): #합계를 구하는 함수
	ret = 0
	while n > 0:
		ret += n%10
		n //= 10
	return ret
def solution(num):
	next_num = num
	while True:
		next_num += 1 #게시글 번호를 1증가 시키고
		length = func_b(next_num) #자릿수를 구한다.
		if length % 2: #만약 구한 자릿수가 짝수라면
			continue
		divisor = func_a(length//2) # 앞자릿수 절반과 뒷자리수 절반을 분리 
		front = next_num // divisor  #몫과 나머지를 동일한 크기로 구하기 위해 
		back = next_num % divisor    #func_a를 사용하여 10을 곱한 수를 찾는다.

		front_sum = func_c(front)
		back_sum = func_c(back)
		if front_sum == back_sum:
			break
	return next_num - num

num1 = 1
ret1 = solution(num1)

print("solution 함수의 반환 값은", ret1, "입니다.")

num2 = 235386
ret2 = solution(num2)

print("solution 함수의 반환 값은", ret2, "입니다.")