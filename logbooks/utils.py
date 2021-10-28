def get_grades_dict():
    """
    Return a reverse orders dictionary of grades with empty lists attached
    """
    grades_dict = {}
    letters = ['c', 'b', 'a']
    for i in range(10, 0, -1):
        if i < 6:
            grades_dict[str(i) + '+'] = []
            grades_dict[str(i)] = []
        else:
            for letter in letters:
                grades_dict[str(i) + letter + '+'] = []
                grades_dict[str(i) + letter] = []
    return grades_dict


def get_grades_tuple():
    """
    Function to retrieve list of grades formatted for model
    """
    # Get a list of climbing grades
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
    # Convert list to tuple
    grades_tuple = tuple(grades)
    return grades_tuple


def sort_bluepoints(bluepoints):
    """
    Sorts a list of bluepoints to return a dictionary of bluepoints by grade
    in the correct order
    """
    # Add bluepoint objects to their corresponding grade in the dict
    grades_dict = get_grades_dict()
    for bluepoint in bluepoints:
        for key in grades_dict:
            if bluepoint.grade == key:
                bluepoint_object = {
                    'route_name': bluepoint.route_name,
                    'crag_name': bluepoint.crag_name,
                    'grade': bluepoint.grade,
                    'comment': bluepoint.comment,
                    'id': bluepoint.id,
                }
                grades_dict[key].append(bluepoint_object)
    # Remove entries for empty grades
    empty_grades = []
    for key in grades_dict:
        if len(grades_dict[key]) == 0:
            empty_grades.append(key)
    for grade in empty_grades:
        grades_dict.pop(grade)
    return grades_dict


def get_max_number_of_grade(sorted_bluepoints):
    """
    Get the max number of bluepoints at any grade for a user
    """
    max_number_of_grade = 0
    for bluepoints in sorted_bluepoints.values():
        if len(bluepoints) > max_number_of_grade:
            max_number_of_grade = len(bluepoints)
    return max_number_of_grade


def get_numbers_of_each_grade(sorted_bluepoints, max_number_of_grade):
    """
    Get a dictionary of the number of bluepoints at each grade
    plus the percentage of the that number compared to the max
    number at any grade
    """
    numbers_of_each_grade = {}
    for grade, bluepoints in sorted_bluepoints.items():
        number_of_bluepoints = len(bluepoints)
        percentage_of_max = (number_of_bluepoints * 100) // max_number_of_grade
        numbers_of_each_grade[grade] = {
            'number_of_bluepoints': number_of_bluepoints,
            'percentage_of_max': percentage_of_max,
        }
    return numbers_of_each_grade
