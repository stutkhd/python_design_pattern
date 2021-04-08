import time

def main():
    l = [2, 7, 3, 4, 9, 1]
    sorter_quick = Sorter(QuickSorter())
    print(sorter_quick.sort(l))
    sorter_quick_timer = TimeSorter(QuickSorter())
    print(sorter_quick_timer.timesort(l))

    sorter_bubbl = Sorter(BubbleSorter())
    print(sorter_bubbl.sort(l))
    sorter_bubbl_timer = TimeSorter(BubbleSorter())
    print(sorter_bubbl_timer.timesort(l))

####
# バブルソート
def bsort(a):
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
    return a

# クイックソート
def qsort(a):
    if len(a) in (0, 1):
        return a

    p = a[-1]
    left = [x for x in a[:-1] if x <= p]
    right = [x for x in a[:-1] if x > p]

    return qsort(left) + [p] + qsort(right)

####

# ①
class Sorter:
    def __init__(self):
        pass

    def sort(self, a):
        raise NotImplementedError

class QuickSorter(Sorter):
    def __init__(self):
        pass

    def sort(self, a):
        return qsort()

class BubbleSorter(Sorter):
    def __init__(self):
        pass

    def sort(self, a):
        return bsort(a)

# ②
# QuickSorterはSorterを継承しているため、TimerSorterでsortするには再度継承が必要
# (クラス名も変更の必要がある)
class TimeSorter(Sorter):
    def __init__(self):
        pass

    def timesort(self, a):
        start = time.time()
        a_sorted = self.sort(a)
        print(time.time() - start)
        return a_sorted

class TimeQuickSorter(TimeSorter):
    def __init__(self):
        pass

    def sort(self, a):
        return qsort(a)

class TimeBubbleSorter(TimeSorter):
    def __init__(self):
        pass

    def sort(self, a):
        return bsort(a)

if __name__ == '__main__':
    main()