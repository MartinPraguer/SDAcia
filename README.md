Projekt běží na stránce - https://sdacia-7661.rostiapp.cz/

SDAcia

přidání/úprava/mazání značek aut (nejprve přes /admin) - Mercedes, Audi, ...

přidání/úprava/mazání typu karoserie (nejprve přes /admin) - Sedan, Combi

přidání/úprava/mazání inzerátů (nejprve přes /admin)

přidání/úprava/mazání komentářů (nejprve přes /admin)

stránka inzerátu auta - popis, výkon, rok výroby, cena, datum přidání inzerátu

(pokročilé) zobrazení podobných aut
přidání komentářů k inzerátu

hlavní strana

nejnovější inzeráty
nejnavštěvovanější inzeráty (pokaždé, když se podívám na stránku inzerátu tak se přičte zobrazení)
nejnovější komentáře
hledání inzerátů dle roku výroby, značky, typu karoserie, ceny

neděláme grafiku, neděláme javascript, neřešíme fotky

používáme GIT

Užitečné příkazy
python -m pip install django==4.1.1

django-admin startproject SDAcia .

python3 manage.py runserver - spuštění serveru

python3 manage.py startapp viewer - přidání aplikace

python3 manage.py makemigrations - vytvoření migrací

python3 manage.py migrate - aplikování migrací

python3 manage.py shell

python manage.py createsuperuser - vytvoření uživatele pro admin rozhraní

Dokumentace QuerySet

Musím umět
stáhnout Python, nainstalovat django
vytvořit django projekt, vytvořit django applikaci
vytvořit ORM model ( **class Movie(Model): **)
vytvořit a aplikovat migraci databáze/modelu
přidat objekt do DB
upravit objekt v DB
smazat objekt
vytvořit url v djangu
vrátit html šablonu naplněnou daty
dědění html šablony
filtrování objektů z DB, získání jednoho konkrétního objektu
odeslat formulář
Tipy
id/primární klíč konkrétního záznamu získám jako car.pk
nalezení tohoto záznamu pak mohu udělat jako Car.objects.get(pk=car_pk)
Jak spustit
git clone git@github.com:alifuk/CZ21.git cd CZ21/SDAcia python3 manage.py makemigrations python3 manage.py migrate python3 manage.py runserver
