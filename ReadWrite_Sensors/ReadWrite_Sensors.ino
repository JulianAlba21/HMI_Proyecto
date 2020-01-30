unsigned long timer=0;
long deltaT = 5000; //us
double valor1=0;
double valor2=0;
double valor3=0;
double valor4=0;
double valor5=0;
double valor6=0;

bool ModoM=false;
bool ModoA=false;

void setup() {
  
  pinMode(LED_BUILTIN, OUTPUT);
  
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);

  pinMode(9, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  
  
  Serial.begin(38400);
  timer = micros();
  digitalWrite(LED_BUILTIN, LOW);
}

void loop(){
 timeSync(deltaT);
 
 double pot1=analogRead(A0);
 double pot2=analogRead(A1);
 double pot3=analogRead(A2);
 double pot4=analogRead(A3);

 getSerialData();
 senToPc(&pot1, &pot2, &pot3, &pot4);
}
//\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////
void timeSync(unsigned long deltaT){
  unsigned long currTime = micros();
  long timeToDelay = deltaT - (currTime - timer);
  if (timeToDelay > 5000){
    delay(timeToDelay / 1000);
    delayMicroseconds(timeToDelay % 1000);
  }
  else if (timeToDelay > 0){
    delayMicroseconds(timeToDelay);
  }
  else
  {
      // timeToDelay is negative so we start immediately
  }
  timer = currTime + timeToDelay;
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
      case 'B':
        tmp = getVal();
        if (tmp != "X" && ModoM == 1){
          valor1 = tmp.toFloat();
          analogWrite(9, valor1);
        }
        break;
      case 'C':
        tmp =getVal();
        if (tmp != "X" && ModoM == 1){
          valor2= tmp.toFloat();
          analogWrite(6, valor2);
        }
        break;
       case 'D':
        tmp =getVal();
        if (tmp != "X" && ModoM == 1){
          valor3= tmp.toFloat();
          analogWrite(5, valor3);
        }
        break;
       case 'E':
        tmp =getVal();
        if (tmp != "X" && ModoA == 1){
          valor4= tmp.toFloat();
          analogWrite(9, valor4);
        }
        break;
       case 'F':
        tmp =getVal();
        if (tmp != "X"  && ModoA == 1){
          valor5= tmp.toFloat();
          analogWrite(6, valor5);
        }
        break;
       case 'G':
        tmp =getVal();
        if (tmp != "X"  && ModoA == 1){
          valor6= tmp.toFloat();
          analogWrite(5, valor6);
        }
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
