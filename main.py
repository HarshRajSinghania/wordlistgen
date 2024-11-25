import itertools
import multiprocessing

def generate_wordlists(characters, word_length):
    wordlists = []
    for r in range(1, word_length + 1):
        permutations = itertools.permutations(characters, r)
        for permutation in permutations:
            word = ''.join(permutation)
            wordlists.append(word)
    return wordlists

def generate_wordlists_parallel(characters, word_length):
    pool = multiprocessing.Pool()
    results = pool.starmap(generate_wordlists, [(characters, word_length)])
    pool.close()
    pool.join()
    return results[0]

# Example usage
input_characters = input("Enter the characters: ")
input_length = int(input("Enter the word length: "))
result = generate_wordlists(input_characters, input_length)
print(result)
