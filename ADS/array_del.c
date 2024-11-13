#include<stdio.h>
void main()
{
int a[10],i,n,pos;
printf("Enter the limit :");
scanf("%d",&n);
printf("Enter the elements :");
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
printf("Array elements are :");
for(i=0;i<n;i++)
{
printf("%d",a[i]);
}
printf("Enter the position to delete :");
scanf("%d",&pos);
for(i=pos;i<n;i++)
{
a[i]=a[i+1];
}
printf("\nconverted array");
for(i=0;i<n-1;i++)
{
printf("%d",a[i]);
}
}
