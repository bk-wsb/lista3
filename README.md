# lista3
# zadanie 1
AUTOMATYZACJA TESTÓW API Z WYKORZYSTANIE CURL

OPIS

  Ten skrypt automatyzuje testowanie endpointów API JSONPlaceholder przy użyciu biblioteki requests.

WYMAGANIA
  - Python 3.x
  - Biblioteka requests (pip install requests)

INSTRUKCJA URUCHOMIENIA
  1. Sklonuj lub pobierz to repozytorium.
  2. Uruchom skryp 'api_test.py' w terminalu:
    > python api_test.py

SKRYPT
  Skrypt testuje następujące endpointy:
  1. posts/1 - sprawdza obecność klucyz: userId, id, title, body
  2. comments/1 - sprawdza obecność kluczy: postId, id, name, email, body
  3. users/1 - sprawdza obecność kluczy: id, name, username, email

WYNIK

  Test posts/1: PASSED; Test comments/1: PASSED; Test users/1: PASSED


# zadanie 2
 AUTOMATYZACJA PROCESÓW Z WYKORZYSTANIEM MAKEFILE

OPIS
Ten projekt zawiera prostą aplikację napisaną w Pythonie na obliczenie delty oraz testy jednostkowe dla tej aplikacji. Automatyzacja procesów testowania i uruchamiania aplikacji jest realizowana za pomocą Makefile.

PLIKI
- app.py: prosta aplikacja na obliczenie delty,
- test_app.py: testy jednostkowe dla aplikacji,
- requirements.txt: plik z zależnościami (pusty),
- Makefile: plik Makefile automatyzujący instalację zależności, uruchamianie testów i aplikacji.

INSTRUKCJA URUCHOMIENIA
  1. Sklonuj lub pobierz to repozytorium.
  2. W terminalu (w ścieżce z plikami i aplikacjami) wpisz komendy:
     > make install
     > make test
     > make run

