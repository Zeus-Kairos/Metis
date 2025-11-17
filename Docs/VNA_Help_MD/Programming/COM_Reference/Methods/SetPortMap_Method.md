##### Write-only  
  
---  
  
## SetPortMap Method

* * *

#### Description

| Set the DUT-to-VNA port mapping for the [Noise
Figure](../../../Applications/Noise_Figure.htm#OptionsExplained), [Gain
Compression](../../../Applications/Gain_Compression_Application.htm),
[IMD](../../../Applications/Swept_IMD.md),
[IMDx](../../../Applications/Swept_IMDx.md),
[IMS](../../../Applications/IMSpectrum.md), or
[IMSx](../../../Applications/IM_Spectrum_for_Converters.md) measurement. Use
the [DeviceInputPort](../Properties/DeviceInputPort_Property.md) and
[DeviceOutputPort](../Properties/DeviceOutputPort_Property.md) commands to
read the DUT input and output ports.

### For Noise Figure:

Port mapping is allowed without restriction when the standard PNA receiver is
used ([NoiseReceiver](../Properties/NoiseReceiver_Property.md) is set to
naStandardReceiver). When the low-noise receiver is selected
([NoiseReceiver](../Properties/NoiseReceiver_Property.md) is set to
naNoiseReceiver) the following restrictions apply:

  * If the low-noise receiver is selected, the DUT output port must be port 2.
  * On high-frequency PNAs that have an internal tuner on port 1, the input port must be port 1 if the internal tuner is selected as the noise tuner. Conversely, if the input port is something other than 1, the internal tuner cannot be selected.
  * For PNAs that have a maximum frequency of 26.5 GHz or less, any port can be selected as the DUT input port.
  * If a vector calibration is desired, the tuner must be connected to the selected input port.

### When setting IMD and IMS channels:

  * When input is 1, output can be 2 or 4.
  * When input is 3, output must be 4.
  * This setting is necessary only when using the limited port mapping feature. [Learn more.](../../../Applications/SweptIMDLimitedPortMapping.md)

  
---|---  
  
####  VB Syntax

| obj.SetPortMap in,out  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj | A [GainCompression](../Objects/GainCompression_Object.md) (object) or A [SweptIMD](../Objects/SweptIMD_Object.md) (object) or An [IMSpectrum](../Objects/IMSpectrum_Object.md) (object) A [NoiseFigure](../Objects/NoiseFigure_Object.md) (object) - [See example program](../../COM_Example_Programs/Setup_Noise_Figure_Port_Mapping.md)  
in | VNA port which is connected to the DUT input.  
out | VNA port which is connected to the DUT output.  
  
#### Return Type

| Not Applicable To read port map, use: [DeviceInputPort
Property](../Properties/DeviceInputPort_Property.htm) [DeviceOutputPort
Property](../Properties/DeviceOutputPort_Property.htm)  
  
#### Default

| 1,2  
  
#### Examples

| gca.SetPortMap 2,1  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT SetPortMap(long input_port,long output_port);  
  
#### Interface

| IGainCompression ISweptIMD IMSpectrum INoiseFigure6  
  
* * *

