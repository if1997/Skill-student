#include <stdio.h>
#include<conio.h>
#include <stdlib.h>
#include<malloc.h>
#include <string.h>
#define LEN sizeof(struct user) 


typedef struct music
{
	char song[20];
	char singer[20];
	struct music *next;
}linklist;
linklist *head,*p,*s;

struct user
{
  char id[20];
  char code[20];
  struct user *unext;
};
struct user *uhead;   



//����ɾ��
int  Delete(void)
{
	linklist *q,*p;
	char Dsong[20],song[25];
	int
	ch='y';
	while(tolower(ch)=='y')
	{
		printf("��������Ҫɾ���ĸ��������س���ȷ�ϣ���");
		gets(Dsong);
		p=head;
		q=NULL;
		while(p!=NULL)
		{
			if(strcmp(p->song,Dsong))
			{
				q=p;
				p=p->next;
			}
			else
			{
				printf("\n*ɾ���ĸ����ǣ�%s,����Ϊ:%s\n",p->song,p->singer);
				printf("\t�����ٴ�ȷ��[y/Y]:");
				ch=getch();
				if(tolower(ch)=='y')
				{
					q->next=p->next;
					sprintf(song,"%s.txt",p->song);
					remove(song);
					break;
				}
			
			}
		}

		if(p==NULL)
		{
			printf("\n\n\t�����ڸø裬�밴���������\n");
			getch;
		}
		printf("\n\n\t*�Ƿ����ɾ����һ�׸���[y/Y],��ɾ��������������...\n");
		ch=getch();
	}
	return 1;
} 
//��Ӹ��� 
int Add()
{
	linklist *p3,*p2;
	char ch1,ch2,song[50],str[1024];

	FILE *fp2;
	p2=head;
	while(p2->next!=NULL)
			p2=p2->next;

	ch1='y';
	while(tolower(ch1)=='y')
	{
		p3=(linklist*)malloc(sizeof(linklist));
		printf("\n\t\t**���Ӹ���**");
		printf("\n\t���������밴���¸�ʽ���룺\n");
		printf("\n\t*����������������");
		gets(p3->song);
		printf("\n\t*����ø����ĸ�������");
		gets(p3->singer);
		printf("\n\t*����Ӹ��");
		printf("\n\t");
		gets(str);
		p3->next=NULL;
		
		ch1='0';
		printf("\n\t��ȷ����������[y/Y],�����������������:");
		ch2=getch();
		printf("\n%c\n",ch2); 
		if(tolower(ch2)=='y')
		{
			p2->next=p3; 
			p2=p3;
			printf("www\n");
			
			sprintf(song,"%s.txt",p3->song);                    //������Ӹ������д���ļ��� 
	   	 	if ((fp2=fopen(song,"w"))==NULL)
	 			
					printf("can not open file\n");
			else
			{
				fputs(str,fp2);
			}
			p3=NULL;
			fclose(fp2);
			printf("\n---������ӳɹ���");
		}
		else
		{
			printf("\n---δ����Ӹ������������������");
			getch();
				
		}
		printf("\n---�Ƿ������ӣ�������ӣ�����[y/Y]���������������");
		ch1=getch();
	
	}
	p2=NULL;
	return 1;
	
}

//�������Ŀ¼ 
int Savemusic()
{
	
	FILE *fp;
	struct music *p;
	p=head;
	if((fp=fopen("music.txt","w"))==NULL)
	{
		printf("\n�����ļ�������˶��ļ�����\n");
		fclose(fp);
		return 1;
	}
	else
	{
		rewind(fp);
		while (p!=NULL)
		{
				fprintf(fp,"%s\t%s\n",p->song,p->singer);
			p=p->next;
		}
		fclose(fp);
		return 1;
	}
	
}


