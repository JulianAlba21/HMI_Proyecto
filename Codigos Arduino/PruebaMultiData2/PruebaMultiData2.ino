unsigned long timer =0;
long loopTime=5000;

void setup() {
  Serial.begin(9600);
  timer=micros();
}

void loop() {
  timeSync(loopTime);
  double val1=((analogRead(A0)+643)/643.0)-1;
  double val2=(analogRead(A2)-10)/1013.0;
  //Serial.println(val);

  sendToPC(&val1, &val2);
}

void timeSync(unsigned long deltaT)
{
  unsigned long currTime = micros();
  long timeToDelay = deltaT - (currTime - timer);
  if (timeToDelay>5000)
  {
   delay(timeToDelay/1000);
   delayMicroseconds(timeToDelay%1000);
  }
  else if (timeToDelay>0)
  {
    delayMicroseconds(timeToDelay);
  }
  else
  {
    
  }
  timer = currTime+timeToDelay;
}

void sendToPC(int* data1, int* data2)
{
  byte* byteData1 = (byte*)(data1);
  byte* byteData2 = (byte*)(data2);
  byte buf[6]={byteData1[0], byteData1[1],
               byteData2[0], byteData2[1]};
  
  Serial.write(buf, 4);
}

void sendToPC(double* data1, double* data2)
{
  byte* byteData1 = (byte*)(data1);
  byte* byteData2 = (byte*)(data2);
  byte buf[8]={byteData1[0],byteData1[1],byteData1[2],byteData1[3],
               byteData2[0],byteData2[1],byteData2[2],byteData2[3]};
  Serial.write(buf, 8);
}


