#include <SoftwareSerial.h>
#define RXD 2
#define TXD 3

SoftwareSerial mySerial(RXD, TXD);

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
}

void loop() {
  if(mySerial.available()) {
    Serial.println(mySerial.readString());
    delay(20);
  }

  mySerial.write("Data From Arduino\r\n");
  delay(500);

}
