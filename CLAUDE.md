# CLAUDE.md

Convenzioni di progetto per Claude Code.

## Linguaggio

- Python 3.10+
- Usare le funzionalità moderne del linguaggio (match/case, union types con `|`, ecc.)

## Testing

- Framework: **pytest**
- I test vanno nella cartella `tests/`
- Ogni modulo `src/foo.py` ha il suo file di test `tests/test_foo.py`
- Eseguire i test con: `pytest`

## Stile

- Tutte le funzioni devono avere **type hints** su parametri e valore di ritorno
- Tutte le funzioni devono avere una **docstring**
- Una funzione per concetto: funzioni brevi e focalizzate

### Esempio corretto

```python
def get_input(prompt: str) -> float:
    """Richiede un numero all'utente e lo restituisce come float."""
    return float(input(prompt))

def somma(a: float, b: float) -> float:
    """Restituisce la somma di due numeri."""
    return a + b
```

### Esempio errato

```python
def somma(a, b): return a + b  # no type hints, no docstring
```
