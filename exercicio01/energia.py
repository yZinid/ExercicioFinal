TARIFA_KWH = 0.28172

FATOR_ICMS_ATE_200 = 0.136363
FATOR_ICMS_ACIMA_200 = 0.333333

FATOR_COFINS_ATE_200 = 0.0614722 
FATOR_COFINS_ACIMA_200 = 0.0730751

FATOR_PIS_PASEP_ATE_200 = 0.013346
FATOR_PIS_PASEP_ACIMA_200 = 0.0158651

def calcular_fornecimento(consumo_kWh):
    return consumo_kWh * TARIFA_KWH

def calcular_icms(consumo_kWh):
    fornecimento = calcular_fornecimento(consumo_kWh)
    if consumo_kWh <= 200:
        fator_icms = FATOR_ICMS_ATE_200 
    else:
        fator_icms = FATOR_ICMS_ACIMA_200 
    icms = fator_icms * fornecimento
    return icms

def calcular_cofins(consumo_kWh):
    fornecimento = calcular_fornecimento(consumo_kWh)
    if consumo_kWh <= 200:
        fator_cofins = FATOR_COFINS_ATE_200 
    else:
        fator_cofins = FATOR_COFINS_ACIMA_200 
    cofins = fator_cofins * fornecimento
    return cofins


def calcular_pis_pasep(consumo_kWh):
    fornecimento = calcular_fornecimento(consumo_kWh)
    if consumo_kWh <= 200:
        fator_pis_pasep = FATOR_PIS_PASEP_ATE_200 
    else:
        fator_pis_pasep = FATOR_PIS_PASEP_ACIMA_200 
    pis_pasep = fator_pis_pasep * fornecimento
    return pis_pasep


def calcular_icms_cofins(consumo_kWh):
    fornecimento = calcular_fornecimento(consumo_kWh)
    if consumo_kWh <= 200:
        fator_icms = FATOR_ICMS_ATE_200
        fator_cofins = FATOR_COFINS_ATE_200
    else:
        fator_icms = FATOR_ICMS_ACIMA_200
        fator_cofins = FATOR_COFINS_ACIMA_200
    return fator_cofins * fator_icms * fornecimento


def calcular_icms_pis_pasep(consumo_kWh):
    fornecimento = calcular_fornecimento(consumo_kWh)
    if consumo_kWh <= 200:
        fator_icms = FATOR_ICMS_ATE_200
        fator_pis_pasep = FATOR_PIS_PASEP_ATE_200
    else:
        fator_icms = FATOR_ICMS_ACIMA_200
        fator_pis_pasep = FATOR_PIS_PASEP_ACIMA_200
    return fator_pis_pasep * fator_icms * fornecimento


def calcular_fatura(consumo_kWh):
    fornecimento = calcular_fornecimento(consumo_kWh)
    icms = calcular_icms(consumo_kWh)
    cofins = calcular_cofins(consumo_kWh)
    pis_pasep = calcular_pis_pasep(consumo_kWh)
    icms_cofins = calcular_icms_cofins(consumo_kWh)
    icms_pis_pasep = calcular_icms_pis_pasep(consumo_kWh)

    fatura_total = (fornecimento + icms + cofins + pis_pasep + icms_cofins + icms_pis_pasep)
    return fatura_total