//�޸ĸ�����Ϣ
int Modify()
{
	linklist *q,*p2,*p3;
	char Msong[20];
	char ch,str[1024],s[20];
	FILE *fp1,*fp2;
	char song[25],song1[25],song2[25];
	do
	{
		printf("\n\t*��������Ҫ�޸ĵĸ��������س���ȷ�ϣ���");
		gets(Msong);
		p=head;
		q=NULL;
		while(p!=NULL)
		{
			if(strcmp(p->song,Msong))
				p=p->next;
			else
			 break;
		}
		
	
				printf("\n\t*��Ҫ�޸ĵĸ����ǣ�%s,�ø����Ϊ %s\n",p->song,p->singer);
				printf("\n\t*��������Ҫ�޸ĵ���Ϣ����:");
				printf("\n\t1.������  2.������  3.���\n");
				printf("\n\t��ѡ��[1/2/3]:");
				ch=getch();
				switch(ch)
				{
					case'1':printf("\n\t*�������޸ĸ�������");
							gets(p->song);
							sprintf(song1,"%s.txt",Msong); 
							sprintf(song2,"%s.txt",p->song); 
							rename(song1,song2);
							break;
					case'2':printf("\n\t*�������޸ĸ�����������");
							gets(p->singer);
							break;
					case'3':printf("\n\t*��������Ӹ��\n");
							gets(str);
							sprintf(song,"%s.txt",p->song);                    //������Ӹ������д���ļ��� 
	   	 					if ((fp2=fopen(song,"w"))==NULL)
	 						{
								printf("can not open file%s\n",s);
								break;
							}
							else
							{
					
							fputs(str,fp2);
							fclose(fp2);
							break;
							}
							
					default:printf("\n---�����������������:\n");
							break;
				}
			
		if(p==NULL)
		{
			printf("\n---��������Ҫ�޸ĵĸ������밴���������\n");
			getch;
		}
		printf("\n---�Ƿ�����޸�[y/Y],���޸İ�����������...\n");
		ch=getch();
	} while(tolower(ch)=='y');
	return 1;
} 

//����Ա���� 
int Admi()
{

			char chp;
			int legalUser;
			printf("* * * * * * * * * * * * * * ** * * * * * * * * * * * * * * ** * * * * * * * * * * *");
			printf("\n* * * * * * * * * * * * * * * ����Ա��¼�ɹ�����* * * * * * * * * * * * * * * *\n");
			printf("\n\t*1.��Ӹ���");
			printf("\n\t*2.ɾ������");
			printf("\n\t*3.�޸ĸ���");
			printf("\n\t*0.�˳���¼");
			
			printf("\n\n\t��ѡ��[1/2/3/4/0]:");
			chp=getche();
			switch(chp)
			{
				case '1':
				 	Add();
					Savemusic();
					Admi();
					break;                                                                                 
				
				case'2':
				Delete();
				Savemusic();
				Admi();
					break;
					
				case'3':
				Modify();
				Savemusic();
				Admi();
					break;
				case'0':legalUser=0;
					break;
				default:printf("ѡ�����\n");
					legalUser=1;
					Admi();
					break;
			}
			return legalUser;
		}




//����Ա��½
int VerificationIdentity()
{
	char userID[20],password[20];    //����ɼ���������û����Ϳ��� 
	char superUID[20],passWD[20];    //����ļ��ж�ȡ���û����Ϳ��� 
	int i,legalUser;
	char ch;
	FILE *fp;
	legalUser=0;
	fp=fopen("superUser.txt","r");
	if(fp==NULL)
	{
		printf("\n\t�ļ������ڣ������������..\n");
		getch();
	}
	else
	{
		do
		{
			ch='0';
			printf("\n\t\t\t   *����Ա��½*    \t\t");
			printf("\n*****�������û���(<15���ַ�):");
			gets(userID);
			
			printf("\n*****����������(<15������,��ĸ�����):");
			gets(password);
			
			rewind(fp);
			while(!feof(fp))
			{
				fscanf(fp,"%s\t%s",superUID,passWD);
				if((strcmp(userID,superUID)==0)&&(strcmp(password,passWD)==0))
				{
					legalUser=1;
					break;
				}
				else
				{
				legalUser=0;
				printf("\n----��������Ƿ���Ҫ���������û��������룿(y/n)");
				ch=getch();
				}
			}
		}
		while((ch=='y')||(ch=='Y'));
	}
	fclose(fp);
	return legalUser;
}













