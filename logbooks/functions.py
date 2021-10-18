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


def sort_bluepoints(bluepoints):
    """
    Sorts a list of bluepoints to return a dictionary of bluepoints by grade
    in the correct order
    """
    grades_dict = get_grades_dict()
    for bluepoint in bluepoints:
        for key in grades_dict:
            if bluepoint.grade == key:
                bluepoint_object = {
                    'route_name': bluepoint.route_name,
                    'crag_name': bluepoint.crag_name,
                    'grade': bluepoint.grade,
                    'comment': bluepoint.comment,
                }
                grades_dict[key].append(bluepoint_object)
    empty_grades = []
    for key in grades_dict:
        if len(grades_dict[key]) == 0:
            empty_grades.append(key)
    for grade in empty_grades:
        grades_dict.pop(grade)
    return grades_dict
