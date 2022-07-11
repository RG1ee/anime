from django.db import models


class RangUser(models.IntegerChoices):
    STUDENT_OF_THЕ_ACADEMY = 1, "Student of the academy" 
    GENIN = 2, "Genin"
    CHUUNIN = 3, "Chuunin"
    SPECIAL_JOUNIN = 4, "Special Jounin"
    JOUNIN = 5, "JOUNIN"
    KAGE = 6, "Kage"
