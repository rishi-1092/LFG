import sys
num = int(input().strip())
ans = 0
recursions = 0
hailstone_seq = []

def hailstoneSum(N):
    global hailstone_seq
    hailstone_seq.append(N)
    global recursions
    recursions+=1
    global ans
    global num
    # print("N " + str(N))
    # print("ans " + str(ans))
    if N == 1 :
        ans += 1
        print(f"Hailstone Series Sum starting from {num} = {ans} \nAfter {recursions} recursions \
        \nHailstone Sequence: {', '.join([str(i) for i in hailstone_seq])}")
        sys.exit(0)
        # return ans
    else :
        ans += N
        if N%2 == 0 :
            hailstoneSum(N = N//2)
        else :
            hailstoneSum(N = ((3*N)+1))

hailstoneSum(N = num)
