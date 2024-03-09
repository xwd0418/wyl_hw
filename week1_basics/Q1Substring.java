package week1_basics;

import java.util.Scanner;

public class Q1Substring {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter string: ");
        String text = scanner.nextLine().trim();

        System.out.print("Enter start index (inclusive): ");
        int start_index = Integer.parseInt(scanner.nextLine());

        System.out.print("Enter end index (exclusive): ");
        int end_index = Integer.parseInt(scanner.nextLine());

        System.out.println(); // print empty line

        // ### DO NOT MODIFY ANYTHING ABOVE !!!!!!###

        // ### START YOUR CODE HERE ###
        System.out.println(text.substring(start_index, end_index));
        // ### DO NOT MODIFY ANYTHING BELOW !!!!!!###
        scanner.close();
    }
}
