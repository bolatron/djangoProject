from django.urls import path

from . import views

app_name = 'accounts'

# Sistemas de urls do app 'accounts';
# O app conta com as urls:
#   * '/' : Tela inicial do sistema, responsável pelas informações de cadastro.
#   * '/home/' : Tela com a listagem das pessoas cadastradas no sistema.
#   * '/generate' : Usada unicamente para gerar cadastros aleatórios.
#   * '/home/edit/<id>' : Tela usada para editar dados de uma pessoa já cadastrada.
#   * '/home/delete/<id>' : Tela udada para deletar dados de uma pessoa já cadastrada.

urlpatterns = [
    path('', views.register, name='register'),
    path('home/', views.cadaster_list, name='cadaster-list'),
    path('generate/', views.create_accounts, name='generate-accounts'),
    path('home/edit/<int:id>', views.editAccount, name='edit-account'),
    path('home/delete/<int:id>', views.deleteAccount, name='delete-account'),
]