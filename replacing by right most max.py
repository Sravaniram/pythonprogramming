#include <stdio.h>

int main()
{int a[100],i,j,k,max=0;
scanf("%d",&k);
for(i=0;i<k;i++)
scanf("%d",&a[i]);
for(i=0;i<k;i++)
{   max=0;
    for(j=i+1;j<k;j++)
    {
        if(max<a[j])
        max=a[j];
    }
    a[i]=max;
}
for(i=0;i<k;i++)
printf("%d ",a[i]);

    return 0;
}
