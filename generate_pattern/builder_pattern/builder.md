## 概要
同じ生成過程で素材の異なるオブジェクトを作るパターン
また、引数を**最低限**にして直感的に使うことができる

## 例題
①タイトル
②ヘッダー
③本文
④フッター

が必要な文章を、HTMLとPlainTextで作成します。

## 特徴
Directorクラスを噛ませていること

constructメソッドに具体的な手順を書き込み、実際の作成はbuilderに任せることで、オプションがかなり簡易化される。  

引数が同じでも、渡されるクラスによって異なるオブジェクトが生成される。

引数をbuilderにしないと、以下のような「telescoping constructor」アンチパターンになる  
telescoping constructor -> constructorの引数が多い  
telescopeはここでは順番に当てはめるという意味  
(望遠鏡のように伸びていくという意味でもいけるらしい)  
１つ１つ順番に当てはめるように、受け取れる引数が１つずつ増えていくようなコンストラクタを作成し、それらを順番に呼び出そうという物  

デメリットはオブジェクトを生成するとき引数の意味がわかりにくい  
変数が増えれば増えるほどそれに合わせたコンストラクタが必要になる -> 追加が面倒

```
class Director():
    def construct(self, format="html", title="", header="", contents=[], footer=""):
        # ...
```

## abcクラス
pythonで抽象化をする方法(言語使用には存在していない) -> 抽象基底クラス  
ABC(Abstract Base Class)という名前のモジュール  
抽象クラスはABCMetaというメタクラスで定義できる。定義した抽象基底クラスをスーパークラスとしてサブクラスを定義することが可能  

```
# 抽象クラス
class AbstractBuilder(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def build_title(self, title):
        pass

# 抽象クラスを継承
class HTMLBuilder(AbstractBuilder):

    def build_title(self, title):
        return "<h1>{}</h1>\n".format(title)

if __name__ == "__main__":
    # これは通る
    assert issubclass(HTMLBuilder().__class__, AbstractBuilder)
    assert isinstance(HTMLBuilder(), AbstractBuilder)
```

HTMLの方で@abstractmethodの抽象モジュールを実装してないとエラーになる。

@abstractmethodは、デコレータを指定したメソッドに処理を記述してサブクラスから呼び出すことも可能

```
class AbstractBuilder(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def build_title(self, title):
        eturn "<h1>{}</h1>\n".format(title)

# 抽象クラスを継承
class HTMLBuilder(AbstractBuilder):

    def build_title(self, title):
        # 継承元のbuild_titleを呼び出す
        super(HTMLBuilder, self).build_title()

if __name__ == "__main__":
    print(HTMLBuilder().sound())
```

(参考:https://qiita.com/kaneshin/items/269bc5f156d86f8a91c4)