def filledOrders(order, k):
    # Write your code here
    
    cnt = 0
    order = sorted(order)
    
    while len(order) > 0 and k >= order[0]:
        cnt += 1
        k -= order[0]
        order = order[1:]
    
    return cnt