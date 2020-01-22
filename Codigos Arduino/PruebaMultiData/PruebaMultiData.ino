unsigned long timer =0;
long loopTime=5000;

void setup() {
  Serial.begin(9600);
  timer=micros();
}

void loop() {
  timeSync(loopTime);
  //double val=((analogRead(A0)+643)/643.0)-1;
  double val=(analogRead(A2)-10)/1013.0;
  //Serial.println(val);

  sendToPC(&val);
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

void sendToPC(int* data)
{
  byte* byteData = (byte*)(data);
  Serial.write(byteData, 2);
}

void sendToPC(double* data)
{
  byte* byteData = (byte*)(data);
  Serial.write(byteData, 4);
}


