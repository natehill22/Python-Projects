from django.db import models

#Creates a class that inherits from models.Model, which allows it to be used as a representation of a database table
class UniversityClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(null=True, blank=True, default=None)

    #Creates a model manager
    objects = models.Manager()

    #Dispalys the object output values in the form of a string
    def __str__(self):
        #Returns input value of title and instructor name as a tuple to display in browser instead of default titles
        display_course = '{0.title}: {0.instructor_name}'
        return display_course.format(self)

    #Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Classes"