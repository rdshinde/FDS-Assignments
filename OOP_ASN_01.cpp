#include<iostream>
#include<bits/stdc++.h>
using namespace std;

class Complex
{
public:

// real variable to hold value of real part and img to hold value of imaginary part
int real,img;
//+ operator overloading
Complex operator +(Complex b)
{
Complex temp;
temp.real=real+b.real;
temp.img=img+b.img;
return temp;
}

//- operator overloading
Complex operator -(Complex b)
{
Complex temp;
temp.real=real-b.real;
temp.img=img-b.img;
return temp;
}
};

int main ()
{
//clrscr();

//Object of class Complex are created
Complex a,b,c,d;
cout<<"\nEnter real and imaginary part of first complex number:";
cin>>a.real>>a.img;
cout<<"\nEnter real and imaginary part of second complex number:";
cin>>b.real>>b.img;
c=a+b;
cout<<"\n("<<a.real<<" + "<<a.img<<"i) + ("<<b.real<<" + "<<b.img<<"i) = ("<<c.real<<" + "<<c.img<<"i)";
d=a-b;
cout<<"\n("<<a.real<<" + "<<a.img<<"i) - ("<<b.real<<" + "<<b.img<<"i) = ("<<d.real<<" + "<<d.img<<"i)";

return 0;
}