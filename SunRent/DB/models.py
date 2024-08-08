from django.db import models
from django.contrib.gis.db import models as gis_models


class Polygon(gis_models.Model):
  name = models.CharField(max_length=100)
  area = gis_models.PolygonField()

  class Meta:
    verbose_name = "Полигон"
    verbose_name_plural = "Полигоны" 

  def __str__(self):
    return self.name
  
class Loscation(gis_models.Model):
  name = models.CharField(max_length=100, blank=True, null=True)
  area = gis_models.PolygonField()

  class Meta:
    verbose_name = "Локация"
    verbose_name_plural = "Локации" 

  def __str__(self):
    return self.name
    
class Scooter(gis_models.Model):
  identifier = models.CharField(max_length=100)
  location = gis_models.PointField()
  battery_percentage = models.FloatField()
  polygon = models.ForeignKey(Polygon, null=True, on_delete=models.CASCADE)

  class Meta:
    verbose_name = "Самокат"
    verbose_name_plural = "Самокаты" 

  def __str__(self):
   return self.identifier

class Department(models.Model):
  name = models.CharField(max_length=100, verbose_name='Название отдела')

  class Meta:
    verbose_name = "Отдел"
    verbose_name_plural = "Отделы" 

  def __str__(self):
    return self.name

class Position(models.Model):
  name = models.CharField(max_length=100, verbose_name='Название должности')  # Добавьте значение по умолчанию
  department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='positions', verbose_name='Отдел')

  class Meta:
    verbose_name = "Должность"
    verbose_name_plural = "Должности" 

  def __str__(self):
    return self.name
  


class User(models.Model):
  first_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Имя")
  last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Фамилия")

  position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='users_position', verbose_name='Должность')
  email = models.EmailField(unique=True, verbose_name="Email", null=True, blank=True)
  contacts = models.BigIntegerField(blank=True, null=True, verbose_name="Контакты")

  COUNTRY_CHOICES = [
    ('KG', 'Бишкек'),
    ('KG', 'Ош'),
    ('KG', 'Джалал-Абад'),
  ]
  country = models.CharField(max_length=100, choices=COUNTRY_CHOICES, verbose_name="Регион")
  
  poligon = models.ForeignKey(Polygon, on_delete=models.CASCADE, blank=True, null=True)

  class Meta:
    verbose_name = "Сотрудники"
    verbose_name_plural = "Сотрудники" 

  def __str__(self):
    return f"{self.first_name} {self.last_name} {self.position}"

class Mission(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mission_for_user', verbose_name='Миссия для user')
  scooter = models.ForeignKey(Scooter, on_delete=models.CASCADE, related_name='scooter', verbose_name='Самокат')
  prioriti = models.BigIntegerField(blank=True, null=True, verbose_name="Приоритет", editable=False)
  
  class Meta:
    verbose_name = "Миссия"
    verbose_name_plural = "Миссии" 
  def save(self, *args, **kwargs):
    if self.scooter.battery_percentage < 5:
      self.prioriti = 1  # Можете назначить любое значение для процента ниже 5%
    elif 5 <= self.scooter.battery_percentage < 20:
      self.prioriti = 2
    elif 20 <= self.scooter.battery_percentage < 30:
      self.prioriti = 3
    elif 30 <= self.scooter.battery_percentage < 40:
      self.prioriti = 4
    elif 40 <= self.scooter.battery_percentage < 50:
      self.prioriti = 5
    elif 50 <= self.scooter.battery_percentage < 70:
      self.prioriti = 6
    elif 70 <= self.scooter.battery_percentage <= 100:
      self.prioriti = 7
    else:
      self.prioriti = None  # Если процент заряда находится вне ожидаемых диапазонов
    super().save(*args, **kwargs)
