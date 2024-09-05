from faker import Faker
import random
from datetime import date

today = date.today()

#klasa bazowa
class movies_library:
    def __init__(self, title, release_year, genre, plays=0):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.plays = plays

    def play(self):
        self.plays += 1

#    def movie(self):
#        print(f"{self.tile} ({self.release_year})")

    def __str__(self):
        return f"{self.title} ({self.release_year})"

#klasa dziedzicząca
class tv_series_library(movies_library):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def play(self):
        self.plays += 1

#    def series(self):
#        print(f"{self.tile} S{self.season}E{self.episode}")

    def __str__(self):
        return f"{self.title} S{self.season:02}E{self.episode:02}"
    
    
      
#klasa do tworzenia losowych list
def create_list(quantity):
    fake = Faker()
    genres = ['Drama', 'Comedy', 'Action', 'Horror', 'Sci-Fi', 'Documentary']
    lista = []
    for _ in range(quantity):
        media_type = random.choice(['movie', 'series'])
        title = fake.catch_phrase()
        release_year = fake.year()
        genre = random.choice(genres)

        if media_type == 'movie':
            lista.append(movies_library(title=title, release_year=release_year, genre=genre))
        else:
            season = random.randint(1, 10)
            episode = random.randint(1, 24)
            lista.append(tv_series_library(title=title, release_year=release_year, genre=genre, season=season, episode=episode))

    return lista


# Funkcja do wyświetlania listy 
def display_lista(lista):
    for i in lista:
        print(str(i))

#Już niepotrzebne
#lista = create_list(10)
#print("Lista filmów i seriali: ")
#display_lista(lista)

# Funkcje do filtrowania listy
def get_movie(lista):
    return sorted([item for item in lista if isinstance(item, movies_library) and not isinstance(item, tv_series_library)], key=lambda x: x.title)

def get_series(lista):
    return sorted([item for item in lista if isinstance(item, tv_series_library)], key=lambda x: x.title)

#Funkcja do wyszukiwania filmów i seriali po tytule
def search(lista, title):
    for item in lista:
        if item.title.lower() == title.lower():
            return item
    return None 

#Funkcja generująca ilość odtworzeń
def generate_views(lista):
    item = random.choice(lista)
    views = random.randint(1, 100)
    item.plays += views
    return f"{item.title} zyskał {views} nowych odtworzeń."

# Funkcja uruchamiająca generate_views 10 razy
def generate_views_10_times(lista):
    for _ in range(10):
        print(generate_views(lista))

# Funkcja zwracająca top n najpopularniejszych tytułów
def top_titles(lista, n=3, content_type=None):
    if content_type == 'movies':
        filtered = get_movie(lista)
    elif content_type == 'series':
        filtered = get_series(lista)
    else:
        filtered = lista
    
    sorted_lista = sorted(filtered, key=lambda x: x.plays, reverse=True)
    return sorted_lista[:n]


# Funkcja do dodawania seriali z pełnymi sezonami
def add_full_season(lista, title, release_year, genre, season, episodes_count):
    for episode in range(1, episodes_count + 1):
        series = tv_series_library(title, release_year, genre, season, episode)
        library.append(series)

#Funkcjaktóra wyświetla liczbę odcinków 
    def display_series_count(lista, series_title):
        count = sum(1 for media in lista if isinstance(media, tv_series_library) and media.title == series_title)
        print(f"Liczba odcinków serialu '{series_title}' w bibliotece: {count}")

#Działania:
if __name__ == "__main__":
    # Wywietlanie listy
    lista = create_list(15)
    print("Biblioteka filmów i seriali: ")
    display_lista(lista)

    # Wyświetlanie listy z podziałem na filmy i seriale
    print("\nFilmy:")
    for movie in get_movie(lista):
        print(movie)

    print("\nSeriale:")
    for series in get_series(lista):
        print(series)

    # Test funkcji search
    print("\nWyszukiwanie:")
    title = input("Podaj tytuł do wyszukania: ")
    found_item = search(lista, title)
    if found_item:
        print(f"Znaleziono: {found_item}")
    else:
        print("Nie znaleziono takiego tytułu.")

    # Generowanie losowych odtworzeń
    print("\nGenerowanie 10 losowych odtworzeń:")
    generate_views_10_times(lista)

    # Wyświetlanie najpopularniejszych tytułów
    print(f"\nNajpopularniejsze tytuły dnia {today} :")
    for item in top_titles(lista, n=3):
        print(f"{item} - {item.plays} odtworzeń")

    # Wyświetlanie najpopularniejszych filmów
    print("\nNajpopularniejsze filmy:")
    for item in top_titles(lista, n=3, content_type='movies'):
        print(f"{item} - {item.plays} odtworzeń")

    # Wyświetlanie najpopularniejszych seriali
    print("\nNajpopularniejsze seriale:")
    for item in top_titles(lista, n=3, content_type='series'):
        print(f"{item} - {item.plays} odtworzeń")