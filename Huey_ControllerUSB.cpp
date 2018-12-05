/****************************************************************
 * CpE 185 - Final Project: USB Controller
 *
 * Andersen Huey
 *
 * Lecture: Dennis Dahlquist
 * Lab: Eric Telles
 *
 * The button will print 1 to the master when the button is
 * pressed
 *
 ***************************************************************/

#include "mbed.h"                   //Include library

Serial pc(SERIAL_TX, SERIAL_RX);    //Declare the ports for USB

DigitalIn myButton(PB_4);           //Button on pin 4
DigitalIn myButton2(PB_5);

int main() {

    myButton.mode(PullDown);        //Pull down resistor, default state 0
    myButton2.mode(PullDown);
    int reset = 0;                  //Used to prevent repeated signals when
                                    //holding down the button
    while(1) {
        if(myButton && reset == 0){ //If myButton is on and reset is off
            pc.printf("1");
            wait(0.15);             //Wait 0.15 second
            reset = 1;              //Reset = 1
        }

        else if(myButton2)          //If the second button is pressed
            pc.printf("2");         //Send the exit signal

        else if(!myButton) {        //If the button isn't pressed
            reset = 0;              //Reset = off
        }
    }
}
