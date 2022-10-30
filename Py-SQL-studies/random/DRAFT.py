import requests

from decimal import Decimal

URL_BRASIL = "https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json"

ESTADOS = [
    "AC",
    "AL",
    "AP",
    "AM",
    "BA",
    "CE",
    "ES",
    "GO",
    "MA",
    "MT",
    "MS",
    "MG",
    "PA",
    "PB",
    "PR",
    "PE",
    "PI",
    "RJ",
    "RN",
    "RS",
    "RO",
    "RR",
    "SC",
    "SP",
    "SE",
    "TO",
    "DF",
]


retornar_url_por_uf = (
    lambda estado: f"https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/{estado}/{estado}-c0001-e000545-r.json"
)

resultados_por_estado = {}

for estado in ESTADOS:
    sigla_estado = estado.lower()

    request = requests.get(retornar_url_por_uf(sigla_estado))

    if request.status_code == 200:
        json = request.json()
        resultados_por_estado[sigla_estado] = json.get("pst").replace(",", ".")

resultados_ordenados = sorted(
    resultados_por_estado.values(),
    key=lambda v: Decimal(v),
    reverse=True,
)

resultado_final = {}

for resultado in resultados_ordenados:
    for estado, percentual in resultados_por_estado.items():
        if resultado == percentual:
            resultado_final[estado] = resultado


for indice, estado in enumerate(resultado_final.keys()):
    percentual = resultado_final.get(estado)
    print(f"{indice}: {estado.upper()}: {percentual}%")
    