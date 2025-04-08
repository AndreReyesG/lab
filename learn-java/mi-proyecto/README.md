## Estructura básica de un proyecto Java
Una estructura común (tipo manual, sin frameworks ni herramientas com Mave/Gradle) se ve así:
```
mi-proyecto/
├── src/
│   └── com/
│       └── andre/
│           ├── Main.java
│           └── util/
│               └── Hola.java
├── bin/  ← aquí van los .class compilados
└── README.md
```

> Las carpetas `com/andre/` reflejan el paquete `com.andre`, una convención de nombres de paquetes Java.

## ¿Cómo se compila?
Desde la raiz del proyecto:
```bash
javac -d bin src/com/andre/Main.java src/com/andre/util/Hola.java
```
- `-d bin` -> Indica que los `.class` deben ir a la carpeta `bin`.
- Puedes compilar todos los archivos `.java` automáticamente así:
```bash
find src -name "*.java" | xargs javac -d bin
```

## ¿Cómo se ejecuta?
Si `Main.java` contiene:
```java
package com.andre;

import com.andre.util.Hola;

public class Main {
    public static void main(String[] args) {
        Hola.saludar();
    }
}
```
Entonces debes ejecutar desde la raiz del proyecto con:
```bash
java -cp bin com.andre.Main
```
- `-cp bin` -> Añade el classpath donde están los `.class`.

## `makefile` básico para compilar, correr y crear `.jar`
### ¿Cómo se usa?
```
make         # compila
make run     # ejecuta
make jar     # crea un .jar ejecutable
make clean   # borra bin/ y dist/
```
