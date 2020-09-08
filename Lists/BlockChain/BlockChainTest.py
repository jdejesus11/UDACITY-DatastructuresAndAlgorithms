from BlockChain import BlockChain,Block

print("TEST #1: Inserting 5 elements into blockchain object.")

"""
TEST #1: Inserting 5 elements into blockchain object.
"""
chain = BlockChain()
chain.add("Juan Carlos")
chain.add("Sandra")
chain.add("Maria")
chain.add("Alexandra")
print(chain)

print("TEST #2: Inserting N elements into blockchain object.")
"""
TEST #2: Inserting N numbers into blockchain object.
"""
chain = BlockChain()
n = 10
for _ in range(n):
    chain.add(_)

print(chain)
print()

print("TEST #3: Inserting N null into blockchain object.")
"""
TEST #3: Inserting N None elements into blockchain object.
"""
chain = BlockChain()
n = 5
for _ in range(n):
    chain.add(None)
print(chain)
print()

print("TEST #4: Inserting ONE blockchain into another blockchain object.")
"""
TEST #4: Inserting N None elements into blockchain object.
"""
inner_chain = BlockChain()
inner_chain.add("Inner_1")
inner_chain.add("Inner_2")
inner_chain.add("Inner_3")

chain = BlockChain()
n = 1
for _ in range(n):
    chain.add(inner_chain)

counter = 1
pointer = chain.root
while (pointer):
      print(f"SUB BLOCKCHAIN NODES #{counter}")
      print(pointer.data)
      pointer = pointer.next
      counter+=1
print()