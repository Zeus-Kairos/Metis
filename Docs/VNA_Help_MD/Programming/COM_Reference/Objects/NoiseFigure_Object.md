# NoiseFigure Object

* * *

### Description

Controls the Noise Figure application settings.

### Accessing the NoiseFigure object

Dim app as AgilentPNA835x.Application
app.[CreateCustomMeasurementEx](../Methods/CreateCustomMeasurementEx_Method.md)(1,
"NoiseFigure", "NF", 1) Dim NoiseFig Set NoiseFig =
app.ActiveChannel.[CustomChannelConfiguration](../Properties/CustomChannelConfiguration_Property.md)  
---  
  
### See Also:

  * Example programs

  *     * [Create and Cal a NoiseFigure Measurement](../../COM_Example_Programs/Create_and_Cal_a_NoiseFigure_Measurement.md)

    * [Create and Cal an NFX Measurement](../../COM_Example_Programs/Create_and_Cal_an_NFX_Measurement.md)

  * [About Noise Figure Measurements](../../../Applications/Noise_Figure.md)

  * [Noise Figure Calibration Object](NoiseCal_Object.md)

  * [app.NoiseSourceState (ON and OFF)](../Properties/NoiseSourceState_Property.md)

  * [ENRFile Object](ENRFile_Object.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

### Method

|

### Interface

### [See History](IIFConfiguration_Object.md#history)

|

### Description  
  
---|---|---  
[GetSnPData](../Methods/GetSnpData_Method.md) |  INoiseFigure7 |  Reads noise parameter snp data.  
[SetPortMap](../Methods/SetPortMap_Method.md) |  INoiseFigure6 |  Maps DUT ports to PNA-X ports (Opt 028)  
[WriteSnPData](../Methods/WriteSnPData_Method.md) |  INoiseFigure7 |  Reads noise parameter data to snp file.  
  
### Property

|

### Interface

|

### Description  
  
[AmbientTemperature](../Properties/AmbientTemperature_Property.md) |  INoiseFigure |  Sets the air temperature at which the measurement is being performed.  
[DeviceInputPort](../Properties/DeviceInputPort_Property.md) |  INoiseFigure6 |  Read DUT input port map  
[DeviceOutputPort](../Properties/DeviceOutputPort_Property.md) |  INoiseFigure6 |  Read DUT output port map  
[ImpedanceStates](../Properties/ImpedanceStates_Property.md) |  INoiseFigure |  Sets the number of impedance states to use during calibrated measurements.  
[NarrowBand](../Properties/NarrowBand_Property.md) |  INoiseFigure8 |  Enable narrowband compensation  
[NoiseAverageFactor](../Properties/NoiseAverageFactor_Property.md) |  INoiseFigure |  Set averaging of noise receiver.  
[NoiseAverageState](../Properties/NoiseAverageState_Property.md) |  INoiseFigure |  Turn noise averaging ON and OFF  
[NoiseBandwidth](../Properties/NoiseBandwidth_Property.md) |  INoiseFigure |  Set bandwidth of noise receiver.  
[NoiseGain](../Properties/NoiseGain_Property.md) |  INoiseFigure |  Set gain state of noise receiver.  
[NoiseGainCTCheck](../Properties/NoiseGainCTCheck.md) |  INoiseFigure3 |  Turns noise threshold checking ON and OFF.  
[NoiseReceiver](../Properties/NoiseReceiver_Property.md) |  INoiseFigure5 |  Sets and returns the receiver to use for noise measurements.  
[NoiseReceiverSweepTime](../Properties/NoiseReceiverSweepTime_Property.md) |  INoiseFigure3 |  Returns an estimate of sweep time.  
[NoiseTuner](../Properties/NoiseTuner_Property.md) |  INoiseFigure |  Sets and returns the noise tuner identifier,  
[NoiseTunerIn](../Properties/NoiseTunerIn_Property.md) |  INoiseFigure |  Sets and returns the port identifier of the ECal noise tuner Input  
[NoiseTunerOut](../Properties/NoiseTunerOut_Property.md) |  INoiseFigure |  Sets and returns the port identifier of the ECal noise tuner Output  
[SourcePullForSParameters](../Properties/SourcePullForSParameters_Property.md) |  INoiseFigure4 |  Set and read the use of source pull technique to compute S22 on Noise Figure on Converters.  
  
###  NoiseFigure History

Interface |  Introduced with VNA Rev:  
---|---  
INoiseFigure |  8.0  
INoiseFigure3 |  9.0  
INoiseFigure4 |  9.1  
INoiseFigure5 |  9.2  
INoiseFigure6 |  9.22  
INoiseFigure7 |  9.80  
INoiseFigure8 |  10.15  
  
* * *

