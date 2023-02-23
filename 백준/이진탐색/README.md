# K번째 수
### mid // i(행번호) mid보다 작은 i번째 행의 숫자 개수를 알수 있다.
for i in range(1, n + 1):
    count += min(mid // i, n) 이 식으로 n,n 배열의 숫자중 mid보다 작은 숫자가 몇개인지 알 수있다.
count가 k보다 크면 start = mid + 1 작으면 end = mid - 1