#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int p[110];

bool cmp(int a,int b)
{
    return a >b ;
}

int main()
{
    int T,n,i,Case=1,res=0;
    cin >> T;
    while ( T-- )
    {
        scanf("%d",&n);
        for (i=0; i<n; i++)
            scanf("%d",&p[i]);
        sort(p,p+n,cmp);
        for (i=1,res=0; i<n; i++)
        {
            res += i*p[i];
        }
       printf("Case #%d: %d\n",Case++,res);
    }

    return 0;
}
