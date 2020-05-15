const byte numLeds = 6;
byte ledPin[numLeds] = {2, 3, 4, 5, 6, 7};

const byte buffSize = 40;
char inputBuffer[buffSize];
char messageFromPC[buffSize];
char ledState;
const char startMarker = '<';
const char endMarker = '>';
byte bytesRecvd = 0;
boolean readInProgress = false;
boolean newDataFromPc = false;

void setup() {
  Serial.begin(9600);

  for(byte i= 0; i < numLeds; i++){
    pinMode(ledPin[i], OUTPUT);
    digitalWrite(ledPin[i], HIGH);
  } 
  delay(500);
  for(byte i= 0; i < numLeds; i++){
    digitalWrite(ledPin[i], LOW);
  }
  Serial.println("<Arduino ready>");
}

void loop() {
  getDataFromPc();
  //Update led state
}

void getDataFromPc(){
  if(Serial.available() > 0){
    char x = Serial.read();
    if(x == endMarker){
      readInProgress = false;
      newDataFromPc = true;
      inputBuffer[bytesRecvd] = 0;
      parseData();
      updateLedState();
    }

    if(readInProgress){
      inputBuffer[bytesRecvd] = x;
      bytesRecvd ++;
      if (bytesRecvd == buffSize) {
        bytesRecvd = buffSize - 1;
      }
    }
    
    if(x == startMarker){
      bytesRecvd = 0;
      readInProgress = true;
    }
  }
}

void parseData(){
  char * strtokIndx;

  strtokIndx = strtok(inputBuffer,",");
  strcpy(messageFromPC, strtokIndx);
  Serial.print(messageFromPC);
  Serial.print(',');
  strtokIndx = strtok(NULL, ",");
  ledState = *strtokIndx;
  Serial.println(ledState);
}


void updateLedState(){
  int i;
  if(strcmp(messageFromPC, "LED1") == 0){
    i = 0;
  }else if(strcmp(messageFromPC, "LED2") == 0){
    i = 1;
  }else if(strcmp(messageFromPC, "LED3") == 0){
    i = 2;
  }else if(strcmp(messageFromPC, "LED4") == 0){
    i = 3;
  }else if(strcmp(messageFromPC, "LED5") == 0){
    i = 4;
  }else if(strcmp(messageFromPC, "LED6") == 0){
    i = 5;
  }

  if(ledState == 'H'){
    digitalWrite(ledPin[i], HIGH);
  }else if(ledState == 'L'){
    digitalWrite(ledPin[i], LOW);
  }
}
