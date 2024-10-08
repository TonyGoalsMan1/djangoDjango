from django.db import models

#models.Model — это базовый класс для всех моделей в Django.
class Cat(models.Model):
    # CharField — это поле для строк(например, имя, порода, длина шерсти).
    name = models.CharField(max_length=100)
    #IntegerField — это поле для чисел (например, возраст).
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    fur_lenth = models.CharField(max_length=100)
    #__str__ метод — позволяет указать, как объект будет
    # представлен (например, в панели администратора или при выводе в консоли).
    def __str__(self):
        return self.name