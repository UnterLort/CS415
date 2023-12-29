
//@Kyle Stewart @Temperature.java version 1
import java.util.Scanner;

public class TemperatureConversion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter temperature in Celsius
        System.out.println("Enter temperature in Celsius:");
        // Read the input from the user and store as C
        double C = scanner.nextDouble();

        // Convert temperature from Celsius to Fahrenheit
        double F = (C * 9 / 5) + 32;

        // Print the converted temperature and Celsius
        System.out.printf("%.1f C = %.1f F", C, F);

        // Close the scanner
        scanner.close();
    }
}