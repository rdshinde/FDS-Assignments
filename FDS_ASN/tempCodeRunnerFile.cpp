for(int i=0;str[i]!='\0';i++)
	{
		if(str[i]=='(' || str[i]=='[' || str[i]=='{')
			push(str[i]);
		if(str[i]==')'||str[i]==']'||str[i]=='}')
		{
			ch=pop();
			if((str[i]==')'&& ch!='(') ||(str[i]==']'&& ch!='[')||(str[i]=='}'&& ch!='{'))
			{
				cout<<"\nNot parenthesized At "<<i<<" = "<<str[i];
				flag=1;
				break;
			}
		}