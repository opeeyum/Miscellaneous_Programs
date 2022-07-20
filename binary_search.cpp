#include<iostream>
using namespace std;

int Binary_search(int*, int, int, int);

int main()
{
    // Length of an array
    int n=0;
    cout<<"Enter, How many numbers: ";
    cin>>n;

    // Filling up the array
    int a[n];
    cout<<"Enter sorted list of numbers: ";
    for(int i=0; i<n; ++i)
    cin>>a[i];

    // Taking value to be find
    int target=0;
    cout<<"Enter target to be found: ";
    cin>> target;

    // Calling Binary search function
    int ans = Binary_search(a, target, 0, n-1);

    // Binary Search function will return -1 if target not in the array
    if(ans == -1)
    cout<<target<<" not found! "<<"\n";

    // Binary Search function will return index if target is in the array
    else
    cout<<target<<" found at index "<<ans<<", a["<<ans<<"] = "<<target<<"\n";
}

int Binary_search(int* a, int target, int first, int last)
{
    // Find mid
    int mid = (first+last) / 2;

    // If a[mid] is the target return mid
    if(a[mid] == target)
    return mid;
    
    // If Array has only one element and a[mid] is not the target
    else if(first == last)
    return -1;
       
    // If a[mid] is greater than target, search in left to the mid   
    else if(a[mid] > target)
    return Binary_search(a, target, first, mid-1);
    
    // If a[mid] is less or equal to the target, search in right to the mid
    else
    return Binary_search(a, target, mid+1, last);

}
