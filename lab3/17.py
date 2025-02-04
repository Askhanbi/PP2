# Function 1     Task 6

def reversen(sentence):
    words = sentence.split(" ")
    string = []
    for word in words:
        string.insert(0, word)
    return string

Ssentence = str(input("You're sentence: "))

print(" ".join(reversen(Ssentence)))