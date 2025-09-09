# WOKWI

We can begin understanding physical computers in the real
world by working with some.

Now, arduino machines are little circuit boards which are easily programmable and 
have physical space for things like wires to connect to them for us to mess with.

The board we are working with specifically is the ARDUINO NANO

Now, these boards are relatively cheap (~$25), but we aren't going to be buying them 
because we would still need all the wires and batteries and lights and stuff.

So, to work with these machines, we are going to use an online simulator: WOKWI

https://wokwi.com/

WOKWI simulates far more than just Arduino boards, but we will be using 
them for this module.

Here we can navigate to:
- Arduino (Uno, Mega, Nano)
- Arduino Nano (under "Start from Scratch")

And we have a blank slate.


# What are we looking at:

- Right area: the board and assets we are using/connecting together
- Left Side: Where you put your code to run the thing.

## Show Clicking Add

## Show connecting wires


## Show Simple Example:


The code:
```
// Make sure D8 is plugged into the light
int A = 8;

void setup() {
  // put your setup code here, to run once:
  pinMode(A, OUTPUT);
  digitalWrite(A, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
    digitalWrite(A, HIGH);
    delay(1000);
    digitalWrite(A, LOW);
    delay(1000);
}
```

Pictures just in case it don't load:

![wokwi_0.png](assets/wokwi_0.png)
![wokwi_1.png](assets/wokwi_1.png)