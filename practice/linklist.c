#include <stdio.h>
#include <stdlib.h>

struct node
{
  int data;
  struct node *next;
};
void insert_first(struct node**,int);
void insert_last(struct node**,int);
void insert_pos(struct node**,int,int);
void delete_first(struct node**);
void delete_last(struct node**);
void traverse(struct node*);
void count(struct node**);
void reverse(struct node**);
void main()
{
  struct node *head=NULL;
  int ch, pos, item,a;
  while(1)
  {
      printf("\n 0. exit \n 1. insert at the begining \n 2. inssert at the last \n 3. insert at specific position \n 4. delete from the first\n 5. delete from the last \n 6. count the element \n 7. reverse \n 8. traverse \n \n enter your choice : ");
      scanf("%d",&ch );
      switch (ch)
      {
        case 0: exit(0);
        case 1: printf("enter the infomation : ");
                scanf("%d",&item);
                insert_first(head,item);
                break;
        case 2: printf("enter the infomation : ");
                scanf("%d",&item);
                insert_last(head,item);
                break;
        case 3: printf("enter the infomation : ");
                scanf("%d",&item);
                printf("enter the position :");
                scanf("%d\n",&pos);
                insert_pos(head,item,pos);
                break;
        case 4: head=delete_first(head);
                break;
        case 5: head=delete_last(head);
                break;
        case 6: head=count(head);
                break;
        case 7: head=reverse(head)
                break;
        case 8: traverse(head);
                break;
        case 9: head=sort(head);
                break;
        default:printf("wrong input .!! :( \n");
                exit(0);
      }
  }
}


void traverse(struct node*head)
{
  loc=head;
  while loc!=NULL
  {
    printf(info->loc);
    loc=next->loc
  }
}


void insert_first(struct node**phead,item)
{
  newnode=(struct node *)malloc(sizeof(struct node))
  newnode->info=item
  newnode->next=*phead
  *phead=newnode
  return;
}


void insert_last(struct node*head, item)
{
  loc=head
  newnode=(struct node *)malloc(sizeof(struct node))
  newnode->info=item;
  newnode->next=NULL;
  if (loc== NULL)
  {
    newnode=head;
  }
  else
  {
    while (loc->next != NULL)
    {
      loc=loc->next;
    }
    loc->next=newnode;
  }
  return;
}


void count(struct node*head)
{
  loc=head
  cnt=0
  while (loc!=NULL)
  {
    cnt+=1
    loc=loc->next
  }
  return(cnt);
}


void insert_pos(struct node*head,item,pos)
{
  if (head==NULL)
  {
    printf("empty list\n");
    return;
  }
  loc=head;
  ncnt=1;
  while (loc!=NULL && pos-1>nct)
  {
    ncnt+=1;
    loc=loc->next;
  }
  if (loc==NULL || pos<=0)
  {
    printf("position given is invalid\n");
    return;
  }
  newnode=(struct node *)malloc(sizeof(struct node))
  newnode->info=item;
  if (pos==1)
  {
    newnode->next=head;
    head=newnode;
  }
  else
  {
    newnode->next=loc->next;
    loc->next=newnode;
  }
  return;
}


void delete_first(struct node*head)
{
  if (head==NULL)
  {
    printf("empty list\n");
  }
  temp=head;
  head=head->next;
  printf("info->temp\n");
  temp->next=NULL;
  free(temp);
  return;
}


void delete_last(struct node*head)
{
  if (head==NULL)
  {
    printf("empty list\n");
    return;
  }
  loc=head;
  while(loc->next!=NULL)
  {
    locp=temp;
    loc=locp->next;
  }
  if (loc==head)  /* next->t=NULL*/
  {
    head=NULL;
  }
  else
  {
    locp->next=NULL
  }
  printf(loc->info);
  free(loc);
  return;
}


void reverse(struct node**head)
{
  if (head==NULL || head->next=NULL)
  {
    return;
  }
  loc=head;
  locp=NULL;
  while(loc!=NULL)
  {
    locn=loc->next;
    loc->next=locp;
    locp=loc;
    loc=locn;
  }
  head=locp;
  return;
}
