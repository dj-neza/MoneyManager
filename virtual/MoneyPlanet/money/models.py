# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Users(models.Model):
	user_name = models.CharField(max_length=50)
	e_mail = models.EmailField(max_length=254)
	pass_word = models.CharField(max_length=100)
	balance = models.IntegerField(default=0)
	currency = models.CharField(default="€", max_length=20) # € or $
	decimal = models.IntegerField(default=0) # 0-. 1-
	def __str__(self):
		return self.user_name

@python_2_unicode_compatible
class Categories(models.Model):
	user_cat = models.ForeignKey(Users, on_delete=models.CASCADE)
	cat_name = models.CharField(max_length=50)
	cat_for = models.IntegerField(default=0) # 0-exp, 1-inc
	def __str__(self):
		return self.cat_name

@python_2_unicode_compatible
class Wallets(models.Model):
	user_wal = models.ForeignKey(Users, on_delete=models.CASCADE)
	wal_name = models.CharField(max_length=50)
	wal_balance = models.IntegerField(default=0)
	def __str__(self):
		return self.wal_name

@python_2_unicode_compatible
class Goals(models.Model):
	user_goal = models.ForeignKey(Users, on_delete=models.CASCADE)
	goal_name = models.CharField(max_length=50)
	goal_amount = models.IntegerField(default=0)
	goal_deadline = models.DateField()
	amount_now = models.IntegerField(default=0)
	def __str__(self):
		return self.goal_name

@python_2_unicode_compatible
class Incomes(models.Model):
	user_inc = models.ForeignKey(Users, on_delete=models.CASCADE)
	inc_name = models.CharField(max_length=50)
	wal_inc = models.ForeignKey(Wallets, on_delete=models.CASCADE)
	cat_inc = models.ForeignKey(Categories, on_delete=models.CASCADE)
	inc_date = models.DateField()
	inc_amount = models.FloatField(default=1)
	inc_rep = models.IntegerField(default=0) # 0-no, 1-daily, 2-monthly, 3-yearly
	inc_debt = models.BooleanField(default=False)
	inc_debt_to = models.CharField(default="", blank=True, null=True, max_length=50)
	def __str__(self):
		return self.inc_name

@python_2_unicode_compatible
class Expenses(models.Model):
	user_exp = models.ForeignKey(Users, on_delete=models.CASCADE)
	exp_name = models.CharField(max_length=50)
	cat_exp = models.ForeignKey(Categories, on_delete=models.CASCADE)
	wal_exp = models.ForeignKey(Wallets, on_delete=models.CASCADE)
	exp_date = models.DateField()
	exp_amount = models.FloatField(default=1)
	exp_rep = models.IntegerField(default=0) # 0-no, 1-daily, 2-weekly, 3-yearly
	exp_loan = models.BooleanField(default=False)
	exp_loan_to = models.CharField(default="", blank=True, null=True, max_length=50)
	def __str__(self):
		return self.exp_name

