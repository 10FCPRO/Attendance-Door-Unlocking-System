#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>

#define FIREBASE_HOST "projectnet-fba8a-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "dXS1ACuqWfpz8QfhEuaaV9jjW9LdQ5zu9m3WpSsu"
#define WIFI_SSID "Androidj"
#define WIFI_PASSWORD "NetworksProj"

void setup() {
  Serial.begin(9600);

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
}

void loop() {

  int num = Firebase.getInt("num");

  if(num == 1){
      Serial.write("1");
      Firebase.setInt("num",0);
  // handle error
  if (Firebase.failed()) {
      Serial.print("setting /num failed:");
      Serial.println(Firebase.error());  
      return;
  }
  }
  delay(1000);
}
