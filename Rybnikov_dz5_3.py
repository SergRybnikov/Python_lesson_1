import random

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

def people():
    k = 0
    t = 0
    while k < len(klasses):
        if k >= len(tutors):
            yield (None, klasses[k])
            k += 1
            t += 1
            break
        else:
            yield (tutors[t], klasses[k])
            k += 1
            t += 1
for gen in people():
    print(gen)