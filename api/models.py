from django.db import models
from django.contrib.auth.models import User

class Building(models.Model):
    Name = models.CharField(max_length=255)
    GpsLatitude = models.CharField(max_length=255)
    GpsLongitude = models.CharField(max_length=255)
    def __str__(self):
        return self.Name

class GroupNodes(models.Model):
    Name = models.CharField(max_length=255)
    Building = models.ForeignKey(Building, related_name="GroupsNodes")
    def __str__(self):
        return self.Name

class Node(models.Model): #One node equivalente one rpi with n accelerometers
    Name = models.CharField(max_length=255)
    UserId = models.ForeignKey(User) #Owner
    Shared = models.ManyToManyField(User,related_name="SharedWith",blank=True) #Shared with ..
    Synced = models.BooleanField(default=False)
    GroupsNode = models.ManyToManyField(GroupNodes, related_name="Nodes")
    PingTime = models.IntegerField()
    def __str__(self):
        return self.Name

class Accelerometer(models.Model):
    NodeId = models.ForeignKey(Node, related_name="Accelerometers")
    MemoryAddress = models.CharField(max_length=255)
    Status = models.BooleanField() #False if because it is dead
    
class AccelerationComponent(models.Model):
    AccelerometerId = models.ForeignKey(Accelerometer, related_name="Data") #(x,y,z) vs time
    ServerTime = models.DateField(auto_now_add=True)
    AccelerometerTime = models.DateField()
    XValue = models.FloatField()
    YValue = models.FloatField()
    ZValue = models.FloatField()
    def __str__(self):
        return str(self.XValue)+"|"+str(self.YValue)+"|"+str(self.ZValue) #Returning as X-Y-Z
