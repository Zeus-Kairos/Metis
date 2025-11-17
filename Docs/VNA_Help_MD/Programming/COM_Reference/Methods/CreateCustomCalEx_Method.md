#### Write-only

|

#####  
  
---|---  
  
## CreateCustomCalEx Method

* * *

#### Description

|  Returns [IGuidedCalibration](../Objects/GuidedCalibration_Object.md) for
the specified channel. With a handle to the IGuidedCalibration interface, you
can query it for the following objects for properties appropriate to the
calibration setup for the particular meastype (channel). IGuidedCalibration
interface is used to configure a calibration (specify connectors, cal kits,
and so forth). It is also used to access any custom calibration properties
required for unique application channels like Noise Figure or Gain
Compression. To access these special properties, make this call on the
IGuidedCalibration interface: CustomInterface =
IGuidedCalibration.[CustomCalConfiguration](../Properties/CustomCalConfiguration_Property.md)();
The interface returned by this call can be used to set and get the custom
properties on the following application cal objects:

  * [NoiseCal Object](../Objects/NoiseCal_Object.md)
  * [GainCompressionCal Object](../Objects/GainCompressionCal_Object.md)
  * [SweptIMDCal Object](../Objects/SweptIMDCal_Object.md)

Note: Use [CreateCustomCal_Method](CreateCustomCal_Method.md) to create FCA
calibration objects.  
---|---  
  
#### VB Syntax

|  calmgr.CreateCustomCalEx (chan)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calMgr |  [Cal Manager](../Objects/CalManager_Object.md) (Object)  
chan |  (long integer) Channel number in which to create the Cal object.  
  
#### Return Type

|  [IGuidedCalibration](../Objects/GuidedCalibration_Object.md)  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim guidedcal  
Set guidedcal = CalManager.CreateCustomCalEx(1)

### See Also

  * [Noise Figure example](../../COM_Example_Programs/Create_and_Cal_a_NoiseFigure_Measurement.md)
  * [Gain Compression example](../../COM_Example_Programs/Create_and_Cal_a_Gain_Compression_Measurement.md)

  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT CreateCustomCalEx(long channel, IDispatch** ppObject);  
  
#### Interface

|  ICalManager5  
  
* * *

  

