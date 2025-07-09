def all_equal(lst: list) -> bool:

    return len(set(lst)) <= 1

if __name__ == "__main__":

    print(all_equal([1,11,1])) 
    print(all_equal([1,1,1])) 
    print(all_equal([.1,.1,.1])) 