#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

#define SERVOMIN  1000 // in us
#define SERVOMAX  2000 // in us

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

int analogPin = A0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pwm.begin();
  pwm.setPWMFreq(50);

  uint8_t twbrbackup = TWBR;
  TWBR = 12;
}

void loop() {
  pwm.writeMicroseconds(0, map(analogRead(analogPin), 0, 1023, SERVOMIN, SERVOMAX));//Converti en temps haut, la valeur de l'entrée A0
  delay(100);
}
