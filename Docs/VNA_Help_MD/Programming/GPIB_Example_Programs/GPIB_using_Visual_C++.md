# GPIB using Visual C++

* * *

##### [ See Other SCPI Example Programs](SCPI_Example_Programs.md)

/*  
* This example assumes the user's PC has a National Instruments GPIB board. The example is comprised of three basic parts:  
*  
* 1. Initialization  
* 2. Main Body  
* 3. Cleanup  
*  
* The Initialization portion consists of getting a handle to the VNA and then doing a GPIB clear of the VNA.  
*  
* The Main Body consists of the VNA SCPI example.  
*  
* The last step, Cleanup, releases the VNA for front panel control.  
*/  
  
#include <stdio.h>  
#include <stdlib.h>  
  
/*  
* Include the WINDOWS.H and DECL-32.H files. The standard Windows  
* header file, WINDOWS.H, contains definitions used by DECL-32.H and  
* DECL-32.H contains prototypes for the NI GPIB routines and constants.  
*/  
#include <windows.h>  
#include "decl-32.h"  
  
#define ERRMSGSIZE 1024 // Maximum size of SCPI command string  
#define ARRAYSIZE 1024 // Size of read buffer  
  
#define BDINDEX 0 // Board Index of GPIB board  
#define PRIMARY_ADDR_OF_PNA 16 // GPIB address of VNA  
#define NO_SECONDARY_ADDR 0 // VNA has no Secondary address  
#define TIMEOUT T10s // Timeout value = 10 seconds  
#define EOTMODE 1 // Enable the END message  
#define EOSMODE 0 // Disable the EOS mode  
  
int pna;  
char ValueStr[ARRAYSIZE + 1];  
char ErrorMnemonic[21][5] = {"EDVR", "ECIC", "ENOL", "EADR", "EARG",  
"ESAC", "EABO", "ENEB", "EDMA", "",  
"EOIP", "ECAP", "EFSO", "", "EBUS",  
"ESTB", "ESRQ", "", "", "", "ETAB"};  
  
  
void GPIBWrite(char* SCPIcmd);  
char *GPIBRead(void);  
void GPIBCleanup(int Dev, char* ErrorMsg);  
  
  
int main()  
{  
  
char *opc;  
char *result;  
char *value;  
  
/*  
* =========================================  
* INITIALIZATION SECTION  
* =========================================  
*/  
  
/*  
* The application brings the VNA online using ibdev. A device handle,VNA, is returned and is used in all subsequent calls to the VNA.  
*/  
pna = ibdev(BDINDEX, PRIMARY_ADDR_OF_PNA, NO_SECONDARY_ADDR,  
TIMEOUT, EOTMODE, EOSMODE);  
if (ibsta & ERR)  
{  
printf("Unable to open handle to PNA/nibsta = 0x%x iberr = %d/n",  
ibsta, iberr);  
return 1;  
}  
  
/*  
* Do a GPIB Clear of the VNA. If the error bit ERR is set in ibsta, call GPIBCleanup with an error message.  
*/  
ibclr (pna);  
if (ibsta & ERR)  
{  
GPIBCleanup(pna, "Unable to perform GPIB clear of the PNA");  
return 1;  
}  
  
/*  
* =========================================  
* MAIN BODY SECTION  
* =========================================  
*/  
  
// Reset the analyzer to instrument preset  
GPIBWrite("SYSTem:FPRESET");  
  
// Create S11 measurement  
GPIBWrite("CALCulate1:PARameter:DEFine:EXT 'My_S11',S11");  
  
// Turn on Window #1  
GPIBWrite("DISPlay:WINDow1:STATe ON");  
  
// Put a trace (Trace #1) into Window #1 and 'feed' it from the measurement  
GPIBWrite("DISPlay:WINDow1:TRACe1:FEED 'My_S11'");  
  
// Setup the channel for single sweep trigger  
GPIBWrite("INITiate1:CONTinuous OFF;*OPC?");  
opc = GPIBRead();  
GPIBWrite("SENSe1:SWEep:TRIGger:POINt OFF");  
  
// Set channel parameters  
GPIBWrite("SENSe1:SWEep:POINts 11");  
GPIBWrite("SENSe1:FREQuency:STARt 1000000000");  
GPIBWrite("SENSe1:FREQuency:STOP 2000000000");  
  
// Send a trigger to initiate a single sweep  
GPIBWrite("INITiate1;*OPC?");  
opc = GPIBRead();  
  
// Must select the measurement before we can read the data  
GPIBWrite("CALCulate1:PARameter:SELect 'My_S11'");  
  
// Read the measurement data into the "result" string variable  
GPIBWrite("FORMat ASCII");  
GPIBWrite("CALCulate1:DATA? FDATA");  
result = GPIBRead();  
  
// Print the data to the display console window  
printf("S11(dB) - Visual C++ SCPI Example for PNA/n/n");  
value = strtok(result, ",");  
while (value != NULL)  
{  
printf("%s/n", value);  
value = strtok(NULL, ",");  
}  
  
/*  
* =========================================  
* CLEANUP SECTION  
* =========================================  
*/  
  
/* The VNA is returned to front panel control. */  
ibonl(pna, 0);  
  
return 0;  
}  
  
/*  
* Write to the VNA  
*/  
void GPIBWrite(char* SCPIcmd)  
{  
int length;  
char ErrorMsg[ERRMSGSIZE + 1];  
length = strlen(SCPIcmd) ;  
  
ibwrt (pna, SCPIcmd, length);  
if (ibsta & ERR)  
{  
strcpy(ErrorMsg, "Unable to write this command to PNA:/n");  
strcat(ErrorMsg, SCPIcmd);  
  
GPIBCleanup(pna, ErrorMsg);  
exit(1);  
}  
}  
  
/*  
* Read from the VNA  
*/  
char* GPIBRead(void)  
{  
ibrd (pna, ValueStr, ARRAYSIZE);  
if (ibsta & ERR)  
{  
GPIBCleanup(pna, "Unable to read from the PNA");  
exit(1);  
}  
else  
return ValueStr;  
}  
  
/*  
* After each GPIB call, the application checks whether the call succeeded. If an NI-488.2 call fails, the GPIB driver sets the corresponding bit in the global status variable. If the call failed, this procedure prints an error message, takes the VNA offline and exits.  
*/  
void GPIBCleanup(int Dev, char* ErrorMsg)  
{  
printf("Error : %s/nibsta = 0x%x iberr = %d (%s)/n",  
ErrorMsg, ibsta, iberr, ErrorMnemonic[iberr]);  
if (Dev != -1)  
{  
printf("Cleanup: Returning PNA to front panel control/n");  
ibonl (Dev, 0);  
}  
}

