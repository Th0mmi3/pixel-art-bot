from icrawler.builtin import BingImageCrawler, BaiduImageCrawler

class grabber:
    def __init__(self, _path, _amount):
        #self.prompt = _prompt
        self.path = _path
        self.amount = _amount

    def grab(self, prompt):
        google_crawler = BingImageCrawler(
            feeder_threads=1,
            parser_threads=1,
            downloader_threads=4,
            storage={'root_dir': self.path}
        )
        google_crawler.crawl(keyword=prompt, filters=dict(size='large'), max_num=self.amount)