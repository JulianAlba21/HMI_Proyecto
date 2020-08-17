#include <Wire.h>
#include <Adafruit_ADS1015.h>
#include <TimerOne.h>

Adafruit_ADS1115 ads(0x49);

unsigned long timer=0;
long deltaT = 5000; //us

bool ModoM=false;
bool ModoA=false;

bool enviar=false;

bool V=true;//Estado variador

bool LQR=false;//Estado control LQR codigo L
bool PID=false;//Estado control PID codico N

double P=0; //Variable proporcional
double I=0; //Variable integral
double D=0; //Variable derivativa

//pines de arduino
int rele=7;
int variador =9;
int SensorTE = A0;
int SensorTS = A1;

double LTE = 0.05;
double LTS = 0.08;
double LTG = 0.09;
double LTC = 0.010;
double LFV = 0; //Lectura frecuencia variador/ señal de control

double MFV = 0; //Manual frecuencia variador

double SetPoint = 0; //Set point

void setup(){

pinMode(LED_BUILTIN, OUTPUT);
pinMode(variador, OUTPUT);
pinMode(rele, OUTPUT);
pinMode(SensorTE, INPUT);
pinMode(SensorTS, INPUT);

timer = micros();
digitalWrite(LED_BUILTIN, LOW);

digitalWrite(rele,V);
Serial.begin(38400);
delay(10);
//ads.setGain(GAIN_TWOTHIRDS);
ads.begin();
delay(500);
}
void loop(){
timeSync(deltaT);

if (enviar== true){
LTE = ads.readADC_SingleEnded(0)*0.0176;
LTG = ads.readADC_SingleEnded(1)*0.0826;
LTC = ads.readADC_SingleEnded(2)*0.08;
LTS = ads.readADC_SingleEnded(3)*0.0186;
//Serial.print(LTE); Serial.print('\t');
//Serial.print(LTG); Serial.print('\t');
//Serial.print(LTC); Serial.print('\t');
//Serial.print(LTS); Serial.println('\t');
senToPc(&LTE, &LTG, &LTC, &LTS);
}
getSerialData();

if(!Serial) {  //check if Serial is available... if not,
Serial.end();      // close serial port
delay(100);
Serial.begin(38400); // reenable serial again
}

}

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

void getSerialData(){
  while (Serial.available()){
    char input = Serial.read();
    String tmp = "";
    switch(input){
    
      case 'A':
        digitalWrite(LED_BUILTIN, LOW);
        ModoM=false;
        ModoA=!ModoA;
        break;
      case 'M':
        digitalWrite(LED_BUILTIN, HIGH);
        ModoA=false;
        ModoM=!ModoM;
        break;
      case 'E':
        enviar=!enviar;
        break;
      case 'V':
          V=!V;
          digitalWrite(rele,V);
        break;
      case 'F':
        tmp = getVal();
        if (tmp != "X" && ModoM == 1){
          MFV = tmp.toFloat();
          MFV=map(MFV,0,60,0,255);
          analogWrite(variador, MFV);}
        break;
      //Automatico
      case 'S':
        tmp = getVal();
        if (tmp != "X" && ModoA == 1){
          SetPoint = tmp.toFloat();}
        break;
        
      case 'L':
        if(PID==true){
          PID=!PID;}
        LQR=!LQR;
        break;

      case 'N':
        if(LQR==true){
          LQR=!LQR;}
        PID=!PID;
        break;
      case 'P':
        tmp = getVal();
        if (tmp != "X" && ModoA == 1 && PID==true){
          P = tmp.toFloat();}
        break;
      case 'I':
        tmp = getVal();
        if (tmp != "X" && ModoA == 1 && PID==true){
          I = tmp.toFloat();}
        break;

      case 'D':
        tmp = getVal();
        if (tmp != "X" && ModoA == 1 && PID==true){
          D = tmp.toFloat();}
        break;
    }
  }
}

String getVal(){
  String recvString = "";
  while (Serial.available()){
    char input = Serial.read();
    if (input == '%'){
      return recvString;
    }
    recvString += input;
  }
  return "X";
}

void senToPc(int* data1, int* data2, int* data3, int* data4){
  byte* byteData1=(byte*)(data1);
  byte* byteData2=(byte*)(data2);
  byte* byteData3=(byte*)(data3);
  byte* byteData4=(byte*)(data4);
  
  byte buf[8]={byteData1[0], byteData1[1],
               byteData2[0], byteData2[1],
               byteData3[0], byteData3[1],
               byteData4[0], byteData4[1]};
  Serial.write(buf, 8);
}

void senToPc(double* data1, double* data2, double* data3, double* data4){
  byte* byteData1=(byte*)(data1);
  byte* byteData2=(byte*)(data2);
  byte* byteData3=(byte*)(data3);
  byte* byteData4=(byte*)(data4);
  
  byte buf[16]={byteData1[0], byteData1[1],byteData1[2], byteData1[3],
                byteData2[0], byteData2[1],byteData2[2], byteData2[3],
                byteData3[0], byteData3[1],byteData3[2], byteData3[3],
                byteData4[0], byteData4[1],byteData4[2], byteData4[3]};
  Serial.write(buf, 16);
  }
