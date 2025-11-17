# SYSTem:CAPability:HARDware:MODule Commands

* * *

Returns various capabilities of the PXIe/USB VNA.

SYSTem:CAPability:HARDware:MODule: [COUNt?](SystCapHardModule.md#count) [SERial?](SystCapHardModule.md#SERial) [MODel?](SystCapHardModule.md#model) [OPT?](SystCapHardModule.md#opt) [FPGA?](SystCapHardModule.md#fpga) | [COUNt?](SystCapHardModule.md#FPGACount)  
  
---  
  
Click on a red keyword to view the command details.

See Also

  * [Example Programs](../GPIB_Example_Programs/Perform_a_CalAllChannels_Calibration.md)

  * [Guided Cal commands](Sense/CorrGuided.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SYSTem:CAPability:HARDware:MODule:COUNt?

Applicable Models: All but M9485A (Read-only) Returns the number of modules
that are part of the current VNA instance. Learn more about Multiport VNA.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:MOD:COUNt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:MODule<n>:SERial?

Applicable Models: All (Read-only) Returns the serial number of the specified
module.  
---  
Parameters |   
<n> | Module number. This is the order in which the module appears in the Multiport VNA. This is not the slot number in a chassis. Learn more about module number.  
Examples | SYST:CAP:HARD:MOD3:SERial?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:MODule<n>:MODel?

Applicable Models: All (Read-only) Returns the model number of the specified
module. [See frequency ranges of VNA
models](../../Support/Configurations.htm).  
---  
Parameters |   
<n> | Module number. This is the order in which the module appears in the Multiport VNA. This is not the slot number in a chassis. Learn more about module number.  
Examples | SYST:CAP:HARD:MOD3:MODel?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:MODule<n>:OPT?

Applicable Models: All (Read-only) Returns the options that are installed in
the specified module. [See a list of VNA
options](../../Support/Configurations.htm). See
[SYSTem:CAPability:LICenses:CATalog?](SystCapability.md#SYSTem:CAPability:LICenses:CATalog)
for software product/options.  
---  
Parameters |   
<n> | Module number. This is the order in which the module appears in the Multiport VNA. This is not the slot number in a chassis. Learn more about module number.  
Examples | SYST:CAP:HARD:MOD3:OPT? 'Possible return string: "010,551"  
Return Type | A comma-separated string.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:MODule<n>:FPGA:COUNt?

Applicable Models: All (Read-only) Returns the number of FPGA boards in the
module.  
---  
Parameters |   
<n> | Module number. This is the order in which the module appears in the Multiport VNA. Learn more about module number.  
Examples | SYST:CAP:HARD:MOD3:FPGA:COUNt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:MODule<n>:FPGA<x>?

Applicable Models: All (Read-only) Returns the version number of specified
FPGA board.  
---  
Parameters |   
<n> | Module number. This is the order in which the module appears in the Multiport VNA. Learn more about module number.  
<x> | FPGA board number. Choose from 1 to the value returned by [SYST:CAP:HARD:MOD<n>:FPGA:COUNt?](SystCapHardModule.md#FPGACount)  
Examples | SYST:CAP:HARD:MOD3:FPGA2?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

