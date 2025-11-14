import java.util.Scanner;
public class PasswordChecker{
    public static void main(String[]args){
    Scanner input = new Scanner(System.in);
    
    System.out.print("Enter your Password: ");
    String userPassword = input.next();
   
    int length = userPassword.length();
   
    if(length > 10){
    System.out.print("Strong Password");    
    }
    else if(length >= 10){
    System.out.print("medium Password");    
    }
    else if(length <= 6){
    System.out.print("weak Password");    
    }
    else if(length < 1){
    System.out.print("invalid Password");    
    }

    }
}
