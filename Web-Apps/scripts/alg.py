def algorithm(results):
    genres = {'rock':0, 'hip hop':0, 'classical':0, 'pop':0, 'country':0, 'r&b':0, 'metal':0, 'alternative':0, 'edm':0}

    q1 = results[0]
    if q1 == 'home':
        genres['classical'] += 1
        genres['alternative'] += 1
        genres['edm'] += 2
        genres['pop'] += 1
    elif q1 == 'outdoors':
        genres['country'] += 2
        genres['alternative'] += 1
    elif q1 == 'gym':
        genres['hip hop'] += 2
        genres['rock'] += 2
        genres['pop'] += 1
        genres['metal'] += 1
    elif q1 == 'date':
        genres['r&b'] += 1
        genres['pop'] += 1
    elif q1 == 'golf':
        genres['classical'] += 3

    q2 = results[1]
    if q2 == 'game':
        genres['hip hop'] += 1
        genres['edm'] += 1
    elif q2 == 'walk':
        for key in genres:
            genres[key] += 1
    elif q2 == 'run':
        for key in genres:
            genres[key] += 2
    elif q2 == 'wo':
        genres['hip hop'] += 3
        genres['rock'] += 2
        genres['metal'] += 2
    elif q2 == 'fish':
        genres['country'] += 3
    elif q2 == 'drive':
        genres['r&b'] += 1
        genres['pop'] += 1
        genres['alternative'] += 1
    elif q2 == 'mood':
        genres['r&b'] += 3
    elif q2 == 'sport':
        genres['metal'] += 2
        genres['hip hop'] += 2
        genres['pop'] += 1
    elif q2 == 'relax':
        genres['classical'] += 2
        genres['pop'] += 1
    elif q2 == 'dance':
        genres['edm'] += 3

    q3 = results[2]
    if q3 == 'aqua':
        genres['alternative'] += 3
    elif q3 == 'pisc':
        pass
    elif q3 == 'arie':
        genres['rock'] += 3
    elif q3 == 'taur':
        genres['classical'] += 3
    elif q3 == 'gemi':
        genres['edm'] += 3
    elif q3 == 'canc':
        genres['r&b'] += 3
    elif q3 == 'leo':
        genres['pop'] += 3
    elif q3 == 'virg':
        genres['classical'] += 3
    elif q3 == 'libr':
        genres['country'] += 3
    elif q3 == 'scor':
        genres['hip hop'] += 3
    elif q3 == 'sagi':
        genres['alternative'] += 3
    elif q3 == 'capr':
        genres['metal'] += 3

    q4 = results[3]
    if q4 == 'happy':
        genres['pop'] += 1
        genres['alternative'] += 1
    elif q4 == 'sad':
        genres['r&b'] += 1
    elif q4 == 'angry':
        genres['hip hop'] += 1
        genres['metal'] += 2
    elif q4 == 'content':
        genres['pop'] += 2
    elif q4 == 'roman':
        genres['r&b'] += 1
        genres['country'] += 1
        genres['rock'] += 1
        genres['alternative'] += 1
    elif q4 == 'broken':
        genres['r&b'] += 2
        genres['country'] += 2
        genres['rock'] += 1
    elif q4 == 'hype':
        genres['edm'] += 2
        genres['hip hop'] += 1
        genres['rock'] += 1

    q5 = results[4]
    if q5 == '12':
        genres['classical'] += 1
    elif q5 == '17':
        genres['hip hop'] += 1
    elif q5 == '24':
        genres['country'] += 1
        genres['hip hop'] += 2
    elif q5 == '40':
        genres['metal'] += 2
        genres['rock'] += 2
        genres['hip hop'] -= 2
    elif q5 == '60':
        genres['alternative'] += 1
        genres['classical'] += 1
        genres['hip hop'] -= 3
    elif q5 == 'old':
        genres['classical'] += 4
        genres['hip hop'] -= 4


    maxValue = max(genres.values())
    answer = [k for k, v in genres.items() if v == maxValue]

    if len(answer) > 1:
        return answer[0]

    return answer
