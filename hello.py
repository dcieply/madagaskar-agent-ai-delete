"""Prosty skrypt wypisujący powitanie z Madagaskaru."""

GREETING = "Witaj z Madagaskaru!"


def greet() -> str:
    """Zwraca tekst powitania."""
    return GREETING


def main() -> None:
    print(greet())


if __name__ == "__main__":
    main()
