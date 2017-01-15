from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from .models import Users, Categories, Wallets, Goals, Expenses, Incomes
import logging
import re
from django.contrib import messages
from django.core.exceptions import ValidationError
from .service import *

logger = logging.getLogger('debuglog')

def transaction(request, user_id, type):
	"""function for handling transactions 
	TYPE param: 1 - transaction
				2 - expense
				3 - income"""
	if type == 1:
		name = request.POST['expName']
		date = request.POST['expDate']
		amount = request.POST['amount']
		transact_type = request.POST.get('transactions')
		t_from = request.POST.get('t_from')
		rep = 0
		if 'repeat' in request.POST:
			rep = int(request.POST.get('repeat_transaction'))
		if (transact_type == '1'):
			t_to = request.POST.get('t_to')
			t1 = Incomes(user_inc = Users.objects.get(pk=user_id), inc_name=name, cat_inc= Categories.objects.get(user_cat = Users.objects.get(pk=user_id), cat_name="Transaction", cat_for=1), wal_inc=Wallets.objects.get(pk=t_from), inc_date=date, inc_amount=amount, inc_rep=rep)
			if t1 is not None:
				t1.save()
			t2 = Expenses(user_exp = Users.objects.get(pk=user_id), exp_name=name, cat_exp= Categories.objects.get(user_cat = Users.objects.get(pk=user_id), cat_name="Transaction", cat_for=0), wal_exp=Wallets.objects.get(pk=t_to), exp_date=date, exp_amount=amount, exp_rep=rep)
			if t2 is not None:
				t2.save()
		elif(transact_type == '2'):
			excat = request.POST.get('excat1')
			loaned = ""
			if 'loan' in request.POST:
				loaned = request.POST['loaned']
			t = Expenses(user_exp = Users.objects.get(pk=user_id), exp_name=name, cat_exp= Categories.objects.get(pk=excat), wal_exp=Wallets.objects.get(pk=t_from), exp_date=date, exp_amount=amount, exp_rep=rep, exp_loan=True, exp_loan_to=loaned)
			if t is not None:
				t.save()
			u = Users.objects.get(pk=user_id)
			if u is not None:
				u.balance -= int(amount)
				u.save()
		elif(transact_type == '3'):
			incat = request.POST.get('incat1')
			indebt = ""
			if 'debt' in request.POST:
				indebt = request.POST['indebt']
			t = Incomes(user_inc = Users.objects.get(pk=user_id), inc_name=name, cat_inc= Categories.objects.get(pk=incat), wal_inc=Wallets.objects.get(pk=t_from), inc_date=date, inc_amount=amount, inc_rep=rep, inc_debt=True, inc_debt_to=indebt)
			if t is not None:
				t.save()
			u = Users.objects.get(pk=user_id)
			if u is not None:
				u.balance += int(amount)
				u.save()
	elif type == 2:
		name = request.POST['expName']
		date = request.POST['expDate']
		amount = request.POST['amount']
		t_from = request.POST.get('exp_wal')
		rep = 0
		if 'repeat' in request.POST:
			rep = int(request.POST.get('repeatit'))
		excat = request.POST.get('exp_cat')
		loaned = ""
		if 'loan' in request.POST:
			loaned = request.POST['loaned']
		t = Expenses(user_exp = Users.objects.get(pk=user_id), exp_name=name, cat_exp= Categories.objects.get(pk=excat), wal_exp=Wallets.objects.get(pk=t_from), exp_date=date, exp_amount=amount, exp_rep=rep, exp_loan=True, exp_loan_to=loaned)
		if t is not None:
			t.save()
		u = Users.objects.get(pk=user_id)
		if u is not None:
			u.balance -= int(amount)
			u.save()
	elif type == 3:
		name = request.POST['incName']
		date = request.POST['incDate']
		amount = request.POST['amount']
		t_from = request.POST.get('inc_wal')
		rep = 0
		if 'repeat' in request.POST:
			rep = int(request.POST.get('repeatit2'))
		incat = request.POST.get('inc_cat')
		indebt = ""
		if 'debt' in request.POST:
			indebt = request.POST['indebt']
		t = Incomes(user_inc = Users.objects.get(pk=user_id), inc_name=name, cat_inc= Categories.objects.get(pk=incat), wal_inc=Wallets.objects.get(pk=t_from), inc_date=date, inc_amount=amount, inc_rep=rep, inc_debt=True, inc_debt_to=indebt)
		if t is not None:
			t.save()
		u = Users.objects.get(pk=user_id)
		if u is not None:
			u.balance += int(amount)
			u.save()

