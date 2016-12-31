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
	user = get_object_or_404(Users, pk=user_id)
	return render(request, 'money/app.html', {'user': user})