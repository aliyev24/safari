from . import base_request
from bs4 import BeautifulSoup


class SummerTour(base_request.BaseRequest):
    def __init__(self, url: str, params={}, proxy=None):
        super().__init__()
        if proxy:
            self.set_proxies(proxy)

        self.url = url
        self.params = params
        self.response = None
        self.soup = None
        self.page = 1

    def open_page(self):
        self.response = self.request.get(self.url,
                                         params=self.params,
                                         timeout=(60, 60))
        self.soup = BeautifulSoup(self.response.text, 'lxml')

        return self.response.status_code

    def get_content(self):
        tour_list = self.soup.find('tbody').find_all('tr')
        for tour in tour_list:
            tour_details = [x.text.strip() for x in tour.find_all('td')]
        return tour_details
