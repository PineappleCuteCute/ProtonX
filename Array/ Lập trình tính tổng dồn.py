def exercise2(aList):
    
    # Lập trình tại đây
    result = None
    
    return result
    
    
# TEST CODE
SECOND = '2'
try:
    q = SECOND
    inp = [
        [1, 2, 3, 4], 
        [-1, 2000, 33999, 3], 
        [1000, -200, 30, 3, 50]
        ]
    out = [
        [1, 3, 6, 10],
        [-1, 1999, 35998, 36001],
        [1000, 800, 830, 833, 883]
        ]
    
    res_list = [False for _ in range(len(inp))]
    for i, inpi in enumerate(inp):
        res_list[i] = exercise2(inpi) == out[i]
    
    ans = 'Câu {}:\n'.format(q)
    for i, item in enumerate(res_list):
        if not res_list[i]:
            ans += "\nTest case {} được tính đúng?: {}.\n\t Giá trị đầu vào: {}".format(i + 1, res_list[i], inp[i])
        else:
            ans += "\nTest case {} được tính đúng?: {}.".format(i + 1, res_list[i])
    print(ans)
except Exception as e:
    print("Lỗi thực thi: ", e)