#include <SparkFun_Bio_Sensor_Hub_Library.h>
#include <Wire.h>

// Reset pin, MFIO pin
int resPin = 4;
int mfioPin = 5;

SparkFun_Bio_Sensor_Hub bioHub(resPin, mfioPin); 

bioData body; 
unsigned long start_time = 0;

void setup(){

  Serial.begin(115200);

  Wire.begin();
  int result = bioHub.begin();
  if (result == 0) // Zero errors!
    Serial.println("Sensor started!");
  
  bioHub.configSensor();

  Serial.println("Loading up the buffer with data....");
  delay(4000);
  start_time = millis();
}

void loop(){
    body = bioHub.readSensor();
    Serial.print(millis() - start_time);
    Serial.print(",");
    Serial.print(body.irLed);
    Serial.print(",");
    Serial.println(body.redLed);
    delay(250); 
  
}