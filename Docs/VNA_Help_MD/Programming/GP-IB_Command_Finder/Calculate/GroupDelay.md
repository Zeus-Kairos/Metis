# Group Delay Aperture Commands

* * *

Controls the Aperture setting used to make Group Delay measurements.

These commands are Superseded by the
[CALCulate:MEASure:GDELay](MeasureGDELay.md) commands.

CALCulate:GDELay [FREQuency](GroupDelay.md#freq)
[PERCent](GroupDelay.md#percent) [POINts](GroupDelay.md#points)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Learn about Group Delay Aperture](../../../S4_Collect/Use_Limits_to_Test_Devices.md)

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).

* * *

## CALCulate<cnum>:GDELay:FREQuency <value>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
group delay aperture using a fixed frequency range. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<value> | Frequency range (in Hz) to use for the aperture setting. Choose between the equivalent of two data points and the channel frequency span.  
Examples | CALC:GDEL:FREQ 1E6  
Query Syntax | CALCulate<cnum>:GDELay:FREQuency?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Frequency range that equates to 11 points. This can be changed to two points with a [preference setting](../../../System/Preferences.md#GroupDelay).  
  
* * *

## CALCulate<cnum>:GDELay:PERCent <value>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
group delay aperture using a percent of the channel frequency span. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<value> | Percent of frequency span to use for the aperture setting. Choose between the equivalent of two data points and 100 percent of the channel frequency span.  
Examples | 'set to 25 percent of the channel frequency span CALC:GDEL:PERC 25  
Query Syntax | CALCulate<cnum>:GDELay:PERCent?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Percent of frequency span that equates to 11 points. This can be changed to two points with a [preference setting](../../../System/Preferences.md#GroupDelay).  
  
* * *

## CALCulate<cnum>:GDELay:POINts <value>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
group delay aperture using a fixed number of data points. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<value> | Number of data points to use for the aperture setting. Choose between two points and the number of points in the channel.  
Examples | 'set to 25 data points CALC:GDEL:POIN 25  
Query Syntax | CALCulate<cnum>:GDELay:POINts?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 11 points. This can be changed to two points with a [preference setting](../../../System/Preferences.md#GroupDelay).  
  
* * *

