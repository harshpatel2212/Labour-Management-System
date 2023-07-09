from django.db import models

# Create your models here.


class District(models.Model):
    dist_id = models.IntegerField(primary_key=True)
    dist_name = models.CharField(max_length=100)
    dist_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'labourer_db\".\"district'


class Person(models.Model):
    person_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dist_id = models.IntegerField()
    birth_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'labourer_db\".\"person'


class Bank_Details(models.Model):
    person_id = models.IntegerField(primary_key=True)
    bank_name = models.CharField(max_length=100)
    bank_head_branch = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    Account_holder_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'labourer_db\".\"Bank_details'


class Supervisor(models.Model):
    sup_id = models.IntegerField(primary_key=True)
    person_id = models.IntegerField()
    salary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'labourer_db\".\"supervisor'
