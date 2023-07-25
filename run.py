import requests
import pandas as pd
import json

edificios = pd.read_csv('data/edificios.csv', sep='|')
for i in edificios.index:
    tipo = edificios['tipo'][i]
    diccionarioE = {
        'nombre' : edificios['nombre'][i],
        'direccion' : edificios['dirección'][i],
        'ciudad' : edificios['ciudad'][i],
        'tipo' : tipo.lower(),
    }

    rEdificios = requests.post("http://127.0.0.1:8000/api/edificios/",
        auth=('frantgod', '07102002'), json=diccionarioE)
    print(rEdificios.text)


propietarios = pd.read_csv('data/propietarios.csv', sep='|')
for i in propietarios.index:
    diccionarioP = {
        'cedula' : str(propietarios['cedula'][i]),
        'nombre' : propietarios['nombre'][i],
        'apellido' : propietarios['apellido'][i],
    }

    rPropietarios = requests.post("http://127.0.0.1:8000/api/propietarios/",
        auth=('frantgod', '07102002'), json=diccionarioP)
    print(rPropietarios.text)


departamentos = pd.read_csv('data/departamentos.csv', sep='|')

# Todos los Propietarios
rP = requests.get("http://127.0.0.1:8000/api/propietarios/", auth=('frantgod', '07102002'))
propietariosD = json.loads(rP.content)['results']

# Todos los Edificios
rE = requests.get("http://127.0.0.1:8000/api/edificios/", auth=('frantgod', '07102002'))
rE2 = requests.get("http://127.0.0.1:8000/api/edificios/?page=2", auth=('frantgod', '07102002'))
edificiosD = json.loads(rE.content)['results'] + json.loads(rE2.content)['results']

for i in departamentos.index:
    for p in propietariosD:
        if str(departamentos['Propietario'][i]) == p['cedula']:
            propietario = p['url']

    for e in edificiosD:
        if departamentos['Edificio'][i] == e['nombre']:
            edificio = e['url']

    diccionarioD = {
        'propietario' : propietario,
        'edificio' : edificio,
        'costo' :  int(departamentos['Costo'][i]),
        'nro_cuartos' : int(departamentos['Cuartos'][i]),
    }

    rDepartamentos = requests.post("http://127.0.0.1:8000/api/departamentos/",
        auth=('frantgod', '07102002'), json=diccionarioD)
    print(rDepartamentos.text)