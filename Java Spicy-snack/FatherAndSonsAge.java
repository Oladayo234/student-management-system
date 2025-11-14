import java.util.Scanner;
public class FatherAndSonsAge{
    public static void main(String[]args){
    Scanner input = new Scanner(System.in);
    
    System.out.println("Enter fathers age: ");
    int currentFatherAge = input.nextInt();

    System.out.println("Enter son's age: ");
    int currentSonAge = input.nextInt();

    int yearsDifference = 2 * currentSonAge - currentFatherAge;

    if(currentFatherAge > 80 || currentSonAge > 80){
      System.out.println("OUT OF RANGE");
    }
    else{ 
        System.out.printf("The father was twice the age of the son %d years ago. ", yearsDifference);
    }
    }
}
