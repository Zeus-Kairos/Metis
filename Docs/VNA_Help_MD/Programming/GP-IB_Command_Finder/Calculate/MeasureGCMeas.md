# CALCulate:MEASure:GCMeas Commands

Sets and reads Gain Compression Analysis controls.

CALCulate:MEASure:GCMeas ANAlysis | CWFRequency | DISCrete | [:STATe] | ENABle | XAXis  
---  
  
Click a keyword to view the command details.

### Other Gain Compression commands

The calibration commands listed in this topic are supplemental to the Guided
Cal commands.

  * [CALC:MEAS:DEFine](Measure.md#CALCulate:MEASure:DEFine) \- creates a gain compression measurement.

  * [SENS:GCSetup](../Sense/Gain_Compression.md) \- Most Gain Compression settings.

  * [CALC:MEAS:GCData](MasureGCData.md) \- Gain Compression data commands

  * Gain compression data can also be saved to a *.csv file. [Learn how.](../../../Applications/Gain_Compression_Application.md#Saving2D)

See Also

  * [Learn about Gain Compression Application](../../../Applications/Gain_Compression_Application.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<cnum>:MEASure<mnum>:GCMeas:ANALysis:CWFRequency <num>

Applicable Models: c (Read-Write) Set and return the CW frequency for a
compression analysis trace.  
---  
Parameters |   
<cnum> |  Channel number of the measurement (optional).  
<mnum> |  Measurement number for each measurement.  
<num> |  CW frequency in Hz. Choose a frequency within the range of the gain compression channel.  
Examples |  CALC:MEAS2:GCM:ANAL:CWFR 1e9  
calculate2:measure2:gcmeas:analysis:cwfrequency 1e10  
Query Syntax |  CALCulate<cnum>:MEASure<mnum>:GCMeas:ANALysis:CWFRequency?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:GCMeas:ANALysis:DISCrete[:STATe] <bool>

Applicable Models: All with Option S93070xB or S9x070B (Read-Write) Sets and
returns whether the CW frequency for the compression analysis trace can be set
to only the discrete frequencies or provides interpolation.  
---  
Parameters |   
<cnum> |  Channel number of the measurement (optional).  
<mnum> |  Measurement number for each measurement.  
<bool> |  ON (or 1) - Discrete data points only. OFF (or 0) - Interpolated data points.  
Examples |  CALC:MEAS2:GCM:ANAL:DISC ON  
calculate2:measure2:gcmeas:analysis:discrete off  
Query Syntax |  CALCulate<cnum>:MEASure<mnum>:GCMeas:ANALysis:DISCrete?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:GCMeas:ANALysis:ENABle <bool>

Applicable Models: All with Option S93070xB or S9x070B (Read-Write) Enables
and disables a compression analysis trace.  
---  
Parameters |   
<cnum> |  Channel number of the measurement (optional).  
<mnum> |  Measurement number for each measurement.  
<bool> |  ON (or 1) - Enable compression analysis. OFF (or 0) - Disable compression analysis.  
Examples |  CALC:MEAS2:GCM:ANAL:ENAB ON  
calculate2:measure2:gcmeas:analysis:enable off  
Query Syntax |  CALCulate<cnum>:MEASure<mnum>:GCMeas:ANALysis:ENABle?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:GCMeas:ANALysis:XAXis <char>

Applicable Models: All with Option S93070xB or S9x070B (Read-Write) Sets and
returns the type of data to display on the x-axis of a compression analysis
trace.  
---  
Parameters |   
<cnum> |  Channel number of the measurement (optional).  
<mnum> |  Measurement number for each measurement.  
<bool> |  Data to display on X-axis. Choose from:

  * PIN \- Input power to the DUT.
  * PSOurce \- power from the source.

  
Examples |  CALC:MEAS2:GCM:ANAL:XAX PIN  
calculate2:measure2:gcmeas:analysis:xaxis psource  
Query Syntax |  CALCulate<cnum>:MEASure<mnum>:GCMeas:ANALysis:XAXis?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  PIN  
  
* * *

