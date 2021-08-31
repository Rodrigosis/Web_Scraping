import requests
import uuid
import pathlib
from bs4 import BeautifulSoup
import urllib3

from src.domain.scraping import Scraping, Manga
from src.infra.database import Database
from src.infra.storage import Storage


class UrlOne(Scraping):

    def __init__(self):
        self.db = Database()
        self.s3 = Storage()
        self.http = urllib3.PoolManager()

    def add_new(self, url: str) -> Manga:
        manga = Manga(manga_id=str(uuid.uuid4()), link=url)
        soup = self.get_html(url=url)
        # print(soup.prettify())

        name = soup.find('h1', {'class': 'titulo text-uppercase'}).text
        name = name.replace('Ler', '')
        name = name.replace('Online', '')
        manga.name = name.strip()

        check_manga_exist = self.db.get_manga_by_name(manga.name)
        if check_manga_exist:
            return check_manga_exist[0]

        text_block = soup.find('div', {'class': 'serie-texto'})
        text_block = text_block.p.p.text
        text_block = text_block.split('\n')
        manga.about = text_block[0]

        text_block.remove(text_block[0])
        manga.alternative_names = []
        for name in text_block:
            name = name.replace('Nome alternativo:', '')
            manga.alternative_names.append(name.strip())

        text_block = soup.find('div', {'class': 'serie-infos'}).text
        text_block = text_block.split('\n')
        for line in text_block:
            if 'Autor:' in line:
                author = line.replace('Autor:', '')
                manga.author = author.strip()
            elif 'Categorias:' in line:
                categories = line.replace('Categorias:', '')
                manga.categories = [x.strip() for x in categories.split(',')]

        manga = self.chapters_info(manga=manga, html=soup)
        manga = self.get_image(manga=manga, html=soup)

        self.db.set_manga(manga=manga)
        # self.s3.set_file(image_name=manga.image, folder='/mangas/front/')

        return manga

    def update(self, manga_id: str, url: str) -> Manga:
        soup = self.get_html(url=url)
        manga = self.chapters_info(manga=Manga(manga_id=manga_id), html=soup)
        return manga

    def get_html(self, url: str) -> BeautifulSoup:
        page = self.http.request('GET', url)

        if page.status == 200:
            return BeautifulSoup(page.data, features='html.parser')
        else:
            raise Exception(f'Request status_code {page.status}')

    def chapters_info(self, manga: Manga, html) -> Manga:
        chapters = html.find('ul', {'class': 'capitulos'})
        chapters = chapters.find_all('li')
        manga.num_cap = len(chapters)

        last_cap = chapters[-1].text
        last_cap = last_cap.replace('Capítulo', '')
        manga.last_cap = float(last_cap)
        return manga

    def get_image(self, manga: Manga, html) -> Manga:
        img_block = html.find('div', {'class': 'serie-capa'})
        img_url = img_block.img['src']

        response = requests.get(img_url)

        path = pathlib.Path(__file__).parent.parent.parent.resolve()
        path = str(path) + '/infra/images/'

        f = open(path + manga.id + '.jpg', 'wb')
        f.write(response.content)
        f.close()

        manga.image = manga.id + '.jpg'
        return manga
