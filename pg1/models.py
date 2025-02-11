from django.db import models,connections
# Create your models here.
#using 2nd db reg2
'''
class sig(models.Model):
    us=models.CharField(max_length=255,primary_key=True)
    fn=models.CharField(max_length=255)
    ln=models.CharField(max_length=255)
    #ps=models.CharField(max_length=255)
    cn=models.IntegerField()
    class Meta:
        db_table='signin'
        #db='reg2'
'''
class pro(models.Model):
    us=models.CharField(max_length=255,primary_key=True)
    pic=models.IntegerField()
    pp=models.CharField(max_length=255)
    clg=models.CharField(max_length=255)
    rt=models.IntegerField()
    class Meta:
        db_table='prop'
        #db='reg2'
