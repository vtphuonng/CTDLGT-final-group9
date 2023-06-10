from django.db import models

# Create your models here.
class books(models.Model):
    book_id = models.CharField(max_length=255,primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    borower_name = models.CharField(max_length=255)
    identity_id = models.IntegerField(default=0)
    borrow_day =  models.CharField(max_length=255)
    return_day =  models.CharField(max_length=255)
    days_late = models.IntegerField(default=0)
    fee_return_late = models.IntegerField(default=0)    

    def __str__(self) -> str:
        return(f'{self.book_id} {self.title} {self.author} {self.borower_name} {self.identity_id} {self.borrow_day} {self.return_day}\
               {self.days_late} {self.fee_return_late}')