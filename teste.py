#include <Servo.h>

Servo aileGauche;
Servo aileDroite;

int pinSignalRF = 2; // Exemple d'entrée du signal RF
int signalLu = 0;

int pinServoGauche = 9;
int pinServoDroite = 10;

bool ailesOuvertes = false;

void setup() {
  Serial.begin(9600);
  pinMode(pinSignalRF, INPUT);
  
  aileGauche.attach(pinServoGauche);
  aileDroite.attach(pinServoDroite);
  
  // Position de départ (ailes fermées)
  aileGauche.write(0);
  aileDroite.write(0);
}

void loop() {
  signalLu = digitalRead(pinSignalRF);

  if (signalLu == HIGH) {  // Si bouton de la télécommande est pressé
    if (!ailesOuvertes) {
      ouvrirAiles();
      ailesOuvertes = true;
    } else {
      fermerAiles();
      ailesOuvertes = false;
    }

    delay(1000); // Anti-rebond pour éviter double activation
  }
}

void ouvrirAiles() {
  for (int pos = 0; pos <= 90; pos++) {
    aileGauche.write(pos);
    aileDroite.write(pos);
    delay(15);
  }
}

void fermerAiles() {
  for (int pos = 90; pos >= 0; pos--) {
    aileGauche.write(pos);
    aileDroite.write(pos);
    delay(15);
  }
}
