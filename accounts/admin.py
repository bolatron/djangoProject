from django.contrib import admin

from .models import Account

admin.site.site_header = 'Administração'

#   Registrando o modelo 'Account' na seção de administração do site
# para que os dados sejam lidos e manipulados por contas de admin.
admin.site.register(Account)