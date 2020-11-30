const int LED[] = {4,5,6,7,8,9,10,11,12,13};
int sensor = A0;
int val = 0;
int bomba = 3;
int umiRelat = 30;
int tempoRega = 1000;


void setup() {
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(bomba, OUTPUT);
  Serial.begin(9600);

}


// the loop routine runs over and over again forever:
void loop() {
  
  
  int umi = analogRead(sensor);
  umi = map(umi ,1023, 0, 0, 100);
  Serial.println(umi);
  delay(1); 


  if(umi < umiRelat){
      digitalWrite(bomba, LOW);
      delay(tempoRega);
      digitalWrite(bomba, HIGH);
  }


  if(umi > 10){
    digitalWrite(LED[0], HIGH);
    }else{
      digitalWrite(LED[0], LOW);
    }
    if(umi > 20){
      digitalWrite(LED[1], HIGH);
      }
    else{
        digitalWrite(LED[1], LOW);
        }
        if(umi > 30){
      digitalWrite(LED[2], HIGH);
      }
    else{
        digitalWrite(LED[2], LOW);
        }
        if(umi > 40){
      digitalWrite(LED[3], HIGH);
      }
    else{
        digitalWrite(LED[3], LOW);
        }
        if(umi > 50){
      digitalWrite(LED[4], HIGH);
      }
    else{
        digitalWrite(LED[4], LOW);
        }
        if(umi > 60){
      digitalWrite(LED[5], HIGH);
      }
    else{
        digitalWrite(LED[5], LOW);
        }
        if(umi > 70){
      digitalWrite(LED[6], HIGH);
      }
    else{
        digitalWrite(LED[6], LOW);
        }
        if(umi > 80){
      digitalWrite(LED[7], HIGH);
      }
    else{
        digitalWrite(LED[7], LOW);
        }
        if(umi > 90){
      digitalWrite(LED[8], HIGH);
      }
    else{
        digitalWrite(LED[8], LOW);
        }
        if(umi > 95){
      digitalWrite(LED[9], HIGH);
      }
    else{
        digitalWrite(LED[9], LOW);
        }
        

  }
 
