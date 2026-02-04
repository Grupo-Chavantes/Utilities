# Mapping from DESPESA CÓDIGO to Class.Fornecedor
DESPESA_CODIGO_TO_CLASS_FORNECEDOR = {
    5329: "55||56", # MOVEIS E EQUIPAMENTOS
    5330: "57||58", # OBRA
    5202: "", # JUROS/MULTAS PASSIVAS
    4191: "", # TRIBUTOS E OBRIGAÇÕES FISCAIS / DESPESAS BANCARIAS / TARIFAS
    5351: "", # IR SOBRE RESGATES
    5352: "", # IOF SOBRE RESGATES
    5281: "", # SALARIOS
    5331: "", # VALE TRANSPORTE
    5284: "", # FGTS
    5363: "", # FERIAS
    5364: "", # VERBAS RESCISORIAS
    5332: "", # VALE ALIMENTAÇÃO
    5365: 60, # MEDICINA DO TRABALHO
    5366: 47, # RELOGIO DE PONTO
    5289: 30, # MANUTENÇÃO GERADOR
    5290: "15||35", # SERVIÇO DE MANUTENÇÃO PREVENTIVA E CORRETIVA DE EQUIPAMENTOS MÉDICOS E HOSPITALARES /ENGENHARIA CLÍN
    5291: 59, # SERVIÇOS DE EXAMES LABORATORIAIS
    5292: "24||29||41", # SISTEMA DE GERENCIAMENTO E INFORMAÇÃO INTEGRADO / SOFTWARE DE GESTÃO / MONITORAMENTO / LOCAÇÃO DE EQ
    5293: 31, # SERVIÇO DE REMOÇÃO
    5294: 23, # SERVIÇOS DE IMAGEM DIAGNÓSTICO RX/TOMO/RESSONÂNCIA/MAMA
    5295: "1||40||43", # SERVIÇOS DE SEGURANÇA
    5296: 22, # SERVIÇOS DE LIMPEZA
    5297: 26, # SERVIÇO DE LAVANDERIA
    5298: "34||35", # SERVIÇO DE MANUTENÇÃO PREVENTIVA PREDIAL
    5299: 2, # NUTRIÇÃO E DIETÉTICA ALIMENTAÇÃO DE FUNCIONÁRIOS E PACIENTES
    5300: 16, # ESTERILIZAÇÃO DE MATERIAIS
    5301: 64, # UNIFORMES E CRACHÁS DE FUNCIONÁRIOS
    5345: 38, # OUTROS SERVIÇOS DE TERCEIROS
    5303: "14||54||62", # MATERIAL DE CAMPANHAS E INDENTIDADE VISUAL USO PERMANENTE
    5304: 53, # MATERIAIS MÉDICOS / DE ENFERMAGEM / EPI USO INTERNO (UTILIZÁVEL)
    5305: "50||51||52", # MATERIAL DE EXPEDIENTE
    5306: 48, # MEDICAMENTOS DE USO INTERNO (UTILIZÁVEL)
    5307: 19, # GASES MEDICINAIS
    5309: "64||65", # SEGUROS
    5310: 33, # TELEFONIA
    5311: "", # AGUA
    5312: 24, # INTERNET
    5313: "", # ENERGIA ELETRICA
    5342: "", # CENTRO DE SERVIÇOS INTEGRADOS - CSI
    5367: 64, # PAGAMENTOS EXTRAORDINARIOS/ESTORNOS
    5322: "3||36", # SERVIÇOS MEDICOS
    5323: 4, # COORDENAÇÃO ADM
    5324: 4, # COORDENAÇÃO DE FARMACIA
    5325: 4, # COORDENAÇÃO DE ENFERMAGEM
    5326: 13, # SUPERVISÃO DE ENFERMAGEM
    5327: 13, # DIRETOR MEDICO
    5335: 13 # SUPERVISÃO ADM
}


