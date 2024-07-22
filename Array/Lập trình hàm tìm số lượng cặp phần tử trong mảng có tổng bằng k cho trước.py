import collections
def exercise3(aList, k):
    # Lập trình tại đây
    cnt = 0
    for i in range(aList):
        for j in range(aList):
            if i + j == k:
                cnt += 1
    return cnt
    
# TEST CODE

THIRD = '3'

try:
    q = THIRD
    inp = [
        ([1, 2, 1], 3),
        ([-1, 10, 10, 2], 9),
        ([0, 0, 0, 1, 1, 1, -1, 0], 1),
        ([1] * 1000, 2), # Mảng có 6000 nghìn số 1
    ]
    out = [
        2,
        2,
        12,
        499500
    ]
    
    res_list = [False for _ in range(len(inp))]
    for i, inpi in enumerate(inp):
        res_list[i] = exercise3(*inpi) == out[i]
    
    ans = 'Câu {}:\n'.format(q)
    for i, item in enumerate(res_list):
        if not res_list[i]:
            ans += "\nTest case {} được tính đúng?: {}.\n\t Giá trị đầu vào: {}".format(i + 1, res_list[i], inp[i])
        else:
            ans += "\nTest case {} được tính đúng?: {}.".format(i + 1, res_list[i])
    print(ans)
except Exception as e:
    print("Lỗi thực thi: ", e)