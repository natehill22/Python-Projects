from django.db import models

PREFIX_CHOICES = {
    ('Mrs.','Mrs.',),
    ('Ms.','Ms.',),
    ('Mr.','Mr.',),
    ('Sir','Sir',),
    ('Lady','Lady',),
    ('Dr.','Dr.',),
    ('Mx.','Mx.',),
    ('Ind.','Ind.',),
    ('Pr.','Pr.',),
}


class Profile(models.Model):
    title = models.CharField(max_length=60, choices=PREFIX_CHOICES, blank=True, null=False)
    firstname = models.CharField(max_length=60, default="", blank=True, null=False)
    lastname = models.CharField(max_length=60, default="", blank=True, null=False)
    email = models.CharField(max_length=60, default="", blank=True, null=False)
    username = models.CharField(max_length=60, default="", blank=True, null=False)


    objects = models.Manager()
    def __str__(self):
        return self.firstname + " " + self.lastname


