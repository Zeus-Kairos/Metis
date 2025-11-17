# Calculate:Normalize Commands

* * *

Specifies the normalization features used for a receiver power calibration.

These commands are [Superseded](../../Replacement_Commands.md) (Sept 2004).

See the replacement commands in a new [Receiver Power Cal
example.](../../GPIB_Example_Programs/Perform_a_Source_Cal_using_SCPI.htm#Receiver)

![](../../../assets/images/Programming/calnorm.gif)

Click on a keyword to view the command details.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about Receiver Cal](../../../S3_Cals/PwrCalibration.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Save and recall your receiver power calibration (which use .CST file
commands):

  * [SENS:CORR:CSET:SAVE](../Sense/CorrCset.md#sccsv)

  * [SENS:CORR:CSET[:SEL]](../Sense/CorrCset.md#sccse)

Or use these two commands and specify either .STA or .CST file extensions:

  * [MMEM:LOAD](../Memory.md#recall)

  * [MMEM:STOR](../Memory.md#save)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:Select](Parameter.md#cps)

* * *

## CALCulate<cnum>:NORMalize[:IMMediate] Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA Note: This command
is replaced with [SENS:CORR:COLL:METH
RPOWer](../Sense/Sense_Correction.htm#sccm) and [SENS:CORR:COLL[:ACQ]
POWer](../Sense/Sense_Correction.htm#scca) See an example of a [Receiver Power
Calibration](../../GPIB_Example_Programs/Perform_a_Source_Cal_using_SCPI.htm#Receiver).
(Write only) Stores the selected measurements data to that measurements
divisor buffer for use by the Normalization data processing algorithm. This
command is not compatible with ratioed measurements such as S-parameters. It
is intended for receiver power calibration when the selected measurement is of
an unratioed power type. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:NORM  
calculate1:normalize:immediate  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:NORMalize:STATe <ON | OFF> Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA Note: This command
is replaced with [SENS:CORR[:STATe] ON|OFF](../Sense/Sense_Correction.md#scs)
(Read-Write) Specifies whether or not normalization is applied to the
measurement. Normalization is enabled only for measurements of unratioed power
where it serves as a receiver power calibration. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<ON | OFF> | ON (or 1) \- normalization is applied to the measurement. OFF (or 0)  normalization is NOT applied to the measurement.  
Examples | CALC:NORM:STAT ON  
calculate2:normalize:state off  
Query Syntax | CALCulate<cnum>:NORMalize:STATe?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:NORMalize:INTerpolate[:STATe] <ON | OFF> Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA Note: This command
is replaced with [SENS:CORR:INT[:STATe]
ON|OFF](../Sense/Sense_Correction.htm#scis) (Read-Write)  Turns normalization
interpolation ON or OFF. Normalization is enabled only for measurements of
unratioed power, where it serves as a receiver power calibration. See Critical
Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<ON | OFF> | ON (or 1)  turns interpolation ON. OFF (or 0)  turns interpolation OFF.  
Examples | CALC:NORM:INT ON  
calculate2:normalize:interpolate:state off  
Query Syntax | CALCulate<cnum>:NORMalize:INTerpolate[:STATe]?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON

