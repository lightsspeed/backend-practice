def count_frequency(lst):
    frequency = {}
    print("\nDry Run of Count Frequency Algorithm:")
    print("-" * 50)
    print(f"Starting with empty frequency dictionary: {frequency}")
    
    # Iterate through each item in the list
    for index, item in enumerate(lst):
        print(f"\nStep {index+1}: Processing item '{item}'")
        
        # If item already in dictionary, increment its count
        if item in frequency:
            frequency[item] += 1
            print(f"  Found existing entry for '{item}', incrementing count to {frequency[item]}")
        # Otherwise, add it to dictionary with count 1
        else:
            frequency[item] = 1
            print(f"  First occurrence of '{item}', adding to dictionary with count 1")
            
        print(f"  Current frequency dictionary: {frequency}")
    
    print("\n" + "-" * 50)
    print("Final frequency count:")
    for item, count in frequency.items():
        print(f"{item}: {count}")
        
    return frequency

# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 2, 3, 1, 4]
    print(f"Input list: {my_list}")
    freq = count_frequency(my_list)
    
    print("\nSummary of frequencies:")
    for item, count in sorted(freq.items()):
        print(f"Item {item} appears {count} time(s)")