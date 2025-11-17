# Calculate:Format Commands

These commands are Superseded by the
[CALCulate:MEASure:FORMat](Measure.md#CALCulate:MEASure:FORMat) commands.

* * *

CALCulate: | [FORMat](Format_Calc.md#format) | [UNIT](Format_Calc.md#Unit)  
---  
  
Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).

See Also

  * [Example](../../GPIB_Example_Programs/Setup_the_Display_using_GPIB.md) using this command.

  * [Learn About Data Format](../../../S1_Settings/Data_Format.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

* * *

CALCulate<cnum>:FORMat <char>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
the display format for the measurement. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<char> | Choose from:

  * MLINear
  * MLOGarithmic
  * PHASe
  * UPHase 'Unwrapped phase
  * IMAGinary
  * REAL
  * POLar
  * SMITh
  * SADMittance 'Smith Admittance
  * SWR
  * GDELay 'Group Delay
  * KELVin
  * FAHRenheit
  * CELSius
  * PPHase 'Positive Phase
  * IMPedance
  * VOLT
  * COMPlex

  
Examples | CALC:FORM MLIN  
calculate2:format polar  
Query Syntax | CALCulate<cnum>:FORMat?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | MLOG  
  
* * *

CALCulate<cnum>:FORMat:UNIT <dataFormat>, <units>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
and returns the units for the specified data format. Measurements with display
formats other than those specified are not affected. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<dataFormat> | Choose from:

  * MLOG \- Log magnitude
  * MLIN \- Linear magnitude

  
<units> | For unratioed MLOG measurements, choose from:

  * DB Units are displayed in decibels.
  * DBM Units are displayed in dBm. 0 dBm = 0.001 watt
  * DBMV Units are displayed in dBmV. 0 dBmV = 0.001 volt  
DBmV value depends on the reference impedance: dBmV = dBm + 30 + 10*log10(Z0)

  * DBMA Units are displayed in dBmA. 0 dBmA = 0.001 Ampere
  * DBUV Units are displayed in dBuV. 0 dBuV = 1 uV   
DBuV value depends on the reference impedance: dBuV = dBm + 90 + 10*log10(Z0)

For unratioed MLIN measurements, choose from:

  * U \- No units. Linear magnitude without conversion
  * W \- Units are displayed in Watts
  * V \- Units are displayed in Volts
  * A \- Units are displayed in Amperes

  
Examples | CALC:FORM:UNIT MLOG, DBM  
calculate2:format:unit mlog,dbmv  
Query Syntax | CALCulate<cnum>:FORMat:UNIT? <dataFormat>  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | MLOG, DBM  
  
* * *

