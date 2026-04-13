from src.utils import somma


def get_input(prompt: str) -> float:
    """Richiede un numero all'utente e lo restituisce come float."""
    return float(input(prompt))


def main() -> None:
    """Entry point principale."""
    a = get_input("Inserisci il primo numero: ")
    b = get_input("Inserisci il secondo numero: ")
    print(f"Risultato: {somma(a, b)}")


if __name__ == "__main__":
    main()
