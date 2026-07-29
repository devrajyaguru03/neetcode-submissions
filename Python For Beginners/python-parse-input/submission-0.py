from typing import List

def read_integers() -> List[int]:
    Int_input = input().split(",")
    return [int(x) for x in Int_input]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())