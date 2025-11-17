# Capabilities Object

* * *

### Description

These properties return capabilities of the remote VNA.

### Accessing the Capabilities object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim cap As Capabilities  
Set cap = app.Capabilities

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [ICapabilities History](Capabilities_Object.md#Interface1)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

[See History](Capabilities_Object.md#Interface1) | 

###  
  
---|---|---  
[GetPortNumber Method](../Methods/GetPortNumber_Method.md) | ICapabilities4 | Returns the port number for the specified string port name.  
  
### Properties

|

###

|

### Description  
  
[AvailableMeasurementClasses](../Properties/AvailableMeasurementClasses_Property.md) | ICapabilities7 | Returns the measurement classes on the VNA  
[CpuRevision](../Properties/CpuRevision_Property.md) | ICapabilities6 | Returns the CPU speed of the VNA  
[DirectoryPath](../Properties/DirectoryPath_Property.md) | ICapabilities10 | Returns the directory location.  
[DspRevision](../Properties/DSPRevision_Property.md) | ICapabilities6 | Returns the DSP Revision number  
[DspFpgaRevision](../Properties/DspFpgaRevision_Property.md) | ICapabilities6 | Returns the DSP FPGA Revision number  
[FirmwareMajorRevision](../Properties/FirmwareMajorRevision_Property.md) | ICapabilities | Returns integer portion of firmware revision number.  
[FirmwareMinorRevision](../Properties/FirmwareMinorRevision.md) | ICapabilities | Return decimal portion of firmware revision number.  
[FirmwareSeries](../Properties/FirmwareSeries_Property.md) | ICapabilities | Returns the Alpha portion of the firmware revision number.  
[GPIBPortCount](../Properties/GPIBPortCount_Property.md) | ICapabilities3 | Returns the number of GPIB ports (1or 2)  
[HasDirectReceiverAccess](../Properties/HasDirectReceiverAccess_Property.md) | ICapabilities12 | Returns whether or not the analyzer has direct receiver access (front-panel jumpers).  
[HasLowFrequencyExtension](../Properties/HasLowFrequencyExtension_Property.md) | ICapabilities16 | Returns whether or not the VNA has the low frequency extension (LFE) installed.  
[IFBWList](../Properties/IFBWList_Property.md) | ICapabilities8 | Returns a list of supported IFBW values.  
[InternalDCReceiverCount](../Properties/InternalDCReceiverCount_Property.md) | ICapabilities14 | Returns the number of internal DC receivers in the analyzer.  
[InternalDCReceiverNames](../Properties/InternalDCReceiverNames_Property.md) | ICapabilities14 | Returns a list of names of the internal DC receivers.  
[InternalDCSourceCount](../Properties/InternalDCSourceCount_Property.md) | ICapabilities14 | Returns the number of internal DC sources in the analyzer.  
[InternalDCSourceNames](../Properties/InternalDCSourceNames_Property.md) | ICapabilities14 | Returns a list of names of the internal DC sources.  
[InternalSourcePortCount](../Properties/InternalSourcePortCount_Property.md) | ICapabilities13 | Returns the number of internal source ports.  
[InternalSourcePortNames](../Properties/InternalSourcePortNames_Property.md) | ICapabilities13 | Returns a list of internal source port names.  
[InternalTestsetPortCount](../Properties/InternalTestsetPortCount_Property.md) | ICapabilities | Returns the number of VNA test ports.  
[InternalTestsetPortNames](../Properties/InternalTestsetPortNames_Property.md) | ICapabilities13 | Returns a list of internal test port names.  
[IsFrequencyOffsetPresent](../Properties/IsFrequencyOffsetPresent_Property.md) | ICapabilities | Returns the presence of Frequency Offset Option S93080A/B (True or False).  
[IsReceiverStepAttenuatorPresent](../Properties/IsReceiverStepAttenuatorPresent_Property.md) | ICapabilities | Returns the presence of receiver step attenuators (True or False).  
[IsReferenceBypassSwitchPresent](../Properties/IsReferenceBypassSwitchPresent_Property.md) | ICapabilities | Returns the presence of the reference switch (True or False).  
[MaximumFrequency](../Properties/MaximumFrequency_cap_Property.md) | ICapabilities | Returns the maximum frequency of the VNA.  
[MaximumNumberOfChannels](../Properties/MaximumNumberOfChannels_Property.md) | ICapabilities2 | Returns the maximum possible number of Channels  
[MaximumNumberOfPoints](../Properties/MaximumNumberOfPoints.md) | ICapabilities | Returns the maximum possible number of data points.  
[MaximumNumberOfTracesPerWindow](../Properties/MaximumNumberOfTracesPerWindow_Property.md) | ICapabilities2 | Returns the maximum possible number of traces per window  
[MaximumNumberOfWindows](../Properties/MaximumNumberOfWindows_Property.md) | ICapabilities2 | Returns the maximum possible number of windows  
[MaximumReceiverStepAttenuator](../Properties/MaximumReceiverStepAttenuator_Property.md) | ICapabilities | Returns the maximum amount of receiver attenuation.  
[MaximumSourceALCPower](../Properties/MaximumSourceALCPower_Property.md) | ICapabilities | Returns the maximum amount of source ALC power.  
[MaximumSourceStepAttenuator](../Properties/MaximumSourceStepAttenuator_Property.md) | ICapabilities | Returns the maximum amount of source attenuation.  
[MeasurementClassProperties](../Properties/MeasurementClassProperties_Property.md) | ICapabilities8 | Returns a handle to the MeasurementClassProperties Object  
[MinimumFrequency](../Properties/MinimumFrequency_cap_Property.md) | ICapabilities | Returns the minimum frequency of the VNA.  
[MinimumNumberOfPoints](../Properties/MinimumNumberOfPoints.md) | ICapabilities | Returns the minimum possible number of data points.  
[MinimumReceiverStepAttenuator](../Properties/MinimumReceiverStepAttenuator_Property.md) | ICapabilities | Returns the minimum amount of receiver attenuation.  
[MinimumSourceALCPower](../Properties/MinimumSourceALCPower_Property.md) | ICapabilities | Returns the minimum amount of source ALC power.  
[ModelNumber](../Properties/ModelNumber_Property.md) | ICapabilities11 | Returns the model number of the VNA.  
[NoiseReceiverNoiseBWList](../Properties/NoiseReceiverNoiseBWList_Property.md) | ICapabilities13 | Returns the list of supported Noise Bandwidths values when using a noise receiver (option 029).  
[PowerRange](Power_Range_Object.md) | ICapabilities15 | Returns the PowerRange object.  
[PresetMaxFrequency](../Properties/PresetMaxFrequency_Property.md) | ICapabilities13 | Returns the maximum specified frequency of the analyzer. Does not include any over-sweep.  
[PresetMinFrequency](../Properties/PresetMinFrequency_Property.md) | ICapabilities13 | Returns the minimum specified frequency of the analyzer. Does not include any over-sweep.  
[ReceiverCount](../Properties/ReceiverCount_Property.md) | ICapabilities | Returns the number of receivers in the VNA.  
[ReceiverStepAttenuatorStepSize](../Properties/ReceiverStepAttenuatorStepSize_Property.md) | ICapabilities | Returns the step size of the attenuator.  
[ReceiverTemperature Property](../Properties/ReceiverTemperature_Property.md) | ICapabilities9 | Returns the temperature on the receiver board.  
[ResBWList](../Properties/ResBWList_Property.md) | ICapabilities8 | Returns a list of Res BW values that are supported by IM Spectrum.  
[ResBWListSA](../Properties/ResBWList_Property.md) | ICapabilities17 | Returns the list of supported Resolution BW values for the SA channel.  
[SerialNumber](../Properties/SerialNumber_Property.md) | ICapabilities11 | Returns the serial number of the VNA.  
[SourceCount](../Properties/SourceCount_Property.md) | ICapabilities | Returns the number of sources.  
[SourcePortCount](../Properties/SourcePortCount_Property.md) | ICapabilities4 | Returns the number of source ports.  
[SourcePortNames](../Properties/SourcePortNames_Property.md) | ICapabilities4 | Returns the string names of source ports.  
[SourceStepAttenuatorStepSize](../Properties/SourceStepAttenuatorStepSize_Property.md) | ICapabilities5 | Returns a value indicating the step size of the source attenuator.  
[StandardReceiverNoiseBWList](../Properties/StandardReceiverNoiseBWList_Property.md) | ICapabilities13 | Returns the list of supported Noise Bandwidths values when using the NA receiver for noise measurements (option 028).  
[TestPortNames](../Properties/TestPortNames_Property.md) | ICapabilities13 | Returns a list of test port names including external test set ports.  
  
###  ICapabilities History

I Interface | Introduced with VNA Rev:  
---|---  
ICapabilities | 3.5  
ICapabilities2 | 5.23  
ICapabilities3 | 6.0  
ICapabilities4 | 7.20  
ICapabilities5 | 8.04  
ICapabilities6 | 9.10  
ICapabilities7 | 9.33  
ICapabilities8 | 9.40  
ICapabilities9 | 9.50  
ICapabilities10 | 10.0  
ICapabilities11 | 10.0  
ICapabilities12 | 10.40  
ICapabilities13 | 10.40  
ICapabilities14 | 10.45  
ICapabilities15 | 12.70  
ICapabilities16 | 12.80  
ICapabilities17 | 13.25

