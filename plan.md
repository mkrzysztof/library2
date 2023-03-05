# System wypożyczeń w bibliotece.

Biblioteka ma czytelników którzy wypożyczają i zwracają książki.
Czytelnik może mieć na jednocześnie wypożyczonych tylko określoną ilość
książek. Czytelnik może zarezerwować dany tytuł, będzie on na niego czekał
tylko określony czas.

## Wypożyczenie książki:
1. Wejdź na profil czytelnika
2. Zeskanuj (wpisz) kod wypożyczanej książki, jeśli został przekroczony
limit wypożyczonych książek, to nie powinno być możliwości wypożyczenia
innej książki

## Oddanie książki:
1. Wejście na zwracanie książki(bez wchodzenia na profil) i
zeskanowanie/wpisanie kodu książki.

## Wejście na profil czytelnika:
możliwość:

1. Przejrzenia wypożyczonych książek wraz z terminem ich oddania
2. Oddanie książki
3. Przedłużenie wypożyczenia na następny okres
4. Przetrzymane książki powinny być jakoś wyróżnione
5. Wypożyczenia książki
6. Rezygnacja z danego zamówienia
6. Informacja o już dostępnych zamówionych książkach
7. Przeszukianie katalogu książek wraz z możliwością zamówienia danego tytułu.

## Bibliotekarz:
1. Powinien mieć możliwość wyszukania książek po tytule (kawałku) oraz po
autorze i stwierdzenia czy książka jest dostępna, a jeśli jej nie ma jaki jest
najbliższy termin zwrotu, powinna być też możliwość zamówienia książki dla
danego czytelnika, ewentualnie czy książka nie została już zamówiona i przez
kogo.
2. Tworzenie i usuwanie czytelników.

## Katalog biblioteczny:
1. Powinien mieć możliwość szukania książek po autorze, tytule i wyświetlać
informacje o dostępności tytułu (dostępny/wypożyczony/zarezerwowany/brak w
bibliotece takiego tytułu). Powinny być wyświetlane wszystkie egzemplarze
z danego tytułu.

## Jak to wszystko powinno wyglądać:
Aplikacja powinna mieć domyślną funkję katalogu bibliotecznego, oraz możliwość
zalogowania się. W zależności od użytkownika może to być czytelnik lub
bibliotekarz

### Na razie skupimy się na module bibliotekarza:
W ekranie głównym powinna być możliwość zwrotu książki, bez wchodzenia na
profil danego czytelnika. Oraz wyszukania książki.

Po wejściu na profil czytelnika mamy podgląd wypożyczonych książek wraz z
terminem ich oddania (data, ilość dni), możliwość przedłużenia wypożyczenia,
oddanie książki i jeśli jest możliwość wypożyczenie książki. Oraz wyszukania
książki.

Zakładanie i likwidacja "konta" czytelnika.