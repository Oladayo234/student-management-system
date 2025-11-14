import java.util.Scanner;
public class Calculator{
    public static void main(String[]args){
    Scanner input = new Scanner(System.in);
    
    System.out.println("Enter first integer: ");
    int firstInterger = input.nextInt();

    System.out.println("Enter arithmetric operator: ");
    String arithmeticOperator = input.next();

    System.out.println("Enter second integer: ");
    int secondInterger = input.nextInt();

    int sum = firstInterger + secondInterger;
    int subtraction = firstInterger - secondInterger;
    int product = firstInterger * secondInterger;
    double division = firstInterger / secondInterger;

    
    if(arithmeticOperator.equals("+")){
      System.out.println(sum);
    }

    if(arithmeticOperator.equals("-")){
      System.out.println(subtraction);
    }

    if(arithmeticOperator.equals("*")){
      System.out.println(product);
    }
    if(arithmeticOperator.equals("/")){
      System.out.println(division);
    }

    }
}
