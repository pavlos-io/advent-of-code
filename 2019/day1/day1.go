package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func getFuel(mass int) int {
	return mass/3 - 2
}

func main() {
	f, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	sc := bufio.NewScanner(f)
	p1, p2 := 0, 0

	for sc.Scan() { // reads file line by line
		num, _ := strconv.Atoi(sc.Text())
		p1 += getFuel(num)

		for num > 0 {
			num = getFuel(num)
			if num > 0 {
				p2 += num
			}
		}
	}

	fmt.Println(p1, p2)

	if err := sc.Err(); err != nil {
		log.Fatal(err)
	}
}
