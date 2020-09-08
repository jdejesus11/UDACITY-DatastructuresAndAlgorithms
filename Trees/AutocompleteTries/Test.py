
from AutocompleteTries import Trie

my_trie = Trie()
word_list = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in word_list:
    my_trie.insert(word)

def print_test(test_name,my_trie,word):
    print()
    print("---------------------------")
    print(test_name)
    suffixes_1 = my_trie.find(word)
    if (suffixes_1 is not None and len(suffixes_1) > 0):
        print(f"The word {word} has the following matches: ")
        print(suffixes_1)
    else:
        print(f"The word does not contain matches. ")
    print("---------------------------")



print_test("Test #0: Word with size = 0",my_trie,"")

print_test("Test #1: Word with size = 1",my_trie,"f")

print_test("Test #2: a whole word",my_trie,"trigonometry")

print_test("Test #3: Word with size = 1",my_trie,"t")

print_test("Test #4: Word does not exist",my_trie,"hello world")

