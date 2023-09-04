def maxCost(cost, labels, dailyCount):
    # Write your code here
    
    mx_cost = 0
    produced = 0
    daily_cost = 0
    for c, l in zip(cost, labels):
        daily_cost += c
        if l == "legal":
            produced += 1
        
        if produced == dailyCount:
            mx_cost = max(mx_cost, daily_cost)
            daily_cost = 0
            produced = 0
    
    return mx_cost