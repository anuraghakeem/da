stable matching:
#include <iostream>
#include <cstring>
#include <queue>
using namespace std;

int Ranking[100][100], ManPref[100][100], WomanPref[100][100], Next[100], Current[100];

int main()  {
    int T, N, i, j, m, w;
    queue <int> freeMen;
        cout<<"No of men and women\n";
        cin>>N;
        for (i = 1; i <= N; i++) {
            cout<<"Woman "<<i<<"prefernce list\n";
            for (j = 1; j <= N; j++)
                cin>>WomanPref[i][j];        }
        for (i = 1; i <= N; i++) {
            cout<<"Man "<<i<<"prefernce list\n";
            for (j = 1; j <= N; j++)
                cin>>ManPref[i][j];
        }
        for (i = 1; i <= N; i++)
            for (j = 1; j <= N; j++)
                Ranking[i][WomanPref[i][j]] = j;
        memset(Current, 0, (N + 1) * sizeof(int));
        for (i = 1; i <= N; i++) {
            freeMen.push(i);
            Next[i] = 1;
        }
        while (!freeMen.empty())    {
            m = freeMen.front();
            w = ManPref[m][Next[m]++];
            if (Current[w] == 0)   {
                Current[w] = m;
                freeMen.pop();
            } else if (Ranking[w][m] < Ranking[w][Current[w]])  {
                freeMen.pop();
                freeMen.push(Current[w]);
                Current[w] = m;
            }
        }
        cout<<endl;
        cout<<"Men\t"<<"Woman\n";
        for (w = 1; w <= N; w++)
            cout<< Current[w]<<"\t"<< w << endl;
    return 0;
}



