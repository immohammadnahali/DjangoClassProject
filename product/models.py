from django.db import models
from django.contrib.auth.models import AbstractUser
from slugify import slugify, SLUG_OK


class teach(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    fullname = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    educational_stage = models.CharField(max_length=100, null=True, blank=True)
    field_of_study = models.CharField(max_length=100, null=True, blank=True)
    university = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField()
    comment = models.TextField()

    CATEGORY_CHOICES = [
        ('chemistry', 'شیمی'),
        ('graphic', 'گرافیک'),
        ('sport', 'تربیت بدنی'),
        ('programming', 'برنامه نویسی'),
        ('programming', 'زبان انگلیسی'),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        self.slug = slugify(self.fullname)
        super().save(*args, **kwargs)


class product(models.Model):
    teach = models.ForeignKey(teach, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.ImageField()
    sessions = models.PositiveSmallIntegerField()
    description = models.TextField()
    LEVEL_CHOICES = (
        ('beginner', 'مبتدی'),
        ('intermediate', 'متوسط'),
        ('advanced', 'پیشرفته'),
    )
    STATUS_CHOICES = (
        ('ongoing', 'در حال برگزاری'),
        ('completed', 'تکمیل شده'),
        ('upcoming', 'در انتظار شروع'),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ongoing',
        verbose_name='وضعیت دوره'
    )
    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        null=True,
        blank=True,
        verbose_name='سطح دوره'
    )

    slug = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Futurecoursess(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    teacher = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class bestteachers(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class article(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class new_login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class test_teacher(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class students(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ManyToManyField(test_teacher)

    def __str__(self):
        return self.name


class test_info_teacher(models.Model):
    teacher = models.OneToOneField(test_teacher, on_delete=models.CASCADE)
    # teach=models.OneToOneField(teach, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return str(self.teacher)
