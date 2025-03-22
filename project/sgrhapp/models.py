from django.db import models

""" # Create your models here.
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
        return self.name + ' by ' + self.user.username """
    
    # Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=512, blank=True, null=True)
    morada = models.CharField(max_length=512, blank=True, null=True)
    dt_criacao = models.DateTimeField(default=datetime.now())
    email = models.CharField(max_length=512, blank=True, null=True)
    telem = models.IntegerField(max_length=15, blank=True, null=True)
    telef = models.IntegerField(max_length=15, blank=True, null=True)
    class Meta:
        db_table = 'cliente'
