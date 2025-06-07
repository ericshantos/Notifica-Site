[🇬🇧] [Read in English](README.md)

# Portfolio Tracker API

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.1.1-green.svg)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)

API para rastreamento de visitas em portfólios com relatórios diários automatizados por e-mail.

## 📋 Pré-requisitos

- Python 3.9+
- Conta do Gmail com "Senhas de App" configurada (veja abaixo)
- Dependências listadas em `requirements.txt`

## 🔐 Configuração do Gmail

Para enviar e-mails através do Gmail, você precisará configurar uma "Senha de App":

1. Acesse sua [Conta do Google](https://myaccount.google.com/)
2. Navegue até "Segurança" → "Senhas de App"
3. Selecione "Aplicativo" como `Mail` e "Dispositivo" como `Outro (Nomeie conforme preferir)`
4. Clique em "Gerar" e copie a senha gerada
5. Use esta senha no lugar da sua senha normal no arquivo `.env`

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/ericshantos/VisitTracker_API.git
   cd VisitTracker_API
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` com suas credenciais:
   ```ini
   EMAIL_ADDRESS=seu-email@gmail.com
   EMAIL_PASSWORD=sua-senha-de-app
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   ```

5. Execute a aplicação:
   ```bash
   python run.py
   ```

## 🏗 Arquitetura

A API segue uma estrutura modular com separação clara de responsabilidades:

```
app/
├── controllers/    # Lógica de controle das requisições
├── models/         # Modelos de dados e esquemas
├── routers/        # Definição de rotas e endpoints
├── services/       # Lógica de negócio e serviços
├── utils/          # Utilitários e ferramentas auxiliares
└── views/          # Renderização de respostas e templates
```

Principais componentes:

1. **Rastreamento de Visitas**:
   - `VisitTracker` registra cada acesso aos endpoints
   - Armazena contagem total e horários de acesso

2. **Agendamento de Relatórios**:
   - `ReportScheduler` envia relatórios diários em horário configurável
   - Utiliza threads para operar em background

3. **Envio de E-mails**:
   - `EmailSender` fornece interface SMTP para envio
   - `EmailReporter` gera relatórios HTML formatados

4. **API REST**:
   - Rotas definidas via `Router` (wrapper para Blueprints do Flask)
   - Respostas padronizadas com `StandardResponse`

## 🛠 Ferramentas de Desenvolvimento

- **Formatação**: Black e isort para estilo de código consistente
- **Linting**: Flake8 para verificação de qualidade
- **Type Checking**: Mypy para verificação estática de tipos
- **Segurança**: Bandit para análise de vulnerabilidades
- **Pre-commit**: Hooks automatizados antes de cada commit

Para configurar os hooks de pre-commit:
```bash
pre-commit install
```

## 📬 Endpoints

- `GET /` - Endpoint principal que registra visitas e retorna mensagem de boas-vindas

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
