#include <iostream>
using namespace std;
int main()
{   string str1, str2;
    int length = 0;
    cout<<"Enter first string: ";
    getline(cin, str1);
    cout<<"Enter second string: ";
    getline(cin, str2);
    cout<<"\nResult: ";
    if(str1.length()==str2.length())
    {   int i =0;
        while(str1[i] != '\0')
        {   int j = 0;
            while(str2[j] != '\0')
            {   if(str1[i] == str2[j])
                {   length++;
                    break;  }
                j++;    }
            i++;    }
        if(str1.length()==length)
        {   cout<<"An anagram."<<endl;  }
        else
        {   cout<<"Not an anagram."<<endl;  }   }
    else
    {   cout<<"Not an anagram."<<endl;    }    }
