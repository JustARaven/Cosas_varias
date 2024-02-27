import java.util.Scanner;
import java.util.InputMismatchException;
// En caso de requerirse números excesivamente grandes se podía utilizar "java.math.BigInteger" pero considero que no es necesario.

public class Ejercicio_2 {
    public static void main(String[] args) {
        // Enunciado: Pedir por teclado un número entero positivo y que nos devuelva el número de cifras que tiene
        Scanner scanner = new Scanner(System.in); // Crea el objeto Scanner
        boolean validarEntrada = false; // Inicializa la variable de comprobación
        int numero = 0; // Inicializa la variable del input númerico

        while (!validarEntrada) {
            System.out.println("Ingresa un número entero positivo: ");
            try {
                numero = scanner.nextInt(); // Intenta leer un entero
                if (numero <= 0) {
                    System.out.println("El número debe ser positivo, intentalo de nuevo.");
                } else {
                    validarEntrada = true; // La entrada es válida, sale del while
                }
            } catch (InputMismatchException e) {
                System.out.println("La entrada es inválida, ingresa solo números enteros.");
                scanner.next(); // Descarta la entrada incorrecta
            }
        }
        int contadorDeCifras = contarCifras(numero); // Llama a el método para contar las cifras
        System.out.println("El número tiene " + contadorDeCifras + " cifra(s).");
    }

    public static int contarCifras(int numero) {
        int contador = 0;
        while (numero > 0) {
            numero /= 10; // Divide el número entre 10 para "eliminar" una cifra
            contador++; // Incrementa el contador de cifras
        }
        return contador; // Devuelve el total de cifras
    }
}