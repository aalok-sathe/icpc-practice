// Aalok Sathe

#include<iostream>

// convenient native variable names to use
#define L -1
#define R +1
#define space " "

using namespace std;

int which_child(int p, int q)
{
    if (p == q)
        return 0;
    return (p < q)?L:R;
}

int main()
{

    // total number of testcases
    int P;
    cin >> P;

    for (int i = 0; i < P; i++)
    {
        // read the data set number
        int K;
        cin >> K;
        
        // read in p, forward slash, and q.
        char f;
        int p,q;
        cin >> p >> f >> q;
        
        if (which_child(p,q) == 0)
        {
            cout << K << " " << p << "/" << (p+q) << endl;
            continue;
        }
        else if (which_child(p,q) == L)
        {
            cout << K << " " << q << "/" << (q-p) << endl;
            continue;
        }
        else if (which_child(p,q) == R)
        {   
        
            // go up "faster" by taking mod
            int new_p = p % q;
            int depth = (p-new_p)/q;
            
            p = new_p;
            
            // go up the tree as long as we are still a right child
            /*
            while ((which_child(p,q) == R) and (++depth))
            {
                p -= q;
                //cout << p << "/" << q << "\t" << depth << endl;
            }
            */
            // p/q is not one, so make a switch to other branch at the relative root
            if (p != q)
            {
                q -= p;
                p += q;
                //cout << p << "/" << q << "\t" << depth << endl;
            }
            else if (p == q) // p/q is one, so we are at absolute root. go down the left now. 
                q += p;
            
            // go down the same depth on the left.
            
            q += depth*p;
            /*
            while (depth--)
            {
                q += p;
                //cout << p << "/" << q << "\t" << depth << endl;
            }
            */  
            cout << K << " " << p << "/" << q << endl;
            
            continue;
        }
    }

	return 0;
}
