def find_max_value_key(d):

    return max(d.items(), key=lambda x:x[1]) if d else None

if __name__ == "__main__":

    d = {'apple': 3, 'banana': 2, 'orange': 1}

    print(find_max_value_key(d))