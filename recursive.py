import sys
num = int(input().strip())
ans = 0

def hailstoneSum(N):
    global ans
    # print("N " + str(N))
    # print("ans " + str(ans))
    if N == 1 :
        ans += 1
        print(ans)
        sys.exit(0)
        # return ans
    else :
        ans += N
        if N%2 == 0 :
            hailstoneSum(N = N//2)
        else :
            hailstoneSum(N = ((3*N)+1))

hailstoneSum(N = num)
# finalAns = hailstoneSum(N = num)
# print(finalAns)