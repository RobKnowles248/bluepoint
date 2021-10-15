def get_grades_tuple():
    """
    Function to retrieve list of grades formatted for model
    """
    # Get an array of climbing grades
    grades = []
    letters = ['a', 'b', 'c']
    for i in range(1, 10):
        if i < 6:
            grades.append((str(i), str(i)))
            grades.append((str(i) + '+', str(i) + '+'))
        else:
            for letter in letters:
                grades.append((str(i) + letter, str(i) + letter))
                grades.append((str(i) + letter + '+', str(i) + letter + '+'))
    grades_tuple = tuple(grades)
    return grades_tuple
