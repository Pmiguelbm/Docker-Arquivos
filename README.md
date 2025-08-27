# Sistema de Upload de Arquivos com Django e Docker

Este projeto implementa um sistema completo de upload de arquivos usando Django, Docker e PostgreSQL, com as seguintes características:

## 🏗️ Arquitetura

- **Container Django**: Aplicação Django com Gunicorn
- **Container Nginx**: Proxy reverso para servir a aplicação
- **Container PostgreSQL**: Banco de dados para persistência
- **Volumes Docker**: Para persistir dados e uploads

## 🚀 Funcionalidades

- ✅ Upload de arquivos com drag & drop
- ✅ Interface moderna e responsiva
- ✅ Listagem de arquivos enviados
- ✅ Download de arquivos
- ✅ Exclusão de arquivos
- ✅ Validação de tipos e tamanhos
- ✅ Persistência em volumes Docker
- ✅ API REST para uploads

## 📋 Pré-requisitos

- Docker
- Docker Compose

## 🛠️ Instalação e Execução

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd django-docker-app
```

2. **Execute com Docker Compose:**
```bash
docker-compose up --build
```

3. **Acesse a aplicação:**
- URL: http://localhost
- Admin: http://localhost/admin

## 🔧 Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# Django Settings
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=False

# Database Settings
POSTGRES_DB=django_db
POSTGRES_USER=django_user
POSTGRES_PASSWORD=django_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

### Portas Utilizadas

- **80**: Nginx (proxy reverso)
- **8000**: Django (desenvolvimento)
- **5432**: PostgreSQL

## 📁 Estrutura do Projeto

```
django-docker-app/
├── django_app/                 # Projeto Django principal
│   ├── settings.py            # Configurações
│   ├── urls.py                # URLs principais
│   └── wsgi.py                # WSGI application
├── file_upload/               # App de upload
│   ├── models.py              # Modelo UploadedFile
│   ├── views.py               # Views da aplicação
│   ├── forms.py               # Formulários
│   └── urls.py                # URLs do app
├── templates/                 # Templates HTML
├── static/                    # Arquivos estáticos
├── requirements.txt           # Dependências Python
├── Dockerfile                 # Container Django
├── docker-compose.yml         # Orquestração
├── nginx.conf                 # Configuração Nginx
└── README.md                  # Este arquivo
```

## 🗄️ Banco de Dados

O PostgreSQL é configurado automaticamente com:
- **Database**: django_db
- **User**: django_user
- **Password**: django_password

## 📤 Upload de Arquivos

### Tipos Suportados
- Documentos: .txt, .pdf, .doc, .docx
- Imagens: .jpg, .jpeg, .png, .gif
- Arquivos compactados: .zip, .rar

### Limites
- Tamanho máximo: 50MB por arquivo
- Armazenamento: Volume Docker persistente

## 🔒 Segurança

- Validação de tipos de arquivo
- Limite de tamanho
- CSRF protection
- Sanitização de nomes de arquivo

## 🐳 Comandos Docker Úteis

```bash
# Construir e iniciar
docker-compose up --build

# Executar em background
docker-compose up -d

# Parar serviços
docker-compose down

# Ver logs
docker-compose logs -f

# Executar comandos Django
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

# Acessar shell do container
docker-compose exec web bash
```

## 🧪 Desenvolvimento

Para desenvolvimento local:

1. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

2. **Configurar banco:**
```bash
python manage.py migrate
python manage.py createsuperuser
```

3. **Executar servidor:**
```bash
python manage.py runserver
```

## 📝 Licença

Este projeto é de uso educacional.
