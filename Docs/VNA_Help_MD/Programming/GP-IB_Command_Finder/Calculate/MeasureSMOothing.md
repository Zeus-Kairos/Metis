# CALCulate:MEASure:SMOothing Commands

Controls point-to-point smoothing. Smoothing is a noise reduction technique
that averages adjacent data points in a measurement trace. Choose the amount
of smoothing by specifying either the number of points or the aperture.
Smoothing is not the same as CALC:AVERage which averages each data point over
a number of sweeps.

CALCulate:MEASure:SMOothing APERture POINts [:STATe]  
---  
  
Click a keyword to view the command details.

See Also

  * [Learn about Smoothing](../../../S2_Opt/Trce_Noise.md#Smoothing)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<cnum>:MEASure<mnum>:SMOothing:APERture <num>

Applicable Models: All (Read-Write) Sets the amount of smoothing as a
percentage of the number of data points in the channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Percentage value. Choose any number between:  
1 and 25  
Examples | CALC:MEAS:SMO:APER 2  
calculate2:measure2:smoothing:aperture 20.7  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:SMOothing:APERture?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:SMOothing:POINts <num>

Applicable Models: All (Read-Write) Sets the number of adjacent data points to
average.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Number of points from 1 point to maximum of 25% of data points in the channel. For example: if number of points in a data trace = 401, the maximum value for points = 100. The points value is always rounded to the closest odd number.  
Examples | CALC:MEAS:SMO:POIN 50  
calculate2:measure2:smoothing:points 21  
Query Syntax | CALCulate<cnum>:MEAsure<mnum>:SMOothing:POINts?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:SMOothing[:STATe] <bool>

Applicable Models: All (Read-Write) Turns data smoothing ON or OFF.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | ON or 1 \- Turns smoothing ON.  
OFF or 0 \- Turns smoothing OFF.  
Examples | CALC:MEAS:SMO ON  
calculate2:measure2:smoothing:state off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:SMOothing[:STATe]  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

