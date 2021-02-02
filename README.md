# Palvelinohjelmointi 2021

## Ajaminen

Mene haluamaasi hakemistoon, luo virtual environment ja aktivoi se.

```bash
cd 01-eka-endpoint
python3 -m venv venv
source venv/bin/activate
```

Asenna tarvittavat paketit `requirements.txt` filestä.


```bash
pip install -r requirements.txt
```

Aja softa (esimerkki)

```bash
uvicorn main:app --reload
```

## Satunnaisia juttuja

### Asennettujen kirjastojen tallentaminen tiedostoon

```bash
pip freeze > requirements.txt
```

### Virtual environmentin deaktivointi

```bash
deactivate
```