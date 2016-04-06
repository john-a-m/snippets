def answer(chunk, word):

    if len(word) == 1:
        return chunk.replace(word, '')

    acc = set()
    recurse(chunk, word, acc)

    return sorted(acc)[0]

def recurse(chunk, word, acc):

    if word not in chunk:
        acc.add(chunk)
        return

    chunks = []

    starts = range(len(chunk) - len(word) + 1)
    stops = range(len(word), len(chunk) + 1)

    for start, stop in zip(starts, stops):
        if chunk[start:stop] == word:
            chunks.append(chunk[:start] + chunk[stop:])

    for new_chunk in chunks:
        recurse(new_chunk, word, acc)

if __name__ == "__main__":

    print answer("lolol", "lol")
    print answer("lololololo", "lol")
    print answer("goodgooogoogfogoood", "o")
    print answer("goodgooogoogfogoood", "goo")
