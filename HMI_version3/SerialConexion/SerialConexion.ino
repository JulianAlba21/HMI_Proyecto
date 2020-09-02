//LIBRERIAS
#include <Wire.h>
#include <Adafruit_ADS1015.h>
#include <TimerOne.h>

//DIRECCIÓN COMUNICACION ADS1115
Adafruit_ADS1115 ads(0x49);

//VARIABLES GENERALES DE CONTROL

//LONGS
unsigned long timer=0;
long deltaT = 5000; //us

//BOOLS
bool ModoM=false;
bool ModoA=false;
bool enviar=false;
bool V=true;//Estado variador
bool LQR=false;//Estado control LQR codigo L
bool PID=false;//Estado control PID codico N

//DOUBLES
double P=0; //Variable proporcional
double I=0; //Variable integral
double D=0; //Variable derivativa

double LTE = 0.0; //Lectura Temperatura de Entrada
double LTS = 0.0; //
double LTG = 0.0;
double LTC = 0.0;
double LFV = 0.0; //Lectura frecuencia variador/ señal de control
double MFV = 0; //Manual frecuencia variador
double SetPoint = 0; //Set point

//DECLARARCION DE PINES
int rele=7;
int variador =9;
int SensorTE = A0;
int SensorTS = A1;

// FUNCIONES

void timeSync(unsigned long deltaT){
  unsigned long currTime = micros();
  long timeToDelay = deltaT - (currTime - timer);
  if (timeToDelay > 5000){
    delay(timeToDelay / 1000);
    delayMicroseconds(timeToDelay % 1000);}
  else if (timeToDelay > 0){
    delayMicroseconds(timeToDelay);}
  else{
      // timeToDelay is negative so we start immediately}
  timer = currTime + timeToDelay;}
}
