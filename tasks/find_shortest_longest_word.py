__all__ = ("find_shortest_longest_word",)

import string


def find_shortest_longest_word(text: str) -> tuple[str, str] | tuple[None, None]:
    """Находит самое короткое и самое длинное слово.

    Returns:
        (<самое короткое слово>, <самое длинное слово>) – если text содержит слова,
        (None, None) – иначе

    Example:
        >> find_shortest_longest_word("а бб ввв")
        ("а", "ввв")
        >> find_shortest_longest_word(" \n\t ")
        (None, None)
    """
    words = []
    for word in text.split():
        pure = word.strip(".,?!-()")
        if pure:
            words.append(pure)
    if not words:
        return None, None
    if len(words) == 1:
        return words[0], words[0]
    return min(words, key=len), max(words, key=len)
