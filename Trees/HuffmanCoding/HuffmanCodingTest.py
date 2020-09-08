import HuffmanCoding

"""
TEST #1: GENERAL CASE
"""
print("-----------------------------------------------")
print("Test #1: GENERAL ENCODING - DECODING CASE")
message = "AAAAAAABBBCCCCCCCDDEEEEEE"
print(f"Original message: {message}")
huffman = HuffmanCoding.HuffmanCode(message)
binary_data = huffman.huffman_encoding()
print(f"Binary data: {binary_data}")
decoded_data = huffman.huffman_decoding(binary_data)
print(f"Decoded data: {decoded_data}")
print("-----------------------------------------------")


"""
TEST #2: EDGE CASE #1
"""
print("-----------------------------------------------")
print("Test #2: MESSAGE WITH ONE TYPE OF CHAR")
message = "ZZZZZZ"
print(f"Original message: {message}")
huffman = HuffmanCoding.HuffmanCode(message)
binary_data = huffman.huffman_encoding()
print(f"Binary data: {binary_data}")
decoded_data = huffman.huffman_decoding(binary_data)
print(f"Decoded data: {decoded_data}")
print("-----------------------------------------------")

"""
TEST #3: EDGE CASE #3
"""
print("-----------------------------------------------")
print("Test #3: EMPTY MESSAGE")
message = ""
print(f"Original message: {message}")
huffman = HuffmanCoding.HuffmanCode(message)
binary_data = huffman.huffman_encoding()
print(f"Binary data: {binary_data}")
decoded_data = huffman.huffman_decoding(binary_data)
print(f"Decoded data: {decoded_data}")
print("-----------------------------------------------")

"""
TEST #4: GENERAL CASE
"""
print("-----------------------------------------------")
print("Test #4: TWO TYPES OF CHARS")
message = "ZZAA"
print(f"Original message: {message}")
huffman = HuffmanCoding.HuffmanCode(message)
binary_data = huffman.huffman_encoding()
print(f"Binary data: {binary_data}")
decoded_data = huffman.huffman_decoding(binary_data)
print(f"Decoded data: {decoded_data}")
print("-----------------------------------------------")

"""
TEST #5: EDGE CASE #5
"""
print("-----------------------------------------------")
print("Test #5: SPECIAL CHARS")
message = "./,=-"
print(f"Original message: {message}")
huffman = HuffmanCoding.HuffmanCode(message)
binary_data = huffman.huffman_encoding()
print(f"Binary data: {binary_data}")
decoded_data = huffman.huffman_decoding(binary_data)
print(f"Decoded data: {decoded_data}")
print("-----------------------------------------------")





