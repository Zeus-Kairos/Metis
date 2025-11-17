# CALCulate:MEASure:GDELay Commands

Controls the Aperture setting used to make Group Delay measurements.

CALCulate:MEASure:GDELay FREQuency PERCent POINts  
---  
  
Click a keyword to view the command details.

See Also

  * [Learn about Group Delay Aperture](../../../S4_Collect/Use_Limits_to_Test_Devices.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<cnum>:MEASure<mnum>:GDELay:FREQuency <value>

Applicable Models: All (Read-Write) Sets group delay aperture using a fixed
frequency range.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<value> | Frequency range (in Hz) to use for the aperture setting. Choose between the equivalent of two data points and the channel frequency span.  
Examples | CALC:MEAS2:GDEL:FREQ 1E6  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:GDELay:FREQuency?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Frequency range that equates to 11 points. This can be changed to two points with a [preference setting](../../../System/Preferences.md#GroupDelay).  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:GDELay:PERCent <value>

Applicable Models: All (Read-Write) Sets group delay aperture using a percent
of the channel frequency span.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<value> | Percent of frequency span to use for the aperture setting. Choose between the equivalent of two data points and 100 percent of the channel frequency span.  
Examples | 'set to 25 percent of the channel frequency span CALC:MEAS2:GDEL:PERC 25  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:GDELay:PERCent?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Percent of frequency span that equates to 11 points. This can be changed to two points with a [preference setting](../../../System/Preferences.md#GroupDelay).  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:GDELay:POINts <value>

Applicable Models: All (Read-Write) Sets group delay aperture using a fixed
number of data points.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<value> | Number of data points to use for the aperture setting. Choose between two points and the number of points in the channel.  
Examples | 'set to 25 data points CALC:MEAS2:GDEL:POIN 25  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:GDELay:POINts?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 11 points. This can be changed to two points with a [preference setting](../../../System/Preferences.md#GroupDelay).  
  
* * *

