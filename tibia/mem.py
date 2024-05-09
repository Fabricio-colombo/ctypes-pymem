import psutil

pid = 17288
enderecos = [0x0B407018, 0x0B41AEA0, 0x0B44DC50, 0x14367C64, 0x1D9830A4]

def obter_valor_endereco(pid, endereco):
    processo = psutil.Process(pid)
    try:
        info = processo.memory_full_info()
        for regiao in info._asdict()['maps']:
            if regiao['addr'] == endereco:
                return regiao['size']
        return None
    except psutil.NoSuchProcess:
        return None

valores = {}
for endereco in enderecos:
    valor = obter_valor_endereco(pid, endereco)
    if valor is not None:
        valores[endereco] = valor

print("Valores atuais dos endereços de memória:")
for endereco, valor in valores.items():
    print(f"Endereço: {endereco}, Valor: {valor}")
