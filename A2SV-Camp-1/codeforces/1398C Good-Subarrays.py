for i in range(int(input())):
    size = int(input())
    s = input()
    nums = []
    nums.extend(s)
    nums = list(map(int, nums))
    prefix = [0]
    from collections import defaultdict
    dic = defaultdict(int)
    res = 0

    for num in nums:
        prefix.append(prefix[-1]+num)
    # print(prefix)
    for l in range(size):
        left=prefix[l]-l+1
        dic[left]+=1
        right=prefix[l+1]-(l)
        if right in dic:
            res+=dic[right]

    print(res)
