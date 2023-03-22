#include <SoftwareSerial.h>
#include <Servo.h> 
SoftwareSerial mySerial(2,3); //RX,TX
int servoPin = 9;
  Servo Servo1; 
void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  delay(5000);
  Servo1.attach(servoPin); 
}

void loop() {
  String incoming = "";
  boolean intReady = false;
  while(mySerial.available()){
    incoming = mySerial.readString();
    intReady = true;
  }
  if(intReady){
    Serial.println("fb:" + incoming);
    Servo1.write(0); 
    delay(3000);
    Servo1.write(90); 
    delay(1000); 
  }
}
