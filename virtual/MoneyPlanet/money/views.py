from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Users, Categories, Wallets, Goals, Expenses, Incomes

def index(request):
	if 'logout' in request.POST:
		logout(request)
	user_list = Users.objects.all()
	template = loader.get_template('money/index.html')
	context = {
		'user_list': user_list,
	}
	return HttpResponse(template.render(context, request))

"""u = User.objects.get(username='john')
u.set_password('new password')
u.save()"""

def app(request, user_id):
	if 'LOGIN' in request.POST:
		username = request.POST['username']
		password = request.POST['password1']
	  	user = authenticate(username=username, password=password)
	  	if user is not None:
	  		u = Users.objects.get(user_name=username)
	    	if u is not None:
	    		user_id = u.pk
	    	login(request, user)
	elif 'SIGNUP' in request.POST:
		username = request.POST['username']
		email = request.POST['email2']
		pass1 = request.POST['password2']
		pass2 = request.POST['password22']
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
			w1.save()
			w2.save()
			c1 = Categories(user_cat = Users.objects.get(pk=user_id), cat_name="Transaction", cat_for=1)
			c2 = Categories(user_cat = Users.objects.get(pk=user_id), cat_name="Transaction")
			c3 = Categories(user_cat = Users.objects.get(pk=user_id), cat_name="Adding goal")
			c1.save()
			c2.save()
			c3.save()
	elif 'transactionSS' in request.POST: 
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
			t1 = Incomes(user_inc = Users.objects.get(pk=user_id), inc_name=name, cat_inc= Categories.objects.get(pk=1), wal_inc=Wallets.objects.get(pk=t_from), inc_date=date, inc_amount=amount, inc_rep=rep)
			t1.save()
			t2 = Expenses(user_exp = Users.objects.get(pk=user_id), exp_name=name, cat_exp= Categories.objects.get(pk=2), wal_exp=Wallets.objects.get(pk=t_to), exp_date=date, exp_amount=amount, exp_rep=rep)
			t2.save()
		elif(transact_type == '2'):
			excat = request.POST.get('excat1')
			loaned = ""
			if 'loan' in request.POST:
				loaned = request.POST['loaned']
			t = Expenses(user_exp = Users.objects.get(pk=user_id), exp_name=name, cat_exp= Categories.objects.get(pk=excat), wal_exp=Wallets.objects.get(pk=t_from), exp_date=date, exp_amount=amount, exp_rep=rep, exp_loan=True, exp_loan_to=loaned)
			t.save()
			u = Users.objects.get(pk=user_id)
			u.balance -= int(amount)
			u.save()
		elif(transact_type == '3'):
			incat = request.POST.get('incat1')
			indebt = ""
			if 'debt' in request.POST:
				indebt = request.POST['indebt']
			t = Incomes(user_inc = Users.objects.get(pk=user_id), inc_name=name, cat_inc= Categories.objects.get(pk=incat), wal_inc=Wallets.objects.get(pk=t_from), inc_date=date, inc_amount=amount, inc_rep=rep, inc_debt=True, inc_debt_to=indebt)
			t.save()
			u = Users.objects.get(pk=user_id)
			u.balance += int(amount)
			u.save()
	elif 'expenseS' in request.POST: 
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
		t.save()
		u = Users.objects.get(pk=user_id)
		u.balance -= int(amount)
		u.save()
	elif 'incomeSS' in request.POST: 
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
		t.save()
		u = Users.objects.get(pk=user_id)
		u.balance += int(amount)
		u.save()
	elif 'goalNew' in request.POST:
		name = request.POST['goalName']
		amount = request.POST['amount']
		date = request.POST['goalDate']
		g = Goals(user_goal=Users.objects.get(pk=user_id), goal_name=name, goal_amount=amount, goal_deadline=date)
		g.save()
	elif 'goalAdd' in request.POST:
		print(request.POST)
		g = Goals.objects.get(pk=request.POST['goalPK'])
		amount = request.POST['amount']
		date = request.POST['goalDate']
		t_from = request.POST.get('t_to')
		nameExp = "Savings for " + g.goal_name
		g.amount_now += int(amount)
		g.save()
		e = Expenses(user_exp = Users.objects.get(pk=user_id), exp_name=nameExp, cat_exp= Categories.objects.get(pk=3), wal_exp=Wallets.objects.get(pk=t_from), exp_date=date, exp_amount=amount)
		e.save()
		u = Users.objects.get(pk=user_id)
		u.balance -= int(amount)
		u.save()
	elif 'walletADD' in request.POST:
		name = request.POST['wallettoadd']
		w = Wallets(user_wal = Users.objects.get(pk=user_id), wal_name=name)
		w.save()
	elif 'walletEDIT' in request.POST:
		name = request.POST['wallet1']
		w = Wallets.objects.get(pk=request.POST['walletPK'])
		w.wal_name = name
		w.save()
	elif 'walletREMOVE' in request.POST:
		w = Wallets.objects.get(pk=request.POST['walletPK'])
		w.delete()
	elif 'catADD' in request.POST:
		name = request.POST['cattoadd']
		inc = 0
		if 'catinc' in request.POST:
			inc = 1
		c = Categories(user_cat = Users.objects.get(pk=user_id), cat_name=name, cat_for=inc)
		c.save()
	elif 'catEDIT' in request.POST:
		name = request.POST['cat1']
		c = Categories.objects.get(pk=request.POST['categoryPK'])
		c.cat_name = name
		c.save()
	elif 'catREMOVE' in request.POST:
		c = Categories.objects.get(pk=request.POST['categoryPK'])
		c.delete()
	elif 'settings' in request.POST:
		currency = request.POST.get('current')
		u = Users.objects.get(pk=user_id)
		u.currency = currency
		u.save()
	elif 'usernameEDIT' in request.POST:
		name = request.POST['username']
		u1 = Users.objects.get(pk=user_id)
		u = User.objects.get(username=u1.user_name)
		u1.user_name = name
		u.username = name
		u.save()
		u1.save()
	elif 'emailEDIT' in request.POST:
		email = request.POST['e-mail']
		u1 = Users.objects.get(pk=user_id)
		u = User.objects.get(username=u1.user_name)
		u.email = email
		u.save()
	elif 'passEDIT' in request.POST:
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']
		if pass1 == pass2:
			u1 = Users.objects.get(pk=user_id)
			u = User.objects.get(username=u1.user_name)
			u.set_password(pass1)
			u.save()
	user = get_object_or_404(Users, pk=user_id)
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


