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
  2. Uruchom skrypy 'api_test.py' w terminalu:
    > python api_test.py

WYNIK

  Test posts/1: PASSED; Test comments/1: PASSED; Test users/1: PASSED

PRZYKŁADOWE TESTY

  Skrypt testuje następujące endpointy:
  1. posts/1 - sprawdza obecność klucyz: userId, id, title, body
  2. comments/1 - sprawdza obecność kluczy: postId, id, name, email, body
  3. users/1 - sprawdza obecność kluczy: id, name, username, email

# zadanie 2
Automatyzacja procesów z wykorzystaniem Makefile AUTOMATYZACJA PROCES
