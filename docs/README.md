# :moneybag: MoneyPlan(e)t :herb:

**MoneyPlan(e)t** je spletna aplikacija namenjena ljudem, ki imajo težave z urejanjem svojih financ in beleženjem stroškov svojega življenja. Z učinkovitim in enostavnim beleženjem stroškov uporabniku pomaga, da prihrani svoj denar in vidi, za kaj največ zapravlja. Uporabnik lahko svoj denar usmeri v izpolnjevanje večjih ciljev, ki jih lahko ustvari in si nastavi rok za izpolnitev, ter nato dodaja denar. Vsak uporabnik ima na voljo več *denarnic* (denarnica, kreditna kartica, račun na banki...) za katere lahko beleži stroške. Slednje lahko razporeja po kategorijah, lahko pa si nastavi tudi avtomatično ponavljanje stroškov (npr za vsakomesečne račune). Aplikacija omogoča tudi enostavno beleženje izposojenega denarja in posojil drugim ljudem, ter izpis različnih statistik. 

## Ciljna publika in naprave
Ciljni uporabniki so predvsem ljudje, ki so vajeni uporabe tehnologije in želijo urediti svoje finance in kaj prihraniti. Vseeno je aplikacija preprosta za uporabo, tako da jo lahko uporablja tudi kdo, ki rabi tehnologije ni tako vešč. Aplikacija je primerna za uporabo na vsaki napravi (računalnik, tablica, mobilni telefon), najbolj pa je priročna uporaba na večjem zaslonu (sploh pri pregledu statistik). 

## Struktura spletišča
Odločila sem se za hierarhično organizacijo spletne strani in se osredotočila na vsebino. Domača stran tako že sama po sebi prikazuje informacije (izdatke), obenem pa z gumbi in meniji omogoča hiter prehod na vse ostale dele, tako da lahko uporabnik le z nekaj kliki naredi karkoli. 

## Različni brskalniki
Za testiranje sem uporabila Firefox, Chrome in Safari. Aplikacija je večinoma dobro delovala tudi pri spreminjanju velikosti, problemi so se pojavili le pri dinamičnem spreminjanju form, saj v Safariju ni delovalo brisanje class atirbutov. 

## 2 posebna gradnika
1. Dodala sem dinamičen hamburger menu, ki se z manjšo animacijo prikaže ali skrije in je zelo uporaben tudi pri responsive designu, saj ni v napoto. 
2. Poleg tega sem implementirala tudi način prikaza podatkov z zavihki, kar mi je omogočilo poudarek vsebine, saj je večinoma celotna vsebina na zaslonu. 

## Dodatni komentarji & problemi
Moj glavni problem je bil, da validator ne omogoča align atributa. Sama sem vse naredila na ta način in nekaterih stvari potem nisem mogla enako implementirati brez tega, zato se mi je malo pokvaril design.