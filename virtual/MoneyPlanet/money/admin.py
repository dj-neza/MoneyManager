from django.contrib import admin

from .models import Users, Categories, Wallets, Goals, Incomes, Expenses

admin.site.register(Users)
admin.site.register(Categories)
admin.site.register(Wallets)
admin.site.register(Goals)
admin.site.register(Incomes)
admin.site.register(Expenses)