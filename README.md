# Mini Twitter Api 
- Projeto desenvolvido utilizando django-rest e postgres utilizando um container docker. Esta api possibilida cadastros de novo usuarios, login, logout, postagens, um feed geral de todos os usuarios cadastrados no sistema e um feed destinado a um usuario a qual não aparece suas postagens do mesmo apenas dos outros usuarios,ao logar recebe um token que espira em 2 horas e 30 minutos. 
## Tecnologias utilizadas 
- Python
- PostgreSQL
- Django-rest
- Docker

## Objetivos Propostos
- :one: Cadastro de Usuário.
- :two: Autenticação (login + token temporario).
- :three: Fazer uma publicação.
- :four: Feed Geral com as ultimos 10 postagens.

## Descrição do Banco de Dados 
### Usuário:
- username: Um campo que armazena uma string unica entre todos os usuários. obrigatorio ao criar um usuario.
- password: Um campo que armazena uma string, obrigatorio ao criar um usuário.
- email: Um campo que armazena um email unico entre todos os usuários, obrigatorio ao criar um usuário.
- userDescricao: Um campo que armazena uma string, não obrigatorio.
- userFollows: Um campo que aramazena os seguidores do usuario.
### Postagem:
- user: Um campo que relaciona a tabela de postagens com o usario que fez, ao deletar o usuario suas postagens também são excluidas.
- titulo: Um campo que armazena uma string, campo obrigatorio ao criar uma postagem.
- Descricao: Um campo que armazena uma string, campo obrigatorio ao criar uma postagem.
- Imagem: Um campo que armazena uma imagem, não obrigatorio.
## Descrição das rotas criadas
- `http://127.0.0.1:8000/admin/`: Area de administrado do django.
- `http://127.0.0.1:8000/api/usuarios/` Ao fazer uma requisição (GET) a esta endpoint ela retornara um json com todos os usuários cadastrados na plataforma. 
- `http://127.0.0.1:8000/api/cadastro/` Ao fazer uma requisição (POST) com username, email,password,password_confirm em formato json.
- `http://127.0.0.1:8000/usuario/post/` Esta endpoit só pode ser acessada por usuario logado, ao fazer uma requisição (POST) com titulo, descrico em formato json ela cria um post vinculado ao usario logado.
- `http://127.0.0.1:8000/usuario/post/` Ao fazer uma requisição (GET), retorna as ultimas 10 postagens da api, excluindo as que pertecem ao usuario que fez a requisição.
- `http://127.0.0.1:8000/api/login/` Ao fazer uma requisição (POST) com username e password em formato json, o usuário sera logado e recebera um token para poder acessar a area de post, (Adicionar no header Authorization e passar Token "Codigo disponibilizado").
- `http://127.0.0.1:8000/api/logout/` Ao fazer uma requisição (GET) a endpoint apagara o token associado ao usuário.
## Deploy
- O projeto esta feito deploy no heroku pode ser acessado pelo <a href="https://api-minitw.herokuapp.com/">Link<a>, todas as urls que foram mostradas estão em funcionamento.
