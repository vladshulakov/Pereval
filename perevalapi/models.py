from django.db import models
from django.utils import timezone

def get_image_path(instance, file):
    return f'photos/pereval-{PerevalAdded.objects.last().id}/{file}'

ACTIVITIES = [
    ('foot', 'пеший'),
    ('bike', 'велосипед'),
    ('car', 'автомобиль'),
    ('motorbike', 'мотоцикл'),
]


BEAUTYTITLE = [
    ('poss', 'перевал'),
    ('mountain_peak', 'горная вершина'),
    ('gorge', 'ущелье'),
    ('plateau', 'плато'),
]


STATUS = [
    ('new', 'новый'),
    ('pending', 'на модерации'),
    ('accepted', 'принят'),
    ('rejected', 'не принят'),
]


LEVELS = [
    ('', 'не указано'),
    ('1A', '1a'),
    ('1B', '1б'),
    ('2А', '2а'),
    ('2В', '2б'),
    ('3А', '3а'),
    ('3В', '3б'),
    ]


class Users(models.Model):
    mail = models.EmailField('почта', unique=False)
    phone = models.CharField('телефон', max_length=15)
    name = models.CharField('имя', max_length=30)
    surname = models.CharField('фамилия', max_length=30)
    otch = models.CharField('отчество', max_length=30)

    def __str__(self):
        return f'{self.surname}'


class Coords(models.Model):
    latitude = models.FloatField('широта', max_length=9, blank=True)
    longitude = models.FloatField('долгота', max_length=9, blank=True)
    height = models.IntegerField('высота', blank=True)


class Levels(models.Model):
    winter = models.CharField('зима', max_length=2, choices=LEVELS, default='')
    summer = models.CharField('лето', max_length=2, choices=LEVELS, default='')
    autumn = models.CharField('осень', max_length=2, choices=LEVELS, default='')
    spring = models.CharField('весна', max_length=2, choices=LEVELS, default='')

    def __str__(self):
        return f'зима: {self.winter}, лето: {self.summer}, осень: {self.autumn}, весна: {self.spring}'




class PerevalAdded(models.Model):
    status = models.CharField(choices=STATUS, max_length=25, default='new')
    beautyTitle = models.CharField('тип', choices=BEAUTYTITLE, max_length=50)
    title = models.CharField('название', max_length=50, blank=True)
    other_titles = models.CharField('иные названия', max_length=50)
    connect = models.CharField('соединение', max_length=250)
    add_time = models.DateTimeField(default=timezone.now, editable=False)
    coord_id = models.OneToOneField(Coords, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    levels = models.OneToOneField(Levels, on_delete=models.CASCADE)


class Images(models.Model):
    name = models.CharField(max_length=50)
    photos = models.ImageField('Фото', upload_to=get_image_path, blank=True, null=True)
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE, related_name='images', default=0)