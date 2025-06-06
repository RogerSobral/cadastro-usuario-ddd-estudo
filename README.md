# Cadastro de Usuários - Projeto com DDD, Testes e Boas Práticas

Este projeto é um exemplo didático de como organizar uma aplicação de cadastro de usuários seguindo os princípios de **Domain-Driven Design (DDD)**, **Clean Architecture**, e utilizando testes automatizados com `pytest`.

---

## 📁 Estrutura do Projeto

```
cadastro-usuarios-ddd/
├── app/
│   ├── domain/
│   │   ├── entities/
│   │   │   └── user.py
│   ├── repositories/
│   │   └── in_memory_user_repository.py
│   └── use_cases/
│       └── create_user.py
├── tests/
│   └── test_create_user.py
├── requirements.txt
└── README.md
```

---

## 📦 Requisitos

- Python 3.10 ou superior
- Git instalado

---

## 🚀 Como rodar o projeto localmente

1. **Clone o repositório:**

```bash
git clone https://github.com/RogerSobral/cadastro-usuario-ddd-estudo.git
cd cadastro-usuario-ddd-estudo
```

2. **Crie um ambiente virtual:**

```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**

- **Windows**:
```bash
venv\Scripts\activate
```

- **Linux/macOS**:
```bash
source venv/bin/activate
```

4. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

---

## 🧪 Rodando os testes

O projeto possui testes automatizados que verificam:

- Cadastro de usuário válido
- E-mail inválido
- Senha fraca
- Usuário com e-mail duplicado

### Para rodar os testes:

```bash
pytest
```

Você verá uma saída como:

```
====================== test session starts ======================
collected 4 items

tests/test_create_user.py ....                        [100%]

======================= 4 passed in 0.12s =======================
```

---

## 🧠 Conceitos Aplicados

- DDD: Separação por camadas (Entidades, Casos de Uso, Repositórios)
- Testes automatizados com `pytest`
- Simulação de repositórios com repositório em memória
- Validações simples com regex para e-mail e senha

---

## 📚 Referências para estudo

- [Clean Architecture - Robert C. Martin](https://www.amazon.com.br/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164)
- [Domain-Driven Design - Eric Evans](https://www.amazon.com.br/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)
- [Documentação do Pytest](https://docs.pytest.org/)
- [Curso de Python com TDD na Prática (gratuito)](https://app.rocketseat.com.br/)

---

## 🧑‍💻 Autor

**Roger Sobral**  
Desenvolvedor Python e Instrutor Técnico no Senac Santana.

---

## 📄 Licença

Este projeto está sob a licença MIT.