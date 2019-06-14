#include <LiquidCrystal_I2C.h>

#include <Wire.h>


#include <SoftwareSerial.h>

#define CHANNEL1 9
#define CHANNEL2 6

SoftwareSerial XBEE(10, 11); // RX, TX
LiquidCrystal_I2C lcd(0x27, 16, 2);//Communicate with LCD

char c[7];
uint8_t i = 0;
String str;
void setup() {
  // Open serial communications and wait for port to open:
  lcd.init();
  lcd.init();
  lcd.backlight();
  lcd.setCursor(1,0);
  lcd.print("Light 1:");
  lcd.print("0%");
  lcd.setCursor(1,1);
  lcd.print("Light 2:");
  lcd.print("0%");
  Serial.begin(9600);
  pinMode(CHANNEL1, OUTPUT);
  pinMode(CHANNEL2, OUTPUT);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // set the data rate for the SoftwareSerial port
  XBEE.begin(9600);
  analogWrite(CHANNEL1, 255);
  analogWrite(CHANNEL2, 255);
}
//Read Serial
void loop() { // run over and over
  while (XBEE.available())
  {
    c[i] = XBEE.read();
    i++;
  }

  i = 0;
  str = c;

  for (int j = 0; j < 7; j++)
  {
    c[j] = '\0';
  }
  
  if (str[1] == '/')
  {
    int channel = str[0] - '0';

    if (channel == 1)
    {
      String value1 = str.substring(2, str.length());
      
      Serial.println(value1);
//  
      uint8_t percent1 = value1.toInt();
      int pwm1 = 255-percent1*2.55;
      analogWrite(CHANNEL1, pwm1);
      lcd.setCursor(9,0);
      lcd.print(percent1);
      lcd.setCursor(9+value1.length(),0);
      lcd.print("%");
      lcd.setCursor(9+value1.length()+1,0);
      lcd.print(" ");
    }
    else if (channel == 2)
    {
      String value2 = str.substring(2, str.length());
      
      Serial.println(value2);
  
      uint8_t percent2 = value2.toInt();
      int pwm2 = 255-percent2*2.55;
      analogWrite(CHANNEL2, pwm2);
      lcd.setCursor(9,1);
      lcd.print(percent2);
      lcd.setCursor(9+value2.length(),1);
      lcd.print("%");
      lcd.setCursor(9+value2.length()+1,1);
      lcd.print(" ");
    }
  }
  
  delay(500);
}
