# LVS CLI - Cliente para API de Business

## 📋 Descrição do Projeto

Este projeto é uma Interface de Linha de Comando (CLI) em Python para interagir com APIs de business. A CLI fornece operações completas de CRUD (Create, Read, Update, Delete) com autenticação JWT via OAuth2. Funciona tanto no Windows (CMD/PowerShell) quanto em shells Unix (bash).

**Funcionalidades Principais:**
- Autenticação OAuth2 com Basic Auth + JWT
- Operações CRUD completas (Create, Get, Update, Delete)
- Gerenciamento automático de tokens
- Suporte a escopos (READ/WRITE)
- Processamento de arquivos JSON
- Compatibilidade multiplataforma

## 🎯 Casos de Uso

A CLI `lvs` foi projetada para:
- **Gestão de dados empresariais** via API
- **Automação de processos** de negócio
- **Integração com sistemas** BackOffice
- **Scripts de administração** e deploy
- **Migração e backup** de dados
- **Desenvolvimento e testes** de APIs

## 🚀 Instalação Rápida

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git (para clonar o repositório)

### Método 1: Instalação via pip (Recomendado)

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd python-cli

# Crie e ative um ambiente virtual
python -m venv .venv

# Windows (PowerShell)
.\.venv\Scripts\activate

# Windows (CMD)
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

# Instale o pacote em modo desenvolvimento
pip install -e .
```

### Método 2: Instalação Direta

```bash
# Instale diretamente do repositório
pip install git+<url-do-repositorio>
```

## ⚙️ Configuração

### Variáveis de Ambiente

Configure as credenciais de API:

**Windows (PowerShell):**
```powershell
[Environment]::SetEnvironmentVariable("LVS_USERNAME", "seu_usuario", "User")
[Environment]::SetEnvironmentVariable("LVS_PASSWORD", "sua_senha", "User")
```

**Windows (CMD):**
```cmd
setx LVS_USERNAME "seu_usuario"
setx LVS_PASSWORD "sua_senha"
```

**Linux/macOS:**
```bash
echo 'export LVS_USERNAME="seu_usuario"' >> ~/.bashrc
echo 'export LVS_PASSWORD="sua_senha"' >> ~/.bashrc
source ~/.bashrc
```

## 💻 Uso da CLI

### Comandos Disponíveis

#### 1. Autenticação
```bash
# Exibir token JWT atual
lvs -auth

# Com escopo específico
lvs -auth -scope WRITE
```

#### 2. Operações CRUD

**Criar Business:**
```bash
lvs -create business.json
```

**Obter Business:**
```bash
# Exibir na console
lvs -get 123

# Salvar em arquivo
lvs -get 123 -output business.json
lvs -get 123 > business.json
```

**Atualizar Business (PUT - substituição completa):**
```bash
lvs -put 123 business_updated.json
```

**Atualizar Business (POST - atualização parcial):**
```bash
lvs -post 123 business_partial_update.json
```

**Deletar Business:**
```bash
lvs -delete 123
```

### Exemplo de Arquivo business.json
```json
{
  "id": "123",
  "name": "Minha Empresa LTDA",
  "type": "Tecnologia",
  "status": "ACTIVE",
  "address": {
    "street": "Rua Exemplo",
    "number": "123",
    "city": "São Paulo",
    "state": "SP"
  },
  "contact": {
    "email": "contato@empresa.com",
    "phone": "+5511999999999"
  },
  "metadata": {
    "createdAt": "2024-01-01T00:00:00Z",
    "updatedAt": "2024-01-01T00:00:00Z"
  }
}
```

### Obter Ajuda
```bash
lvs --help
```

**Saída:**
```
usage: lvs [-h] [-create FILE] [-get ID] [-put ID FILE] [-post ID FILE] 
           [-delete ID] [-auth] [-output FILE] [-scope SCOPE]

LVS Client CLI

optional arguments:
  -h, --help       show this help message and exit
  -create FILE     Criar business a partir de arquivo JSON
  -get ID          Obter business específico por ID
  -put ID FILE     Atualizar business completo (PUT)
  -post ID FILE    Atualizar business parcial (POST)
  -delete ID       Deletar business por ID
  -auth            Exibir token de autenticação
  -output FILE     Arquivo de saída para o comando get
  -scope SCOPE     Escopo para autenticação (READ/WRITE)
