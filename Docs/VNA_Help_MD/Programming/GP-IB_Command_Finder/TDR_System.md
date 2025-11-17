# SYSTem:TDR Commands

SYSTem:TDR :FREQuency:  
| [MAXimum  
](TDR_System.htm#TdrCapFreqMax) | [MINimum](TDR_System.md#TdrCapFreqMin) :PRESet  
---  
  
Click on a red keyword to view the command details.

See Also

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SYSTem:TDR:CAPability:FREQuency:MAXimum <freq>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) Set/Get stop
limit frequency in TDR app. The value change gets effective after TDR preset.  
---  
Parameters |   
<freq> | Stop limit frequency   
Examples | SYST:TDR:CAP:FREQ:MAX 9E6  
system:tdr:capability:frequency:maximum?  
Query Syntax | SYSTem:TDR:CAPability:FREQuency:MAXimum ]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Same as the product default stop frequency   
  
* * *

## SYSTem:TDR:CAPability:FREQuency:MINimum <freq>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) Set/Get start
limit frequency in TDR app. The value change gets effective after TDR preset.  
---  
Parameters |   
<freq> | Start limit frequency   
Examples | SYST:TDR:CAP:FREQ:MIN 9E3  
system:tdr:capability:frequency:minimum?  
Query Syntax | SYSTem:TDR:CAPability:FREQuency:MINimum ]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Same as the product default start frequency   
  
* * *

## SYSTem:TDR:PRESet

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
executes a TDR preset. When TDR application is not launched, this command
launches it without VNA-TDR GUI.  
---  
Examples | SYST:TDR:PRES  
system:tdr:preset  
Default | Not Applicable  
  
* * *

##

