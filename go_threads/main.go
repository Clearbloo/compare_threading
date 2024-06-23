package main

import (
	"sync"
	"time"
)

func greet(n int, wg *sync.WaitGroup) {
	defer wg.Done()
	if n%3 == 0 {
		time.Sleep(1000 * time.Millisecond)
	} else {
		time.Sleep(100 * time.Millisecond)
	}
	// fmt.Println("Hello", n)
}

func main() {
	var wg sync.WaitGroup

	for i := 0; i <= 100000; i++ {
		wg.Add(1)
		go greet(i, &wg)
	}

	wg.Wait()
}
