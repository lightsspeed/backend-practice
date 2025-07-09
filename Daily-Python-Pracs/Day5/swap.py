from typing import Tuple

def rotate_values(a: int , b: int, c: int) -> Tuple[int, int, int]:

    a,b,c = b,c,a
    return a,b,c


if __name__ == "__main__":

    
    a : int = 10
    b : int = 20
    c : int = 30
  
    print(rotate_values(a,b,c))

