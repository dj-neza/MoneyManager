from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Users, Categories, Wallets, Goals, Expenses, Incomes

def index(request):
	user_list = Users.objects.all()
	template = loader.get_template('money/index.html')
	context = {
		'user_list': user_list,
	}
	return HttpResponse(template.render(context, request))

def app(request, user_id):
	if 'transactionSS' in request.POST: 
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
			t2 = Expenses(user_exp = Users.objects.get(pk=user_id), exp_name=name, cat_exp= Categories.objects.get(pk=1), wal_exp=Wallets.objects.get(pk=t_to), exp_date=date, exp_amount=amount, exp_rep=rep)
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
	user = get_object_or_404(Users, pk=user_id)
	wallet_list = Wallets.objects.filter(user_wal=user_id)
	category_list_exp = Categories.objects.filter(user_cat=user_id, cat_for=0)
	category_list_inc = Categories.objects.filter(user_cat=user_id, cat_for=1)
	goal_list = Goals.objects.filter(user_goal=user_id)
	expense_list = Expenses.objects.filter(user_exp=user_id)
	income_list = Incomes.objects.filter(user_inc=user_id)
	return render(request, 'money/app.html', {'user': user, 'wallet_list': wallet_list, 'category_list_exp': category_list_exp, 'category_list_inc': category_list_inc, 'goal_list': goal_list, 'expense_list': expense_list, 'income_list': income_list})
