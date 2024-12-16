def get_grade(score):
    """Determine grade based on the score."""
    grade_thresholds = [
        (0.9, "A"),
        (0.8, "B"),
        (0.7, "C"),
        (0.6, "D"),
        (0.0, "F"),
    ]
    
    for threshold, grade in grade_thresholds:
        if score >= threshold:
            return grade
    return "Invalid"

def main():
    """Main program to handle input and output."""
    try:
        score = float(input("Enter Score between 0.0 and 1.0: "))
        if not 0.0 <= score <= 1.0:
            print("Number Entered Out of Range")
            return
        
        grade = get_grade(score)
        print(f"Grade: {grade}")
    except ValueError: 
        print("Entry not a numerical value")

print(get_grade.__doc__) #prints docstring inside the "get_grade" function
print(main.__doc__) #prints docstring inside the "main" function

if __name__ == "__main__": #checks if the code is not used as a module elswhere if true runs main()
    main()
