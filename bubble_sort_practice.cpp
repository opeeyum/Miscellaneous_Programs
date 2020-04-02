#include<iostream>
#include<algorithm>
using namespace std;
void bubble_sort(int*, int);
int main()
{
    int n;
    cout<< "Enter how many numbers: ";cin>>n;
    int a[n];
    cout<< "Enter numbers: ";
    for(int i = 0; i<n; ++i)
    {
        cin>>a[i];
    }
    bubble_sort(a, n);
    for(int i = 0; i<50; ++i)
    {
        cout<<"-";
    }
    cout<<endl;
    cout<<"Final result: ";
    for(int i = 0; i<n; ++i)
    {
        cout<<a[i]<< " ";
    }
    cout<<endl;
}
void bubble_sort(int a[], int n)
{
    for(int i = 0; i<n-1; ++i)
    {
        int flag =0;
        for(int j=0; j<n-i-1; ++j)
        {
            if(a[j]> a[j+1])
            {
                swap(a[j+1], a[j]);
                flag++;
            }
        }
        cout<<"Pass "<<i<<" result: ";
        for(int i = 0; i<n; ++i)
        {
        cout<<a[i]<< " ";
        }
        cout<<endl;
        if(flag == 0)
        {
            break;
        }
    }
}

