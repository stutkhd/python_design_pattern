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

# ①：配列のソートをクイックソートまたはバブルソートを実行（方向①）
class Sorter:
    def __init__(self, sorter):
        self.sorter = sorter

    def sort(self, a):
        return self.sorter.sort(a)

class SortImple: # こいつはいつ発生する？
    def sort(a):
        raise NotImplementedError

# SortImpleと同じ関数名じゃなくても良い
class QuickSorter(SortImple):
    def __init__(self):
        pass
    def sort(self, a):
        return qsort(a)


class BubbleSorter(SortImple):
    def __init__(self):
        pass
    
    def sort(self, a):
        return bsort(a)

# ②：後に、①の機能に、ソートの時間を計測する機能を足す
class TimeSorter(Sorter):
    def timesort(self, a):
        start = time.time()
        a_sorted = self.sorter.sort(a) # 継承してるから使える？
        print(time.time() - start)
        return a_sorted

if __name__ == '__main__':
    main()


