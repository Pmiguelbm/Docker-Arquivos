# 📋 Instruções de Uso - Sistema de Upload Django Docker

## 🚀 Início Rápido

### 1. Pré-requisitos
- Docker Desktop instalado e rodando
- Docker Compose disponível
- Pelo menos 2GB de RAM livre

### 2. Execução
```bash
# Windows
start.bat

# Linux/Mac
./start.sh
```

### 3. Acesso
- **Aplicação**: http://localhost
- **Admin Django**: http://localhost/admin

## 🏗️ Arquitetura do Sistema

### Containers
1. **web** (Django + Gunicorn)
   - Porta: 8000 (interno)
   - Framework: Django 4.2.7
   - WSGI: Gunicorn com configuração otimizada

2. **nginx** (Proxy Reverso)
   - Porta: 80 (externo)
   - Configuração de segurança
   - Cache para arquivos estáticos

3. **db** (PostgreSQL)
   - Porta: 5432
   - Configuração otimizada
   - Persistência via volume

### Volumes
- `postgres_data`: Dados do PostgreSQL
- `uploads_volume`: Arquivos enviados pelos usuários

## 📁 Estrutura de Arquivos

```
django-docker-app/
├── django_app/              # Projeto Django principal
├── file_upload/             # App de upload de arquivos
├── templates/               # Templates HTML
├── static/                  # Arquivos estáticos
├── Dockerfile               # Container Django
├── docker-compose.yml       # Orquestração
├── nginx.conf               # Configuração Nginx
├── gunicorn.conf.py         # Configuração Gunicorn
├── postgresql.conf          # Configuração PostgreSQL
├── requirements.txt         # Dependências Python
├── start.bat/start.sh       # Scripts de inicialização
├── run_tests.bat/run_tests.sh # Scripts de teste
├── backup.sh                # Script de backup
├── monitor.sh               # Script de monitoramento
└── README.md                # Documentação principal
```

## 🔧 Comandos Úteis

### Gerenciamento de Containers
```bash
# Iniciar todos os serviços
docker-compose up -d

# Parar todos os serviços
docker-compose down

# Ver logs em tempo real
docker-compose logs -f

# Ver logs de um serviço específico
docker-compose logs -f web
docker-compose logs -f nginx
docker-compose logs -f db

# Reiniciar um serviço
docker-compose restart web
```

### Comandos Django
```bash
# Executar migrações
docker-compose exec web python manage.py migrate

# Criar superusuário
docker-compose exec web python manage.py createsuperuser

# Coletar arquivos estáticos
docker-compose exec web python manage.py collectstatic

# Shell Django
docker-compose exec web python manage.py shell

# Backup do banco
docker-compose exec db pg_dump -U django_user django_db > backup.sql
```

### Monitoramento
```bash
# Ver status dos containers
docker-compose ps

# Ver uso de recursos
docker stats

# Executar script de monitoramento
./monitor.sh

# Executar backup
./backup.sh
```

## 🧪 Testes

### Executar Todos os Testes
```bash
# Linux/Mac
./run_tests.sh

# Windows
run_tests.bat
```

### Testes Individuais
```bash
# Testes unitários
docker-compose exec web python -m pytest file_upload/tests.py -v

# Testes com cobertura
docker-compose exec web python -m pytest --cov=file_upload

# Verificar qualidade do código
docker-compose exec web flake8 .
docker-compose exec web black --check .
docker-compose exec web isort --check-only .
```

## 🔒 Segurança

### Configurações Implementadas
- Headers de segurança no Nginx
- Validação de tipos de arquivo
- Limite de tamanho (50MB)
- CSRF protection
- Sanitização de nomes de arquivo
- Configuração segura do PostgreSQL

### Variáveis de Ambiente
Crie um arquivo `.env` na raiz:
```env
SECRET_KEY=sua-chave-secreta-muito-segura
DEBUG=False
POSTGRES_DB=django_db
POSTGRES_USER=django_user
POSTGRES_PASSWORD=django_password
```

## 📊 Monitoramento e Logs

### Logs Importantes
- **Django**: `docker-compose logs web`
- **Nginx**: `docker-compose logs nginx`
- **PostgreSQL**: `docker-compose logs db`

### Métricas
- Uso de CPU e memória: `docker stats`
- Status dos containers: `docker-compose ps`
- Health check: http://localhost/health/

## 🔄 Backup e Restore

### Backup Automático
```bash
./backup.sh
```

### Backup Manual
```bash
docker-compose exec db pg_dump -U django_user django_db > backup_$(date +%Y%m%d_%H%M%S).sql
```

### Restore
```bash
docker-compose exec -T db psql -U django_user django_db < backup.sql
```

## 🚨 Troubleshooting

### Problemas Comuns

1. **Porta 80 já em uso**
   ```bash
   # Verificar o que está usando a porta
   netstat -ano | findstr :80
   # Parar o serviço ou mudar a porta no docker-compose.yml
   ```

2. **Erro de permissão no PostgreSQL**
   ```bash
   # Reiniciar o container do banco
   docker-compose restart db
   ```

3. **Arquivos não aparecem**
   ```bash
   # Verificar se o volume está montado
   docker volume ls
   # Verificar permissões
   docker-compose exec web ls -la uploads/
   ```

4. **Erro de migração**
   ```bash
   # Resetar migrações
   docker-compose exec web python manage.py migrate --fake-initial
   ```

### Logs de Debug
```bash
# Ver logs detalhados
docker-compose logs -f --tail=100

# Ver logs de um serviço específico
docker-compose logs web --tail=50
```

## 📈 Performance

### Otimizações Implementadas
- Gunicorn com workers otimizados
- Nginx com cache de arquivos estáticos
- PostgreSQL com configurações de performance
- Compressão de arquivos estáticos
- Headers de cache apropriados

### Monitoramento de Performance
```bash
# Ver uso de recursos
docker stats

# Ver logs de performance
docker-compose logs web | grep "gunicorn"
```

## 🔄 Atualizações

### Atualizar Dependências
```bash
# Reconstruir containers
docker-compose build --no-cache

# Atualizar e reiniciar
docker-compose up -d --build
```

### Atualizar Código
```bash
# Parar containers
docker-compose down

# Fazer pull das mudanças
git pull

# Reconstruir e iniciar
docker-compose up -d --build
```

## 📞 Suporte

### Informações do Sistema
- **Versão Django**: 4.2.7
- **Versão Python**: 3.11
- **Versão PostgreSQL**: 15
- **Versão Nginx**: Alpine (latest)

### Contatos
- Documentação: README.md
- Issues: GitHub Issues
- Logs: `docker-compose logs`

---

**Nota**: Este sistema foi projetado para uso educacional e pode ser adaptado para produção com configurações adicionais de segurança.
