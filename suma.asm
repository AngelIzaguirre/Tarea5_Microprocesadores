// Suma las constantes 2 y 3 y almacena el resultado en R0

@2     // Carga la constante 2 en el registro A
D=A    // Guarda el valor de A (2) en D

@3     // Carga la constante 3 en el registro A
D=D+A  // Suma el valor de A (3) con el valor almacenado en D (2), y guarda el resultado en D

@0     // Carga la dirección 0 en el registro A (R0)
M=D    // Almacena el valor de D (5) en la dirección 0 (R0)
