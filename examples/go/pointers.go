package main

import "fmt"

func main() {
	x := 10
	y := &x // &{variable} means that to make a pointer to that value
	z := x
	fmt.Println("x:, ", x, ", y value: ", y, ", value of what y is pointing to: ", *y, ", z: ", z) //*{variable} means find the value from root pointer
	fmt.Println("Memory Address of x: ", &x)
	fmt.Println("Memory Address of y: ", &y)
	fmt.Println("Memory Address of z: ", &z)

	*y++ // Update the value in the pointer
	fmt.Println("x:, ", x, ", y value: ", y, ", value of what y is pointing to: ", *y, ", z: ", z)
	x++
	fmt.Println("x:, ", x, ", y value: ", y, ", value of what y is pointing to: ", *y, ", z: ", z)
	z += 20
	fmt.Println("x:, ", x, ", y value: ", y, ", value of what y is pointing to: ", *y, ", z: ", z)
}