# Mapping from DESPESA CÓDIGO to Tipo Fornecedor
DESPESA_CODIGO_TO_TIPO_FORNECEDOR = {
    5329: 2, # MOVEIS E EQUIPAMENTOS > Fornecedor Materiais
    5330: "1||2", # OBRA
    5202: "", # JUROS/MULTAS PASSIVAS
    4191: "", # TRIBUTOS E OBRIGAÇÕES FISCAIS / DESPESAS BANCARIAS / TARIFAS
    5351: "", # IR SOBRE RESGATES
    5352: "", # IOF SOBRE RESGATES
    5281: "", # SALARIOS
    5331: "", # VALE TRANSPORTE
    5284: "", # FGTS
    5363: "", # FERIAS
    5364: "", # VERBAS RESCISORIAS
    5332: "", # VALE ALIMENTAÇÃO
    5365: 3, # MEDICINA DO TRABALHO > Fornecedor Médicos
    5366: 1, # RELOGIO DE PONTO > Fornecedor Serviços
    5289: 1, # MANUTENÇÃO GERADOR > Fornecedor Serviços
    5290: 1, # SERVIÇO DE MANUTENÇÃO PREVENTIVA E CORRETIVA DE EQUIPAMENTOS MÉDICOS E HOSPITALARES /ENGENHARIA CLÍN > Fornecedor Serviços
    5291: 1, # SERVIÇOS DE EXAMES LABORATORIAIS > Fornecedor Serviços
    5292: 1, # SISTEMA DE GERENCIAMENTO E INFORMAÇÃO INTEGRADO / SOFTWARE DE GESTÃO / MONITORAMENTO / LOCAÇÃO DE EQ > Fornecedor Serviços
    5293: 1, # SERVIÇO DE REMOÇÃO > Fornecedor Serviços
    5294: 1, # SERVIÇOS DE IMAGEM DIAGNÓSTICO RX/TOMO/RESSONÂNCIA/MAMA > Fornecedor Serviços
    5295: 1, # SERVIÇOS DE SEGURANÇA > Fornecedor Serviços
    5296: 1, # SERVIÇOS DE LIMPEZA > Fornecedor Serviços
    5297: 1, # SERVIÇO DE LAVANDERIA > Fornecedor Serviços
    5298: 1, # SERVIÇO DE MANUTENÇÃO PREVENTIVA PREDIAL > Fornecedor Serviços
    5299: 1, # NUTRIÇÃO E DIETÉTICA ALIMENTAÇÃO DE FUNCIONÁRIOS E PACIENTES > Fornecedor Serviços
    5300: 1, # ESTERILIZAÇÃO DE MATERIAIS > Fornecedor Serviços
    5301: 1, # UNIFORMES E CRACHÁS DE FUNCIONÁRIOS > Fornecedor Serviços
    5345: 1, # OUTROS SERVIÇOS DE TERCEIROS > Fornecedor Serviços
    5303: 2, # MATERIAL DE CAMPANHAS E INDENTIDADE VISUAL USO PERMANENTE > Fornecedor Materiais
    5304: 2, # MATERIAIS MÉDICOS / DE ENFERMAGEM / EPI USO INTERNO (UTILIZÁVEL) > Fornecedor Materiais
    5305: 2, # MATERIAL DE EXPEDIENTE > Fornecedor Materiais
    5306: 2, # MEDICAMENTOS DE USO INTERNO (UTILIZÁVEL) > Fornecedor Materiais
    5307: 2, # GASES MEDICINAIS > Fornecedor Materiais
    5309: 1, # SEGUROS > Fornecedor Serviços
    5310: 1, # TELEFONIA > Fornecedor Serviços
    5311: "", # AGUA > Fornecedor Serviços
    5312: 1, # INTERNET > Fornecedor Serviços
    5313: "", # ENERGIA ELETRICA > Fornecedor Serviços
    5342: "", # CENTRO DE SERVIÇOS INTEGRADOS
    5367: "1||2||3", # PAGAMENTOS EXTRAORDINARIOS/ESTORNOS
    5322: 3, # SERVIÇOS MEDICOS > Fornecedor Médicos
    5323: 1, # COORDENAÇÃO ADM > Fornecedor Serviços
    5324: 1, # COORDENAÇÃO DE FARMACIA > Fornecedor Serviços
    5325: 1, # COORDENAÇÃO DE ENFERMAGEM > Fornecedor Serviços
    5326: 1, # SUPERVISÃO DE ENFERMAGEM > Fornecedor Serviços
    5327: 1, # DIRETOR MEDICO > Fornecedor Serviços
    5335: 1 # SUPERVISÃO ADM > Fornecedor Serviços
}


