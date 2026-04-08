from app.models.grade import Grade

def calculate_grade(score: int) -> Grade:
    if score >= 70:
        return Grade.A
    elif score >= 60:
        return Grade.B
    elif score >= 50:
        return Grade.C
    elif score >= 40:
        return Grade.D
    elif score >= 30:
        return Grade.E
    else:
        return Grade.F