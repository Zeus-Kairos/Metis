# SignalProcessingModuleFour Object

* * *

### Description

Contains the properties for configuring the DSP (digital filters) in the
PNA-X.

![](../../../assets/images/Programming/DSPBlockDiag.gif)

[See the entire IF Path Block
diagram.](../../../IFAccess/IF_Path_Configuration.htm)

DSP Version 5 Notes Programs that control these settings, or state files that
are saved, will yield different results when run or recalled on VNAs with DSP
4 versions versus DSP 5 Versions. Stage 2 settings are IGNORED with DSP 5
Versions. [Learn more about DSP Versions](../../../S0_Start/HelpAbout.md)  
---  
  
### Accessing the SignalProcessingModuleFour object

Dim app as AgilentPNA835x.Application  
Dim chan as Channel  
Set chan = app.ActiveChannel  
Dim digFilter as SignalProcessingModuleFour  
Set digFilter = chan.SignalProcessingModuleFour

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * About PNA-X Pulse Capabilities

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

###

|

### Description  
  
---|---|---  
None |  |   
  
### Properties

|

### Interface

[See History](IIFConfiguration_Object.md#history) | 

### Description  
  
[ADCCaptureMode](../Properties/ADCCaptureMode_Property.md) | ISignalProcessingModuleFour | Sets ADC capture mode: auto or manual  
[FilterErrors](../Properties/FilterErrors_Property.md) | ISignalProcessingModuleFour | Returns errors with manual digital filter settings  
[FilterMode](../Properties/FilterMode_Property.md) | ISignalProcessingModuleFour | Sets digital filter mode:auto or manual  
[Stage1Coefficients](../Properties/Stage1Coefficients_Property.md) | ISignalProcessingModuleFour | Sets Stage1Coefficients  
[Stage1Frequency](../Properties/Stage1Frequency_Property.md) | ISignalProcessingModuleFour | Sets Stage1 NCO frequency  
[Stage1MaximumCoefficient](../Properties/Stage1MaximumCoefficient_Property.md) | ISignalProcessingModuleFour | Returns the maximum value of any single stage1coefficient.  
[Stage1MaximumCoefficientCount](../Properties/Stage1MaximumCoefficientCount_Property.md) | ISignalProcessingModuleFour | Returns the maximum number of Stage1 coefficients.  
[Stage1MaximumCoefficientSum](../Properties/Stage1MaximumCoefficientSum_Property.md) | ISignalProcessingModuleFour | Returns the maximum sum of all Stage1 coefficients.  
[Stage1MinimumCoefficientCount](../Properties/Stage1MinimumCoefficientCount_Property.md) | ISignalProcessingModuleFour | Returns the minimum number of Stage1 coefficients  
[Stage2Coefficients](../Properties/Stage2Coefficients_Property.md) | ISignalProcessingModuleFour | Sets Stage2 Coefficients  
[Stage2MaximumCoefficient](../Properties/Stage2MaximumCoefficient_Property.md) | ISignalProcessingModuleFour | Returns the maximum value of any single stage2 coefficient.  
[Stage2MaximumCoefficientCount](../Properties/Stage2MaximumCoefficientCount_Property.md) | ISignalProcessingModuleFour | Returns the maximum number of Stage2 coefficients  
[Stage2MaximumCoefficientSum](../Properties/Stage2MaximumCoefficientSum_Property.md) | ISignalProcessingModuleFour | Returns the maximum sum of all Stage2 coefficients.  
[Stage2MinimumCoefficientCount](../Properties/Stage2MinimumCoefficientCount_Property.md) | ISignalProcessingModuleFour | Returns the minimum number of Stage2 coefficients  
[Stage3Coefficients](../Properties/Stage3Coefficients_Property.md) | ISignalProcessingModuleFour2 | Sets and returns Stage3Coefficients.  
[Stage3FilterType](../Properties/Stage3FilterType_Property.md) | ISignalProcessingModuleFour | Sets and returns stage3 filter type  
[Stage3FilterTypes](../Properties/Stage3FilterTypes_Property.md) | ISignalProcessingModuleFour | Returns the names of supported types of Stage3 filters.  
[Stage3MaximumCoefficient](../Properties/Stage3MaximumCoefficient_Property.md) | ISignalProcessingModuleFour2 | Returns the maximum number of coefficients for Stage3.  
[Stage3MaximumCoefficientCount](../Properties/Stage3MaximumCoefficientCount_Property.md) | ISignalProcessingModuleFour2 | Returns the maximum number of Stage3coefficients  
[Stage3MinimumCoefficient](../Properties/Stage3MinimumCoefficient_Property.md) | ISignalProcessingModuleFour2 | Returns the minimum value of any single stage3coefficient.  
[Stage3MinimumCoefficientCount](../Properties/Stage3MinimumCoefficientCount_Property.md) | ISignalProcessingModuleFour2 | Returns the minimum number of Stage3coefficients  
[Stage3Parameter](../Properties/Stage3Parameter_Property.md) | ISignalProcessingModuleFour | Sets and returns the parameter value of the current filter type.  
[Stage3ParameterMaximum](../Properties/Stage3ParameterMaximum_Property.md) | ISignalProcessingModuleFour | Returns maximum parameter value for the current filter type.  
[Stage3ParameterMinimum](../Properties/Stage3ParameterMinimum_Property.md) | ISignalProcessingModuleFour | Returns minimum parameter value for the current filter type.  
[Stage3Parameters](../Properties/Stage3Parameters_Property.md) | ISignalProcessingModuleFour | Returns the names of parameters for the current filter type.  
  
###  ISignalProcessingModuleFour History

Interface | Introduced with VNA Rev:  
---|---  
ISignalProcessingModuleFour2 | 9.90  
ISignalProcessingModuleFour | 7.2  
  
* * *

