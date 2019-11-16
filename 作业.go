package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"time"
)
func c(a int64){
	fmt.Println(time.Unix(a,0).Local())
}
func main() {
	fmt.Println("input numbers and input 'result' to see the results latter")
	for i:=0;;i++ {
		data := bufio.NewScanner(os.Stdin)
		data.Scan()
		if data.Text()=="result"{
			fmt.Println("The results are:")
			return
		}
		b:=data.Text()
		a,_:=strconv.ParseInt(b,10,0)
		defer c(a)
		fmt.Println("input ok!")
	}
}