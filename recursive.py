import sys
num = int(input().strip())
ans = 0
recursions = 0

def hailstoneSum(N):
    global recursions
    recursions+=1
    global ans
    global num
    # print("N " + str(N))
    # print("ans " + str(ans))
    if N == 1 :
        ans += 1
        print(f"Hailstone Series Sum starting from {num} = {ans} \After {recursions} recursions!")
        sys.exit(0)
        # return ans
    else :
        ans += N
        if N%2 == 0 :
            hailstoneSum(N = N//2)
        else :
            hailstoneSum(N = ((3*N)+1))

hailstoneSum(N = num)
