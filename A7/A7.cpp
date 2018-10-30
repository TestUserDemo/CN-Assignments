#include<iostream>
#include<iomanip>
#include<fstream>
#include<string>

using namespace std;

int main()
{
	cout<<"Packet Analyser"<<endl;
	string sr_no, time, source, destination, protocol, len, info;
	int i, count, choice;

	do
	{
		ifstream file("packetsCaptured.csv");
		count=-1;
		i=0;
		cout<<"\nEnter the protocol you want to see";
		cout<<"\n1.IP\n2.TCP\n3.UDP\n4.Ethernet\n5.All protocols\n6.Exit";
		cin>>choice;
		
		string protocolChoice;
		switch(choice)
		{
			case 1:
				protocolChoice="ICMP";
				break;
			case 2:
				protocolChoice="TCP";
				break;
			case 3:
				protocolChoice="UDP";
				break;
			case 4:
				protocolChoice="ARP";
				break;
			case 5:
				protocolChoice="ALLPROTOCOLS";
				break;
			case 6:
				break;
		}
		while(file.good() and choice!=6)
		{
			getline(file, sr_no, ',');
			getline(file, time, ',');
			getline(file, source, ',');
			getline(file, destination, ',');
			getline(file, protocol, ',');
			getline(file, len, ',');
			getline(file, info, '\n');
			
			protocol= string(protocol, 1, protocol.length()-2);
			
			if(protocol==protocolChoice || protocol=="Protocol" || protocolChoice=="ALLPROTOCOLS")
			{
				cout<<setw(8)<<left<<i++;
				cout<<setw(30)<<left<<string(source, 1, source.length()-2);
				cout<<setw(30)<<left<<string(destination, 1, destination.length()-2);
				cout<<setw(8)<<left<<protocol;
				cout<<setw(8)<<left<<string(len, 1, len.length()-2);
				cout<<string(info, 1, info.length()-2)<<"\n\n";
				count++;
				
			}
		}
		file.close();
		if(choice!=6)
			cout<<"\nTotal packets"<<count;
	
	}while(choice!=6);

	return 0;

}
