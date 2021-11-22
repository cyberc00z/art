#include <iostream>
using namespace std;

extern "C" {
   int ProcC_CallWithParameterList(int, int);
   int ProcC_CallWithStackFrame(int, int);

   int __stdcall ProcSTD_CallWithParamterList(int, int);
   int __stdcall ProcSTD_CallWithStackFrame(int, int);
}

extern "C" {
   int ReadFromConsole(unsigned char);
   void DisplayToConsole(char *, int);
   void DoSubtraction();
}

int ReadFromConsole(unsigned char by){
    cout << "Enter " << by << ": ";
    int i;
    cin >> i;
    return i;
}

void DisplayToConsole(char* x, int n)
{
    cout << x << n << endl << endl;
}

int main(){
    DoSubtraction();

    cout << "C-Call With Paramters : 10-3 =  " << ProcC_CallWithParameterList(10, 3) << endl;
    cout << "C-Call With Stack Frame : 10-3 = " << ProcC_CallWithStackFrame(10, 3) << endl;
    cout << "STD-Call With Paramters :  10-3 = " << ProcSTD_CallWithParamterList(10,3) << endl;
    cout << "STD-Call With Stack Frame : 10-3 = " << ProcSTD_CallWithStackFrame(10,3) << endl;
    system("pause");
}
