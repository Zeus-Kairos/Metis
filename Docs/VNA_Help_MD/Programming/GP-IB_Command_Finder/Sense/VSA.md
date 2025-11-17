# Vector Signal Analyzer Commands

Controls the connection between the VNA and the Vector Signal Analyzer (89600
VSA) Application.

SENSe:VSA CONNect | [:STATe] DATA | MOD | PIN1 | [:STATe] | PINWav | [:STATE] | POU2 | [:STATe] | STReam | [:STATe] DTRigger | [:STATe] FREQuency | CENTer IF | OFFSet LO | SIDE SAVe | INCLude | [:STATe] SHOW SPECtrum | AUTOtune STAtus | REPort?  
---  
  
Click on a red keyword to view the command details.

See Also

  * [Learn about VSA Application](../../../Applications/Modulation_Distortion/Link_VNA_to_89600_VSA.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<ch>:VSA:CONNect[:STATe]

(Read-Write) Set and read the VNA to VSA connection state.  
---  
Parameters |   
<ch> | Any existing SA or MOD/MODX channel. If unspecified, value is set to 1.  
<bool> | Choose from: OFF (or 0)\- Disconnect VNA from VSA 89600 ON (or 1)\- Connect VNA to VSA 89600  
Examples | SENS:VSA:CONN ON  
Query Syntax | SENSe<ch>:VSA:CONNect[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SENSe<ch>:VSA:DATA:MOD:PIN1[:STATe]

(Read-Write) Set to stream input power to a VSA measurement channel.  
---  
Parameters |   
<ch> | Any existing SA or MOD/MODX channel. If unspecified, value is set to 1.  
<bool> | Choose from: OFF (or 0) \- Do not stream input power to VSA. ON (or 1) \- Stream input power to VSA.  
Examples | SENS:VSA:DATA:MOD:PIN1 ON  
Query Syntax | SENSe<ch>:VSA:DATA:MOD:PIN1[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SENSe<ch>:VSA:DATA:MOD:PINWav[:STATe]

(Read-Write) Set to stream ideal input power to VSA measurement channel.  
---  
Parameters |   
<ch> | Any existing SA or MOD/MODX channel. If unspecified, value is set to 1.  
<bool> | Choose from: OFF (or 0) \- Do not stream ideal input power to VSA. ON (or 1) \- Stream ideal input power to VSA.  
Examples | SENS:VSA:DATA:MOD:PINWav ON  
Query Syntax | SENSe<ch>:VSA:DATA:MOD:PIN1[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SENSe<ch>:VSA:DATA:MOD:POU2[:STATe]

(Read-Write) Set to stream output power to a VSA measurement channel.  
---  
Parameters |   
<ch> | Any existing SA or MOD/MODX channel. If unspecified, value is set to 1.  
<bool> | Choose from: OFF (or 0) \- Do not stream output power to VSA. ON (or 1) \- Stream output power to VSA.  
Examples | SENS:VSA:DATA:MOD:POU2 ON  
Query Syntax | SENSe<ch>:VSA:DATA:MOD:POU2[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SENSe<ch>:VSA:DATA:STReam[:STATe]

(Read-Write) Set and read the data stream state.  
---  
Parameters |   
<ch> | Any existing SA or MOD/MODX channel. If unspecified, value is set to 1.  
<bool> | Choose from: OFF (or 0) \- Do not stream data from VNA to VSA. ON (or 1) \- Stream data from VNA to VSA.  
Examples | SENS:VSA:DATA:STR ON  
Query Syntax | SENSe<ch>:VSA:DATA:STReam[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SENSe<ch>:VSA:DTRigger[:STATe]

(Read-Write) Set and read the state of the digital trigger. This command is
used to make the time domain IQ exported data starting time identical sweep-
to-sweep. Disabling this command makes the exported data less stable from
sweep-to-sweep.  
---  
Parameters |   
<ch> | Any existing SA or MOD/MODX channel. If unspecified, value is set to 1.  
<bool> | Choose from: OFF (or 0)\- Disable digital trigger. ON (or 1)\- Enable digital trigger.  
Examples | SENS:VSA:DTR 1  
Query Syntax | SENSe<ch>:VSA:DTRigger[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SENSe<ch>:VSA:FREQuency:CENTer

(Read-Write) Set and read the VSA center frequency which determines the LO
frequency (LO Freq = VSA Center ± IF Offset) and the display center frequency
of the VNA and VSA 89600.  
---  
Parameters |   
<ch> | Any existing SA or MOD/MODX channel. If unspecified, value is set to 1.  
<num> | Center frequency. Choose any number between the minimum and maximum frequency limits of the analyzer. Units are Hz.  
Examples | SENS:VSA:FREQ:CENT 6e9  
Query Syntax | SENSe<ch>:VSA:FREQuency:CENTer?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3.021e9  
  
* * *

## SENSe<ch>:VSA:IF:OFFSet

(Read-Write) Set and read the IF offset used for calculating the LO frequency.  
---  
Parameters |   
<ch> | Any existing SA or MOD/MODX channel. If unspecified, value is set to 1.  
<num> | IF offset value in Hertz. The range is 0 to 21 MHz.  
Examples | SENS:VSA:IF:OFFS 20e6  
Query Syntax | SENSe<ch>:VSA:IF:OFFSet?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 21e6  
  
* * *

## SENSe<ch>:VSA:LO:SIDE

(Read-Write) Set and read the LO side.  
---  
Parameters |   
<ch> | Any existing SA or MOD/MODX channel. If unspecified, value is set to 1.  
<enum> | Choose from: LOW \- LO Freq = VSA Center - IF Offset HIGH \- LO Freq = VSA Center + IF Offset  
Examples | SENS:VSA:LO:SIDE LOW  
Query Syntax | SENSe<ch>:VSA:LO:SIDE?  
Return Type | Enumeration  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | LOW  
  
* * *

## SENSe<ch>:VSA:SAVe:INCLude[:STATe]

(Read-Write) Sets to automatically save the VSA state file and embed it into
the VNA state file (.csa file).  
---  
Parameters |   
<ch> | Any existing SA or MOD/MODX channel. If unspecified, value is set to 1.  
<bool> | Choose from: OFF (or 0)\- Disable the VSA state within VNA state file ON (or 1)\- Enable the VSA state within VNA state file  
Examples | SENS:VSA:DTR 1  
Query Syntax | SENSe<ch>:VSA:SAVe:INCLude[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SENSe<ch>:VSA:SHOW

(Write-only) Sets the VSA window in front of the VNA GUI when the VSA-to-VNA
connection is running.  
---  
Parameters |   
<ch> | Any existing SA or MOD/MODX channel. If unspecified, value is set to 1.  
Examples | SENS:VSA:SHOW  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:VSA:SPECtrum:AUTOtune

(Write-only) Sets the VSA spectrum settings to match the current SA coherent
repetition rate. In addition, it forces the VSA RBW to match the coherent tone
spacing.  
---  
Parameters |   
<ch> | Any existing SA or MOD/MODX channel. If unspecified, value is set to 1.  
Examples | SENS:VSA:SPEC:AUTO  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:VSA:STAtus:REPort?

(Read-only) Reads the status of the VNA to VSA connection and configuration
status. [Learn
more](../../../Applications/Modulation_Distortion/Link_VNA_to_89600_VSA.htm#VSA_Status_Dialog_Help).  
---  
Parameters |   
<ch> | Any existing SA or MOD/MODX channel. If unspecified, value is set to 1.  
Examples | SENS:VSA:STA:REP?  
Return Type | Char  
  
* * *

