// Aalok Sathe
#include<iostream>
#include<limits.h>

using namespace std;

int main()
{
    int p;    
    cin >> p;
    
    int arr[15];
 
    for(int i = 0; i < p; i++)
    {
        int k;
        cin >> k;
        
        for(int j = 0; j < 15; cin >> arr[j++]);
        
        int island_count = 0;
        for(int a = 1; a < 15-1; a++)
            if (arr[a] > arr[a-1])
                island_count++;

        cout << k << " " << island_count << endl;
    }     
       
	return 0;
}
