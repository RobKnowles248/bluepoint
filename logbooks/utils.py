def get_grades_list():
    """
    Function to retrieve list of grades for get_sort_grade function
    """
    grades = []
    letters = ['a', 'b', 'c']
    for i in range(1, 10):
        if i < 6:
            grades.append(str(i))
            grades.append(str(i) + '+')
        else:
            for letter in letters:
                grades.append(str(i) + letter)
                grades.append(str(i) + letter + '+')
    return grades


def get_grades_tuple():
    """
    Function to retrieve tuple of grades formatted for model
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


def get_logbook_data(bluepoints):
    """
    Return a dictionary containing a sorted dictionary of bluepoints 
    by grade and the max number of bluepoints for any grade
    for use in the logbook template
    """
    sorted_bluepoints = {}
    bluepoints = bluepoints.order_by('sort_grade').reverse()
    max_number_of_grade = 0
    for bluepoint in bluepoints:
        grade = bluepoint.grade
        if grade in sorted_bluepoints.keys():
            sorted_bluepoints[grade]['bluepoints'].append(bluepoint)
            sorted_bluepoints[grade]['number'] += 1
            if sorted_bluepoints[grade]['number'] > max_number_of_grade:
                max_number_of_grade = sorted_bluepoints[grade]['number']
        else:
            sorted_bluepoints[grade] = {
                'bluepoints': [bluepoint],
                'number': 1
            }
            if max_number_of_grade == 0:
                max_number_of_grade = 1
    for data in sorted_bluepoints.values():
        data['percentage'] = (data['number'] * 100) // max_number_of_grade
    return {
        'sorted_bluepoints': sorted_bluepoints,
        'max_number_of_grade': max_number_of_grade
    }


def get_sort_grade(grade):
    """
    Get the number of the grade provided used for sorting
    """
    grades_list = get_grades_list()
    sort_grade = grades_list.index(str(grade)) + 1
    return sort_grade