//��ʼ��������Ϣ
int InitMusic()
{
	FILE *fp;
	struct music *p1,*p2;
	fp=fopen("music.txt","r");
	if(fp==NULL)
	{
		printf("δ�ܳ�ʼ��\n");
		fclose(fp);
		return 0;
	}
	else
	{
		p1=(struct music *)malloc(sizeof(linklist));
		head=p1;
	
		while(!feof(fp))
		{
			fscanf(fp,"%s\t%s\n",p1->song,p1->singer);
			p2=p1;
			p1=(struct music*)malloc(sizeof(linklist));
			p2->next=p1;
			
		}
		p2->next=NULL;
		p2=NULL;
		p1=NULL;
		p1=head;
		
		
		fclose(fp);
		return 1;
	}
	
} 

//�û���¼���� 
int user()
    {
      int userflag=1; 
      char ch,ch1;
      while(userflag)
     {
        printf("\n\t ----------------------��ӭ�����û�����-------------------\n");
        printf("\t                        1.ע��                              \n");
        printf("\t                         2.��¼                             \n");
        printf("\t                         0.�˳�                             \n");
        printf("\t -----------------------------------------------------------\n");
        printf("\t*����������ѡ��(0/1/2):");
        ch=getche();
        getch();
        switch (ch)
       {
          case'1' : userflag=signin();//����ע��ģ��,ע��ɹ�����2 
          break;
          case'2' : userflag=login();//���õ�¼ģ�飬��¼�ɹ�����1 
          break;
          case'0' : userflag=0;
          break;
          default : printf("\n\t*�������������ѡ��\n\n\n");
          break;
       }
       
     }
      return userflag;
    }
    
    
//ע�ắ��
int signin()
    {
    	read(); 
      struct user *p3,*p2;
      char ch;
      int signinflag;
      
      p2=uhead;
      while (p2->unext!=NULL)
      p2=p2->unext;
      ch='y';
        p3=(struct user*)malloc(LEN);
        printf("\n\t*�밴���¸�ʽ����\n");
        printf("\t*������ע���û�����");
        gets(p3->id);
        printf("\n\t*���������룻");
        gets(p3->code);
        p3->unext=NULL;
        printf("\n\t*��ȷ����������(Y/y),�����������������......"); 
        ch=getche();
        if((ch=='y')||(ch=='Y'))
        {
          p2->unext=p3;
          p2=p3;
          p2->unext=NULL;
          save();  //ע�����ӵ��û��������ļ� 
          printf("\n\t*��ϲ��ע��ɹ��������������......");
          getch();
          putch('\n');
          signinflag=2;
        }
        else
        {
          printf("\n\t*δ��ע��ɹ����������������.......");
          getch();
          putch('\n');
          signinflag=0;
        }
        free(p3);
        return signinflag;
    }
      
        
      
    
      
        
      
    
//��¼����
int login()
    { 
      read();
      char ch,ch1;
      char id[20],code[20];
      struct user *p;
      int flag=0,xflag;
      p=uhead;
      do 
      {
        printf("\n\t*�����û�����С��19���ַ���:");
        gets(id);
        printf("\n\t*���������루С��19�����֣�:");
        gets(code);
        while (p!=NULL)
        {
          if((strcmp(id,p->id)==0)&&(strcmp(code,p->code)==0))
          {
          	flag=1;
            break;
		  }
          else
            p=p->unext;
        }
        if(flag)//��½�ɹ�����ʼѡ��
        {
          while(xflag)
          {
            printf("\n\t* * * * * * * * * * * *��ӭ�������û�������* * * * * * * * * * * * * *\n");
            printf("\t                          1.���                                         *\t");
            printf("\t                          2.�޸�����                                     *\n");
            printf("\t                           0.�˳�                                        *\n");
            printf("\t   * * * * * * * * * * * * * * *  * * * * * * * * * * * * * * * * * * * * \n") ;
            printf("\n\t*������ѡ��1/2/0��:");
            ch=getche();
            ch1=getch(); 
            putch('\n');
            switch(ch)
            {
              case'1':xflag=diange();
              break;
              case'2':xflag=change();
              break;         
			  case'0':xflag=0;
              break;
              default:printf("\n\t*�������,���������룺");
              xflag=3;break;
            }
          }
          break;
        }
        else  //��½ʧ��
        {
        	printf("\n\t *�û���������������"); 
          printf("\n\t*�Ƿ����������û��������룿��y/n��");
           ch=getche();
           getch();
           putch('\n');
        }
      }
      while (ch=='y'||ch=='Y');
      return 0;
    }
    
            
