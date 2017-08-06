// Recursion: Fibonacci Numbers
// Cracking the Coding Interview Challenge
// https://www.hackerrank.com/challenges/ctci-fibonacci-numbers


#include <iostream>

using namespace std;

int fibonacci(int n) {
    if(n == 0){
        return 0;
    }else if(n == 1){
        return 1;
    }else{
        return fibonacci(n-1) + fibonacci(n-2);
    }
}


// Provided

int main() {
    int n;
    cin >> n;
    cout << fibonacci(n);
    return 0;
}