```

## 🔧 Funcionamento Interno

### Fluxo de Autenticação
1. **Basic Auth** → Credenciais das variáveis de ambiente
2. **Token JWT** → Obtido via OAuth2 com scope específico
3. **Bearer Token** → Usado para requisições à API BackOffice
4. **Renovação Automática** → Token é renovado quando expirado

### Estrutura do Projeto
```
python-cli/
├── lvs.py              # Código principal da CLI
├── setup.py            # Configuração de instalação
├── requirements.txt    # Dependências do projeto
├── README.md           # Este arquivo
└── examples/           # Exemplos de uso
    ├── business.json           # Exemplo completo
    ├── business_create.json    # Para criação
    └── business_update.json    # Para atualização
```

## 🔐 Segurança

- **Autenticação OAuth2** com fluxo Client Credentials
- **Tokens JWT** com expiração controlada
- **Credenciais seguras** em variáveis de ambiente
- **Escopos de acesso** (READ/WRITE) para controle granular
- **HTTPS obrigatório** para todas as comunicações

## 🐛 Solução de Problemas

### Problema: Comando 'lvs' não encontrado
**Solução:**
```bash
# Reinstale o pacote
pip uninstall lvs-cli
pip install -e .

# Ou execute diretamente
python lvs.py -get 123
```

### Problema: Erro de autenticação
**Solução:**
```bash
# Verifique variáveis de ambiente
echo $LVS_USERNAME  # Linux/macOS
echo %LVS_USERNAME% # Windows CMD
$env:LVS_USERNAME   # Windows PowerShell

# Teste a autenticação
lvs -auth
```

### Problema: Token expirado
**Solução:**
```bash
# A renovação é automática, mas force uma nova autenticação
lvs -auth -scope WRITE
```

### Problema: Erro de módulo não encontrado
**Solução:**
```bash
# Instale dependências manualmente
pip install requests
```

## 🔄 Desenvolvimento

### Adicionar Novos Comandos
1. Edite `lvs.py` e adicione nova função na classe `LVSClient`
2. Adicione parser argument em `main()`
3. Atualize `setup.py` se necessário
4. Reinstale: `pip install -e .`

### Exemplo: Adicionar comando 'list'
```python
def list_businesses(self, filters=None):
    """Lista todos os businesses com filtros opcionais"""
    endpoint = "/businesses"
    if filters:
        endpoint += f"?{filters}"
    return self.make_authenticated_request("GET", endpoint)

# No main():
parser.add_argument('-list', action='store_true', help='Lista todos os businesses')
```

## 🌐 Compatibilidade

### Sistemas Operacionais Testados
- ✅ Windows 10/11 (CMD, PowerShell)
- ✅ Linux (Ubuntu, CentOS, Debian)
- ✅ macOS (bash, zsh)

### Shells Suportados
- Windows Command Prompt (CMD)
- Windows PowerShell
- Bash
- Zsh
- Fish

## 📦 Distribuição

### Empacotamento para PyPI
```bash
# Instale ferramentas de build
pip install build twine

# Crie distribuição
python -m build

# Upload para PyPI
twine upload dist/*
```

### Instalação por Terceiros
```bash
pip install lvs-cli
```

## 🚦 Próximos Passos

1. [ ] Adicionar comando `list` para listagem com filtros
2. [ ] Implementar paginação para grandes conjuntos de dados
3. [ ] Adicionar suporte a configurações via arquivo YAML
4. [ ] Criar testes automatizados completos
5. [ ] Adicionar autocompletion para shells
6. [ ] Implementar modo verbose para debug
7. [ ] Adicionar suporte a múltiplos ambientes (dev, staging, prod)

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

---

**💡 Dica Profissional:** Use aliases para comandos frequentes:

```bash
# No .bashrc ou $PROFILE
alias lvs-get='lvs -get'
alias lvs-auth='lvs -auth'
alias lvs-create='lvs -create'

# Exemplo de uso rápido:
lvs-get 123 > business_123.json
```

**📞 Suporte:** Para issues e dúvidas, abra uma issue no repositório do projeto.