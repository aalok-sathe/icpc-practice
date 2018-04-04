#include<iostream>
#include<math.h>
#include<string>

using namespace std;

int main()
{
    int A,B = 0;
    char genderB;

    while(A>=0 and B>=0 and (cin >> A >> B >> genderB))
    {
        int depthA  = (A>0)? (int) (log(A+1)/log(2)) : 0;
        int depthB  = (B>0)? (int) (log(B+1)/log(2)) : 0;
        int widthAB = NULL;

        cout << depthA << " " << depthB << endl; // DEBUG

        string relation = string();

        if(abs(depthA - depthB) > 5)
            relation += "kin";
        else
        {

        }

        cout << relation << endl;
    }

	return 0;
}
