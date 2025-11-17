# Output Commands

* * *

Controls two output functions: RF power and Noise Source.

OUTPut: | [MANual:NOISe[:STATe]](Output.md#NoiseState) | [[:STATe]](Output.md#RFOUt)  
---  
  
Click on a red keyword to view the command details.

See Also

  * [Example Programs](../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

## OUTPut:MANual:NOISe[:STATe] "**usbNsSrcID ",<bool>**

Applicable Models: All without M937xA and P93xxA/B (Read-Write) Sets and reads
the noise source [(28V)](../../Rear_Panel/XRtour.md#28) ON or OFF. Note:
usbNsSrcID is an optional parameter. If this optional parameter is
specified, it turns the noise source on/off for the specified devices.  
---  
Parameters |   
<bool> | ON (1) \- Noise source ON OFF (0) \- Noise source OFF  
Examples | OUTP:MAN:NOIS "U1832A MY12345678",1  
output:manual:noise:state "U1832A MY12345678",1  
Query Syntax | OUTPut:MANual:NOISe[:STATe]?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | For VNA models with a [Noise Figure option](../../Applications/Noise_Figure.md#OptionsExplained) (028/029/H29), the 28V line is always ON. The ON/OFF state is also available from a VNA softkey menu. For VNA models WITHOUT a Noise Figure option (028/029/H29), the 28V line is OFF by default and survives a preset. The ON/OFF state is NOT available from a VNA softkey menu.  
  
* * *

## OUTPut[:STATe] <ON | OFF>

Applicable Models: All (Read-Write) Turns RF power from the source ON or OFF.
[See note about source power state with instrument state save and
recall](../../S1_Settings/Power_Level.htm#powerDiag).  
---  
Parameters |   
<ON | OFF> | ON (or 1) - turns RF power ON OFF (or 0) - turns RF power OFF  
Examples | OUTP ON  
output:state off  
Query Syntax | OUTPut[:STATe]?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