# Mapping from Cod. Historico to DocTipo
COD_HISTORICO_TO_DOCTIPO = {
    2: 1,  # Cheque
    5: 1,  # Cheque
    6: 1,  # Cheque
    33: 1,  # Cheque
    53: 1,  # Cheque
    102: 1,  # Cheque
    103: 1,  # Cheque
    106: 1,  # Cheque
    113: 1,  # Cheque
    114: 1,  # Cheque
    153: 1,  # Cheque
    185: 1,  # Cheque
    243: 1,  # Cheque
    274: 1,  # Cheque
    312: 1,  # Cheque
    326: 1,  # Cheque
    408: 1,  # Cheque
    452: 1,  # Cheque
    453: 1,  # Cheque
    456: 1,  # Cheque
    457: 1,  # Cheque
    458: 1,  # Cheque
    598: 1,  # Cheque
    603: 1,  # Cheque
    618: 1,  # Cheque
    653: 1,  # Cheque
    813: 1,  # Cheque
    410: 2,  # Depósito
    411: 2,  # Depósito
    482: 2,  # Depósito
    502: 2,  # Depósito
    503: 2,  # Depósito
    505: 2,  # Depósito
    506: 2,  # Depósito
    510: 2,  # Depósito
    511: 2,  # Depósito
    512: 2,  # Depósito
    513: 2,  # Depósito
    514: 2,  # Depósito
    515: 2,  # Depósito
    516: 2,  # Depósito
    517: 2,  # Depósito
    518: 2,  # Depósito
    519: 2,  # Depósito
    520: 2,  # Depósito
    530: 2,  # Depósito
    605: 2,  # Depósito
    606: 2,  # Depósito
    613: 2,  # Depósito
    623: 2,  # Depósito
    631: 2,  # Depósito
    830: 2,  # Depósito
    910: 2,  # Depósito
    911: 2,  # Depósito
    912: 2,  # Depósito
    913: 2,  # Depósito
    914: 2,  # Depósito
    915: 2,  # Depósito
    916: 2,  # Depósito
    917: 2,  # Depósito
    918: 2,  # Depósito
    919: 2,  # Depósito
    920: 2,  # Depósito
    52: 3,  # TED
    62: 3,  # TED
    250: 3,  # Folha de Pagamento > TED
    361: 3,  # Pagamento conta água > TED
    362: 3,  # Pagamento conta luz > TED
    363: 3,  # Pagamento conta telefone > TED
    393: 3,  # TED
    438: 3,  # TED
    470: 3,  # Transferência enviada > TED
    976: 3,  # TED
    983: 3,  # TED
    48: 4,  # DOC
    58: 4,  # DOC
    63: 4,  # DOC
    166: 4,  # DOC
    223: 4,  # DOC
    397: 4,  # DOC
    776: 4,  # DOC
    59: 7,  # Boleto
    69: 7,  # Boleto
    109: 7,  # Boleto
    461: 7,  # Boleto
    495: 7,  # Boleto
    9: 13,  # Tarifas Bancárias
    10: 13,  # Tarifas Bancárias
    43: 13,  # Tarifas Bancárias
    44: 13,  # Tarifas Bancárias
    45: 13,  # Tarifas Bancárias
    46: 13,  # Tarifas Bancárias
    47: 13,  # Tarifas Bancárias
    54: 13,  # Tarifas Bancárias
    56: 13,  # Tarifas Bancárias
    127: 13,  # Tarifas Bancárias
    129: 13,  # Tarifas Bancárias
    141: 13,  # Tarifas Bancárias
    142: 13,  # Tarifas Bancárias
    162: 13,  # Tarifas Bancárias
    170: 13,  # Tarifas Bancárias
    181: 13,  # Tarifas Bancárias
    187: 13,  # Tarifas Bancárias
    201: 13,  # Tarifas Bancárias
    205: 13,  # Tarifas Bancárias
    214: 13,  # Tarifas Bancárias
    225: 13,  # Tarifas Bancárias
    231: 13,  # Tarifas Bancárias
    239: 13,  # Tarifas Bancárias
    244: 13,  # Tarifas Bancárias
    256: 13,  # Tarifas Bancárias
    261: 13,  # Tarifas Bancárias
    262: 13,  # Tarifas Bancárias
    263: 13,  # Tarifas Bancárias
    275: 13,  # Tarifas Bancárias
    310: 13,  # Tarifas Bancárias
    311: 13,  # Tarifas Bancárias
    327: 13,  # Tarifas Bancárias
    344: 13,  # Tarifas Bancárias
    353: 13,  # Tarifas Bancárias
    359: 13,  # Tarifas Bancárias
    392: 13,  # Tarifas Bancárias
    405: 13,  # Tarifas Bancárias
    426: 13,  # Tarifas Bancárias
    429: 13,  # Tarifas Bancárias
    431: 13,  # Tarifas Bancárias
    432: 13,  # Tarifas Bancárias
    435: 13,  # Tarifas Bancárias
    442: 13,  # Tarifas Bancárias
    499: 13,  # Tarifas Bancárias
    670: 13,  # Tarifas Bancárias
    286: 15,  # IPVA
    316: 15,  # IPVA
    639: 15,  # IPVA
    833: 15,  # IPVA
    28: 16,  # Fatura
    979: 18,  # FGTS
    144: 19,  # Transferência enviada > PIX
    445: 19,  # PIX
    821: 19  # PIX
}
