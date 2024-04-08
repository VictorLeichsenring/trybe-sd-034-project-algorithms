def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    quantidade_online = 0

    for horario in permanence_period:
        if not (isinstance(horario[0], int) and isinstance(horario[1], int)):
            return None

        if horario[0] <= target_time <= horario[1]:
            quantidade_online += 1

    return quantidade_online
