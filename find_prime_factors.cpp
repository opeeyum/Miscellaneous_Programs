#include <iostream>
using namespace std;

void prime_factors(int n)
{
    //Starting with 2 as is netiher prime nor composite.
    int temp = 2;
    while(n > 1)
    {
        //Check divisibility by a number and keep dividing until becomes non-divisible
        if(n%temp == 0)
        cout<<temp<<" ";
        while(n % temp == 0)
        n /= temp;
        
        temp++;
    }
    cout<<endl;

}

int main()
{
    int arr[] = {4, 6, 8, 10, 12};
    int n = 5;
    for(int i=0; i<n; i++)
    {
        prime_factors(arr[i]);
    }
}