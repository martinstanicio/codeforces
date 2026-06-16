# # 001. Sopa de Letras
#
# Se te proporciona una palabra objetivo $w$ y un conjunto de $n$ cadenas de
# caracteres. Tu tarea consiste en calcular cuántas veces aparece la palabra $w$
# o su versión invertida dentro de este conjunto de cadenas como una subcadena
# contigua.
#
# Si la palabra $w$ es un palíndromo (es decir, se lee igual al derecho y al
# revés), cada una de sus apariciones en las cadenas se debe contabilizar una
# sola vez.
#
# ## Input
#
# La primera línea contiene una cadena de caracteres $w$ — la palabra objetivo a
# buscar.
#
# La segunda línea contiene un único entero $n$ — la cantidad de cadenas de
# caracteres.
#
# Las siguientes $n$ líneas contienen, cada una, una cadena de caracteres $s_i$.
#
# Todas las cadenas de caracteres consisten únicamente de letras minúsculas del
# alfabeto inglés.
#
# ## Output
#
# Imprime un único entero — la cantidad total de veces que la palabra $w$ (o su
# versión invertida) aparece como subcadena en las $n$ cadenas dadas.
#
# ## Example
#
# ### Input
#
# ```text
# palo
# 5
# oolapspalo
# retrossss
# llolap
# z
# palopaloolap
# ```
#
# ### Output
#
# ```text
# 6
# ```


def word_search(string: str, target_words: set[str]) -> int:
    matches = 0
    target_word_indexes = [0] * len(target_words)

    # Este algoritmo no funciona para el caso donde dos apariciones de una misma
    # target_word están superpuestas (por ejemplo, "aba" en "ababa"). Corregir.
    for char in string:
        for i, target_word in enumerate(target_words):
            if char != target_word[target_word_indexes[i]]:
                target_word_indexes[i] = 0

            if char == target_word[target_word_indexes[i]]:
                target_word_indexes[i] += 1

            if target_word_indexes[i] == len(target_word):
                matches += 1
                target_word_indexes[i] = 0

    return matches


def main() -> None:
    word = input()
    n = int(input())
    strings: list[str] = []

    for _ in range(n):
        string = input()
        strings.append(string)

    target_words = set([word, word[::-1]])

    answer = sum(word_search(string, target_words) for string in strings)

    print(answer)


if __name__ == "__main__":
    main()
