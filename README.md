# djangoProject
Projeto destinado à 1° etapa do processo seletivo na E-soft Sistemas.

## 1 - Pacotes necessários:
  * Python >= 3.8.5
  * Django 3.1.5
  
#### 1.1 - Bibliotecas do Python necessárias:
  * os
  * urllib
  * json
  * random
  
#### 1.2 - Instalação:
  1. Clone o repositório usando: <code>git clone https://github.com/ArthurGM18/djangoProject</code>.
  2. Utilize <code>cd djangoProject/</code> para entrar na pasta com os arquivos.
  3. Execute o comando <code>python manage.py runserver</code> ou <code>python3 manage.py runserver</code> para rodar o servidor.
  4. Abra o link onde o site está hospedado.
 
## 2 - Sobre o Sistema

#### 2.1 - Funcionamento geral

  O sistema desenvolvido administra o cadastramento e a listagem dos dados de pessoas em um site utilizando o framework Django, juntamente com a linguagem Python.  Como o assunto principal é a aplicação deste sistema para a web, foi indispensável o envolvimento com linguagens de construção de páginas web como **html** e mecanismos para adicionar estilo a um documento web como o **css**. Com isso temos uma aplicação dividida em algumas seções que serão apresentadas detalhadamente ao longo deste texto.
  
#### 2.2 - Sistema de cadastramento

  A forma como os dados são cadastrados é bem simples. Todo formulário de cadastro deverá seguir um padrão possuindo os campos:
  
    * nome
    * sobrenome
    * idade
    * data de nascimento
    * email
    * apelido
    * observações
    
  **obs¹**: Os campos marcados com "!" são obrigatórios.
  **obs²**: O campo "data de nascimento" utiliza o padrão AAAA-MM-DD, ex: 1999-11-23.
  
  Após preencher os campos corretamente basta clicar no botão "Cadastrar" que os dados serão salvos no banco e o usuário será redirecionado para a página de listagem de cadastros.
  
#### 2.3 - Listagem dos cadastros

  Nesta tela será apresentado uma paginação com uma listagem de todos os cadastros existentes no banco de dados. Cada página contém uma lista de 10 cadastros que podem ser navegados atravém de setas no rodapé da página. Além disso, os dados estão apresentados em ordem alfabética crescente.
  Usuários do sistema que são **superusuários** podem editar e excluir os dados cadastrados, caso seja logado em um usuário que não possua tal status, essas opções não irão aparecer. Para facilitar a vida, já está definido um **superusuário** no sistema, e para acessá-lo, basta entrar na parte administrativa criada pelo próprio Django, clicando na opção "Admin" pela barra de navegação:
  * **Login**: admin
  * **Senha**: admin
  
#### 2.4 - Geração de cadastros aleatórios

  Foi adicionado uma opção para gerar cadastros aleatórios. Este recurso se encontra na barra de navegação como **Gerar Cadastros**. Para isso é utilizado uma api geradora de nomes aleatórios disponível em https://gerador-nomes.herokuapp.com/nome/aleatorio, e com ela é possível preencher os dados fictícios cadastramento.
  Toda vez que a opção de geração de cadastros for ativada, **serão criados 5 novos cadastros**, e pode levar alguns segundos para a ação ser concluída. Ao final deste processo a página será atualizada com os novos cadastros já inseridos na lista.
