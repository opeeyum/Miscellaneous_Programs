/*
 Anagram: An anagram is a word formed by rearranging the letters of a different word,
 typically using all the original letters exactly once.

 For example: 
    1. The word anagram itself can be rearranged into nagaram.
    2. The word binary into brainy
    3. The word adobe into abode.

 Best Appraoch:
  1. First check both the string's should be of same length. 
     IF yes Continue;
     ELSE break;
  2. Create an additional array (let's say helper) of size 42, as there are 26 small alphabets and 26 Capital alphabets.
  3. Initalize the array to 0 (Zero).
  4. Now while traversing the first string there can be two cases,
     Case 1: Get a small alphabet, then increment helper's value at index == (ascii value - 'a')%10 by 1.
     Case 2: GEt a capital alphabet, then increment helper's value at index == {(ascii value - 'A')%10 + 26} by 1.
  5. Now while traversing the second string decrement the helper's value by 1 same as cases at STEP 4.
  6. Finally traverse the additional array (i.e helper) if all the values are 0 (zero) then the given strings were anagram otherwise NO.

  Time complexity: O(n)
  Space complexity: O(1)
  
*/

#include <iostream>
using namespace std;

int main()
{   
    string str1, str2;

    cout<<"Enter first string: ";
    getline(cin, str1);

    cout<<"Enter second string: ";
    getline(cin, str2);

    cout<<"\nResult: ";

    // Both the strings should be of same length.
    if(str1.length() != str2.length())
    cout<<"Not an anagram."<<endl;

    else
    {
        // Additional helper array
        int helper[42], i=0;

        // Intializing helper array to Zero
        for(; i<42; i++)
        helper[i] = 0;

        // Traversing first string
        for(i=0; i<str1.length(); i++)
        {
            // For small alphabets
            if('a' <= str1[i] && str1[i] <= 'z')
            helper[(str1[i] - 'a') % 10]++;

            // For capital alphabets
            else if('A' <= str1[i] && str1[i] <= 'Z')
            helper[(str1[i] - 'a') % 10 + 26]++;
        }

        // Traversing second string
        for(i=0; i<str2.length(); i++)
        {
            // For small alphabets
            if('a' <= str2[i] && str2[i] <= 'z')
            helper[(str2[i] - 'a') % 10]--;

            // For capital alphabets
            else if('A' <= str2[i] && str2[i] <= 'Z')
            helper[(str2[i] - 'a') % 10 + 26]--;
        }

        // Traversing the helper array
        for(i=0; i<42; i++)
        {
            if(helper[i] != 0)
            {
                cout<<"Not an angram."<<endl;
                exit(0);
            }
        }
        cout<<"An angram."<<endl;
    }

    return 0;    
}
