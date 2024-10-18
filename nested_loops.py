# Authors   : Victor DeSouza
# Emails    : victordesouz@umass.edu
# Spire IDs : 34569497
def get_names(first_names, last_names):
    full_names = [] 
    for i in first_names:
        for j in last_names:
            full_name = (i + ' ' + j)
            full_names.append(full_name)
    return full_names

# first_names = ['Ari', 'Taylor']
# last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

# print(get_names(first_names, last_names))

def average_scores(scores):
    average_grades = []
    for student in scores:
        total_score = 0
        for grade, late in student:
            if late == 0:
                penalty = 1
            elif late == 1:
                penalty = .9
            elif late == 2:
                penalty = .75
            elif late == 3:
                penalty = .5
            else:
                penalty = 0

            penalized_grade = grade * penalty
            total_score += penalized_grade
        
        average = total_score / len(student)
        average_grades.append(average)

    return average_grades

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

print(average_scores(scores))