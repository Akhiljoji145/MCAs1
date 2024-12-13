#include<stdio.h>
void main()
{
int limit,n,a[10],choice,left=0,right=0,value,i;
printf("enter the limit");
scanf("%d",&limit);
while(1)
{
printf("\nQueue Operations:\n1.Insert\n2.Delete\n3.Peek\n4.IsEmpty\n5.Size\n");
printf("enter the choice");
scanf("%d",&choice);
switch(choice){
case 1:
printf("enter the value :");
scanf("%d",&value);
if(a[right]==limit && a[left]==limit)
{
printf("\nqueue overflow");
}
else if(a[right]==0)
{
a[right]=value;
right+=1;
printf("\nvalue added successfully\n");
for(i=0;i<limit;i++)
{
printf("%d ",a[i]);
}
break;
case 2:
if(a[left]==right && a[right]==left)
{
printf("\nqueue is empty");
}
else 
{
a[left]=0;
left+=1;
}
for(i=0;i<limit;i++)
{
printf("%d",a[i]);
}
break;

case 3:
printf("%d",a[left]);
break;
case 4:
if(a[left]==right && a[right]==left)
{
printf("\nqueue is empty");
}
else
{
printf("\nstack is full");
}
break;
case 5:
if(a[left]==limit && a[right]==limit)
{
printf("\nqueue is empty");
}
else
{
printf("\nSize : %d",limit);
}
break;
}
}
}

}
