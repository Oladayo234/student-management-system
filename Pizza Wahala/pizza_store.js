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

    const input = require('prompt-sync')();
    let pizzaType = input('Enter pizza type: ');
    let numberOfGuest = input('Enter number of guest: ');
 
    let numberOfSlices = 0;
    let pricePerBox = 0;


    if (pizzaType === "sapa size")){
       numberOfSlices = 4;
       pricePerBox = 2000;}

    else if (pizzaType === "small money")){
            numberOfSlices = 6;
            pricePerBox = 2400;}

    else if (pizzaType === "big boys")){
            numberOfSlices = 8;
            pricePerBox = 3000;}

    else if (pizzaType === ("odogwu")){
            numberOfSlices = 12;
            pricePerBox = 4200;}

    let numberOfBoxes = Math.ceil(numberOfGuest / numberOfSlices);
    let remainder = (numberOfSlices * numberOfBoxes) - numberOfGuest;
    let price = pricePerBox * numberOfBoxes;
    let total = numberOfBoxes * numberOfSlices;


    System.out.printf("price = %d.%n%d per box for %d boxes.", price, pricePerBox, numberOfBoxes);

    System.out.printf("Total slice: %d.%nRemaining slices: %d%n", total, remainder);

    System.out.printf("%s pizza contains %d per box.%n%d boxes should be sufficient for %d people as it would contain %d slices in all%n", pizzaType, numberOfSlices, numberOfBoxes, numberOfGuest, total);



