//GET SERIAL DATA - MANUAL AND GENERAL COMMUNICATION INMERSE

void getSerialData(){
  while (Serial.available()){
    char input = Serial.read();
    String tmp = "";
    switch(input){
    
      case 'A'://activar desactivar modo automatico
        ModoM=false;
        ModoA=!ModoA;
        break;
      case 'M'://Activar desactivar modo manual
        ModoA=false;
        ModoM=!ModoM;
        break;
      case 'E'://activar desactivar el envio de datos
        enviar=!enviar;
        break;
      case 'V'://Activar desactivar el funcionamiento del variador
          V=!V;
          digitalWrite(rele,V);
        break;
      case 'F'://Funcion para escribir el PWM que se envia al variador
        tmp = getVal();
        if (tmp != "X" && ModoM == true){
          MFV = tmp.toFloat();
          MFV=map(MFV,0,30,0,255/2);
          analogWrite(variador, MFV);}
        break;
      //Automatico
      case 'S'://Funcion para obtener el set point de control
        tmp = getVal();
        if (tmp != "X" && ModoA == true){
          SetPoint = tmp.toFloat();}
        break;
        
      case 'N'://Activa el control tipo PID
        if(ModoA==true){
          LQR=false;
          PID=!PID;}
        break;

      case 'L'://Activa el control tipo LQR
        if(ModoA==true){
          PID=false;
          LQR=!LQR;}
        break;
      case 'P'://lee el valor de la variable proporcional
        tmp = getVal();
        if (tmp != "X" && ModoA == true && PID==true){
          P = tmp.toFloat();}
        break;
      case 'I'://lee el valor de la variable integral
        tmp = getVal();
        if (tmp != "X" && ModoA == true && PID==true){
          I = tmp.toFloat();}
        break;

      case 'D'://lee el valor de la variable derivativa
        tmp = getVal();
        if (tmp != "X" && ModoA == true && PID==true){
          D = tmp.toFloat();}
        break;
    }
  }
}

String getVal(){//funcion para obtener el valor numerico relacionado según la letra
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