//��躯��
int diange()
{
	char song[20],singer[20];
	char ch;
	int flag=1,diangeflag=0;
	while(flag)
	{
		printf("\n\t1.����������             ");
	    printf("\n\t2.����������             ");
	    printf("\n\t0.�˳�                    "); 
	    printf("\n\t*������ѡ��1/2/0��:");
        ch=getche();
        getch();
        switch(ch)
        {
    	  case '1':  flag=findsong();
    	  break;
    	  case '2': flag=findsinger();
    	  break;
    	  case '0': 
    	  {
    	  	flag=0;
    	  	diangeflag=1;
    	    break;
		  }
		  
    	  default: printf("\n\t*�������,���������룺");
    	  break;
	    }
        if(flag==4)//����ʧ�ܱ�־
        {
          printf("\n\t*�������ҵĸ���/���ֲ����ڣ�\n");
          printf("\t*�Ƿ�������ң�(y/n)");
          ch=getche();
          getch();
          putch('\n');
          if((ch=='y')||(ch=='Y'))
             ;
          else diangeflag=1;
        }
	
	}

	 return diangeflag;
 } 

//�޸��û�����//���� 
int change()
{
	int i;
	char ch,ch1;
	struct user *p,*q;
	
	int flag=1,flag2=0;
	char code[20],code1[20],code2[20];
	printf("����������ԭʼ���룺(���س���ȷ��)");
	gets(code); 
	p=uhead;
		q=NULL;
		while(p!=NULL)
		{
			if(strcmp(p->code,code)==0)
			{
				//flag2=1;
		      	break;
			}
			else
	    	  	p=p->unext;
		}
		
		while(1)
		{
			printf("\n���������������룺�����س���ȷ�ϣ�");
			gets(code1);
			for(i=0;i<3;i++)
			{
				printf("\n���ٴ�����ȷ�������룺�����س���ȷ�ϣ�");
			    gets(code2); 
			    if(strcmp(code1,code2)==0)
			    {
			    	printf("\n����ȷ���Ƿ������Ա������������޸ġ�y/n��");
			    	ch1=getche();
			    	getch();
					if((ch1=='y')||(ch1=='Y'))
					{  
					    strcpy(p->code,code1);
						save();
			            flag=0;
					}
			    }
			    if(flag==0)
			    	break;
			    else 
			    	continue;
			    
			}
			if(i==3)
			{
				printf("\n�޸�����ʧ�ܣ����������û��������");
				flag=0;
			}
			else
			{
				printf("\n�޸�����ɹ��������µ�½");
				break;
			}
		}

	return flag;
} 

//���޸���Ϣ�������ļ���

int  save()
{
	FILE *fp;
	struct user *p;
	p=uhead;
	if((fp=fopen("user.txt","w"))==NULL)
	{
		printf("\n\t*�����ļ�����������˶��ļ�����\n");
		fclose(fp);
		return 1;
	}
	else
	{
		rewind(fp);
		while (p!=NULL)
		{
			fprintf(fp,"%s\t%s\n",p->id,p->code);
			p=p->unext;
		}
		fclose(fp);
		return 0;
	}
}

