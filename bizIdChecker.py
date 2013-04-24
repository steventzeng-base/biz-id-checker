
input = '04595257'
#input = '10458575'

def checkBID(bid):
    check = [1,2,1,2,1,2,4,1]
    total = sum([i/10+i%10 for i in [int(x)* y for x, y in zip(bid, check)]])
    return total%10==0 or (bid[6] == '7' and (total + 1)%10 == 0)

print checkBID(input)


