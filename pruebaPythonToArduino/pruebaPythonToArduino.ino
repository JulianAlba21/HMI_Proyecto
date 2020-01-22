unsigned long timer=0;
long deltaT = 5000; //us
double valor1=0;
double valor2=0;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(38400);
  timer = micros();
  digitalWrite(LED_BUILTIN, LOW);
}

void loop(){
 timeSync(deltaT);
 getSerialData();
 senToPc(&valor1, &valor2);
}
//\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////
void timeSync(unsigned long deltaT){
  unsigned long currTime = micros();
  long timeToDelay = deltaT - (currTime - timer);
  if (timeToDelay > 5000)
  {
    delay(timeToDelay / 1000);
    delayMicroseconds(timeToDelay % 1000);
  }
  else if (timeToDelay > 0)
  {
    delayMicroseconds(timeToDelay);
  }
  else
  {
      // timeToDelay is negative so we start immediately
  }
  timer = currTime + timeToDelay;
}

void getSerialData(){
  while (Serial.available())
  {
    char input = Serial.read();
    String tmp = "";
    switch(input)
    {
      case 'K':
        tmp = getVal();
        if (tmp != "X")
        {
          valor1 = tmp.toFloat();
          digitalWrite(LED_BUILTIN, HIGH);
        }
        break;
      case 'S':
        tmp =getVal();
        if (tmp != "X")
        {
          valor2= tmp.toFloat();
          digitalWrite(LED_BUILTIN, LOW);
        }
        break;
    }
  }
}

String getVal(){
  String recvString = "";
  while (Serial.available())
  {
    char input = Serial.read();
    if (input == '%')   // this is the end of message marker so that the program knows when to update the g_scaleFactor variable 
    {
      return recvString;
    }
    recvString += input;
  }
  return "X";   // failed to receive the EOM marker
}

void senToPc(int* data1, int* data2){
  byte* byteData1=(byte*)(data1);
  byte* byteData2=(byte*)(data2);
  byte buf[4]={byteData1[0], byteData1[1],
                byteData2[0], byteData2[1]};
  Serial.write(buf, 4);
}

void senToPc(double* data1, double* data2){
  byte* byteData1=(byte*)(data1);
  byte* byteData2=(byte*)(data2);
  byte buf[8]={byteData1[0], byteData1[1],byteData1[2], byteData1[3],
                byteData2[0], byteData2[1],byteData2[2], byteData2[3]};
  Serial.write(buf, 8);
  }
