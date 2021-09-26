''' grades = [[70,75,80],[70,80,90,100],[80,100]]

english = grades[0]
''' ''' print(english) ''' '''
total = 0
for mark in english:
    total = total + mark
    answer = total / len(english)
print(answer)'''

def average(grades):
    average = []
    for grades_list in grades:
        total = 0
        for mark in grades_list:
            total = total + mark

        average.append(total / len(grades_list))
    print(average) 
grades = [[70,75,80],[70,80,90,100],[80,100]]
average(grades)