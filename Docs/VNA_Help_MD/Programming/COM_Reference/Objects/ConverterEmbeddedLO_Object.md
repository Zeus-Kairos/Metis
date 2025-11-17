# ConverterEmbeddedLO Object

* * *

### Description

Provides access to the properties that allow IMDx and IMSpectrum measurements
of converters that contain an embedded LO.

This interface contains all the same properties and methods of the Embedded LO
interface (used for FCA measurements) EXCEPT access to the
[EmbeddedLODiagnostic Object](EmbeddedLODiagnostic_Object.md).

### Accessing the ConverterEmbeddedLO Interface

Access the Interface through the [Converter](Converter_Object.md) Object. Dim
app Set app = CreateObject("AgilentPNA835x.Application") app.Reset ' Create a
Measurement object, in this case using the IMeasurement interface Dim meas
app.CreateCustomMeasurement 1, "Swept IMD Converters", -1 set meas =
app.activemeasurement dim converter set converter =
app.ActiveChannel.GetConverter dim elo set elo = converter.ConverterEmbeddedLO
elo.IsOn = 1  
---  
  
### See Also:

[VNA Automation
Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.htm)

[The VNA Object Model](The_Analyzer_Object_Model.md)

[Making Embedded LO Measurements](../../../Applications/Embedded_LO.md)

### Methods

|

### Interface

IConverterEmbeddedLO is abbreviated as ICELO [See History](IMixer_Interface.md#History) | 

### Description  
  
---|---|---  
[ResetLOFrequency](../Methods/ResetLOFrequency_Method.md) |  ICELO |  Reset LO Delta frequency.  
[ResetTuningParameters](../Methods/ResetTuningParameters_Method.md) |  ICELO |  Resets the tuning parameters to their defaults.  
  
### Properties

|

###

|

### Description  
  
[BroadbandTuningSpan](../Properties/BroadbandTuningSpan_Property.md) |  ICELO |  Set broadband sweep span.  
[IsOn](../Properties/IsOn_Property.md) |  ICELO |  Set and return Embedded LO ON | OFF.  
[LOFrequencyDelta](../Properties/LOFrequencyDelta_Property.md) |  ICELO |  Sets and returns LO delta frequency.  
[MaxPreciseTuningIterations](../Properties/MaxPreciseTuningIterations_Property.md) |  ICELO |  Sets and returns precise tuning iterations.  
[NormalizePoint](../Properties/NormalizePoint_Property.md) |  ICELO |  Sets and returns tuning point.  
[PreciseTuningTolerance](../Properties/PreciseTuningTolerance_Property.md) |  ICELO |  Sets and returns precise tuning tolerance.  
[TuningIFBW](../Properties/TuningIFBW_Property.md) |  ICELO |  Sets and returns the IF Bandwidth for tuning sweeps.  
[TuningMode](../Properties/TuningMode_Property.md) |  ICELO |  Sets and returns the method used to determine the embedded LO Frequency.  
[TuningSweepInterval](../Properties/TuningSweepInterval_Property.md) |  ICELO |  Set how often a tuning sweep is performed.  
  
### ICELO History

Interface |  Introduced with VNA Rev:  
---|---  
ICELO |  9.00  
  
* * *

