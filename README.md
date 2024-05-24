# Projekt-Dokumentation 1304

Fabian Meyer, Justus Meister


### 1 Beschreibung

Der CodingComrad ist ein Discord-Bot, welcher ihnen mit Hilfe von KI Technologie Informationen über verschiedene coding bezogene Themen bereitstellen kann.


### 2 User Stories

| US-№ | Verbindlichkeit | Typ | Beschreibung                       |
| ---- | --------------- | --- | ---------------------------------- |
| 1    |    muss             |   funktional  | Als User möchte ich den Discord-Bot zu einem Server hinzufügen können. |
| 2  |       muss          |  funktional   |   Als User möchte ich den Bot einem gewissen Text-Kanal zuweisen können (sodass der Bot nur in diesem Channel aktiv ist), damit die anderen Kanäle nicht "missbraucht" werden.              |
| 3  |      muss           |  funktional   |     Als User möchte ich in einem Kanal Commands, welche mit dem Statement "." eingeleitet werden, ausführen, um den Bot zu gebrauchen.               |
| 4  |      muss           |  funktional   |   Als User möchte ich vom Bot Informationen über verschiedene coding-relevante Topics erhalten können.                                |


### 3 Testfälle

| TC-№ | Ausgangslage | Eingabe | Erwartete Ausgabe |
| ---- | ------------ | ------- | ----------------- |
| 1.1  |      -        |  1. Einladungslink geöffnet, 3. Hinzufügen drücken       |      2. Menu zum Hinzufügen des Bots, 4. Bot zu Server hinzugefügt           |
| 2.1  |      Bot auf Server       |  1. ".prefChannel"     |     2. Preferred channel set to (Channel)              |
| 3.1  |     -     |   -     |           -        |
| 4.1  |      Bot auf Server        |   1. ".inf python if"      |      2. Infos zu If Statements in Python             |



## 5 Planen

| AP-№ | Frist | Zuständig | Beschreibung | geplante Zeit |
| ---- | ----- | --------- | ------------ | ------------- |
| 0.A  |   15.03.24    |     Meister     |     Erstellen der Dokumentation         |    15'         |
| 0.B  |   15.03.24    |     Meister, Meyer     |     Informieren über KI-Framework (Tensorflow, GPT-2)         |    60'         |
| 1.A  |    15.03.24   |   Meyer        |      Erstellen des Bots        |      25'         |
| 3.A  |   15.03.24    |    Meister       |     Command-Prefix festlegen (".")       |      10'         |
| 0.C  |   15.03.24    |     Meyer     |     Dokumentation aktualisieren        |    30'         |
| 4.A  |   15.03. - 22.03.24    |    Meister       |      Informationsbeschaffungs-Command implementieren        |      60'         |
| 4.B  |   22.03.24    |    Meyer       |      Informationsbeschaffungs-Command implementieren        |      60'         |
| 2.A  |   22.03.24    |     Meyer      |        Prefered Channel Funktion Implementieren      |        60'       |
| 0.C  |   22.03.24    |     Meister     |     Dokumentation aktualisieren        |    30'         |
| 2.B  |   22.03. - 05.04.24|     Meister      |        Prefered Channel Funktion Implementieren      |        60'       |
| 0.D  |   05.04. - 26.04.24    |     Meister, Meyer      |     Dokumentation fertigstellen         |      60'         |



✍️ Die Nummer hat das Format `N.m`, wobei `N` die Nummer der User Story ist, auf die sich das Arbeitspaket bezieht, und `m` von `A` an nach oben buchstabiert. Beispiel: Das dritte Arbeitspaket, das die zweite User Story betrifft, hat also die Nummer `2.C`.

✍️ Ein Arbeitspaket sollte etwa 45' für eine Person in Anspruch nehmen. Die totale Anzahl Arbeitspakete sollte etwa Folgendem entsprechen: `Anzahl R-Sitzungen` ╳ `Anzahl Gruppenmitglieder` ╳ `4`. Wenn Sie also zu dritt an einem Projekt arbeiten, für welches zwei R-Sitzungen geplant sind, sollten Sie auf `2` ╳ `3` ╳`4` = `24` Arbeitspakete kommen. Sollten Sie merken, dass Sie hier nicht genügend Arbeitspakte haben, denken Sie sich weitere "Kann"-User Stories für Kapitel 1.2 aus.


## 6 Realisieren

| AP-№ | Datum | Zuständig | geplante Zeit | tatsächliche Zeit |
| ---- | ----- | --------- | ------------- | ----------------- |
| 0.A  |   15.03.24    |    Meister, Meyer       |     15'          |     10'              |
| 0.B  |    15.03.24   |    Meister      |        60'       |       90'            |
| 1.A  |    15.03.24   |     Meyer      |      25'         |          40'         |
| 3.A  |    15.03.24   |    Meister       |      10'         |         10'          |
| 0.C  |    15.03.24   |      Meyer     |       30'        |             30'      |
| 4.A  |  22.03.24     |       Meister    |      60'         |           60'        |
| 4.B  |    22.03.24   |       Meyer    |     60'          |           70'        |
| 2.A  |    22.03.24   |      Meyer     |      60'         |         60'          |
| 0.C  |   22.03.24    |     Meister      |     30'          |        20'           |
| 2.B  |    05.04.24   |         Meister  |       60'        |           40'        |
| 0.D  |   05.04.24    |       Meister, Meyer    |        60'       |         80'          |




### 6 Testprotokoll

| TC-№ | Datum | Resultat | Tester |
| ---- | ----- | -------- | ------ |
| 1.1  |       |          |        |
| ...  |       |          |        |



### 7 Auswertung

