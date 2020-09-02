//cuerpo principal
void setup(){
  
pinMode(LED_BUILTIN, OUTPUT);
pinMode(variador, OUTPUT);
pinMode(rele, OUTPUT);
pinMode(SensorTE, INPUT);
pinMode(SensorTS, INPUT);


///PINES CON FINES DE VALIDACIÓN

pinMode(5,OUTPUT);
pinMode(6,OUTPUT);


timer = micros();
digitalWrite(LED_BUILTIN, LOW);

digitalWrite(rele,V);
Serial.begin(38400);
delay(10);
//ads.setGain(GAIN_TWOTHIRDS);
ads.begin();
delay(500);


Timer1.initialize(500);
//se llama la funcion de interrupcion al final de este sketch
Timer1.attachInterrupt(interrupcion);
}


void loop(){
timeSync(deltaT);//SINCRONIZACION

if (enviar== true){
//LECTURA DE VALORES
LTE = ads.readADC_SingleEnded(0)*0.0176;
LTG = ads.readADC_SingleEnded(1)*0.0826;
LTC = ads.readADC_SingleEnded(2)*0.08;
LTS = ads.readADC_SingleEnded(3)*0.0186;

//MOSTRAR VALORES EN TERMINAL

//Serial.print(LTE); Serial.print('\t');
//Serial.print(LTG); Serial.print('\t');
//Serial.print(LTC); Serial.print('\t');
//Serial.print(LTS); Serial.println('\t');

//ENVIAR VARIABLES

senToPc(&LTE, &LTG, &LTC, &LTS, &LFV);//ENVIAR DATA
}
getSerialData();//RECIBIR DATA

if (ModoA == false && ModoM == false){
  LFV=0.0;
  analogWrite(variador,0);
  }

if (ModoM==true){analogWrite(variador,MFV);}
else if (ModoA==true){analogWrite(variador,map(LFV,0,30,0,255));}

//Replica de señales
//replica de temperatura
if (LTE<=30){analogWrite(5,map(LTE,0,30,0,255/2));}
//replica señal de control
analogWrite(6,map(LFV,0,30,0,255/2));

}


//FUNCION DE LA INTERRUPCION
void interrupcion(){
  if (LQR == true){
    c_LQR();
  }
  else if (PID == true){
    c_PID();
  }
  }
