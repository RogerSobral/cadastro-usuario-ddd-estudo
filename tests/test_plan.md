# 🧪 Plano de Testes: Cadastro de Usuário
> Este documento define os testes que validam a regra de negócio do cadastro de usuário.
> Aplicação desenvolvida em Python com Flask, MySQL e arquitetura DDD.
---
## ✅ Caso de Uso: Cadastro de novo usuário
### 1. [SUCESSO] Deve cadastrar usuário com dados válidos
- **Dado**: Nome, e-mail e senha corretos
- **Quando**: Os dados são enviados para a API
- **Então**: Deve retornar status `201 Created` e mensagem de sucesso
- **E**: O usuário deve ser salvo no banco de dados com senha criptografada
---
## ❌ Casos de Erro (validações)
### 2. [ERRO] Não deve cadastrar usuário com e-mail já existente
- **Dado**: Um e-mail já cadastrado
- **Quando**: Tenta-se cadastrar novamente com o mesmo e-mail
- **Então**: Deve retornar status `400 Bad Request` e mensagem "Usuário já existe"
---
### 3. [ERRO] Não deve aceitar e-mail inválido
- **Exemplo de entrada**: `joao@email`, `@gmail.com`, `joao@`
- **Então**: Deve retornar status `400 Bad Request` e mensagem "E-mail inválido"
---
### 4. [ERRO] Senha deve ter no mínimo 8 caracteres
- **Exemplo de entrada**: `"abc123"` (senha curta)
- **Então**: Deve retornar status `400 Bad Request` e mensagem "Senha fraca"
---
### 5. [ERRO] Nome obrigatório
- **Exemplo de entrada**: nome vazio `""` ou só espaços `"   "`
- **Então**: Deve retornar status `400 Bad Request` e mensagem "Nome obrigatório"
---
### 6. [ERRO] Campos obrigatórios não preenchidos
- **Dado**: Campos ausentes no corpo da requisição (ex: sem e-mail ou senha)
- **Então**: Deve retornar status `400` com mensagens específicas de erro para cada campo
---
## 🛡️ Regras de segurança
### 7. [SEGURANÇA] A senha não deve ser armazenada em texto puro
- **Verificação**: O campo de senha no banco deve conter um hash (ex: bcrypt)
- **Então**: Mesmo que um invasor acesse o banco, não verá senhas reais
---
## 🧪 Extras (opcional)
### 8. [UX] Mensagens de erro devem ser amigáveis e específicas
- Mensagens genéricas como “erro no servidor” devem ser evitadas quando for erro de usuário
---
## 🧰 Ferramentas de Teste
- **Python**: `pytest`, `pytest-flask`
- **Cobertura**: `pytest-cov`
- **Testes de integração**: `Flask Client`
---
## 🗂️ Localização dos testes
/tests
└── /users
└── test_create_user.py 
