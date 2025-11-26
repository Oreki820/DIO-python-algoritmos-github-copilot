def fatorial(n: int) -> int:
    """Calcula o fatorial de n."""
    if n < 0:
        raise ValueError("Não existe fatorial de número negativo.")
    if n in (0, 1):
        return 1

    resultado = 1
    for i in range(2, n+1):
        resultado *= i
    return resultado

if __name__ == "__main__":
    print("Fatorial de 5:", fatorial(5))
