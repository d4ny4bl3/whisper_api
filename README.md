# FastAPI Whisper API

## Popis

Tato aplikace poskytuje REST API postavené na FastAPI pro:

- Načtení stavu modelu Whisper.

- Převod řeči na text (použitím modelu Whisper).

- Zobrazení aktuální verze API.

## Požadavky

- Python 3.9+

- FastAPI

- Uvicorn (pro spuštění serveru)

- Knihovny pro model Whisper

- FFmpeg (pro zpracování zvukových souborů)

## Instalace

1. Naklonujte projekt z repozitáře:

``` git clone https://github.com/d4ny4bl3/whisper_api ```

``` cd whisper_api ```

2. Vytvořte a aktivujte virtuální prostředí:

``` python -m venv env ```

``` source venv/bin/activate  # Na Windows použijte: venv\Scripts\activate ```

3. Nainstalujte požadované balíčky:

``` pip install -r requirements.txt ```

4. Ujistěte se, že máte nainstalovaný FFmpeg a přidaný do PATH.


## Spuštění aplikace

Spusťte aplikaci pomocí Uvicorn:

``` uvicorn main:app --reload ```

Server bude dostupný na:

- Swagger UI: http://127.0.0.1:8000/docs

- ReDoc: http://127.0.0.1:8000/redoc

## Použití

### Endpointy API

#### Kontrola stavu modelu

- URL: http://127.0.0.1:8000/status/

- Popis: Vrací aktuální stav modelu Whisper.

#### Převod řeči na text

- URL: http://127.0.0.1:8000/docs#/Transcription

- Popis: Přijímá zvukový soubor ve formátu .wav a vrací přepsaný text.

#### Zobrazení verze API

- URL: http://127.0.0.1:8000/version/

- Popis: Vrací aktuální verzi API.