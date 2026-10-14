def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u"}
    return sum(character.lower() in vowels for character in text)