//����������
 int findsong()
     {
     	int i;
       FILE *fp; 
	   char s[20],str[1000];
       struct music  *p;
       char song[20];
       int flag=4;//����ʧ�ܱ�־
       p=head;
       printf("\n\n\t*������Ҫ���ҵĸ�����");
       gets(song);
       while(p!=NULL)
       {
         if(strcmp(p->song,song)==0)
         {
         	output(song);
	        fclose(fp);
            flag=1;
            printf("\n\t*��������˳�......");
            getch();
          }
          p=p->next;
       }
       return flag;
     }
 
 //�����ֲ���
 int findsinger()
     {
       char  song[50][20];
       char singer[20];
       int flag=4,i=0,j,k;   //����ʧ�ܱ�־
       struct music *p;
    
       p=head;
       printf("\n\n\t*������Ҫ���ҵĸ���������");
       gets(singer);
       while(p!=NULL)
       {
         if(strcmp(singer,p->singer)==0)
         {
          i++;
          strcpy(song[i-1],p->song);
        
         }
        

         flag=1;
         p=p->next;
       }
       if(flag!=4)
       {
         printf("\n\n\t*�ø��ֵĸ������£�\n");
         for(j=0;j<i;j++)
         printf("\t*%d\t%s\n", j+1,song[j]);
         printf("\n\t*������Ҫ���ҵĸ������(����):");
         scanf("%d",&k) ;
         output(song[k-1]);
         printf("\n\t*��������˳�......");
         getch();
       }
       return flag;
     }


//��ӡ������Ӧ���ļ�
int output(char p[])
{
	int i;
	FILE *fp; 
	char s[20],str[1000];
		   sprintf(s,"%s.txt",p);
       	   if ((fp=fopen(s,"r"))==NULL)
	       {
	   	    printf("\n\t*can not open file%s\n",s);
		    exit(0);
	       }
	       fgets(str,1000,fp);
	       printf("\n\t��ʣ�");
	       puts(str);
	       fclose(fp);
	       return 0;
} 

//���ļ��ж�ȡ�û���������,��ŵ������� 
int read()
{
	FILE *fp;
	struct user *p1,*p2;
	fp=fopen("user.txt","r");
	if(fp==NULL)
	{
		printf("\n\t*δ�ܳ�ʼ���û���Ϣ\n");
		fclose(fp);
		return 0;
	}
	else
	{
		p1=(struct user*)malloc(LEN);
		uhead=p1;   //���������û���Ϣ���������uhead��  
		while(!feof(fp))
		{
			fscanf(fp,"%s\t%s\t\n",p1->id,p1->code);
			p2=p1;
			p1=(struct user*)malloc(LEN);
			p2->unext=p1;
		}
		p2->unext=NULL;
		p2=NULL;
		free(p1);
		fclose(fp);
		return 1;
	}
} 

int main()
 {
 	int i,legalUser=0;
 	char chp='0',ch;
 	InitMusic();
	read();
 	
 	do
	{
		printf("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *");
		printf("\n           					                    	 ");
		printf("\n\t* * * * * * * * * * * *��ӭ������ϵͳ* * * * * * * * * * * **");
		printf("\n\t*                        			              *\t");
		printf("\n\t*                        1.�û���¼                           *");
		printf("\n\t*                        			              *\t");
		printf("\n\t*                        2.����Ա��¼                         *");
		printf("\n\t*                        			              *\t");
		printf("\n\t*                        0.�˳�                               *");
		printf("\n\t*                        			              *\t");
		printf("\n\t*                      ��ѡ�����[1/2/0]                        *");
		printf("\n\t*                        			              *\t");
		printf("\n\t* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n");
	 
		chp=getch();		
	
		switch(chp)
		{
			case'1':
					if(user()!=0)
						legalUser=1; 
					else
						legalUser=0;
				
					break;
			case'2':
			if(VerificationIdentity()==1)
			{	
				if(Admi()==1)
					legalUser=0;
				break;
			}
			 
					
			else 	legalUser=0;
					break;
			case'0':
					return 0;
			default:
				system("cls");
				printf("ѡ�����\n");
				legalUser=0;
					break;
			
		}
	
	} while(legalUser==0);
	return 0;
}


