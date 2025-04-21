/*
 * PascalCase -> Nombre de archivos y nombres de clases
 * javac NombreArchivo.java -> compilar
 * java NombreArchivo -> ejecutar
*/

public class Intro {
    public static void main(String[] args) {
        System.out.println("hello world");

        // Primitivo - solo GUARDAR valor
        int myInt; // Declarar variable
        myInt = 400; // Asignar valor
        double pi = 3.1416;
        boolean bool = true;
        char character = 'a';

        // Objeto
        Integer myInteger;
        Double myDouble;
        Character myChar;
        String myString = "ABC";
        System.out.println(myString);

        String str = "Good morning";
        System.out.println("length: " + str.length());
        System.out.println(str.toLowerCase());
        System.out.println(str.toUpperCase());

        String x = "Hello";
        String y = "Hello";
        System.out.println(x.equals(y));

        // Condicionales
        if (myInt == 400) {
            System.out.println("Numeros iguales");
        } else {
            System.out.println("Diferentes");
        }

        // Arrays
        int[] myArray;
        myArray = new int[5];
        for (int i = 0; i < 5; i++) {
            myArray[i] = i + 1;
        }

        for (int i = 0; i < myArray.length; i++) {
            System.out.printf("myArray[%d] = %d\n", i, myArray[i]);
        }

        hello();
        hello();
        hello();
        hello("Moka");
    }

    /*
     * Permisos función -> public, private, protected
     * static -> De clase
    */
    public static void hello() {
        System.out.println("hello");
    }

    // Sobrecarga
    public static void hello(String name) {
        System.out.println("hello, " + name);
    }
}
