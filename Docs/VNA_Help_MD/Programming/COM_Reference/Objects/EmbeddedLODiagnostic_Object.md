# EmbeddedLODiagnostic Object

* * *

### Description

Allows access to the properties that provide information about the broadband
and precise tuning of an embedded LO.

### Accessing the EmbeddedLODiagnostic Interface

Access the Interface through the EmbeddedLO Object.

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
  
Dim embeddedLODiagnostic  
Set embeddedLODiagnostic = embeddedLO.EmbeddedLODiagnostic

See an example program that shows how to create and calibrate a standard
[SMC](../../COM_Example_Programs/Create_and_Cal_an_SMC_Measurement.md) or
[VMC](../../COM_Example_Programs/Create_and_Cal_a_VMC_Measurement.md)
measurement or a [fixed output
SMC](../../COM_Example_Programs/Create_an_SMC_Fixed_Output_Meas.htm)
measurement.

### See Also:

[VNA Automation
Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.htm)

[The VNA Object Model](The_Analyzer_Object_Model.md)

[Making Embedded LO Measurements](../../../Applications/Embedded_LO.md)

[EmbeddedLO Object](EmbeddedLO_Object.md)

### Methods

|

### Interface

[See History](IMixer_Interface.md#History) | 

### Description  
  
---|---|---  
[Clear](../Methods/Clear_Method.md) |  IELODiag |  Clear current diagnostic information.  
  
### Properties

|

###

|

### Description  
  
[IsMarkerOn](../Properties/IsMarkerOn_Property.md) |  IELODiag |  Was a marker was used for a tuning sweep?  
[LODeltaFound](../Properties/LODeltaFound_Property.md) |  IELODiag |  Returns the LO frequency delta from this tuning sweep.  
[NumberOfSweeps](../Properties/NumberOfSweeps_Property.md) |  IELODiag |  Get number of tuning sweeps.  
[MarkerAnnotation](../Properties/MarkerAnnotation_Property.md) |  IELODiag |  Get the marker annotation.  
[MarkerPosition](../Properties/MarkerPosition_Property.md) |  IELODiag |  Get the marker X-axis position.  
[Parameter](../Properties/Parameter_elo_Property.md) |  IELODiag |  Returns the tuning sweep parameter name.  
[StatusAsString](../Properties/StatusAsString_Property.md) |  IELODiag |  Get result of the last tuning sweeps.  
[StepData](../Properties/StepData_Property.md) |  IELODiag |  Get a tuning sweep data.  
[StepTitle](../Properties/StepTitle_Property.md) |  IELODiag |  Returns the tuning sweep title.  
[XAxisAnnotation](../Properties/XAxisAnnotation_Property.md) |  IELODiag |  Get the tuning sweep X axis annotation.  
[XAxisStart](../Properties/XAxisStart_Property.md) |  IELODiag |  Get the Start sweep value.  
[XAxisStop](../Properties/XAxisStop_Property.md) |  IELODiag |  Get the Stop sweep value.  
[YAxisAnnotation](../Properties/YAxisAnnotation_Property.md) |  IELODiag |  Get the tuning sweep Y axis annotation.  
  
###  History

Interface |  Introduced with VNA Rev:  
---|---  
IEmbeddedLODiagnostic |  7.21

