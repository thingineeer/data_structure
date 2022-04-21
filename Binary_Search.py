# 반복문 사용

def binary_search(target, data):  # 이분탐색
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return data[mid]
        elif data[mid] < target:  # 가운데 기준 오른쪽 구간으로 이동
            start = mid + 1
        else:  # 가운데 기준 왼쪽 구간으로 이동
            end = mid - 1

    return None  # 찾는값 없으면 None
