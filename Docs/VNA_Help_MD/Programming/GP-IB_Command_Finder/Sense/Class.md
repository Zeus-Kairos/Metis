# Sense:Class Command

* * *

SENSe:CLASs: [NAME?](Class.md#name)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Learn about Measurement Class](../../../S1_Settings/Measurement_Classes.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<cnum>:CLASs:NAME?

Applicable Models: All (Read-only) Returns the measurement class name of the
specified channel. Use
[CALCulate:MEASure:DEFine](../Calculate/Measure.md#CALCulate:MEASure:DEFine)
and
[CALCulate:MEASure:PARameter](../Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter)
commands to create measurements.  
---  
Parameters |   
<cnum> |  Any existing channel number; if unspecified, value is set to 1.  
Examples |  SENS:CLAS:NAME?  
sense2:class:name? For a standard S-Parameter channel, returns...  
"Standard"  
Default |  Not applicable  
  
* * *

