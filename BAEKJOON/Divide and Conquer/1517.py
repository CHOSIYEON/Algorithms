# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split()))
# swap = 0
#
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[j] > arr[j+1]:
#             temp = arr[j]
#             arr[j] = arr[j+1]
#             arr[j+1] = temp
#             swap += 1
#
# print(swap)
#
# import sys
# input = sys.stdin.readline
#
# def division(arr):
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr)//2
#     left = arr[:mid]
#     right = arr[mid:]
#
#     return conquer(left, right)
#
#
# def conquer(left, right):
#     result = []
#     swap = 0
#
#     left = sorted(left)
#     right = sorted(right)
#
#     print(left)
#     print(right)
#     while len(left) > 0 and len(right) > 0:
#         if left[0] <= right[0]:
#             swap += 1
#             result.append(left.pop(0))
#         else:
#             swap += len(left)
#             result.append(right.pop(0))
#     print(result)
#     print(swap)
#
# n = int(input())
# arr = list(map(int, input().split()))
#
# division(arr)
import sys
def devide(l,r) :
    if l == r :
        return
    mid = (l + r)//2
    devide(l,mid)
    devide(mid+1,r)
    swap(l,mid,mid+1,r)
    return

def swap(ll,lr,rl,rr) :
    global swap_cnt
    temp_list = []
    start_idx = ll #이 변수는 현재 temp_list의 위치를 알려주는 값으로 보면 된다. 0이나 temp_list의 길이로 하지 않는 이유는 ll이 0부터 시작하지 않기 때문이다.
    si,li = ll,rr #si : start_index의 줄임말. li : last_index의 줄임말. 둘다 원래 배열에 값을 넣을 때 사용한다.
    while ll <= lr and rl <= rr : #좌,우 배열 중 한쪽 배열이 temp_list에 다 들어갈 때까지 값을 비교한다.
        if my_list[ll] > my_list[rl] : #오른쪽 배열에 있는 값을 temp_list에 집어넣는다.
            temp_list.append(my_list[rl])
            swap_cnt += (rl-start_idx)
            rl +=1 #
            start_idx +=1
        else :
            temp_list.append(my_list[ll])
            ll += 1
            start_idx += 1
    while ll <= lr : #만약 왼쪽 배열이 temp_list로 덜 들어갔다면, 다 넣어준다.
        temp_list.append(my_list[ll])
        ll +=1
    while rl <= rr : #만약 오른쪽 배열이 temp_list로 덜 들어갔다면, 다 넣어준다.
        temp_list.append(my_list[rl])
        rl += 1
    for z in range(li,si-1,-1) : #temp_list에 넣어준 값을 하나씩 원래 배열로 넣어서 정렬시켜준다.
        my_list[z] = temp_list.pop()
    return


t = int(sys.stdin.readline().rstrip())
my_list = list(map(int,sys.stdin.readline().split()))
swap_cnt = 0
devide(0,len(my_list)-1)
print(swap_cnt)