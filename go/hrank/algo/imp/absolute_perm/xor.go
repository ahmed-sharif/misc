
package main

import (
    "fmt"
)


func optimized_bionomial_coeff(row uint64, n uint64) ([]int) {

    items := make([]int, row + 1)
    items[0] = 1
    
    var index int
    var res int

    for j:= 1; j < (row + 1); j++ {

        if j & (row - j) == 0 {
            res = 1
        } else {
            res = 0
        }
            
        index = j % n
        items[index] = items[index] ^ res

    }
    return items
}
    


func readInt() uint64 {
    var n uint64
    _, err := fmt.Scanf("%d", &n)

    if err != nil {
        panic(err)
    }

    return n
}


func main() {
    n := readInt()
    m := readInt()

    var r uint64
    var res uint64
    var ndx uint64
    numbers := make([]int, n)

    for i := 0; i < n; i++ {
        numb := readInt()
        numbers[i] = numb

    }

    items := optimized_bionomial_coeff(m - 1, n)

    summ := 0

    for _, v := range items{
        summ += v
    }
    r = 0
    if summ == n {
        for _, v:= range numbers{
            r = r ^ v
        }

        for i:=0; i<n; i++{
            fmt.Printf("%d ", r)
        }

        fmt.Printf("\n")

    } else {
        for i:=0; i < n; i++{
            res = 0
            for item := 0; item < len(items); item++{
                if items[item] == 1{
                    ndx = (i + item) % n
                    res = res ^ numbers[ndx]

                }
            }
            fmt.Printf("%d ", res)
        }
        fmt.Printf("\n")
    }

}
