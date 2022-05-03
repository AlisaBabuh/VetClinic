from statistics import mode
from django.db.models import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """
    phone_number = models.CharField(max_length=15, null=True)
    photo = models.ImageField()

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

#Таблица ГРУППА УСЛУГ
class GroupService(models.Model):

    name = models.CharField(max_length=70)
    #Связь с таблицей СПЕЦИАЛЬНОСТЬ 
    #speciality = models.ForeignKey(Speciality, on_delete=CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "type_service"

 #Таблица СПЕЦИАЛЬНОСТЬ
class Speciality(models.Model):

    #Связь с таблицей Ветеринарный врач
    name = models.CharField(max_length=70)
    group_service = models.ManyToManyField(GroupService)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "speciality"

#Таблица УСЛУГА
class Service(models.Model):

    #Связь с таблицей ГРУППА УСЛУГ
    group = models.ForeignKey(GroupService, on_delete=CASCADE)
    name = models.CharField(max_length=70)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "service"


#Таблица ВИД ЖИВОТНОГО
class PetType(models.Model):

    #Связать с таблицей Животное (связь 1 к 1)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

    class Meta:
        db_table = "pet_type"

#Таблица ЖИВОТНОЕ
class Pet(models.Model):

    code_klient = models.ForeignKey(User, on_delete=models.CASCADE)
    #Кличка
    name = models.CharField(max_length=30)

    #Связь с таблицей Вид животного
    type = models.ForeignKey(PetType, on_delete=models.CASCADE)

    #Возраст
    age = models.DateField()
    #Пол животного. Сделать выпадающее окошко для выбора?
    sex = models.CharField(max_length=1)
    #Перенесенные операции
    operations = models.TextField()
    #Противопоказания
    contraindications = models.TextField()
    #Код медицинской карты (связь 1 к 1 по коду медицинской карты)
    #medicalcard = models.ForeignKey(MedicalCard, on_delete=CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "pet"

#Таблица МЕДИЦИНСКАЯ КАРТА
class MedicalCard(models.Model):

    #Связать с таблицей Животное (связь 1 к 1 по коду медицинской карты) - Сделала в Животном
    #models.ForeignKey(Musician, on_delete=models.CASCADE)

    #Связать с таблицей Запись медицинской карты (1 ко многим) - Cделала в Запись медицинской карты
    #medical_record = models.CharField(max_length=20)
    pet = models.OneToOneField(Pet, on_delete=CASCADE, primary_key=True)

    def __str__(self):
        return self.pet.name

    class Meta:
        db_table = "medical_card"

#Таблица ЗАПИСЬ МЕДИЦИНСКОЙ КАРТЫ
class MedicalRecord(models.Model):

    #Связать с таблицей Медицинская карта (связь 1 ко многим по коду записи медицинской карты)
    code_medicalcard = models.ForeignKey(MedicalCard, on_delete=CASCADE)
    #Симптомы
    symptoms = models.CharField(max_length=20)
    #Диагноз
    diagnosis = models.CharField(max_length=20)
    #Схема лечения
    treatment_regimen = models.CharField(max_length=20)
    #Рекомендации
    recomendations = models.CharField(max_length=20)
    #Код типа услуги ????
    code_typeservice = models.ForeignKey(Service, on_delete=CASCADE)

    def __str__(self):
       return self.symptoms

    class Meta:
        db_table = "medical_record"

#Таблица РАСПИСАНИЕ
class Timetable(models.Model):

    #Связь с таблицей Ветеринарный врач
    cabinet_number = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return str(self.date) + ' ' + str(self.time)

    class Meta:
        db_table = "timetable"

#Таблица ВЕТЕРИНАРНЫЙ ВРАЧ
class VetProfile(models.Model):

    user = models.OneToOneField(User, on_delete=CASCADE, primary_key=True)

    date_of_birth = models.DateField()
    date_employment = models.DateField()
    residence_address = models.CharField(max_length=30)
    passport = models.CharField(max_length=30)
    #Связь с таблицей Специальность
    speciality = models.ForeignKey(Speciality, on_delete=CASCADE)
    #Личная информация
    personal_information = models.TextField()

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    class Meta:
        db_table = "vet_profile"

#Таблица ЗАПИСЬ НА ПРИЕМ
class Record(models.Model):

    #Связь с таблицей Клиент
    code_klient = models.ForeignKey(User, on_delete=CASCADE, related_name='Клиент')
    #Связь с таблицей Врач
    code_vet = models.ForeignKey(User, on_delete=CASCADE, related_name='Врач')
    #Связь с таблицей услуг
    code_typeservice = models.ForeignKey(Service, on_delete=CASCADE)
    #Код расписания
    code_timetable = models.ForeignKey(Timetable, on_delete=CASCADE)
    #Связь с таблицей медицинской карты
    code_medicalcard = models.ForeignKey(MedicalCard, on_delete=CASCADE)

    def __str__(self):
        return self.code_klient.first_name + self.code_klient.last_name

    class Meta:
        db_table = "record"