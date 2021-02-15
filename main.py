import numpy as np

# Введення
# sample = input("Введіть вибірку через пробіл: ").split(" ")
# for i in range(len(sample)):
#     sample[i] = int(sample[i])
# y = float(input("Введіть значення γ, для розрахунку γ-відсотковий наробітокна відмову Tγ: "))
# time1 = int(input("Введіть час, для розрахунку ймовірності безвідмовної роботи: "))
# time2 = int(input("Введіть час, для розрахунку інтенсивності відмов: "))


# Значення по варіанут 29
sample = [
    889, 500, 607, 1656, 265, 20, 122, 1568, 58,
    805, 1177, 248, 71, 75, 1248, 502, 817, 94,
    48, 542, 1088, 216, 1496, 149, 1982, 283,
    15, 226, 241, 545, 401, 499, 673, 373, 641,
    641, 174, 1230, 1190, 203, 206, 600, 677,
    130, 15, 118, 170, 726, 349, 564, 186, 1172,
    462, 521, 285, 553, 432, 1065, 917, 203,
    1056, 63, 445, 44, 311, 639, 680, 114, 356,
    318, 2223, 104, 83, 179, 1875, 241, 404, 0,
    252, 135, 1186, 1808, 1670, 835, 253, 67,
    40, 1125, 153, 16, 718, 623, 337, 165, 957,
    2, 197, 913, 473, 650
            ]
y = 0.63
time1 = 680
time2 = 1468

sample_avarege = np.average(sample)
print("Tср = ",sample_avarege)

sorted_sample = sorted(sample)
h = sorted_sample[-1]/10
print("Довжина одного інтервалу = ",h)

amount = 10
N = len(sorted_sample)
intervals = []
for i in range(amount):
    intervals.append([i*h,(i+1)*h])
    print(i+1,"-й інтервал від ", i*h, "до ", (i+1)*h)

intervals_nums = []
for i,j in intervals:
    tmp = []
    for k in sorted_sample:
        if k >= i and k <= j:
            tmp.append(k)
    intervals_nums.append(tmp)

f = []
for interval_num in intervals_nums:
    f.append(len(interval_num)/(N*h))

print("Статистична щільність розподілу ймовірності відмови:")
for i in range(len(f)):
    print("для ", i + 1, "-го інтервалу f", i+1," = ", f[i])

P0 = 1.000000
P = []
pi = 0
for i in f:
    pi += i*h
    P.append(1-pi)
print("Ймовірність безвідмовної роботи пристрою на час правої границі інтервалу:")
print("P(0) = ", P0)
for i in range(len(P)):
    print("для ", i + 1, "-го інтервалу P(",intervals[i][1],") = ", P[i])

d01 = (1-y)/(1-P[0])
print("d(0,1) = ", d01)

T = 0 + h * d01
print("T",y," = ",T)

def get_intervals(time):
    needed_interval = 0
    for i in intervals:
        if time >= i[0] and time <= i[1]:
            needed_interval = intervals.index(i)
    return needed_interval

def get_P(needed_intervals):
    Qt = 0
    for i in range(needed_intervals):
        Qt += f[i]*h
    Qt += f[needed_intervals]*(time1 - intervals[needed_intervals][0])
    P_time = 1 - Qt
    return P_time

needed_intervals1 = get_intervals(time1)
P_time1 = get_P(needed_intervals1)
print("Ймовірність безвідмовної роботи на час ",time1,"годин = ",P_time1)

needed_intervals2 = get_intervals(time2)
P_time2 = get_P(needed_intervals2)
l = f[needed_intervals2]/P_time2
print("Інтенсивність відмов на час ",time2, " годин = ",l)


