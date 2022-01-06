from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return 'Category name : ' + self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    details = models.TextField()
    price = models.FloatField()
    updated_at = models.DateField()
    created_at = models.DateField()
    language = models.CharField(max_length=16)

    def __str__(self) -> str:
        return 'Course name : ' + self.name

class CourseImage(models.Model):
    image_path = models.FilePathField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return 'Course name : ' + self.course_id.name

class CourseVideo(models.Model):
    video_path = models.FilePathField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return 'Course name : ' + self.name

class Insturctor(models.Model):
    name = models.CharField(max_length=255)
    image = models.FilePathField()
    description = models.TextField()
    rate = models.FloatField()

    def __str__(self) -> str:
        return 'Insturctor name : ' + self.name

class CourseInstructor(models.Model):
    instructor_id = models.ForeignKey(Insturctor, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return 'Insturctor name : ' + self.name
