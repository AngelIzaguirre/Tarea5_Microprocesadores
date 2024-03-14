def parsear_instruccion(linea):
    linea = limpiar_linea(linea)
    if not linea:
        return None

    instruccion = {}
    if linea.startswith('@'):
        instruccion['tipo'] = 'A_COMMAND'
        instruccion['direccion'] = linea[1:]
    elif linea.startswith('('):
        instruccion['tipo'] = 'LABEL'
        instruccion['nombre'] = linea.strip('()')
    else:
        instruccion['tipo'] = 'C_COMMAND'
        partes = linea.split('=')
        if len(partes) == 2:
            instruccion['destino'] = partes[0].strip()
            comp_jump = partes[1].split(';')
            instruccion['comp'] = comp_jump[0].strip()
            if len(comp_jump) == 2:
                instruccion['jump'] = comp_jump[1].strip()
            else:
                instruccion['jump'] = None
        else:
            comp_jump = linea.split(';')
            instruccion['destino'] = None
            instruccion['comp'] = comp_jump[0].strip()
            if len(comp_jump) == 2:
                instruccion['jump'] = comp_jump[1].strip()
            else:
                instruccion['jump'] = None

    return instruccion


def limpiar_linea(linea):
    linea = linea.split("//")[0].strip()
    return linea
