from pymem import *
from pymem.process import *

def ler_enderecos_memoria(pid, endereco1, endereco2):
    try:
        pm = pymem.Pymem("client.exe") # Substitua "client.exe" pelo nome do processo que deseja monitorar
        endereco1_valor = pm.read_int(endereco1)
        endereco2_valor = pm.read_int(endereco2)
        print(f"Valor no endereço {endereco1}: {endereco1_valor}")
        print(f"Valor no endereço {endereco2}: {endereco2_valor}")
    except pymem.exception.ProcessNotFound:
        print("Processo não encontrado.")
    except pymem.exception.MemoryReadError:
        print("Erro ao ler da memória.")

pid = 17288
endereco1 = 0x14367C64
endereco2 = 0x0B44DC50

ler_enderecos_memoria(pid, endereco1, endereco2)
