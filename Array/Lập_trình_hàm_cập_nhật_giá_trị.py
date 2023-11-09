def exercise1(aList, i, value):
    # Check if the index is valid
    if 0 <= i < len(aList):
        aList[i] = value
    return aList

    
# TEST CODE
FIRST = '1'
try:
    q = FIRST
    
    inp = [
        (['thịt gà 🐔', 'thịt heo 🐖', 'phở bò 🍲', 'rau cải 🥬', 'trứng gà 🥚', 'cà chua 🍅'], 1, 'Sandwich 🥪'), 
        (['thịt gà 🐔', 'thịt heo 🐖', 'phở bò 🍲', 'rau cải 🥬', 'trứng gà 🥚', 'cà chua 🍅'], 2, 'Sandwich 🥪'), 
        (['thịt gà 🐔', 'thịt heo 🐖', 'phở bò 🍲', 'rau cải 🥬', 'trứng gà 🥚', 'cà chua 🍅'], 10, 'Sandwich 🥪')
        ]
    out = [
        ['thịt gà 🐔', 'Sandwich 🥪', 'phở bò 🍲', 'rau cải 🥬', 'trứng gà 🥚', 'cà chua 🍅'],
        ['thịt gà 🐔', 'thịt heo 🐖', 'Sandwich 🥪', 'rau cải 🥬', 'trứng gà 🥚', 'cà chua 🍅'],
        ['thịt gà 🐔', 'thịt heo 🐖', 'phở bò 🍲', 'rau cải 🥬', 'trứng gà 🥚', 'cà chua 🍅']
        ]
    
    
    res_list = [False for _ in range(len(inp))]
    for i, inpi in enumerate(inp):
        res_list[i] = exercise1(*inpi) == out[i]
    
    ans = 'Câu {}:\n'.format(q)
    for i, item in enumerate(res_list):
        if not res_list[i]:
            ans += "\nTest case {} được tính đúng?: {}.\n\t Giá trị đầu vào: {}".format(i + 1, res_list[i], inp[i])
        else:
            ans += "\nTest case {} được tính đúng?: {}.".format(i + 1, res_list[i])
    print(ans)

except Exception as e:
    print("Lỗi thực thi: ", e)