def goal_handling(request, user_id, type):
	"""function for handling adding new goals and adding savings to them
	TYPE param: 1 - create new goal
				2 - add to goal"""
	if type == 1:
		name = request.POST['goalName']
		amount = request.POST['amount']
		date = request.POST['goalDate']
		g = Goals(user_goal=Users.objects.get(pk=user_id), goal_name=name, goal_amount=amount, goal_deadline=date)
		if g is not None:
			g.save()
	elif type == 2:
		g = Goals.objects.get(pk=request.POST['goalPK'])
		amount = request.POST['amount']
		date = request.POST['goalDate']
		t_from = request.POST.get('t_to')
		if g is not None:
			nameExp = "Savings for " + g.goal_name
			g.amount_now += int(amount)
			g.save()
			e = Expenses(user_exp = Users.objects.get(pk=user_id), exp_name=nameExp, cat_exp= Categories.objects.get(user_cat = Users.objects.get(pk=user_id), cat_name="Adding goal"), wal_exp=Wallets.objects.get(pk=t_from), exp_date=date, exp_amount=amount)
			if e is not None:
				e.save()
			u = Users.objects.get(pk=user_id)
			if u is not None:
				u.balance -= int(amount)
				u.save()

def wallet_handling(request, user_id, type):
	"""function adding wallets, editing and removing them
	TYPE param: 1 - add wallet
				2 - edit wallet
				3 - remove wallet"""
	if type == 1:
		name = request.POST['wallettoadd']
		w = Wallets(user_wal = Users.objects.get(pk=user_id), wal_name=name)
		if w is not None:
			w.save()
	elif type == 2:
		name = request.POST['wallet1']
		w = Wallets.objects.get(pk=request.POST['walletPK'])
		if w is not None: 
			w.wal_name = name
			w.save()
	elif type == 3:
		w = Wallets.objects.get(pk=request.POST['walletPK'])
		if w is not None:
			w.delete()

def category_handling(request, user_id, type):
	"""function adding categories, editing and removing them
	TYPE param: 1 - add category
				2 - edit category
				3 - remove category"""
	if type == 1:
		name = request.POST['cattoadd']
		inc = 0
		if 'catinc' in request.POST:
			inc = 1
		c = Categories(user_cat = Users.objects.get(pk=user_id), cat_name=name, cat_for=inc)
		if c is not None:
			c.save()
	elif type == 2:
		name = request.POST['cat1']
		c = Categories.objects.get(pk=request.POST['categoryPK'])
		if c is not None:
			c.cat_name = name
			c.save()
	elif type == 3:
		c = Categories.objects.get(pk=request.POST['categoryPK'])
		if c is not None:
			c.delete()

def settings(request, user_id):
	"""function for changing settings"""
	currency = request.POST.get('current')
	u = Users.objects.get(pk=user_id)
	if u is not None:
		u.currency = currency
		u.save()

def profile_settings(request, user_id, type):
	"""function for changing profile settings
	TYPE param: 1 - username change
				2 - email change
				3 - password change"""
	if type == 1:
		name = request.POST['username']
		freeUsername = True
		all_users = list(User.objects.all())
		for us in all_users:
			if (us.username == name):
				freeUsername = False
				break
		if freeUsername:
			u1 = Users.objects.get(pk=user_id)
			if u1 is not None:
				u = User.objects.get(username=u1.user_name)
				if u is not None:
					u1.user_name = name
					u.username = name
					u.save()
					u1.save()
		else:
			messages.error(request, "The username is already taken.")
			logger.debug("Failed change of username of user "+user_id+" - "+name+" is a taken username.")
			return HttpResponseRedirect(reverse('money:app', args=(user_id,)))
	elif type == 2:
		email = request.POST['e-mail']
		if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",email,re.IGNORECASE):
			u1 = Users.objects.get(pk=user_id)
			if u1 is not None:
				u = User.objects.get(username=u1.user_name)
				if u is not None:
					u.email = email
					u.save()
		else:
			messages.error(request, "Invalid email.")
			logger.debug("Failed change of email of user "+user_id+" - "+email+" is invalid.")
			return HttpResponseRedirect(reverse('money:app', args=(user_id,)))
	elif type == 3:
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']
		if pass1 == pass2:
			u1 = Users.objects.get(pk=user_id)
			if u1 is not None:
				u = User.objects.get(username=u1.user_name)
				if u is not None:
					u.set_password(pass1)
					u.save()
		else:
			messages.error(request, "Passwords don't match.")
			logger.debug("Failed change of password of user "+user_id+" - passwords didn't match.")
			return HttpResponseRedirect(reverse('money:app', args=(user_id,)))










