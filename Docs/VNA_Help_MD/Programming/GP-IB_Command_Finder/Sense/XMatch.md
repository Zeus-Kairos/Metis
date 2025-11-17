# SENSe:ACTive Commands

* * *

Controls the [Active Hot Parameters](../../../Applications/Active_Match.md)
configuration.

SENSe:ACTive: | DISP: | INTerpolate[:STATe] | TRACe |IPWer | [PMAP](XMatch.md#Pmap) | [INPut](XMatch.md#PmapInp) | [OUTput](XMatch.md#PmapOut) | SWEep: | PHASe | POINt | POWer | STARt | STEP | STOP | TYPE | TTONe: | MODE | ABSolute | RELative  
---  
  
Click on a keyword to view the command details.

### See Also

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

  * [Programming Example](../../GPIB_Example_Programs/Active_\(Hot\)_Parameters.md)

* * *

## SENSe<ch>:ACTive:DISP:INTerpolate[:STATe] <bool>

Applicable Models: All products with S9x111B (Read-Write) Sets whether or not
interpolation is on for display. Frequency, power, and phase X axis are
supported for display. Interpolation may be applied in the trace.  
---  
Parameters |   
<ch> | Any existing active match channel. If unspecified, value is set to 1.  
<bool> | Choose from: ON or (1) Interpolate the results OFF or (0) Do NOT interpolate the results.  
Examples | SENS:ACTive:DISP:INT 1 sense:active:disp:interpolation off  
Query Syntax | SENSe<ch>:ACTive:DISP:INTerpolation[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SENSe<ch>:ACTive:DISPlay:TRACe<tnum>:IPWer <num>

Applicable Models: All products with S9x111B (Read-Write) Set and read a fixed
trace input power level.  
---  
Parameters |   
<ch> | Any existing active match channel. If unspecified, value is set to 1.  
<tnum> | The number of the trace to set input power. If unspecified, the trace number is set to 1.  
<num> | Input power level. The range is -10 to 0. The units are Hz, dBm, or s.  
Examples | SENS:ACTive:DISPlay:TRACe1:IPWer 0 dBm sense:active:display:trace1:ipwer 0 dBm  
Query Syntax | SENSe<ch>:ACTive:DISPlay:TRACe:IPWer?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:ACTive:PMAP <input>,<output>

Applicable Models: All products with S9x111B (Write only) Sets the input port
and output port of an Active Parameter channel. This setting is necessary only
when using the limited port mapping feature.  
---  
Parameters |   
<ch> | Any existing active match channel. If unspecified, value is set to 1.  
<input> | VNA port connected to the DUT Input. Choose from any ports with dedicated internal source.  
<output> | VNA port connected to the DUT Output. Choose from any ports with dedicated internal source.  
Examples | SENS:ACT:PMAP 1,3 sense2:act:pmap 1,3  
Query Syntax | Not Applicable  
Return Type | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1,3  
  
* * *

## SENSe<ch>:ACTive:PMAP:Input?

Applicable Models: All products with S9x111B (Read only) Returns the VNA test
port to be connected to the DUT input for an AHP channel. The SENS:ACT:PMAP
sets this value.  
---  
Parameters |   
<ch> | Any existing active match channel. If unspecified, value is set to 1.  
Examples | SENS:ACT:PMAP:INP?  
Query Syntax | SENSe:ACTive:PMAP:INPut?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SENSe<ch>:ACTive:PMAP:Output?

Applicable Models: All products with S9x111B (Read only) Returns the VNA test
port to be connected to the DUT output for an AHP channel. The SENS:ACT:PMAP
sets this value.  
---  
Parameters |   
<ch> | Any existing active match channel. If unspecified, value is set to 1.  
Examples | SENS:ACT:PMAP:OUT?  
Query Syntax | SENSe:ACTive:PMAP:OUTPut?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3  
  
* * *

## SENSe<ch>:ACTive:SWEep:PHASe:POINt <num>

Applicable Models: All products with S9x111B (Read-Write) Set and read the
number of phase points. For the tuning tone at the output, a phase sweep is
done for each point.  
---  
Parameters |   
<ch> | Any existing active match channel. If unspecified, value is set to 1.  
<num> | Phase points. Do not exceed the max number of phase points (50).  
Examples | SENS:ACTive:SWE:PHAS:POIN 201 sense:active:sweep:phase:point 101  
Query Syntax | SENSe<ch>:ACTive:SWEep:PHASe:POINt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 8  
  
* * *

## SENSe<ch>:ACTive:SWEep:POWer:STARt <num>

Applicable Models: All products with S9x111B (Read-Write) Set and read the
start power level for a 3D sweep.  
---  
Parameters |   
<ch> | Any existing active match channel. If unspecified, value is set to 1.  
<num> | Start power level in dBm. Choose a value from the min power to max power of the hardware.  
Examples | SENS:ACTive:SWE:POW:STAR 0 sense:active:sweep:power:start 0  
Query Syntax | SENSe<ch>:ACTive:SWEep:POWer:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -10 dBm  
  
* * *

## SENSe<ch>:ACTive:SWEep:POWer:STEP <num>

Applicable Models: All products with S9x111B (Read-Write) Set and read the
number of power steps for a 3D sweep.  
---  
Parameters |   
<ch> | Any existing active match channel. If unspecified, value is set to 1.  
<num> | Number of power steps. The range is 2 to 20001.  
Examples | SENS:ACTive:SWE:POW:STEP 201 sense:active:sweep:power:step 201  
Query Syntax | SENSe<ch>:ACTive:SWEep:POWer:STEP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 201  
  
* * *

## SENSe<ch>:ACTive:SWEep:POWer:STOP <num>

Applicable Models: All products with S9x111B (Read-Write) Set and read the
stop power level for a 3D sweep.  
---  
Parameters |   
<ch> | Any existing active match channel. If unspecified, value is set to 1.  
<num> | Stop power level in dBm. Choose a value from min power to max power of the hardware.  
Examples | SENS:ACTive:SWE:POW:STOP 0 sense:active:sweep:power:stop 0  
Query Syntax | SENSe<ch>:ACTive:SWEep:POWer:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 dBm  
  
* * *

## SENSe<ch>:ACTive:SWEep:TYPE <char>

Applicable Models: All products with S9x111B (Read-Write) Set and read the
sweep type.  
---  
Parameters |   
<ch> | Any existing active match channel. If unspecified, value is set to 1.  
<char> | Sweep type. Choose from:

  * LIN \- frequency linear sweep
  * LOG \- frequency log sweep
  * POW \- power sweep
  * MULT \- Multiple sweep. Sweeps frequency with fixed power and has several sweeps with different power values. This is called a 3D sweep: frequency, power, and phase.

  
Examples | SENS:ACTive:SWE:TYPE LIN sense:active:sweep:type lin  
Query Syntax | SENSe<ch>:ACTive:SWEep:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | LIN  
  
* * *

## SENSe<ch>:ACTive:TTONe:MODE <char>

Applicable Models: All products with S9x111B (Read-Write) Set and read the
tuning tone mode. The tuning tone is the source at the output port to extract
the X parameters.  
---  
Parameters |   
<ch> | Any existing active match channel. If unspecified, value is set to 1.  
<char> | Tuning tone mode. Choose from:

  * ABSolute \- tone power is an absolute power
  * RELative \- tone power is a dBc power relative to the input power

  
Examples | SENS:ACTive:TTON:MODE ABS sense:active:ttone:mode abs  
Query Syntax | SENSe<ch>:ACTive:TTONe:MODE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ABSolute  
  
* * *

## SENSe<ch>:ACTive:TTONe:ABSolute <num>

Applicable Models: All products with S9x111B (Read-Write) Set and read the
absolute tone power level.  
---  
Parameters |   
<ch> | Any existing active match channel. If unspecified, value is set to 1.  
<num> | Absolute tone power level.  
Examples | SENS:ACTive:TTON:ABS -5 sense:active:ttone:absolute -5  
Query Syntax | SENSe<ch>:ACTive:TTONe:ABSolute?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -5 dBm  
  
* * *

## SENSe<ch>:ACTive:TTONe:RELative <num>

Applicable Models: All products with S9x111B (Read-Write) Set and read the
tone power relative to the input power (dBc).  
---  
Parameters |   
<ch> | Any existing active match channel. If unspecified, value is set to 1.  
<num> | Relative tone power level.  
Examples | SENS:ACTive:TTON:REL 10 sense:active:ttone:relative 10  
Query Syntax | SENSe<ch>:ACTive:TTONe:RELative?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -15 dBc  
  
* * *

