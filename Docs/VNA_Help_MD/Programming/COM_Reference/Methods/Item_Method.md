##### Write-only  
  
---  
  
## Item Method

* * *

#### Description

|  Returns an object from the collection of objects. Notes

  * The order of objects within a collection cannot be assumed.
  * Most, but not all, VNA Collections are '1-based'

  
---|---  
  
####  VB Syntax

|  Object[.Item](n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
Object |  Any of the following (collections):

  * [Cables Collection](../Objects/Cables_Collection.md)
  * [CalFactorSegments collection](../Objects/CalFactorSegments_Collection.md)
  * [CalFactorSegmentsPMAR Collection](../Objects/CalFactorSegmentsPMAR_Collection.md)
  * [Cal Sets collection](../Objects/CalSets_Collection.md)
  * [Channels collection](../Objects/Channels_Collection.md)
  * [E5091Testset collection](../Objects/E5091Testset_Collection.md)
  * [ECalModules Collection](../Objects/ECalModules_Collection.md)
  * [ExternalDevices Collection](../Objects/ExternalDevices_Collection.md)
  * [ExternalTestsets collection](../Objects/ExternalTestsets_Collection.md)
  * [FOM collection](../Objects/FOM_Collection.md)
  * [GuidedCalibrationPowerSensors Collection](../Objects/GuidedCalibrationPowerSensors_Collection.md)
  * [LimitTest collection](../Objects/Limit_Test_Collection.md)
  * [Measurements collection](../Objects/Measurements_Collection.md)
  * [NaWindows collection](../Objects/NAWindows_Collection.md)
  * [Ports Collection](../Objects/Ports_Collection.md)
  * [PowerLossSegments collection](../Objects/PowerLossSegments_Collection.md)
  * [PowerLossSegmentsPMAR_Collection](../Objects/PowerLossSegmentsPMAR_Collection.md)
  * [PowerSensors collection](../Objects/PowerSensors_Collection.md)
  * [Segments collection](../Objects/Segments_Collection.md)
  * [Traces collection](../Objects/Traces_Collection.md)
  * [PowerMeterInterfaces Collection](../Objects/PowerMeterInterfaces_Collection.md)

[Learn more about collections in the
VNA](../../Learning_about_COM/Collections_in_the_Analyzer.htm)  
.Item |  Optional - Item is the default property of a collections object and therefore can be called implicitly. For example, the following two commands are equivalent: Channels.Item(3).Averaging = 1  
Channels(3).Averaging = 1  
n |  (variant) \- Number of the item in the collection. In addition, the following collections allow you to specify the name of the item as a string:

  * The [Measurements](../Objects/Measurements_Collection.md), [Traces](../Objects/Traces_Collection.md), and [FOM](../Objects/FOM_Collection.md) collections. For example:  
measCollection("CH_S11_1").InterpolateMarkers

  * The [Cal Sets collection](../Objects/CalSets_Collection.md). For example:   
Calsets("MyCalSet").Description = "New Description"

  * The [ExternalDevices Collection](../Objects/ExternalDevices_Collection.md). For example:  
Set extDev = externalDevices.Item("NewPMAR")

  * The [GuidedCalibrationPowerSensors Collection](../Objects/GuidedCalibrationPowerSensors_Collection.md). For example:  
Set PowerSensor = GuidedCalibrationPowerSensors.Item.Name = "26GHzPowerSensor"

  
  
#### Return Type

|  (Object)  
  
#### Default

|  Not Applicable  
  
#### Examples

|  For i = 1 to Traces.Count 1  
Traces.Item(i).YScale = .5dB  
Next i  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Item(VARIANT index, <interface>** pItem)  
  
#### Interfaces

|  All listed above.  
  
* * *

  

