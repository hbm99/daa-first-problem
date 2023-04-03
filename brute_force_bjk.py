from typing import List, Tuple

list_variations: List[str] = []

# Brute force solution
def brute_force(a : str, b: str) -> Tuple[str, List[int]]:
   generate_VWR('()', 2 * (len(a) + len(b)))
   for variation in list_variations:
      tuple = contains(variation, a, b)
      if tuple[0]:
         return variation, tuple[1]

def contains(chain: str, a: str, b: str) -> Tuple[bool, List[int]]:
   # pretty printing
   colors_chain = [0] * len(chain)
   
   current_a, current_b = 0, 0
   for i in range(len(chain)):
      if current_a < len(a) and a[current_a] == chain[i]:
         current_a += 1
         colors_chain[i] = 1
      if current_b < len(b) and b[current_b] == chain[i]:
         current_b += 1
         if colors_chain[i] == 1:
            colors_chain[i] = 3
         else:
            colors_chain[i] = 2
   return current_a == len(a) and current_b == len(b), colors_chain

def is_balanced(chain: str) -> bool:
   balance = 0
   for item in chain:
      if item == '(':
         balance += 1
      else:
         balance -= 1
      if balance < 0:
         return False
   return balance == 0

def generate_VWR(alphabet : str, size: int) -> None:
   for i in range(1, size + 1):
      generator_VWR(alphabet, [None] * i, 0)

def generator_VWR(alphabet: str, variations : List[str], pos : int) -> None:
   if pos == len(variations):
      variation = ''
      for i in range(len(variations)):
         variation += variations[i]
      if is_balanced(variation):
         list_variations.append(variation)
   else:
      for i in range(len(alphabet)):
         variations[pos] = alphabet[i]   
         generator_VWR(alphabet, variations, pos + 1)
