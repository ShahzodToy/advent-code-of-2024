count = 0

def safe(levels):
    diif = [x-y for x,y in zip(levels, levels[1:])]
    return all(1 <= x <= 3 for x in diif) or all(-1 >= x >= -3 for x in diif)

for report in open("day-2/input.txt"):
    levels = list(map(int, report.split()))
    if any(safe(levels[:index]+ levels[index+1:]) for index in range(len(levels))):
        count += 1
print(count)