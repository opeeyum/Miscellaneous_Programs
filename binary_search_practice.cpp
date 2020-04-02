#include<iostream>
using namespace std;
void Binary_search(int*, int, int, int);
int main()
{
    int n;
    cout<<"Enter, How many numbers: ";
    cin>>n;
    int a[n];
    cout<<"Enter sorted list of numbers: ";
    for(int i=0; i<n; ++i)
    {
        cin>>a[i];
    }
    int value;
    cout<<"Enter value to be found: ";cin>>value;
    Binary_search(a, value, 0, n-1);
}
void Binary_search(int* a, int value, int first, int last)
{
    if(first==last)
    {
        if(a[first]==value)
        {
            cout<<endl;
            cout<<value<<" found at index "<<first<<", a["<<first<<"] = "<<value;
            cout<<endl;
        }
        else
        {
            cout<<endl;
            cout<<value<<" not found! ";
            cout<<endl;
        }
    }
    else
    {
        int mid =(first+last)/2;
        if(a[mid]==value)
        {
           cout<<endl;
           cout<<value<<" found at index "<<mid<<", a["<<mid<<"] = "<<value;
           cout<<endl;
        }
        else if(a[mid]>value)
        {
            Binary_search(a, value, first, mid-1);
        }
        else if(a[mid]<value)
        {
            Binary_search(a, value, mid+1, last);
        }
    }
}
