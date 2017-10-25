#include <iostream>
#include <vector>

using namespace std;

// void CombinationPar(vector < string >& result, string& sample, int deep, int n, int leftNum, int rightNum);
// vector < string > generateParenthesis( int n) ;

void CombinationPar(vector <string> &result, string& sample, int deep, int n, int leftNum, int rightNum) 
{  

    cout << "sample=" << sample << " deep="  << deep << " n=" << n << " leftNum="  << leftNum << " rightNum=" << rightNum << endl;
    if( deep == 2*n)  
    { 
        result.push_back( sample); 
        return; 
    } 

    if( leftNum < n) 
    {
        sample.push_back('('); 
        CombinationPar(result, sample, deep + 1, n, leftNum + 1, rightNum); 
        sample.resize( sample.size()-1);
    } 

    cout << "\n";

    if( rightNum < leftNum) 
    { 
        sample.push_back(')'); 
        CombinationPar( result, sample, deep + 1, n, leftNum, rightNum + 1); 
        sample.resize( sample.size()-1);

    } 
} 

vector < string > generateParenthesis( int n) 
{ 
    vector < string > result; 
    string sample; 
    if( n != 0) 
        CombinationPar( result, sample, 0, n, 0, 0); 
        
    for (vector<string>::const_iterator i = result.begin(); i != result.end(); ++i)
        cout << *i << '\n';

    cout << '\n';
    return result;
} 


int main()
{
    generateParenthesis(3);
    return 0;
}