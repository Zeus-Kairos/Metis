# EmbeddedLO Object

* * *

### Description

Provides access to the properties that allow measurement of mixers that
contain an embedded LO.

### Accessing the EmbeddedLO Interface

Access the Interface through the IMixer Object.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application")  
app.Preset  
  
' FCA Measurements can't share the channel with standard measurements  
' Because preset creates a single measurement in channel 1, we first delete
the standard measurement  
Dim standardMeas As IMeasurement  
Set standardMeas = app.ActiveMeasurement  
standardMeas.Delete  
  
' Create a Measurement object, in this case using the IMeasurement interface  
Dim meas As IMeasurement  
Set meas = app.CreateCustomMeasurementEx(1, "SMC_Forward.SMC_ForwardMeas",
"SC21")  
  
' See if this measurement object supports IMixer  
Dim mixer As IMixer  
Dim embeddedLO  
Set embeddedLO = mixer.EmbeddedLO

Note: The Find Now feature on the Embedded LO dialog is performed remotely by
doing a 'Single Sweep" with ELO enabled. [See example
program](../../COM_Example_Programs/Set_Up_Embedded_LO_Measurement.htm).

See an example program that shows how to create and calibrate a standard
[SMC](../../COM_Example_Programs/Create_and_Cal_an_SMC_Measurement.md) or
[VMC](../../COM_Example_Programs/Create_and_Cal_a_VMC_Measurement.md)
measurement or a [fixed output
SMC](../../COM_Example_Programs/Create_an_SMC_Fixed_Output_Meas.htm)
measurement.

### See Also:

[Example
program](../../COM_Example_Programs/Set_Up_Embedded_LO_Measurement.htm)

[VNA Automation
Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.htm)

[The VNA Object Model](The_Analyzer_Object_Model.md)

[Making Embedded LO Measurements](../../../Applications/Embedded_LO.md)

### Methods

|

### Interface

[See History](IMixer_Interface.md#History) | 

### Description  
  
---|---|---  
[ResetLOFrequency](../Methods/ResetLOFrequency_Method.md) |  IEmbeddedLO |  Reset LO Delta frequency.  
[ResetTuningParameters](../Methods/ResetTuningParameters_Method.md) |  IEmbeddedLO |  Resets the tuning parameters to their defaults.  
  
### Properties

|

###

|

### Description  
  
[BroadbandTuningSpan](../Properties/BroadbandTuningSpan_Property.md) |  IEmbeddedLO |  Set broadband sweep span.  
[EmbeddedLODiagnostic](EmbeddedLODiagnostic_Object.md) |  IEmbeddedLO |  Provides access to the status of tuning sweeps.  
[IsOn](../Properties/IsOn_Property.md) |  IEmbeddedLO |  Set and return Embedded LO ON | OFF.  
[LOFrequencyDelta](../Properties/LOFrequencyDelta_Property.md) |  IEmbeddedLO |  Sets and returns LO delta frequency.  
[MaxPreciseTuningIterations](../Properties/MaxPreciseTuningIterations_Property.md) |  IEmbeddedLO |  Sets and returns precise tuning iterations.  
[NormalizePoint](../Properties/NormalizePoint_Property.md) |  IEmbeddedLO |  Sets and returns tuning point.  
[PreciseTuningTolerance](../Properties/PreciseTuningTolerance_Property.md) |  IEmbeddedLO |  Sets and returns precise tuning tolerance.  
[TuningIFBW](../Properties/TuningIFBW_Property.md) |  IEmbeddedLO |  Sets and returns the IF Bandwidth for tuning sweeps.  
[TuningMode](../Properties/TuningMode_Property.md) |  IEmbeddedLO |  Sets and returns the method used to determine the embedded LO Frequency.  
[TuningSweepInterval](../Properties/TuningSweepInterval_Property.md) |  IEmbeddedLO |  Set how often a tuning sweep is performed.  
  
### IEmbeddedLO History

Interface |  Introduced with VNA Rev:  
---|---  
IEmbeddedLO |  7.21

