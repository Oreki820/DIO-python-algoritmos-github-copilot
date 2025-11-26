def eh_palindromo(texto: str) -> bool:
    """Verifica se um texto é palíndromo."""
    texto_limpo = texto.replace(" ", "").lower()
    return texto_limpo == texto_limpo[::-1]

if __name__ == "__main__":
    print(eh_palindromo("Ame a ema"))
