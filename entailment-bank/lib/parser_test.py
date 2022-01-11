from parser import *

if __name__ == "__main__":
    print(parse_lisp("((((((((((sent1 sent4 sent8) -> int1) sent6) -> int2) sent5) -> int3) ((((((sent1 sent4 sent8) -> int1) sent6) -> int2) sent3 sent7) -> int4)) -> int5) sent2) -> int6)"))