import requests
import json

data = {'primer_numero': '11','segundo_numero': '06','tercer_numero': '10','cuarto_numero': '15','quinto_numero': '20','sexto_numero': '38','lotto_mas': '06','super_lotto': '09','fecha_sorteo': '2019-12-10'}

url = "http://glottopool.pythonanywhere.com/add_lotto"
#data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
res = requests.post(url, data=json.dumps(data), headers=headers)

print(str(res))

