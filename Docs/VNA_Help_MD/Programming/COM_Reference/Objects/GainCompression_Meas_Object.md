# Gain Compression Measurement Object

* * *

### Description

Controls the Gain Compression Analysis settings.

### Accessing the GainCompressionMeas object

Set app = CreateObject("AgilentPNA835x.Application") app.Preset
app.ActiveMeasurement.Delete ' create a GCA measurement
app.CreateCustomMeasureMentEx 1, "Gain Compression","CompIn21", 1 Set meass =
app.Measurements ' get the measurements collection Set ana =
meass(1).CustomMeasurementConfiguration 'get the measurement
ana.AnalysisEnable = true ' enable the analysis mode  
---  
  
### See Also:

  * Example Program [Create and Cal a Gain Compression Measurement](../../COM_Example_Programs/Create_and_Cal_a_Gain_Compression_Measurement.md) (includes Analysis)

  * [GainCompression Object](GainCompression_Object.md)

  * [GainCompressionCal Object](GainCompressionCal_Object.md)

  * [About Gain Compression Application](../../../Applications/Gain_Compression_Application.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

### Method

|

### Interface

### [See History](IIFConfiguration_Object.md#history)

|

### Description  
  
---|---|---  
None |  |   
  
### Property

|

### Interface

|

### Description  
  
[AnalysisCWFreq](../Properties/AnalysisCWFreq_Property.md) |  IGainCompressionMeas |  Set CW frequency.  
[AnalysisEnable](../Properties/AnalysisEnable_Property.md) |  IGainCompressionMeas |  Enable a compression analysis trace.  
[AnalysisIsDiscreteFreq](../Properties/AnalysisIsDiscreteFreq_Property.md) |  IGainCompressionMeas |  Set to discrete or interpolated CW frequencies.  
[AnalysisXAxis](../Properties/AnalysisXAxis_Property.md) |  IGainCompressionMeas |  Sets X-axis display.  
  
###  IGainCompressionMeas History

Interface |  Introduced with VNA Rev:  
---|---  
IGainCompressionMeas |  9.0  
  
* * *

