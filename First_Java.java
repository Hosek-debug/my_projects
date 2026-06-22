import java.util.Scanner;

public class age {
    public static void main(String[]args) {
        System.out.println("This is my first project in Java!");
        System.out.println("Today, it's a system for insert your age and name");
        Scanner insert = new Scanner(System.in);

        System.out.print("Insert your age: ");
        int age = insert.nextInt();

        System.out.println("age: " + age);

        Scanner read = new Scanner(System.in);

        System.out.print("Insert your name: ");
        String name = read.nextLine();

        System.out.println("Hello! " + name);

        if (age >= 18) {
            System.out.println("You are old");
        } 

        else {
            System.out.println("You are young");
        }
    }
}
