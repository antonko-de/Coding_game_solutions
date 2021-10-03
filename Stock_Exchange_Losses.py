# A finance company is carrying out a study on the worst stock investments and would 
#like to acquire a program to do so. 
#The program must be able to analyze a chronological series of stock values in order 
#to show the largest loss that it is possible to make by buying a share at a 
#given time t0 and by selling it at a later date t1. The loss will be expressed as t
#he difference in value between t0 and t1. If there is no loss, the loss will be worth 0.



n = int(input())
# parse all the stock values in a list # 
variations = [int(i) for i in input().split()]
b_diff = 0
for index in range(n-1):
    next_index = index + 1
    # loop to find index groups where the next stock price is lower #
    while next_index < n and variations[index] > variations[next_index]:
        diff = variations[next_index] - variations[index]
        if diff < b_diff:
            # calculate difference
            b_diff = diff
        next_index += 1

print(b_diff)

