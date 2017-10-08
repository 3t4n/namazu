from django.db import models
from django.contrib.auth.models import User

class Building(models.Model):
    Name = models.CharField(max_length=255)
    GpsLatitude = models.CharField(max_length=255)
    GpsLongitude = models.CharField(max_length=255)

class Group_Nodes(models.Model):
    Name = models.CharField(max_length=255)
    Building = models.ForeignKey(Building, related_name="Nodes")
    def __str__(self):
        return self.Name

class Node(models.Model): #One node equivalente one rpi with n accelerometers
    UserId = models.ForeignKey(User) #Owner
    Shared = models.ManyToManyField(User,related_name="Shared_with") #Shared with ..
    Synced = models.BooleanField(default=False)
    Groups_a = models.ManyToManyField(Group_Nodes, related_name="Buildings")
    PingTime = models.IntegerField()
    def __str__(self):
        return self.Name

class Accelerometer(models.Model):
    MemoryAddress = models.CharField(max_length=255)
    Status = models.BooleanField() #False if because it is dead
    
class Acceleration_components(models.Model):
    AccelerometerId = models.ForeignKey(Accelerometer, related_name="data") #(x,y,z) vs time
    ServerTime = models.DateField(auto_now_add=True)
    Accelerometer_time = models.DateField()
    XValue = models.FloatField()
    YValue = models.FloatField()
    ZValue = models.FloatField()
    def __str__(self):
        return str(X_value)+"-"+str(Y_value)+"-"+str(Z_value) #Returning as X-Y-Z
