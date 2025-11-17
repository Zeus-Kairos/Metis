# NoiseCal Object

* * *

### Description

Controls the noise figure calibration settings for amplifiers and converters.
These commands supplement the standard calibration commands on the
[GuidedCalibration Object](GuidedCalibration_Object.md).

### Accessing the NoiseCal object

Dim app as AgilentPNA835x.Application Set noisecal =
pna.GetCalmanager.[CreateCustomCalEx(channelNum)](../Methods/CreateCustomCalEx_Method.md)
Set noiseCalExtension =
noisecal.[CustomCalConfiguration](../Properties/CustomCalConfiguration_Property.md)
noiseCalExtension.NoiseSourceCold = 300  
---  
  
### See Also

  * Examples:

  *     * [Create and Cal a Noise Figure Measurement](../../COM_Example_Programs/Create_and_Cal_a_NoiseFigure_Measurement.md)

    * [Create and Cal an NFX Measurement](../../COM_Example_Programs/Create_and_Cal_an_NFX_Measurement.md)

  * [NoiseFigure Object](NoiseFigure_Object.md)

  * [About Noise Figure Measurements](../../../Applications/Noise_Figure.md)

  * [About NFX Measurements](../../../Applications/Noise_Figure_on_Converters.md)

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
  
[AutoOrientTuner](../Properties/AutoOrientTuner_Property.md) | INoiseCal2 | Sets the state of auto orientation for a noise tuner during Noise Figure for NFX.  
[CalMethod](../Properties/CalMethod_Property.md) | INoiseCal | Sets and returns the method for performing calibration on a noise channel.  
[EnableLOPowerCal](../Properties/EnableLOPowerCal_Property.md) | INoiseCal2 | Enables and disables LO power calibration for NFX.  
[ENRFile](../Properties/ENRFile_Property.md) | INoiseCal | Sets and returns the name of the ENR file associated with the noise source.  
[ForceDeEmbedENRAdapter](../Properties/ForceDeEmbedENRAdapter_Property.md) | INoiseCal2 | Sets and reads the state of ENR adapter de-embedding.  
[ForceDeEmbedSensorAdapter](../Properties/ForceDeEmbedSensorAdapter_Property.md) | INoiseCal2 | Sets and reads the state of noise source adapter de-embedding.  
[ForceDeEmbedThruAdapter](../Properties/ForceDeEmbedThruAdapter_Property.md) | INoiseCal4 | Sets and reads the state of Thru adapter de-embedding.  
[NoiseSourceCalKitType](../Properties/NoiseSourceCalKitType_Property.md) | INoiseCal | Sets and reads the Cal Kit type used to perform a cal at the adapter which is used to connect the noise source (if required.)  
[NoiseSourceCold](../Properties/NoiseSourceCold_Property.md) | INoiseCal | Sets and returns the current temperature at the noise source.  
[NoiseSourceConnectorType](../Properties/NoiseSourceConnectorType_Property.md) | INoiseCal | Sets and reads the connector type of the noise source used during the cal.  
[RcvCharMethod](../Properties/RcvCharMethod_Property.md) | INoiseCal3 | Set and read the method used to characterize the noise receivers.  
  
###  NoiseConfiguration History

Interface | Introduced with VNA Rev:  
---|---  
INoiseCal | 8.0  
INoiseCal2 | 9.10  
INoiseCal3 | 9.70  
INoiseCal4 | 12.90  
  
* * *

