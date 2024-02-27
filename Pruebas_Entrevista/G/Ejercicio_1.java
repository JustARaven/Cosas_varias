public class Ejercicio_1 {
    public static void main(String[] args) {
        // Texto inicial.
        String text2 ="Java is the foundation for virtually every type of networked application and is the global standard for developing and  delivering embedded and mobile applications, games, Web-based content,  and enterprise software. With more than 9 million developers worldwide, Java enables you to efficiently develop, deploy and use exciting applications and services.";
        // Palabra a buscar en el texto inicial.
        String text3 = "million";
        // Enunciado: Muestra por pantalla true o false dependiendo si text2 contiene text3.

        System.out.println(text2.contains(text3)); // Comprueba si el valor de la variable texto2 está contenido en la variable texto3
    }
}