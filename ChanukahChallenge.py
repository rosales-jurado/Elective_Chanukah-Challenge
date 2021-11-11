def noOfCandles(s):
    candle = s[0]
    days = s[1]
    
    neededCandles = days + ((days * (days + 1))/2)
    print('{0} {1}'.format(candle, int(neededCandles)))

n = int(input())
for i in range(n):
    s = [int(j) for j in input().split()]
    noOfCandles(s)
