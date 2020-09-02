//CONTROL PID

//VARIABLES PID

double E=0;
double A_p;
double A_d;
double A_i;
double I_error;

double E_1=0;
double I_error_1=0;
double dif_act= 0;
double Upid=0;
double Upid_c=0;

double Kp=0.01;
double Ki=0.0000725;
double Kd=0.0001;
double Ka=10;

void c_PID(){

double LTSK=LTS+273.15;
double SetPointK=SetPoint+273.15;
  
//LOGICA DEL CONTROLADOR
E=SetPointK-LTSK;
A_p=Kp*E;
A_d=Kd*(E-E_1);
I_error=E+I_error_1-Ka*dif_act;
A_i=Ki*I_error;

Upid=A_p+A_d+A_i;

if (Upid<=0){
  Upid=0;
  Upid_c=0;
}
else if (Upid>=30){
   Upid=30;
   Upid_c=30;
}
else if (Upid>0 && Upid<30){
    Upid_c = Upid;
}

LFV=Upid_c;

//actualización de variables
E_1=E;
I_error_1=I_error;
dif_act=Upid-Upid_c;

}
