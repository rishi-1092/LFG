L, N, k, Q = map(int, input().strip().split())
s = ""
for i in range(L):
    s += input().strip()
kmers_list = []
kmers = {}
for i in range(Q):
    kmer = input().strip()
    kmers[kmer] = 0
    kmers_list.append(kmer)
itr = 0
req_kmers = kmers.keys()
while itr+k <= N:
    if s[itr:itr+k] in req_kmers:
        kmers[s[itr:itr+k]] +=1
    itr+=1

for x in kmers_list:
    print(x, end = " ")
    print(kmers[x])
