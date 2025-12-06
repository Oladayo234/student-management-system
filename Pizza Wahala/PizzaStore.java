import java.util.Scanner;
public class PizzaStore{
    public static void main(String[]args){
       System.out.print("""    
                Hello,
                
                                Welcome to Iya Scambirah Pizza joint

               *********************************MENU********************************
               =====================================================================
               |                      |                     |                      |
               |Pizza Type            | Number of Slices    |Price per Box         |
               =====================================================================
               |                      |                     |                      |
               |Sapa Size             |4                    |2,000                 |
               =====================================================================
               |                      |                     |                      |
               |Small Money           |6                    |2,400                 |
               =====================================================================
               |                      |                     |                      |
               |Big Boys              |8                    |3,000                 |
               =====================================================================
               |                      |                     |                      |
               |Odogwu                |12                   |4,200                 |
               =====================================================================



                """);


    Scanner input = new Scanner(System.in);
    System.out.println("Enter number of guest; ");
    int numberOfGuest = input.nextInt();
    System.out.println("Enter pizza type; ");
    String pizzaType = input.next().toLowerCase();
    int numberOfSlices = 0;
    int pricePerBox = 0;


    if (pizzaType.equals("sapa size")){
       numberOfSlices = 4;
       pricePerBox = 2000;}

    else if (pizzaType.equals("small money")){
            numberOfSlices = 6;
            pricePerBox = 2400;}

    else if (pizzaType.equals("big boys")){
            numberOfSlices = 8;
            pricePerBox = 3000;}

    else if (pizzaType.equals("odogwu")){
            numberOfSlices = 12;
            pricePerBox = 4200;}

    int numberOfBoxes = (int) Math.ceil((double)numberOfGuest / numberOfSlices);
    int remainder = (numberOfSlices * numberOfBoxes) - numberOfGuest;
    int price = pricePerBox * numberOfBoxes;
    int total = numberOfBoxes * numberOfSlices;


    System.out.printf("price = %d.%n%d per box for %d boxes.", price, pricePerBox, numberOfBoxes);

    System.out.printf("Total slice: %d.%nRemaining slices: %d%n", total, remainder);

    System.out.printf("%s pizza contains %d per box.%n%d boxes should be sufficient for %d people as it would contain %d slices in all%n", pizzaType, numberOfSlices, numberOfBoxes, numberOfGuest, total);
    }

}
