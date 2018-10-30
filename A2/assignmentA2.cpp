#include <bits/stdc++.h>

using namespace std;

class Encoder
{
	private:
		vector<int> generator;
		vector<int> codeword;
		vector<int> dataword;
		vector<int> transmit;
		int k,n,g,r;
	public:
		void getDataword();
		void getGenerator();
		void getCodeword();
		void trans();
		void remain();
	
};

void Encoder::getDataword()
{
	string s;
	cout<<"\n Enter the dataword :";
	cin>>s;
	
	//Validations
	for(int i=0; i<s.length();i++)	
	{
		if(s[0]=='0')
		{
			cout<<"\n Invalid. Number should not begin with zero";
			exit(0);
		}
		if((s[i]!='0') && (s[i]!='1'))
		{
			cout<<"\n Invalid";
			exit(0);
		}
	}
	
	//Convert char into int and push it into vector in the same order as before
	for(size_t i=0; i<s.size(); ++i)
	{
		dataword.push_back(s[i]-'0');
	}
	
	k=dataword.size();
	cout<<"\n Dataword size (k) : "<<k<<endl;
}

void Encoder::getGenerator()
{
	string s;
	cout<<"\n Enter the generator : ";
	cin>>s;
	
	//Validations
	for(int i=0; i<s.length(); i++)
	{
		if(s[0]=='0')
		{
			cout<<"\n Error. Number should not begin with zero";
			exit(0);
		}
		
		if((s[i]!='0') && (s[i]!='1'))
		{
			cout<<"\n Invalid";
			exit(0);
		}
	}
	
	//Convert char into int and push it into vector in the same order as before
	for(size_t i=0; i<s.size(); i++)
	{
		generator.push_back(s[i]-'0');
	}
	
	g=generator.size();
	cout<<"\n Generator size (g) : "<<g<<endl;
	
	//Calculate codeword size
	n=g+k-1;
	cout<<"\n Codeword size (n=g+k-1) : "<<n<<endl;
	
	//Calculate no. of redundant bits
	r=n-k;
	cout<<"\n Redundant bits (r=n-k) : "<<r<<endl;
	
}

void Encoder::getCodeword()
{
	int i,j,l;
	for(i=0; i<k; i++)		//push dataword
	{
		codeword.push_back(dataword[i]);
	}
	for(i=0; i<r; i++)		//append redundant bits
	{
		codeword.push_back(0);
	}
	cout<<"\n After appending zeros : ";
	for(i=0; i<codeword.size(); i++)
	{
		cout<<codeword[i]<<setw(2);
	}
	cout<<endl;
	
	for(i=0;i<k;i++)
	{
		j=0;
		l=i;
		if(codeword[l]>=generator[j])
		{
			for(j=0, l=i; j<g; j++,l++)
			{
				if((codeword[l]==1 && generator[j]==1) || (codeword[l]==0 && generator[j]==0))
				{
					codeword[l]=0;
				}
				else
				{
					codeword[l]=1;
				}
			}
		}
	}
	
	vector<int> crc(n);
	for(i=0,j=k; i<r; i++,j++)
	{
		crc[i]=codeword[j];
	}
	cout<<"\n CRC bits : ";
	for(i=0;i<r;i++)
	{
		cout<<crc[i]<<setw(2);
	}
	
	cout<<"\n\n Codeword generated for transmission : ";
	codeword.clear();
	
	for(i=0;i<k;i++)
	{
		codeword.push_back(dataword[i]);
	}
	for(i=0;i<r;i++)
	{
		codeword.push_back(crc[i]);
	}
	for(i=0;i<n;i++)
	{
		cout<<codeword[i]<<setw(2);
	}
	
}

void Encoder::trans()
{
	char ch;
	int i,c;
	cout<<"\n\n Press 'a' if you want to alter a bit else enter any letter : ";
	cin>>ch;
	
	for(i=0; i<n; i++)
	{
		transmit.push_back(codeword[i]);
	}
	
	if(ch=='a' || ch=='A')
	{
		cout<<"\n Enter the bit you want to alter : ";
		cin>>c;
		
		if(transmit[c]==0)
		{
			transmit[c]=1;
		}
		else
		{
			transmit[c]=0;
		}
	}
		
	cout<<"\n The codeword transmitted will be :";
	for(i=0;i<n;i++)
	{
		cout<<transmit[i]<<setw(2);
	}	
}

void Encoder::remain()
{
	int i,j,l;
	for(i=0;i<k;i++)
	{
		j=0;
		l=i;
		if(transmit[l]>=generator[j])
		{
			for(j=0, l=i; j<g; j++,l++)
			{
				if((transmit[l]==1 && generator[j]==1) || (transmit[l]==0 && generator[j]==0))
				{
					transmit[l]=0;
				}
				else
				{
					transmit[l]=1;
				}
			}
		}
	}
	
	vector<int> remainder(n);
	for(i=0,j=k; i<r; i++,j++)
	{
		remainder[i]=transmit[j];
	}
	cout<<"\n\n Remainder : ";
	for(i=0;i<r;i++)
	{
		cout<<remainder[i];
	}
	
	int flag=0;
	for(i=0;i<r;i++)
	{
		if(remainder[i]!=0)
		{
			flag=1;
		}
	}
	
	if(flag==0)
	{
		cout<<"\n\n As syndrome is zero, CRC pass";
	}
	else
	{
		cout<<"\n\n As syndrome is non zero, CRC not pass and message transmitted from sender to receiver contains error";
	}
	cout<<endl;
}


int main()
{
	Encoder e;
	e.getDataword();
	e.getGenerator();
	e.getCodeword();
	e.trans();
	e.remain();
	return 0;
}
