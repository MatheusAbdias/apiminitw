# Mini Twitter Api 
- Projeto desenvolvido utilizando django-rest e postgres utilizando um container docker. Esta api possibilita cadastro de novos usuários, login, logout, postagens, um feed geral de todos os usuários cadastrados no sistema e outro feed destinado a um usuário em específico em que não aparece suas postagens, apenas as de outras pessoas. Ao logar, recebe-se um token que expira em 2 horas e 30 minutos.
## Tecnologias utilizadas 
- Python
- PostgreSQL
- Django-rest
- Docker

## Objetivos Propostos
- :one: Cadastro de usuário.
- :two: Autenticação (login + token temporário).
- :three: Fazer uma publicação.
- :four: Feed Geral com as ultimas 10 postagens.

## Modelgem do Banco de Dados 
### Usuário:
- username: um campo que armazena uma string única entre todos os usuários (obrigatório ao fazer o cadastro.)
- password: armazena uma string (obrigatório ao fazer o cadastro.)
- email: armazena um e-mail único entre todos os usuários (obrigatório ao fazer o cadastro.)
- userDescricao: armazena uma string (não obrigatório.)
- userFollows: armazena os seguidores do usuário.
### Postagem:
- user: campo que relaciona a tabela de postagens com o usuário que fez. Ao deletar a conta, suas postagens também serão excluídas.
- titulo: armazena uma string (obrigatório ao criar uma postagem.)
- Descricao: um campo que armazena uma string (obrigatório ao criar uma postagem.)
- Imagem: armazena uma imagem (não obrigatorio.)
### Diagrama Relacional:<br>
 ![Api Doc](https://i.imgur.com/bMwmDBl.jpg)
## Descrição das rotas criadas
- `http://127.0.0.1:8000/admin/`: Área de administração do django.
- `http://127.0.0.1:8000/api/usuarios/`: Ao fazer uma requisição (GET) a esta endpoint, ela retornará um json com todos os usuários cadastrados na plataforma. 
- `http://127.0.0.1:8000/api/cadastro/`: Ao fazer uma requisição (POST) com *username, email, password, password_confirm* em formato *json*.
- `http://127.0.0.1:8000/usuario/post/`: Esta endpoint só pode ser acessada por usuário logado (em conexão ativa na plataforma). Fazendo esta requisição (POST) com titulo e descrição em formato *json*, ela cria um post vinculado ao usuário logado.
- `http://127.0.0.1:8000/usuario/post/`: Ao fazer uma requisição (GET), retorna as ultimas 10 postagens da api, excluindo as que pertecem ao usuario que fez a requisição.
- `http://127.0.0.1:8000/api/login/`: Ao fazer uma requisição (POST) com username e password em formato json, o usuário sera logado e recebera um token para poder acessar a area de post, (Adicionar no header Authorization e passar Token "Codigo disponibilizado").
- `http://127.0.0.1:8000/api/logout/`: Ao fazer uma requisição (GET) a endpoint apagara o token associado ao usuário.
## Deploy
- O projeto esta feito deploy no heroku pode ser acessado pelo <a href="https://api-minitw.herokuapp.com/">Link<a>, todas as urls que foram mostradas anteriormente estão em funcionamento.
