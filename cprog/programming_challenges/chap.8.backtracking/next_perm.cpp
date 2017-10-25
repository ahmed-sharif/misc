#include <vector>
#include <stdio.h>
#include <iostream>

using namespace std;


void print_vector(vector<int> v)
{
    for (vector<int>::const_iterator i = v.begin(); i != v.end(); ++i)
        cout << *i << ' ';
    cout <<"\n";

}

int solve(int X){
    vector<int> number ;
    while(X){
        number.push_back(X % 10) ;
        X /= 10 ;
    }

    print_vector(number);
    // cout << number;

    reverse(number.begin(),number.end()) ;
    cout <<"after reversing\n";
    print_vector(number);
    int Z = -1 ;

    if(next_permutation(number.begin(),number.end())){
        // if next_permutation exists, update value of Z .
        Z = 0 ;
        for(int i=0;i<number.size();i++){
            Z = Z * 10 + number[i] ;
        }
    }
    return Z ; 
}

int main()
{
    int res;
    printf("%d\n", 1234);
    res = solve(1234);
    printf("%d\n", res);
    res = solve(4321);
    printf("%d\n", res);
}
