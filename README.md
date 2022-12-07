# Hangman

## README.md sisukord

- Tehnoloogia
- Projekti alus
- Funktsionaalsete nõuete loetelu
- Koostajad

## Tehnoloogia

Tehnoloogia, millega töö implementeeritakse ehk programmeerimiskeel on Python3.

## Projekti alus

Projekti aluseks on võetud [Tech with Mike koodibaas](https://www.mrmichaelsclass.com/python-programming/python-projects/hangman)

## Funktsionaalsete nõuete loetelu:

### Äraarvatava sõna valimine

- Äraarvatava sõna valib programm.
- Sõna võetakse tekstifailist suvalise valiku põhimõttel.
- Enne sõna võtmist tekstifailist kontrollitakse funktsiooniga tekstifaili sisu korrektsust (ühel real on üks sõna, iga sõna sisaldab ainult tähti, kõik tähed on väiketähed, sõna pikkus on vähemalt 6 tähte).

### Arvamiste haldamine

- Arvamiste arv on 6.
- Programm kuvab kasutajatele allesjäänud eksimuste arvu enne iga arvamist.
- Kasutaja annab sisendi terminali kaudu, sisendiks võib olla täht.
- Programm jätab meelde kõik unikaalsed sisendid kasutajalt.
- Kasutajalt sisendi saamisel programm võrdleb, kas kasutaja sisestatud täht on äraarvatavas sõnas olemas.

### Õiged arvamised

- Kui kasutaja arvatud täht leidub sõnas, kuvab programm kasutajale tähed õigetel kohtadel sõnas.
- Kui kasutaja on tähte või sõna juba proovinud arvata, kuvatakse talle selle kohta teade Valesti arvamiste arv ei suurene. Kasutajale pakutakse uuesti arvata.
- Kui kasutaja arvatud sõna kattub äraarvatava sõnaga, siis kuvab programm võidusõnumi: “You guessed it!” ja seejärel kuvatakse "I picked" ja sõna, mille programm tekstifailist äraarvamiseks valis.
- Kui kasutaja on kõik sõnas leiduvad tähed ära arvanud, siis kuvab programm võidusõnumi: “You guessed it!” ja seejärel kuvatakse "I picked" ja sõna, mille programm tekstifailist äraarvamiseks valis.

### Valed arvamised

- Kui kasutaja arvas valesti, jätab programm selle meelde ja lisab tähe või sõna valede arvamiste loetellu.
- Iga valesti arvamisega väheneb allesjäänud arvamiste arv ühe võrra.
- Iga valesti arvamisega lisandub mehikesele pea, keha, 1. käsi, 2. käsi, 1. jalg, 2. jalg.
- Kui kasutaja proovib arvata korraga sõna/sõnaosa ja arvab valesti, siis kuvab programm kasutajale sõnumi “is not in my word” koos kõikide valesti arvatud tähte/sõnadega.
- Kui kasutaja on teist korda sama tähte/sõna valesti arvanud, siis talle kuvatakse sõnum: "You already guessed " koos valesti arvatud tähe/sõnaga. Valesti arvamiste arv sel juhul ei suurene, jääb samaks.
- Kui kasutaja valesti arvamiste arv võrdub 6-ga, puuakse kriipsumehike üles ja kasutaja kaotab. Kasutajale kuvatakse sõnum "Game Over!” ja seejärel kuvatakse "I picked" ja sõna, mille programm tekstifailist äraarvamiseks valis.

## Koostajad

FrenchFriesForBallerina, karlklein4, KeitiEk
