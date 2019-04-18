#include <stdio.h>
#include "ftd2xx.h"


UCHAR BitMode;
UCHAR thing;

UCHAR print_IO_state(FT_HANDLE handle){
FT_GetBitMode(handle, &BitMode);  //gets instantaneous values of FTDI pins
return BitMode; //returns hexadecimal value for pin state
}

FT_HANDLE interfacing(){ //Function for Opening Device handler
    FT_HANDLE handle;
    if(FT_Open(0,&handle)!=FT_OK){
        puts("Can't open device");
    }
    else{
        return handle;
    }
}

 UCHAR working(FT_HANDLE handle){ //function reads and returns data
    FT_SetBitMode(handle, 0x00, 0x1); //0x00 is a mask which is actually 00000000 i.e all 8 pins are inputs (1 would be output) 
    //0x1 is parameter for async bitbang mode
    FT_SetBaudRate(handle, 9600);  /* Actually 9600 * 16 */
    thing = print_IO_state(handle);
    return thing;
 }
