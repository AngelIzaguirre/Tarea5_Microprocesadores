# codigo.py

next_memory_address = 16

symbol_table = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576
}

def agregar_simbolo(symbol):
    global next_memory_address
    global symbol_table

    if symbol not in symbol_table:
        symbol_table[symbol] = next_memory_address
        next_memory_address += 1

def traducir_instruccion(instruccion):
    tipo = instruccion.get('tipo')
    if tipo == 'A_COMMAND':
        return traducir_instruccion_a(instruccion)
    elif tipo == 'C_COMMAND':
        return traducir_instruccion_c(instruccion)
    elif tipo == 'LABEL':
        return ''
    else:
        raise ValueError("Tipo de instrucción desconocido: {}".format(tipo))



def traducir_instruccion_a(instruccion):
    global next_memory_address

    direccion = instruccion['direccion']
    
    if not direccion.isdigit() and direccion not in symbol_table:
        agregar_simbolo(direccion)

    if not direccion.isdigit():
        direccion = str(symbol_table[direccion])

    return format(int(direccion), '016b')

def traducir_instruccion_c(instruccion):
    comp = traducir_comp(instruccion['comp'])
    dest = traducir_dest(instruccion.get('destino', 'null'))
    jump = traducir_jump(instruccion.get('jump', 'null'))
    return "111{}{}{}".format(comp, dest, jump)

def traducir_comp(mnemonico):
    comp_table = {
        "0":   "0101010",
        "1":   "0111111",
        "-1":  "0111010",
        "D":   "0001100",
        "A":   "0110000",
        "!D":  "0001101",
        "!A":  "0110001",
        "-D":  "0001111",
        "-A":  "0110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "D+A": "0000010",
        "D-A": "0010011",
        "A-D": "0000111",
        "D&A": "0000000",
        "D|A": "0010101",
        "M":   "1110000",
        "!M":  "1110001",
        "-M":  "1110011",
        "M+1": "1110111",
        "M-1": "1110010",
        "D+M": "1000010",
        "D-M": "1010011",
        "M-D": "1000111",
        "D&M": "1000000",
        "D|M": "1010101"
    }
    return comp_table[mnemonico]

def traducir_dest(mnemonico):
    dest_table = {
        "null": "000",
        "M":    "001",
        "D":    "010",
        "MD":   "011",
        "A":    "100",
        "AM":   "101",
        "AD":   "110",
        "AMD":  "111"
    }
    return dest_table.get(mnemonico, "000")

def traducir_jump(mnemonico):
    jump_table = {
        "null": "000",
        "JGT":  "001",
        "JEQ":  "010",
        "JGE":  "011",
        "JLT":  "100",
        "JNE":  "101",
        "JLE":  "110",
        "JMP":  "111"
    }
    return jump_table.get(mnemonico, "000")
