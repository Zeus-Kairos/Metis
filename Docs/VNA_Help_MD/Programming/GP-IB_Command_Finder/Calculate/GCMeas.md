# Gain Compression Analysis Commands

* * *

Sets and reads Gain Compression Analysis controls.

These commands are Superseded by the
[CALCulate:MEASure:GCMeas](MeasureGCMeas.md) commands.

CALCulate:GCMeas:ANALysis [CWFRequency](GCMeas.md#cwfreq)
[ENABle](GCMeas.md#enable) [ISDisfreq](GCMeas.md#isd)
[XAXis](GCMeas.md#xaxis)  
---  
  
Click on a keyword to view the command details.

### Other Gain Compression commands

The calibration commands listed in this topic are supplemental to the Guided
Cal commands.

  * [CALC:CUSTom:DEFine](Custom.md#CustDef) \- creates a gain compression measurement.

  * [SENS:GCSetup](../Sense/Gain_Compression.md) \- Most Gain Compression settings.

  * [GC:DATA](GCData.md) \- Gain Compression data commands

  * Gain compression data can also be saved to a *.csv file. [Learn how.](../../../Applications/Gain_Compression_Application.md#Saving2D)

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about Compression Analysis](../../../Applications/Gain_Compression_Application.md#Analysis)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<cnum>:GCMeas:ANALysis:ENABle <bool>

Applicable Models: N522xB, N524xB, M9485A, E5080A (Read-Write) Enables and
disables a compression analysis trace.  
---  
Parameters |   
<cnum> |  Channel number of the GCA measurement. There must be a selected measurement on that channel using [Calc:Par:Sel.](Parameter.md#cps) If unspecified, <cnum> is set to 1.  
<bool> |  ON (or 1) - Enable compression analysis. OFF (or 0) - Disable compression analysis.  
Examples |  CALC:GCM:ANAL:ENAB ON  
calculate2:gcmeas:analysis:enable off  
Query Syntax |  CALCulate<cnum>:GCMeas:ANALysis:ENABle?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## CALCulate<cnum>:GCMeas:ANALysis:CWFRequency <num>

Applicable Models: N522xB, N524xB, M9485A, E5080A (Read-Write) Set and return
the CW frequency for a compression analysis trace.  
---  
Parameters |   
<cnum> |  Channel number of the GCA measurement. There must be a selected measurement on that channel using [Calc:Par:Sel.](Parameter.md#cps) If unspecified, <cnum> is set to 1.  
<num> |  CW frequency in Hz. Choose a frequency within the range of the gain compression channel.  
Examples |  CALC:GCM:ANAL:CWFR 1e9  
calculate2:gcmeas:analysis:cwfrequency 1e10  
Query Syntax |  CALCulate<cnum>:GCMeas:ANALysis:CWFRequency?  
Return Type |  Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CALCulate<cnum>:GCMeas:ANALysis:DISCrete | ISD[:STATe] <bool>

Applicable Models: N522xB, N524xB, M9485A, E5080A (Read-Write) Sets and
returns whether the CW frequency for the compression analysis trace can be set
to only the discrete frequencies or provides interpolation.  
---  
Parameters |   
<cnum> |  Channel number of the GCA measurement. There must be a selected measurement on that channel using [Calc:Par:Sel.](Parameter.md#cps) If unspecified, <cnum> is set to 1.  
<bool> |  ON (or 1) - Discrete data points only. OFF (or 0) - Interpolated data points.  
Examples |  CALC:GCM:ANAL:ISD ON  
calculate2:gcmeas:analysis:isdisfrequency off  
Query Syntax |  CALCulate<cnum>:GCMeas:ANALysis:ISDisfrequency?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## CALCulate<cnum>:GCMeas:ANALysis:XAXis <char>

Applicable Models: N522xB, N524xB, M9485A, E5080A (Read-Write) Sets and
returns the type of data to display on the x-axis of a compression analysis
trace.  
---  
Parameters |   
<cnum> |  Channel number of the GCA measurement. There must be a selected measurement on that channel using [Calc:Par:Sel.](Parameter.md#cps) If unspecified, <cnum> is set to 1.  
<bool> |  Data to display on X-axis. Choose from:

  * PIN \- Input power to the DUT.
  * PSOurce \- power from the source.

  
Examples |  CALC:GCM:ANAL:XAX PIN  
calculate2:gcmeas:analysis:xaxis psource  
Query Syntax |  CALCulate<cnum>:GCMeas:ANALysis:XAXis?  
Return Type |  Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  PIN  
  
* * *

* * *

