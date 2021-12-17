import requests
import json



def consulta(cnpj):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    querrystring = {"tokem":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"0690590000123","plugin":"RF"}  
    response = requests.request("GET",url,params=querrystring)

    r = json.loads(response.text)

    return r['nome'],r['logradouro'],r['numero'],r['complemento'],r['bairro'],r['municipio'],r['uf'],r['cep'],r['telefone'],r['email']

        
    

