with open("orbits_input") as fh:
    lo = [line.rstrip('\n') for line in fh.readlines()]
mid = []
low = []
for i in lo:
    mid.append(i[:3])
    low.append(i[-3:])
mid=list(dict.fromkeys(mid))
low=list(dict.fromkeys(low))
for a in mid:
    if a not in low:
        print("Nie krąży {}".format(a))
        return a

print(mid)
print(low)


