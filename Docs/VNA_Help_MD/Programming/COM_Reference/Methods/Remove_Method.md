##### Write-only  
  
---  
  
## Remove Method

* * *

#### Description

|  Removes an item from a collection of objects.  
---|---  
  
####  VB Syntax

|  Object.Remove item  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
Object |  Any of the following (objects)

  * [CalFactorSegments collection](../Objects/CalFactorSegments_Collection.md)
  * [CalFactorSegmentsPMAR Collection](../Objects/CalFactorSegmentsPMAR_Collection.md)
  * [Cal Sets collection](../Objects/CalSets_Collection.md)
  * [Channels Collection](../Objects/Channels_Collection.md)
  * [ExternalDevices Collection](../Objects/ExternalDevices_Collection.md)
  * [GuidedCalibrationPowerSensors Collection](../Objects/GuidedCalibrationPowerSensors_Collection.md)
  * [Measurements collection](../Objects/Measurements_Collection.md)
  * [NAWindows collection](../Objects/NAWindows_Collection.md)
  * [PowerLossSegments collection](../Objects/PowerLossSegments_Collection.md)
  * [PowerLossSegmentsPMAR_Collection](../Objects/PowerLossSegmentsPMAR_Collection.md)
  * [Segments collection](../Objects/Segments_Collection.md)

Note: Segments, CalFactorSegments, and PowerLossSegments have an OPTIONAL
argument [size] referring to the number of segments to remove, starting with
the item parameter. Note: Segments \- When ALL segments are deleted,
[SweepType](../Properties/Sweep_Type_Property.md) is automatically set to
Linear because there are no segments to sweep.  
item |  (variant) \- Collection Item number to be removed. Note: The ExternalDevices Collection requires that you specify item as the string name of the device. For example:  
extDevices.Remove ('mySource")  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Measurements.Remove 3 'Removes the third measurement in the collection
segments.Remove 2,20 'Removes 20 segments (2 - 21)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Remove(VARIANT index); //Measurements HRESULT Remove(VARIANT
index); //Cal Sets HRESULT Remove(long windowNumber); //NAWindows HRESULT
Remove(VARIANT index, long size); //Segments HRESULT Remove(VARIANT index,
long size); //CalFactorSegments(PMAR) HRESULT Remove(VARIANT index, long
size); //PowerLossSegments(PMAR) HRESULT Remove(BSTR name) //ExternalDevices
HRESULT Remove( VARIANT index) // Channels - specify collections index, not
the channel number. HRESULT Remove(VARIANT index);
//GuidedCalibrationPowerSensors  
  
#### Interface

|  All listed above  
  
* * *

