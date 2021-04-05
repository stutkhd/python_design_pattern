## 概要
**既存のクラスを修正することなく、インターフェースを修正する**

## 例題
月報をHTML形式で出力するプログラムを考えます。  

- HtmlWriter クラスがすでにあり、このクラスを使用します。  

- PlainTextReporterクラスもすでにあり、このクラスと同じメソッドで出力できるようにします。（インターフェースを同じにする）  

Adapterパターンは「**継承による実装**」と「**委譲による実装**」の2パターンがあるため、2パターン両方で実装しています。  

## 特徴
継承ver

```python
class HtmlReporter(Reporter, HtmlWriter):
    # ...

    def header(self, title):
        self.out_header()
        self.out_title(title)
        self.out_start_body()

    def main(self, texts):
        # ...
```

１行目はHtmlWriterに対して**汎化(継承)**を、Reporterに対して**実現**をしたいためこのような書き方になっている。  
pythonでは両方継承すればいい。pythonでは多重継承できるためエラーでない

```python
def header(self, title):
    self.out_header()
    self.out_title(title)
    self.out_start_body()
```
header メソッドに対して、元のout_header,out_title,out_start_bodyを使用することで代用している。  
