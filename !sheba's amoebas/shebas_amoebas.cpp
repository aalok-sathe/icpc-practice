//Aalok S. 1 Feb 2018
#include<iostream>

using namespace std;

const int DIM = 101;

void explore(int (&matrix) [DIM][DIM], int i, int j, int group_count, int &group_number, int M, int N, int &map);

int main()
{
	int M,N;
	
	while (cin >> M >> N)
	{		
		int map[DIM*DIM] 		= {0};
		int matrix[DIM][DIM] 	= {0};
		int group_count 		= 0;
		int group_number 		= 0;
		
		for (int i=0; i<M; i++)
		{
			for (int j=0; j<N; j++)
			{
				char c;
				cin >> c;
			
				if (c == '.')				// white pixel
					matrix[i][j] = 0;
				else if (c == '#')			// black pixel
				{
					if (matrix[i][j] > 0)	// it already has a group number
						explore(matrix, i, j, matrix[i][j], group_number, M, N, map);
					else
					{
						group_count+=1;
						matrix[i][j] = group_count;
						explore(matrix, i, j, group_count, group_number, M, N, map);
					}
				}
			}
		}
		
		/*
		for (int i=0; i<M; i++) 
		{
			for (int j=0; j<N; j++)
				cout << matrix[i][j] << " ";
			cout << endl;		
		}
		//*/
		
		cout << group_count << endl;	
	}
		

	return 0;
}

void explore(int (&matrix) [DIM][DIM], int i, j, group_number, &group_count M, N, &map)
{
	for (int m = -1; m < 2; m++)
		for (int n = -1; n < 2; n++)
			if ((i + m >= 0) && (j + n >= 0) && (i + m < M) && (j + n < N))
			{
				if (matrix[i + m][j + n] > 0)
				{
					//if 
					map[matrix[i + m][j + n]] = group_number;
					group_count--;
				}
				
				matrix[i + m][j + n] = group_count;
			}	
				
	
	/*
	for (int ii=0; ii<M; ii++)  ACM ICPC/sheba'
		{
			for (int jj=0; jj<N; jj++)
				cout << matrix[ii][jj] << " ";
			cout << endl;		
		}
		cout << endl;
	*/
}


