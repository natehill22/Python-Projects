from django.db import models

#Creates a class that inherits from models.Model, which allows it to be used as a representation of a database table
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_ID = models.IntegerField(default="", blank=True, null=False)

    #Creates a model manager
    objects = models.Manager()

    #Dispalys the object output values in the form of a string
    def __str__(self):
        #Returns input value of campus name and state abbreviation as a tuple to display in browser instead of default titles
        display_course = '{0.campus_name}: {0.state}'
        return display_course.format(self)

    #Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"