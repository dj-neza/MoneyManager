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

def index(request):
	if 'logout' in request.POST:
		logout(request)
	user_list = Users.objects.all()
	template = loader.get_template('money/index.html')
	context = {
		'user_list': user_list,
	}
	return HttpResponse(template.render(context, request))

def app(request, user_id):
	if 'LOGIN' in request.POST:
		"""function for loging an already existing user into application"""
		username = request.POST['username']
		password = request.POST['password1']
		user = authenticate(username=username, password=password)
		if user is not None:
			u = Users.objects.get(user_name=username)
			if u is not None:
				user_id = u.pk
			login(request, user)
		else:
			messages.error(request, "Wrong username or password.")
			logger.debug("Invalid login with username "+username+" and pass "+password)
			return HttpResponseRedirect(reverse('money:index'))
	elif 'SIGNUP' in request.POST:
		"""function for the registration of new users"""
		username = request.POST['username']
		email = request.POST['email2']
		pass1 = request.POST['password2']
		pass2 = request.POST['password22']
		freeUsername = True
		all_users = list(User.objects.all())
		for us in all_users:
			if (us.username == username):
				freeUsername = False
				break
		if freeUsername:
			if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",email,re.IGNORECASE):
				if pass1 == pass2:
					user = User.objects.create_user(username, email, pass1)
					u = Users(user_name=username)
					user.save()
					u.save()
					u1 = Users.objects.get(user_name=username)
					if u1 is not None:
						user_id = u1.pk
					w1 = Wallets(user_wal = Users.objects.get(pk=user_id), wal_name="Cash")
					w2 = Wallets(user_wal = Users.objects.get(pk=user_id), wal_name="Credit card")
					if w1 is not None and w2 is not None:
						w1.save()
						w2.save()
					c1 = Categories(user_cat = Users.objects.get(pk=user_id), cat_name="Transaction", cat_for=1)
					c2 = Categories(user_cat = Users.objects.get(pk=user_id), cat_name="Transaction")
					c3 = Categories(user_cat = Users.objects.get(pk=user_id), cat_name="Adding goal")
					if c1 is not None and c2 is not None and c3 is not None:
						c1.save()
						c2.save()
						c3.save()
					login(request, user)
				else:
					messages.error(request, "Passwords don't match.")
					logger.debug("Failed registration of user "+username+" - passwords didn't match.")
					return HttpResponseRedirect(reverse('money:index'))
			else:
				messages.error(request, "Invalid email.")
				logger.debug("Failed registration of user "+username+" - invalid email input.")
				return HttpResponseRedirect(reverse('money:index'))
		else:
			messages.error(request, "Username not free.")
			logger.debug("Failed registration of user "+username+" - taken username.")
			return HttpResponseRedirect(reverse('money:index'))
	elif 'transactionSS' in request.POST: 
		transaction(request, user_id, 1)
	elif 'expenseS' in request.POST: 
		transaction(request, user_id, 2)
	elif 'incomeSS' in request.POST: 
		transaction(request, user_id, 3)
	elif 'goalNew' in request.POST:
		goal_handling(request, user_id, 1)
	elif 'goalAdd' in request.POST:
		goal_handling(request, user_id, 2)
	elif 'walletADD' in request.POST:
		wallet_handling(request, user_id, 1)
	elif 'walletEDIT' in request.POST:
		wallet_handling(request, user_id, 2)
	elif 'walletREMOVE' in request.POST:
		wallet_handling(request, user_id, 3)
	elif 'catADD' in request.POST:
		category_handling(request, user_id, 1)
	elif 'catEDIT' in request.POST:
		category_handling(request, user_id, 2)
	elif 'catREMOVE' in request.POST:
		category_handling(request, user_id, 3)
	elif 'settings' in request.POST:
		settings(request, user_id)
	elif 'usernameEDIT' in request.POST:
		profile_settings(request, user_id, 1)
	elif 'emailEDIT' in request.POST:
		profile_settings(request, user_id, 2)		
	elif 'passEDIT' in request.POST:
		profile_settings(request, user_id, 3)
	
	user = Users.objects.get(pk=user_id)
	user2 = User.objects.get(username=user.user_name)
	wallet_list = Wallets.objects.filter(user_wal=user_id)
	category_list_exp = Categories.objects.filter(user_cat=user_id, cat_for=0)
	category_list_inc = Categories.objects.filter(user_cat=user_id, cat_for=1)
	goal_list = Goals.objects.filter(user_goal=user_id)
	expense_list = Expenses.objects.filter(user_exp=user_id)
	income_list = Incomes.objects.filter(user_inc=user_id)
	if goal_list is not None and expense_list is not None and income_list is not None:
		return render(request, 'money/app.html', {'user': user, 'user2': user2,  'wallet_list': wallet_list, 'category_list_exp': category_list_exp, 'category_list_inc': category_list_inc, 'goal_list': goal_list, 'expense_list': expense_list, 'income_list': income_list})
	else:
		return render(request, 'money/app.html', {'user': user, 'user2': user2, 'wallet_list': wallet_list, 'category_list_exp': category_list_exp, 'category_list_inc': category_list_inc})


