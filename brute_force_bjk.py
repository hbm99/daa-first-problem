from typing import List

list_variations: List[str] = []

def brute_force(a : str, b: str) -> str:
   generate_VWR('()', 2 * max(len(a), len(b)))
   for variation in list_variations:
      if contains(variation, a, b):
         return variation

def contains(chain: str, a: str, b: str) -> bool:
   current_a, current_b = 0, 0
   for item in chain:
      if current_a < len(a) and a[current_a] == item:
         current_a += 1
      if current_b < len(b) and b[current_b] == item:
         current_b += 1
   return current_a == len(a) and current_b == len(b)

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

def containsNone(chain: str) -> bool:
   for item in chain:
      if item == None:
         return True
   return False

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
