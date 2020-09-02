//CONTROL LQR
  
//VARIABLES LQR

double Ek=0;
double Vk=0;
double Vk_1= 0;
double Ulqr=0;
double Ulqr_c;

//varibales a kelvin

double LTSK=LTS+273.15;
double SetPointK=SetPoint+273.15;


// Matriz CL
double CL11=1;
double CL12=0;

// Matriz Kest
double Kest11=0.0428;
double Kest12=0.0001;

// Matriz Ki
double Ki11=3.5349e-04;


void c_LQR(){

LTSK=LTS+273.15;
SetPointK=SetPoint+273.15;

//Logica del controlador
Ek=SetPointK-LTSK;//error= Setpoint[K] - LecturaTermocuplaSalida[K]
Vk=Ek+Vk_1;
Ulqr=Ki11*Vk - Kest11*LTSK;


//saturacion de actuadores
if (Ulqr <=0){
  Ulqr_c=0;
  }
else if (Ulqr>30){
  Ulqr_c=30;
  }
else if (Ulqr>0 && Ulqr<30){
    Ulqr_c = Ulqr;
}

//Actualizacion de registros
Vk_1=Vk;


LFV=Ulqr_c;
}
