from PySide6.QtWidgets import QMessageBox
import requests
import json



def consulta(cnpj):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    querrystring = {"tokem":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"0690590000123","plugin":"RF"}  
    
    try:
        response = requests.request("GET",url,params=querrystring)
        r = json.loads(response.text)
        return r['nome'],r['logradouro'],r['numero'],r['complemento'],r['bairro'],r['municipio'],r['uf'],r['cep'],r['telefone'],r['email']
    except:
        msg = QMessageBox()
        msg.setWindowTitle("Erro de CNPJ")
        msg.setText("Digite o CNPJ sem os espaços e caracteres especiais")
        msg.exec()
        return "erro"
        
    

