import random


def jumble_inner_letters(word):
    if len(word) <= 3:
        return word  # Don't jumble short words

    inner_letters = list(word[1:-1])
    random.shuffle(inner_letters)
    jumbled_word = word[0] + ''.join(inner_letters) + word[-1]
    return jumbled_word


def introduce_sophisticated_typos(text, typo_probability):
    words = text.split()
    modified_words = []

    for word in words:
        if random.random() < typo_probability and word.isalpha():
            # Introduce a sophisticated typo by jumbling inner letters
            modified_word = jumble_inner_letters(word)
            modified_words.append(modified_word)
        else:
            modified_words.append(word)

    modified_text = " ".join(modified_words)
    return modified_text


# Example usage
original_text = "And how can I ask you to do that again with words I gave to you?"
typo_probability = 10  # Adjust this value based on the desired level of typos

modified_text = introduce_sophisticated_typos(original_text, typo_probability)
print("Original Text:", original_text)
print("Modified Text:", modified_text)
