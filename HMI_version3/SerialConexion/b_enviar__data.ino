//SEND DATA

//ENVIO DE INTS
void senToPc(int* data1, int* data2, int* data3, int* data4, int* data5){
  byte* byteData1=(byte*)(data1);
  byte* byteData2=(byte*)(data2);
  byte* byteData3=(byte*)(data3);
  byte* byteData4=(byte*)(data4);
  byte* byteData5=(byte*)(data5);
  
  byte buf[10]={byteData1[0], byteData1[1],
               byteData2[0], byteData2[1],
               byteData3[0], byteData3[1],
               byteData4[0], byteData4[1],
               byteData5[0], byteData5[1]};
  Serial.write(buf, 10);
}

//ENVIO DE DOUBLES
void senToPc(double* data1, double* data2, double* data3, double* data4, double* data5){
  byte* byteData1=(byte*)(data1);
  byte* byteData2=(byte*)(data2);
  byte* byteData3=(byte*)(data3);
  byte* byteData4=(byte*)(data4);
  byte* byteData5=(byte*)(data5);
  
  byte buf[20]={byteData1[0], byteData1[1],byteData1[2], byteData1[3],
                byteData2[0], byteData2[1],byteData2[2], byteData2[3],
                byteData3[0], byteData3[1],byteData3[2], byteData3[3],
                byteData4[0], byteData4[1],byteData4[2], byteData4[3],
                byteData5[0], byteData5[1],byteData5[2], byteData5[3]};
                
  Serial.write(buf, 20);
  }
