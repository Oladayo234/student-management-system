import java.util.Scanner;
public class ScoreBoard{
    public static void main(String[]args){
    Scanner input = new Scanner(System.in);
    
    System.out.print("Enter score: ");
    int firstGrade = input.nextInt();

    System.out.print("Enter score: ");
    int secondGrade = input.nextInt();
    
    System.out.print("Enter score: ");
    int thirdGrade = input.nextInt();

    int sum = firstGrade + secondGrade + thirdGrade;
    int average = sum / 3;

    if(average >= 90){
    System.out.println('A');
    }
    else if(average >= 80){
    System.out.println('B');
    }
    else if(average >= 70){
    System.out.println('C');
    }
    else if(average >= 60){
    System.out.println('D');
    }
    else { 
    System.out.println('F');
    }
}
}
