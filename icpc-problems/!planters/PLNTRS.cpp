// Aalok Sathe, 2018-02-15
#include<iostream>
#include<vector>
#include<queue>

#define lld long long int	// Macro defn. to accommodate large numbers

using namespace std;

int main()
{
	lld N;	
	cin >> N;				// Number of test cases
	
	while(N--)				// Loop over all test cases
	{
				
		lld n, m;			// Number of existing pots and new pots, respectively
        cin >> n >> m;
		
							// Initialize priority queues for new and current pots
		priority_queue<lld> current_planters;	//(n);
		priority_queue<lld> new_planters;		//(m);
		
		while(n--)			// Read in sizes of current planters (pots)
		{
			lld t;
			cin >> t;
			current_planters.push(t);
		}
		while(m--)			// Read in sizes of new planters
		{
			lld t;
			cin >> t;
			new_planters.push(t);
		}
		
		bool flag = true;	// Start with assumption "YES" unless proven otherwise
		
		while(!current_planters.empty() and flag)	// Process till all current plants
													// have a new pot
		{
			if (new_planters.empty())				// We have run out of available pots!
				flag = false;						// Indicate failure
				
			else if (new_planters.top() > current_planters.top())
			{
				new_planters.pop();
				new_planters.push(current_planters.top());
				current_planters.pop();
			}
			
			else									// No new pot of appropriate size
				flag = false;						// Indicate failure
				
		}
				
		if (flag)									// No failure encountered
			cout << "YES" << endl;
		else										// Assumption failed
			cout << "NO" << endl;
			
	}	/***************************************	END:	while(N--)		*/
	
	return 0;
}
