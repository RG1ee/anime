from django.db import models


class TransferStatus(models.IntegerChoices):
    CONTINUES = 1, 'Continues'
    FROZEN = 2, 'Frozen'
    COMPLETED = 3, 'Completed'
    ABANDONED = 4, 'Abondoned'
