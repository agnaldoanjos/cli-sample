import argparse
import requests
import json
import sys
import os
import base64
from datetime import datetime

# Configurações
API_BASE_URL = "https://sua-api-backoffice.com/api"  # Altere para sua URL
AUTH_URL = "https://sua-api-auth.com/oauth/token"  # URL de autenticação


class LVSClient:
    def __init__(self):
        self.token = None
        self.token_expiration = None

    def get_basic_auth_header(self):
        """Gera header de autenticação Basic"""
        username = os.getenv('LVS_USERNAME')
        password = os.getenv('LVS_PASSWORD')

        if not username or not password:
            print("Erro: Configure as variáveis de ambiente LVS_USERNAME e LVS_PASSWORD")
            sys.exit(1)

        credentials = f"{username}:{password}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        return f"Basic {encoded_credentials}"

    def get_auth_token(self, scope="READ"):
        """Obtém token JWT da API de autenticação"""
        try:
            headers = {
                "Authorization": self.get_basic_auth_header(),
                "Content-Type": "application/x-www-form-urlencoded"
            }

            data = {
                "grant_type": "client_credentials",
                "scope": scope
            }

            response = requests.post(AUTH_URL, headers=headers, data=data)
            response.raise_for_status()

            auth_data = response.json()
            self.token = auth_data.get("access_token")
            self.token_expiration = auth_data.get("expirationDate")

            return auth_data

        except requests.exceptions.RequestException as e:
            print(f"Erro na autenticação: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Resposta da API: {e.response.text}")
            sys.exit(1)

    def ensure_token(self, scope="READ"):
        """Garante que temos um token válido"""
        if not self.token or self.is_token_expired():
            self.get_auth_token(scope)
        return self.token

    def is_token_expired(self):
        """Verifica se o token expirou"""
        if not self.token_expiration:
            return True

        try:
            expiration_date = datetime.fromisoformat(self.token_expiration.replace('Z', '+00:00'))
            return datetime.now(expiration_date.tzinfo) >= expiration_date
        except:
            return True

    def make_authenticated_request(self, method, endpoint, data=None, scope="READ", file_path=None):
        """Faz requisição autenticada para a API"""
        token = self.ensure_token(scope)

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        url = f"{API_BASE_URL}{endpoint}"

        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=headers)
            elif method.upper() == "POST":
                response = requests.post(url, headers=headers, json=data)
            elif method.upper() == "PUT":
                response = requests.put(url, headers=headers, json=data)
            elif method.upper() == "DELETE":
                response = requests.delete(url, headers=headers)
            else:
                print(f"Método HTTP não suportado: {method}")
                return None

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição {method} para {endpoint}: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Resposta da API: {e.response.text}")
            return None

    def echo_message(self, message):
        print(message)

    def create_business(self, json_file_path):
        """Cria um business a partir de arquivo JSON"""
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                business_data = json.load(f)
        except Exception as e:
            print(f"Erro ao ler arquivo JSON: {str(e)}")
            return False

        result = self.make_authenticated_request("POST", "/business", business_data, "WRITE")
        if result:
            print("Business criado com sucesso!")
            print(json.dumps(result, indent=2, ensure_ascii=False))
            return True
        return False

    def get_business(self, business_id, output_file=None):
        """Obtém um business específico"""
        result = self.make_authenticated_request("GET", f"/business/{business_id}")
        if result:
            if output_file:
                try:
                    with open(output_file, 'w', encoding='utf-8') as f:
                        json.dump(result, f, indent=2, ensure_ascii=False)
                    print(f"Business salvo em: {output_file}")
                except Exception as e:
                    print(f"Erro ao salvar arquivo: {str(e)}")
            else:
                print(json.dumps(result, indent=2, ensure_ascii=False))
            return True
        return False

    def update_business(self, business_id, json_file_path, method="PUT"):
        """Atualiza um business (PUT para substituição completa)"""
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                business_data = json.load(f)
        except Exception as e:
            print(f"Erro ao ler arquivo JSON: {str(e)}")
            return False

        endpoint = f"/business/{business_id}"
        result = self.make_authenticated_request(method, endpoint, business_data, "WRITE")
        if result:
            print(f"Business atualizado com sucesso usando {method}!")
            print(json.dumps(result, indent=2, ensure_ascii=False))
            return True
        return False

    def delete_business(self, business_id):
        """Deleta um business"""
        result = self.make_authenticated_request("DELETE", f"/business/{business_id}", scope="WRITE")
        if result is not None:
            print("Business deletado com sucesso!")
            return True
        return False

def show_auth_token(self):
    """Exibe o token de autenticação atual"""
    auth_data = self.get_auth_token()
    if auth_data:
        print("Token de autenticação:")
        print(f"Token: {auth_data.get('access_token')}")
        print(f"Tipo: {auth_data.get('tokenType', 'Bearer')}")
        print(f"Expiração: {auth_data.get('expirationDate')}")
        return True
    return False


def main():
    client = LVSClient()
    parser = argparse.ArgumentParser(description='LVS Client CLI')

    # Comandos principais
    parser.add_argument('-create', metavar='FILE', help='Criar business a partir de arquivo JSON')
    parser.add_argument('-get', metavar='ID', help='Obter business específico por ID')
    parser.add_argument('-put', nargs=2, metavar=('ID', 'FILE'), help='Atualizar business completo (PUT)')
    parser.add_argument('-post', nargs=2, metavar=('ID', 'FILE'), help='Atualizar business parcial (POST)')
    parser.add_argument('-delete', metavar='ID', help='Deletar business por ID')
    parser.add_argument('-auth', action='store_true', help='Exibir token de autenticação')

    # Opções adicionais
    parser.add_argument('-output', metavar='FILE', help='Arquivo de saída para o comando get')
    parser.add_argument('-scope', metavar='SCOPE', default='READ', help='Escopo para autenticação (READ/WRITE)')
    parser.add_argument('-echo', metavar='STRING', help='Exibe a string fornecida')

    args = parser.parse_args()

    if args.create:
        client.create_business(args.create)
    elif args.get:
        client.get_business(args.get, args.output)
    elif args.put:
        client.update_business(args.put[0], args.put[1], "PUT")
    elif args.post:
        client.update_business(args.post[0], args.post[1], "POST")
    elif args.delete:
        client.delete_business(args.delete)
    elif args.auth:
        client.show_auth_token()
    elif args.echo:
        client.echo_message(args.echo)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()