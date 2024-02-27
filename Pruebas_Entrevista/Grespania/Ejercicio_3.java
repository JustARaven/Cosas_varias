import java.io.File;
import java.io.FileWriter;

public class Ejercicio_3 {
    public static void main(String[] args) {
        // Enunciado: Crea un fichero plano y llama a una URL ficticia donde lo envías a convertir a otro formato. Recoge el fichero que dicha URL ha dejado en tu directorio local.
        // Este proceso de conversión puede ser algo pesado, procura que la ejecución de tu hilo no llegue antes que el fichero devuelto.
        String nombreArchivoOriginal = "archivo_original.txt";
        String nombreArchivoConvertido = "archivo_convertido.txt";
        String rutaArchivo = String.format("%s", nombreArchivoConvertido); // Con esta forma puedes personalizar de forma efectiva el path del fichero

        try {
            // Crear un archivo plano
            File archivoOriginal = new File(nombreArchivoOriginal);
            if (archivoOriginal.createNewFile()) {
                System.out.println("Archivo creado: " + archivoOriginal.getName());
                // Simulación de escritura en el fichero.
                FileWriter escritor = new FileWriter(nombreArchivoOriginal);
                escritor.write("Este es el contenido original del archivo.");
                escritor.close();
            } else {
                System.out.println("El archivo ya existe.");
            }

            // Conversión


            // Recuperación del archivo
            File archivo = new File(rutaArchivo);
            boolean existe = archivo.exists();
            int tiempoDeComprobacion = 5000; // 5s

            while (!existe) {
                System.out.println("Esperando el archivo...");
                try {
                    Thread.sleep(tiempoDeComprobacion); // Hace que el hilo actual se detenga durante "tiempoDeComprobacion" segundos.
                } catch (InterruptedException e) {
                    System.out.println("Interrupción del hilo de espera."); // Gestionar correctamente la interrupción.
                }
                // Vuelve a comprobar la existencia del archivo
                existe = archivo.exists();
            }
            System.out.println("El archivo existe.");

            // Manejo del fichero

        } catch (Exception e) { // Este apartado se debería mejorar de forma adecauda teniendo en cuenta las diferentes excepciones y no generalizarlo.
            System.out.println("Ocurrió un error.");
        }
    }
}