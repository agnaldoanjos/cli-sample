# Exemplo de Projeto CLI em Python

## 📋 Descrição do Projeto

Este projeto é um exemplo prático de como criar uma Interface de Linha de Comando (CLI) em Python que funciona tanto no Windows (CMD/PowerShell) quanto em shells Unix (bash). A CLI demonstra conceitos essenciais como:

- Autenticação JWT com APIs
- Processamento de arquivos JSON
- Criação de comandos personalizados
- Gerenciamento de dependências
- Distribuição via pip

## 🎯 Casos de Uso Exemplo

A CLI `lvs` foi projetada para:
- **Automação de processos** empresariais
- **Integração com APIs** RESTful
- **Processamento batch** de dados JSON
- **Ferramentas de desenvolvimento** internas
- **Scripts de deploy** e administração

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

#### 1. Comando Echo (Teste)
```bash
# Teste básico da CLI
lvs -echo "Hello World"

# Saída esperada:
# Hello World
```

#### 2. Criar Business via JSON
```bash
# Cria um business a partir de arquivo JSON
lvs -create business.json
```

### Exemplo de Arquivo business.json
```json
{
  "name": "Minha Empresa LTDA",
  "type": "Tecnologia",
  "address": {
    "street": "Rua Exemplo",
    "number": "123",
    "city": "São Paulo",
    "state": "SP"
  },
  "contact": {
    "email": "contato@empresa.com",
    "phone": "+5511999999999"
  }
}
```

### Obter Ajuda
```bash
lvs --help
```

**Saída:**
```
usage: lvs [-h] [-create FILE] [-echo STRING]

LVS Client CLI

optional arguments:
  -h, --help     show this help message and exit
  -create FILE   Criar business a partir de arquivo JSON
  -echo STRING   Exibe a string fornecida
```

## 🔧 Funcionamento Interno

### Fluxo de Autenticação
1. **Recupera credenciais** das variáveis de ambiente
2. **Obtém token JWT** da API de autenticação
3. **Valida token** antes das requisições
4. **Envia dados** para o endpoint de business

### Estrutura do Projeto
```
python-cli/
├── lvs.py              # Código principal da CLI
├── setup.py            # Configuração de instalação
├── requirements.txt    # Dependências do projeto
├── README.md           # Este arquivo
└── examples/           # Exemplos de uso
    └── business.json   # Exemplo de JSON
```

## 🐛 Solução de Problemas

### Problema: Comando 'lvs' não encontrado
**Solução:**
```bash
# Reinstale o pacote
pip uninstall lvs-cli
pip install -e .

# Ou execute diretamente
python lvs.py -echo "Teste"
```

### Problema: Erro de autenticação
**Solução:**
```bash
# Verifique variáveis de ambiente
echo $LVS_USERNAME  # Linux/macOS
echo %LVS_USERNAME% # Windows CMD
$env:LVS_USERNAME   # Windows PowerShell
```

### Problema: Erro de módulo não encontrado
**Solução:**
```bash
# Instale dependências manualmente
pip install requests
```

## 🔄 Desenvolvimento

### Adicionar Novos Comandos
1. Edite `lvs.py` e adicione nova função
2. Adicione parser argument em `main()`
3. Atualize `setup.py` se necessário
4. Reinstale: `pip install -e .`

### Exemplo: Adicionar comando 'status'
```python
def check_status():
    print("Sistema operacional normalmente")

# No main():
parser.add_argument('-status', action='store_true', help='Verifica status do sistema')
```

## 🌐 Compatibilidade

### Sistemas Operacionais Testados
- ✅ Windows 10/11 (CMD, PowerShell)
- ✅ Linux (Ubuntu, CentOS)
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

## 🔒 Segurança

- Credenciais armazenadas em variáveis de ambiente
- Tokens JWT com expiração
- Validação de entrada de dados
- Conexões HTTPS com APIs

## 📝 Próximos Passos

1. [ ] Adicionar mais comandos (list, delete, update)
2. [ ] Implementar logs detalhados
3. [ ] Adicionar suporte a configurações via arquivo YAML
4. [ ] Criar testes automatizados
5. [ ] Adicionar autocompletion para shells

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.
