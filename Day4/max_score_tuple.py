from typing import List, Tuple

def highest_score_student(students: List[Tuple[str, any]]) -> List[Tuple[str, float]]:
    if not students:
        return []
    
    valid_students = []
    # Validate and collect valid scores
    for name, score in students:
        try:
            score = float(score)  # Convert to float to handle int or float
            valid_students.append((name, score))
        except (ValueError, TypeError):
            continue  # Skip invalid scores
    
    if not valid_students:
        return []
    
    # Find the maximum score
    max_score = max(score for _, score in valid_students)
    # Collect all students with the maximum score
    return [(name, score) for name, score in valid_students if score == max_score]

# Test cases
if __name__ == "__main__":
    students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
    print(highest_score_student(students))  # Output: [('Bob', 92.0)]
    print(highest_score_student([("Alice", 90), ("Bob", 90)]))  # Output: [('Alice', 90.0), ('Bob', 90.0)]
    print(highest_score_student([("Alice", "invalid"), ("Bob", 85)]))  # Output: [('Bob', 85.0)]
    print(highest_score_student([]))  # Output: []
    print(highest_score_student([("Alice", "invalid")]))  # Output: []