package main

import(
"fmt"

)

func perfectSquare(number[][] int) bool{
    

    rowSum := 0
    for _, value := range number[0]{
        rowSum += value
    }

    for count = 0; count < len(number); count++{
        row := 0
        column := 0
        for index = 0; index < len(number); index++{
            row += number[count][index]
            column += number[index][count]
        }
            if row != targetSum || colSum != targetSum{
                return false
            }

        }
            return true
    }

func main (){

    arr1 := [][]int{{2, 3}, {3, 2}}
    arr2 := [][]int{{2, 4, 5}, {3, 3, 5}, {6, 4, 1}}
    arr3 := []int{1, 2, 3, 4, 5}

    fmt.println(perfectSquare(arr1))
    fmt.println(perfectSquare(arr2))

}
