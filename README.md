# Hangman

## Selle README.md sisukord

- Tehnoloogia
- Funktsionaalsete nõuete loetelu
- Installimine
- Kasutamine
- Koostajad

## Tehnoloogia

Tehnoloogia, millega töö implementeeritakse ehk programmeerimiskeel on Python3.

## Funktsionaalsete nõuete loetelu:

### Äraarvatava sõna valimine

- Äraarvatava sõna valib programm.
- Sõna võetakse tekstifailist suvalise valiku põhimõttel.
- Enne sõna võtmist tekstifailist kontrollitakse funktsiooniga tekstifaili sisu korrektsust (ühel real on üks sõna, iga sõna sisaldab ainult tähti, kõik tähed on väiketähed, sõna pikkus on vähemalt 6 tähte).

### Arvamiste haldamine

- Arvamiste arv on 6.
- Programm kuvab kasutajatele allesjäänud arvamiste arvu enne iga arvamist.
- Kasutaja annab sisendi terminali kaudu, sisendiks võib olla kas täht või mitu tähte (sõna).
- Programm jätab meelde kõik unikaalsed sisendid kasutajalt.
- Kasutajalt sisendi saamisel programm võrdleb, kas kasutaja sisestatud täht/sõna on äraarvatavas sõnas olemas.

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

## Tööde jaotus

### karlklein4

- Kirjutab ümber koodi tutoriali järgi.
- Muudab koodi nii, et mängija saaks arvata 6 korda.
- Kirjutab koodi sisse programmiread, mille abil kuvatakse kasutajale enne iga arvamist allesjäänud arvamiste arvu, näiteks sõnumiga “You have [x] guesses left.”, kus x on allesjäänud arvamiste arv.

### KeitiEk ja FrenchFriesForBallerina

- Kirjutavad testid arvamiste arvu kohta (näiteks test, mis kontrollib, et väljastataks õiged sõnumid olenevalt allesjäänud arvamiste arvule, jne.).
- Moodustavad klassi (näiteks klass Game, mis hoiab infot ühe mängu kohta).

### Kui aega üle jääb:

- KeitiEk – GUI mehikese kuvamiseks
- FrenchFriesForBallerina – Web Scraping sõnade otsimiseks
