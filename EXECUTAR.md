# 🚀 Como Executar - Sistema Django Docker

## ⚡ Execução Rápida (2 minutos)

### 1. Pré-requisitos
- Docker Desktop instalado e rodando
- Pelo menos 2GB de RAM livre

### 2. Executar
```bash
# Windows
start.bat

# Linux/Mac
./start.sh
```

### 3. Acessar
- **Aplicação**: http://localhost
- **Admin**: http://localhost/admin

## 📋 O que foi criado

### Containers
- 🐳 **Django + Gunicorn** (porta 8000)
- 🌐 **Nginx** (porta 80) - Proxy reverso
- 🗄️ **PostgreSQL** (porta 5432) - Banco de dados

### Funcionalidades
- 📤 Upload de arquivos com drag & drop
- 📋 Listagem de arquivos enviados
- 💾 Download de arquivos
- 🗑️ Exclusão de arquivos
- 🔒 Validação de segurança

### Volumes (Persistência)
- `postgres_data`: Dados do banco
- `uploads_volume`: Arquivos enviados

## 🎯 Teste Rápido

1. Acesse http://localhost
2. Arraste um arquivo para a área de upload
3. Adicione uma descrição (opcional)
4. Clique em "Enviar Arquivo"
5. Veja o arquivo na lista à direita

## 🛠️ Comandos Úteis

```bash
# Ver status
docker-compose ps

# Ver logs
docker-compose logs -f

# Parar tudo
docker-compose down

# Reiniciar
docker-compose restart
```

## 📚 Documentação Completa

- **README.md**: Documentação principal
- **INSTRUCOES.md**: Instruções detalhadas
- **RESUMO.md**: Resumo executivo

## 🆘 Problemas Comuns

### Porta 80 em uso
```bash
# Verificar
netstat -ano | findstr :80

# Parar serviço ou mudar porta no docker-compose.yml
```

### Erro de permissão
```bash
# Reiniciar containers
docker-compose restart
```

### Arquivos não aparecem
```bash
# Verificar volumes
docker volume ls
```

## ✅ Sucesso!

Se você conseguiu acessar http://localhost e ver a interface de upload, o sistema está funcionando perfeitamente!

---

**Desenvolvido para a Atividade com Nota #1 - Docker Django**
