# Sense DC

Controls the PXI DC measurement.

SENSe:DC: | [CURRent:RANGe](dc.md#currrang) | SAMPles | [DPOint](dc.md#sampdpo) | [POINts](dc.md#samppoin) | [TIME](dc.md#samptime) | [VOLTage:RANGe](dc.md#voltrang)  
---  
  
Click on a keyword to view the command details.

* * *

## SENSe<ch>:DC:CURRent:RANGe <name>, <num>

Applicable Models: M937xA, M9485A, P937xA (Read-Write) Sets and reads the
range (in Amps) used for sensing current, which must be higher than the
maximum current you expect to measure. This command is available for PXI SMU
only. This is the same function with IKtM911xMeasurement Interface section,
SenseCurrentRange property of the M911x driver.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<name> | String. DC Meter Name. "SMU*C or SMU*V represents the SMU DC Meter name. * is the SMU module number. C means current measurement, V means voltage measurement.  
<num> | Range in Amps (3, 0.001 or 0.0001)  
Examples | SOUR:DC:CURR:RANG "SMU1", 10  
Query Syntax | SENSe<ch>:DC:CURRent:RANGe? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3  
  
* * *

## SENSe<ch>:DC:SAMPles:DPOint <name>, <num>

Applicable Models: M937xA, M9485A, P937xA (Read-Write) Sets and reads the
trigger offset in the measurement sweep. A negative value specifies pre-
trigger samples, and a positive value specifies post-trigger delay samples.
This command is available for PXI SMU only. This is the same function with
IKtM911xMeasurementSweep Interface section, OffsetPoints property of the
M911x driver.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<name> | String. DC Meter Name. "SMU*C or SMU*V represents the SMU DC Meter name. * is the SMU module number. C means current measurement, V means voltage measurement.  
<num> | Offset points value. Value range: 1 to 100000, step 1,   
Examples | SOUR:DC:SAMP:DPO "SMU1", 10  
Query Syntax | SENSe<ch>:DC:SAMPLes:DPOint? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SENSe<ch>:DC:SAMPles:POINTs <name>, <num>

Applicable Models: M937xA, M9485A, P937xA (Read-Write) Sets and reads the DC
measurement number of sample counts per one point measurement. This command is
available for both PXI SMU and Digital/Analog I/O M9341B. For PXI SMU, this is
the same function with IKtM911xMeasurementSweep Interface section, Points
property of the M911x driver.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<name> | String. DC Meter Name. [SMU] "SMU*C or SMU*V represents the SMU DC Meter name. * is the SMU module number. C means current measurement, V means voltage measurement. [M9341B] "AI1", "AI2", "AI3", "AI4", "AOC1" or" AOC2"  
<num> | Sample count value. Value range: 1 to 100000, step 1 (SMU),   
Examples | SOUR:DC:SAMP:POINT "SMU1", 1000  
Query Syntax | SENSe<ch>:DC:SAMPLes:POINTs? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3255 (SMU), 500 (M9341B)  
  
* * *

## SENSe<ch>:DC:SAMPles:TIME <name>, <num>

Applicable Models: M937xA, M9485A, P937xA (Read-Write) Sets and reads the DC
measurement time per one point measurement . The value of
SENSe:DC:SAMPles:POINts can be calculated by this value. This command allows
you to have the same measurement time for different kind of modules whose
sample rates are different. This command is available for both PXI SMU and
Digital/Analog I/O M9341B.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<name> | String. DC Meter Name. [SMU] "SMU*C or SMU*V represents the SMU DC Meter name. * is the SMU module number. C means current measurement, V means voltage measurement. [M9341B] "AI1", "AI2", "AI3", "AI4", "AOC1" or" AOC2",  
<num> | Measurement time in seconds [SMU] M9111A sample time is 5.12usec per point. [M9341B] Only one value can be set for one M9341B module. It sample time is 20 nsec per point.  
Examples | SOUR:DC:SAMP:TIME "SMU1C", 1000  
Query Syntax | SENSe<ch>:DC:SAMPLes:TIME? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0.0166656 (SMU), 0.00001 (M9341B)  
  
* * *

## SENSe<ch>:DC:VOLTage:RANGe <name>, <num>

Applicable Models: M937xA, M9485A, E5080A, P937xA (Read-Write) Sets and reads
the range (in Volts) used for sensing voltage, which must be higher than the
maximum current you expect to measure. This command is available for M937xA,
M9485A with Digital/Analog I/O M9341B or E5080A.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<name> | String. DC Meter Name. "AI1", "AI2", "AI3", or "AI4"  
<num> | Range in Volts (M937xA, M9485A: 1, 5 or 10) (E5080A: 1or 10)  
Examples | SOUR:DC:CURR:RANG "AI1", 10  
Query Syntax | SENSe<ch>:DC:VOLTage:RANGe? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 10  
  
* * *

