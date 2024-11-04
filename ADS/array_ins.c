#include<stdio.h>
void main()
{
int i,a[10],n,pos,in;
printf("enter the limit");
scanf("%d",&n);
printf("enter the numbers");
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
printf("enter the number to be inserted");
scanf("%d",&in);
printf("enter the position");
scanf("%d",&pos);
for(i=n;i>=pos;i--)
{
a[i]=a[i-1];
}
a[pos-1]=in;
printf("Array after deletion :");
for(i=0;i<n;i++)
{
printf("%d",a[i]);
}
}
