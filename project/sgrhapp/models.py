from django.db import models

# Create your models here.
class Study(models.Model):
    class Type(models.TextChoices):
        EXTRACT = "extraction", "extraction"
        SELRED = "selection/reduction", "selectionreduction"
        CLASSIF = "classification", "classification"
    idstudy = models.AutoField(primary_key=True)
    datestudy = models.DateTimeField(default=datetime.now())
    name = models.CharField(max_length=512, blank=True, null=True)
    completed = models.BooleanField(blank=True, null=True)
    directory = models.CharField(max_length=512, blank=True, null=True)
    type = models.CharField(max_length=512, blank=True,
                            null=True, choices=Type.choices, default=Type.EXTRACT)
    patient = models.ForeignKey(
        Patient, models.CASCADE, db_column='patient_idpat')
    user = models.ForeignKey(
        User, models.CASCADE, db_column='user_iduser', null=True, blank=True)

    class Meta:
        db_table = 'study'

    def __str__(self):
        return self.name + ' by ' + self.user.username