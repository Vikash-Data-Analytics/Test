from django.db import models
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class users(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length = 120)
    phone = models.IntegerField(max_length = 10)
    email = models.CharField(max_length = 25)
    department = models.CharField(max_length = 20)
    ctc = models.IntegerField(max_length = 10)
    def __str__(self):
        return self.name

    def register(self):
        self.save()


    @staticmethod
    def get_users_by_email(email):
        try:
            return users.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if users.objects.filter(email = self.email):
            return True

        return False
