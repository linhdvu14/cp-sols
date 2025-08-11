''' Code-Eat Switcher 
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edb/00000000001707b8
'''
def search(nums, target):  # first index >= target
    lo, hi = 0, len(nums)
    for i in range (40):
        mi = lo + (hi - lo) // 2
        if nums[mi] < target:
            lo = mi
        else:
            hi = mi
    if nums[lo] >= target:
        return lo
    return lo+1

def solve(slots, days):
    ratios =[s[0]/s[1] for s in slots]
    slots = [s for r, s in sorted(zip(ratios, slots))]
    
    esums = []  # left
    tmp = 0
    for (c, e) in slots:
        tmp += e
        esums.append(tmp)

    csums = []  # right
    tmp = 0
    for (c, e) in slots[::-1]:
        tmp += c
        csums.append(tmp)
    csums = csums[::-1]

    out = ''
    for (ctarget, etarget) in days:
        if ctarget > csums[0] or etarget > esums[-1]: 
            out += 'N'
            continue

        i = search(esums, etarget)
        c, e = slots[i]
        cc, ee = ctarget - csums[i] + c, etarget - esums[i] + e
        if cc/c + ee/e <=1:
            out += 'Y'
        else:
            out += 'N'
    return out



def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for t in range(T):
        d, s = list(map(int,stdin.readline().strip().split()))
        slots, days = [], []
        for _ in range(s):
            c, e = list(map(int,stdin.readline().strip().split()))
            slots.append((c, e))
        for _ in range(d):
            a, b = list(map(int,stdin.readline().strip().split()))
            days.append((a, b))
        out = solve(slots, days)
        print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
    main()