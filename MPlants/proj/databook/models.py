from django.db import models

# Create your models here.
class Date(models.Model):
    #pk/id
    day=models.CharField("Today's date",max_length=50)

    def __str__(self):
        return self.day

    def all_numbers_to_string(self):
        return ", ".join([data.data for data in self.numbers.all()])

class Info(models.Model):
    data=models.CharField('Info data', max_length=50)
    time=models.ForeignKey(Date,on_delete=models.CASCADE,
                           related_name="numbers")
    def __str__(self):
        return self.data
