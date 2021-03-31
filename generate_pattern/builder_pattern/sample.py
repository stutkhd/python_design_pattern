import abc

def main():
    html = Director().construct(HTMLBuilder())
    text = Director().construct(TextBuilder())
    print(html)
    print('**************')
    print(text)

class Director():

    def construct(self, builder):
        all_str = ''
        all_str += builder.build_title('Monthly Report')
        all_str += builder.build_header("--------")
        all_str += builder.build_contents(["Monday: 20", "Tuesday: 30"])
        all_str += builder.build_footer("-*-*-*-")
        return all_str

class AbstractBuilder(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def build_title(self, title):
        pass

    @abc.abstractmethod
    def build_header(self, title):
        pass

    @abc.abstractmethod
    def build_contents(self, title):
        pass

    @abc.abstractmethod
    def build_footer(self, title):
        pass

# ConcreteBuilder
class HTMLBuilder(AbstractBuilder):

    def build_title(self, title):
        return f"<h1>{title}</h1>\n"

    def build_header(self, header):
        return f"<header><p>{header}</p></header>\n"

    def build_contents(self, contents):
        html_contents = []
        for content in contents:
            html_contents.append(f"<p>{content}</p>\n")
        return ''.join(html_contents)

    def build_footer(self, footer):
        return f"<footer><p>{footer}</p></footer>\n"

# ConcreteBuilder
class TextBuilder(AbstractBuilder):

    def build_title(self, title):
        return f"**{title}**\n"

    def build_header(self, header):
        return f"{header}\n"

    def build_contents(self, contents):
        text_contents = []
        for content in contents:
            text_contents.append(f"{content}\n")
        return "".join(text_contents)

    def build_footer(self, footer):
        return f"{footer}\n"

if __name__ == '__main__':
    main()