from django.db import models

# Create your models here.

STATUS1 = (
    ('BURGER','BURGER'),
    ('LAVASH','LAVASH'),
    ('HAT DOG','HOT DOG'),
    ('PIZZA','PIZZA'),
    ('CHEESE BURGER','CHEESE BURGER'),
    
)


STATUS3 = (
    ('Andijon shahar','Andijon shahar'),
    ('bogishamol','bogishamol'),
    ('yangi bozor','yangi bozor'),
    ('eski shahar','eski shahar'),
    ('bobur shoh kocha','bobur shox kocha'),
)

STATUS = (
    ('Yetqazib berilgan','Yetqazib berilgan'),
    ('Tayyorlanmoqda!','Tayyorlanmoqda!'),
)

class Dastavka(models.Model):
    """
    Dastavka uchun models
    
    """

    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255,choices=STATUS1)
    count = models.PositiveBigIntegerField(default=1, null=True,blank=True)
    price = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    all_price = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    location = models.CharField(max_length=255,choices=STATUS3)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255,choices=STATUS,default='Tayyorlanmoqda!')






    class Meta:
        ordering = ['id']
        verbose_name = 'Dastavka'
        verbose_name_plural = 'Dastavka'




    def __str__(self):
        return f'{self.full_name} {self.title} '


    def producd_price(self):
        return self.price * self.count