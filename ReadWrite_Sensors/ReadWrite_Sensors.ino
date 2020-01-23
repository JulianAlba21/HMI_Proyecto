unsigned long timer=0;
long deltaT = 5000; //us
double valor1=0;
double valor2=0;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  
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
        tmp = getVal();
        if (tmp != "X"){
          valor1 = tmp.toFloat();
          digitalWrite(LED_BUILTIN, HIGH);
        }
        break;
      case 'B':
        tmp =getVal();
        if (tmp != "X"){
          valor2= tmp.toFloat();
          digitalWrite(LED_BUILTIN, LOW);
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
