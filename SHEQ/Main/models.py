from django.db import models


# category list
class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

# status details
class Access_status(models.Model):
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.status

# Main menu items
class MainMenu(models.Model):
    menu_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, blank = True)
    status = models.ForeignKey(Access_status, on_delete=models.CASCADE, )
    def __str__(self):
        return self.menu_name


