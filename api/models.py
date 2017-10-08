from django.db import models
from django.contrib.auth.models import User


class Building(models.Model):
    Name = models.CharField(max_length=255)
    Gpslatitude = models.CharField(max_length=255)
    Gpslongitude = models.CharField(max_length=255)

class Group_Nodes(models.Model):
    Name = models.CharField(max_length=255)
    Building = models.ForeignKey(Building)
    def __str__(self):
        return self.Name

class Node(models.Model): #One node equivalente one rpi with n accelerometers
    User_id = models.ForeignKey(User) #Owner
    Shared = models.ManyToManyField(User,related_name="Shared_with") #Shared with ..
    Synced = models.BooleanField(default=False)
    Groups_a = models.ManyToManyField(Group_Nodes, related_name="Buildings")
    Ping_time = models.IntegerField()
    def __str__(self):
        return self.Name

class Accelerometer(models.Model):
    Memory_Address = models.CharField(max_length=255)
    Status = models.BooleanField() #False if because it is dead
    
class Acceleration_components(models.Model):
    Accelerometer_id = models.ForeignKey(Accelerometer, related_name="data") #(x,y,z) vs time
    Server_time = models.DateField(auto_now_add=True)
    Accelerometer_time = models.DateField()
    X_value = models.FloatField()
    Y_value = models.FloatField()
    Z_value = models.FloatField()
    def __str__(self):
        return str(X_value)+"-"+str(Y_value)+"-"+str(Z_value) #Returning as X-Y-Z
