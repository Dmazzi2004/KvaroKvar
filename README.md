# KvaroKvar
## Dokumentacija: Sustav za upravljanje kvarovima u zgradama
Ovaj projekt je web-aplikacija za evidenciju i upravljanje kvarovima u zgradama. Aplikacija Omogućuje:
-dodavanje prijava kvarova
-pregled i filtriranje po statusu ili datumu
-ažuriranje statusa kvara
-vizualizaciju statistike kvarova po statusu

Aplikacija koristi Python, Flask, PonyORM, SQLite na backendu, te HTML i Chart.js na frontend dijelu. Sve je upakirano u Docker kontejner preko kojega se odvija pokretanje.
struktura aplikacije se rasteže na tri .py, tri .html, jednu CSS, te i docker i textualnu datoteku, od kojih svaka postoji sa razlogom. main.py je za glavni ulaz u aplikaciju, API.py je Flask Blueprint s rutama, baza.py definira bazu i model (PonyORM), index.html služi kao glavni HTML prikaz, Dockerfile je tu za konfiguraciju dockera i requirements.txt je popis potrepština za Python. 

Funkcionalnosti ove aplikacije su vrlo jednostavne, dodavanje kvara, pregled svih kvarova (prijavljenih), ažuriranje i filtriranje statusa kvarova te i grafički prikaz statistike kvarova. Aplikacija automatski prikazuje bar chart statistiku broja kvarova prema njihovim statusima ("prijavljen", "u tijeku", "riješen").


Aplikaciju sam ja osobno pokretao preko Dockera ili Powershella koristeći(jednostavnije preko dockera (http://localhost:5000), ali ovako je zabavnije):

docker build -t kvarovi-app .

docker run -p 5000:5000 kvarovi-app


Autor: Dominik Mazzi

Napomena: Projekt je izrađen (kako bi se izbjeglo usmeno ispitivanje) za kolegij "Informacijski sustavi".


