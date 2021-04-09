import unicodedata
from abc import ABCMeta, abstractmethod

def main():
    # 最初は環境側の具象クラスをインスタンス化
    # それをパラメータにして機能クラスをインスタンス化する
    d1 = Display(StringDisplayImpl('Hello, Japan.'))
    d2 = CountDisplay(StringDisplayImpl('Hello, World.'))
    # Displayを拡張した機能を追加したクラスを使う場合
    d3 = CountDisplay(StringDisplayImpl('Hello, Universe.'))
    d1.display()
    print()
    d2.display()
    print()
    d3.display()
    print()
    d3.multi_display(5)

# 機能側の上位クラス
# 環境側(StringDisplayImpl)の固有の動作を一般的な動作に置き換えている
# 一般的な動作を使ってアレンジするメソッドを使っている
# 機能側の追加クラス(CountDisplay?)はそのアレンジするメソッドだけを改造する
class Display:
    def __init__(self, impl):
        self.impl = impl # 環境側のインスタンスを受けとる
    
    # 以下のメソッドは環境側のクラス固有の動作をするようになっている
    # つまり、誰から呼ばれたか知らなくていい(それはmain()だけが分かればいい)
    def open(self):
        self.impl.raw_open()
    
    def pprint(self):
        self.impl.raw_pprint()

    def close(self):
        self.impl.raw_close()
    
    def display(self):
        self.open()
        self.pprint()
        self.close()

# 環境側の上位クラスであり、テンプレートであり抽象クラス
class DisplayImpl(metaclass=ABCMeta):
    @abstractmethod
    def raw_open(self):
        pass

    @abstractmethod
    def raw_pprint(self):
        pass

    @abstractmethod
    def raw_close(self):
        pass

# 機能側の追加されたメソッドを持つクラス
class CountDisplay(Display):
    def __init__(self, impl):
        super().__init__(impl)
    
    # Displayクラスのdisplayメソッドをアレンジしている
    def multi_display(self, times):
        self.open()
        for _ in range(times):
            self.pprint()
        self.close()

# 環境側の具象クラス
class StringDisplayImpl(DisplayImpl):
    def __init__(self, string):
        self.string = string
        self.width = count_chara(string)
    
    def print_line(self):
        print('+', end='')
        for _ in range(self.width):
            print('-', end='')
        print('+')
    
    def raw_open(self):
        self.print_line()

    def raw_pprint(self):
        print('|{}|'.format(self.string))

    def raw_close(self):
        self.print_line()

def count_chara(cha):
    # 半角文字か全角文字の長さを数える
    length = 0
    for c in cha:
        if unicodedata.east_asian_width(c) in ['W', 'W']:
            length += 2
        else:
            length += 1

    return length

if __name__ == '__main__':
    main()