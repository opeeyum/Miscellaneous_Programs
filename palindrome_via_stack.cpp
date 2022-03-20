#include <iostream>
#define max_size 100
using namespace std;

char a[max_size];
int top=-1;
void push(char c)
{
    a[++top]=c;
    return;
}
char pop()
{
    return a[top--];
}
int main()
{
    string s;
    getline(cin,s);
    int i=0, pallin=1;
    while(s[i]!='\0')
    {
        push(s[i]);
        i++;
    }
    i=0;
    while (s[i]!='\0')
    {
        if(s[i]!=pop())
            {
               pallin=0;
               break;
            }
        i++;
    }
    if(pallin==0)
        cout<<"Not a palindrome";
    else cout<<"Palindrome";

    return 0;
}

