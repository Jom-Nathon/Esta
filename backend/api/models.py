from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nodes')

    def __str__(self):
        return self.title 
    

class PlotCase(models.Model):
    case_number = models.CharField(max_length=100, primary_key=True)
    case_province = models.CharField(max_length=100)
    case_district = models.CharField(max_length=100)
    case_sub_district = models.CharField(max_length=100)

class Plot(models.Model):
    plot_id = models.UUIDField(primary_key=True)
    plot_case = models.ForeignKey(PlotCase, on_delete = models.CASCADE)
    plot_lot_number = models.CharField(max_length=100)
    plot_sale_order = models.CharField(max_length=100)
    plot_type = models.CharField(max_length=100)
    plot_size = models.FloatField()
    plot_upload_date = models.CharField(max_length=100)

class PlotPicture(models.Model):
    picture_id = models.UUIDField(primary_key=True)
    picture_plot = models.ForeignKey(Plot, on_delete = models.CASCADE)
    picture_link = models.CharField(max_length=100)

class PlotMap(models.Model):
    map_id = models.UUIDField(primary_key=True)
    map_plot = models.ForeignKey(Plot, on_delete = models.CASCADE)
    map_link = models.CharField(max_length=255)

class PlotSale(models.Model):
    sale_id = models.UUIDField(primary_key=True)
    sale_plot = models.ForeignKey(Plot, on_delete = models.CASCADE)
    sale_date = models.CharField(max_length=100)
    sale_status = models.CharField(max_length=100)

class PlotPrice(models.Model):
    price_plot = models.OneToOneField(Plot, on_delete = models.CASCADE, primary_key=True)
    price_professional = models.FloatField(default=None, blank=True, null=True)
    price_enforcer = models.FloatField(default=None, blank=True, null=True)
    price_legalgov = models.FloatField(default=None, blank=True, null=True)
    price_committee = models.FloatField(default=None, blank=True, null=True)
    price_predictive = models.FloatField(default=None, blank=True, null=True)
    price_real = models.FloatField(default=None, blank=True, null=True)

class Favorite(models.Model):
    favorite_id = models.UUIDField(primary_key=True, auto_created=True)
    favorite_plot = models.ForeignKey(Plot, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.favorite_id