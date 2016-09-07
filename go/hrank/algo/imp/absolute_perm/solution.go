// https://www.hackerrank.com/challenges/absolute-permutation

package main

import (
	"fmt"
)

func main() {
	times := readInt()
	for i := 0; i < times; i++ {
		n := readInt()
		k := readInt()

		result, possible := generate_absolute_permutation(n, k)
		if possible {
			for _, v := range result {
				fmt.Printf("%d ", v)
			}
			fmt.Printf("\n")
		} else {
			fmt.Println(-1)
		}
	}
}

func readInt() int {
	var n int
	_, err := fmt.Scanf("%d", &n)

	if err != nil {
		panic(err)
	}

	return n
}

func generate_absolute_permutation(n int, k int) ([]int, bool) {
	// var result [n]int
	result := make([]int, n)
	possible := true
	if k == 0 {
		for i := 1; i <= n; i++ {
			result[i-1] = i
		}

		return result, possible
	} else if n%2 == 1 || n%(2*k) != 0 {

		return result, false
	} else {

		number := 1
		outer := n / (2 * k)
		for i := 0; i < outer; i++ {
			for j := 1; j >= 0; j-- {
				for l := 0; l < k; l++ {
					ndx := i*(2*k) + k*j + l
					result[ndx] = number
					number += 1
				}
			}

		}

		return result, possible

	}

}
