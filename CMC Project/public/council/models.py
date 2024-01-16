from django.db import models
from django.shortcuts import render
   
class state(models.Model):
    # nation=models.Model(on_delete=models.CASCADE,null=True)
    state_name=models.CharField(null=True,max_length=50)
    
    def __str__(self):
        return self.state_name
    
class district(models.Model):
    state=models.ForeignKey(state,on_delete=models.CASCADE,null=True)
    district_name=models.CharField(null=True,max_length=50)

    def __str__(self):
        return self.district_name
    
class taluk(models.Model):
    district=models.ForeignKey(district,on_delete=models.CASCADE,null=True)
    taluk_name=models.CharField(null=True,max_length=50)
    
    def __str__(self):
        return self.taluk_name
    
class City(models.Model):
    taluk=models.ForeignKey(taluk,on_delete=models.CASCADE,null=True)
    city_name=models.CharField(null=True,max_length=50)

    def __str__(self):
        return self.city_name
    
class ward_noo(models.Model):
    city=models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    ward_no=models.IntegerField(null=True)

    def __str__(self):
        return str(self.ward_no)
    
class colony(models.Model):
    ward_no = models.ForeignKey(ward_noo, on_delete=models.CASCADE,null=True)
    colony_name=models.CharField(null=True,max_length=50)

    def __str__(self):
        return self.colony_name
    
class number(models.Model):
    ward_no = models.ForeignKey(ward_noo, on_delete=models.CASCADE,null=True)
    phone_no=models.IntegerField(null=True)

    def __str__(self):
        return str(self.id)

class date(models.Model):
     phone_no=models.ForeignKey(number,on_delete=models.CASCADE,null=True)
     date=models.DateField(null=True)

     def __str__(self):
         return str(self.id)

    
# class water(models.Model):
#     colony=models.ForeignKey(colony,on_delete=models.CASCADE,null=True)
#     water_name=models.CharField(null=True,max_length=50)


#     def __str__(self):
#         return self.water_name
    
class Complaints(models.Model):
    state = models.ForeignKey(state, on_delete=models.CASCADE,null=True)
    dist = models.ForeignKey(district, on_delete=models.CASCADE,null=True)
    taluk = models.ForeignKey(taluk, on_delete=models.CASCADE,null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=True)
    ward_noo = models.ForeignKey(ward_noo, on_delete=models.CASCADE,null=True)
    colony = models.ForeignKey(colony, on_delete=models.CASCADE,null=True)
    phone=models.ForeignKey(number,on_delete=models.CASCADE,null=True)
    date=models.ForeignKey(date,on_delete=models.CASCADE,null=True)
    # water = models.ForeignKey(water, on_delete=models.CASCADE,null=True)
    water = models.CharField(null=True,max_length=100)
    garbage = models.CharField(null=True,max_length=100)
    electric = models.CharField(null=True,max_length=100)
    photo = models.ImageField(upload_to='complaint_photos/', null=True) 
    text_area = models.TextField(null=True) 
    location=models.CharField(null=True,max_length=100)


class members(models.Model):
    user_name=models.CharField(null=True,max_length=50)
    password=models.CharField(null=True,max_length=10)
    # is_preferred = models.BooleanField(default=True)
    

    def __str__(self):
        return self.user_name
    
    
class WardMember(models.Model):
    user = models.OneToOneField(members, on_delete=models.CASCADE)
    assigned_wards = models.ManyToManyField(ward_noo)

    def __str__(self):
        return self.user.user_name
    

 