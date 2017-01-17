from html.parser import HTMLParser
from urllib import parse

#inherits from HTMLParser
class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            # href is the attribute, url is the value
            for (attribute, value) in attrs:
                if attribute == 'href':
                    #if uri join it with base url
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    # Returns the set of links
    def page_links(self):
        return self.links

    def error(self, message):
        pass

print(LinkFinder('http://google.com', '/images' ).page_links())