import sys
import analizador
import codigo

def ensamblar(archivo_entrada, archivo_salida):
    # Leer el archivo de entrada
    with open(archivo_entrada, 'r') as f:
        codigo_asm = f.readlines()

    # Parsear el código ensamblador y traducirlo a código binario
    codigo_binario = []
    for linea in codigo_asm:
        instruccion = analizador.parsear_instruccion(linea)
        if instruccion:
            instruccion_binaria = codigo.traducir_instruccion(instruccion)
            codigo_binario.append(instruccion_binaria)

    # Escribir el código binario en el archivo de salida
    with open(archivo_salida, 'w') as f:
        f.write('\n'.join(codigo_binario))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ensamblador.py <archivo_entrada> <archivo_salida>")
        sys.exit(1)

    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    ensamblar(archivo_entrada, archivo_salida)
