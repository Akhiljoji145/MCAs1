#include<stdio.h>
void main()
{
int i,arr[10],search,n;
printf("Enter the limit");
scanf("%d",&n);
printf("Enter the elements");
for(i=0;i<n;i++)
{
scanf("%d",&arr[i]);
}
printf("Enter the to be found");
scanf("%d",&search);
for(i=0;i<n;i++)
{
if(search==arr[i])
{
printf("element found at location : %d\n",i);
}
}
}
