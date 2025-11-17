##### Read-only  
  
---  
  
## Parent Property

* * *

#### Description

|  Returns a handle to the parent object of the collection object being
referred to in the statement. The parent property allows the user to traverse
from an object back up the object hierarchy.  
---|---  
  
####  VB Syntax

|  collection.Parent  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
collection | 

  * [CalFactorSegments collection](../Objects/CalFactorSegments_Collection.md)
  * [CalFactorSegmentsPMAR Collection](../Objects/CalFactorSegmentsPMAR_Collection.md)
  * [Channels collection](../Objects/Channels_Collection.md)
  * [E5091Testset Collection](../Objects/E5091Testset_Collection.md)
  * [ECalModules Collection](../Objects/ECalModules_Collection.md)
  * [ExternalDevices Collection](../Objects/ExternalDevices_Collection.md)
  * [ExternalTestsets Collection](../Objects/ExternalTestsets_Collection.md)
  * [Measurements collection](../Objects/Measurements_Collection.md)
  * [NaWindows collection](../Objects/NAWindows_Collection.md)
  * [PowerLossSegments collection](../Objects/PowerLossSegments_Collection.md)
  * [PowerLossSegmentsPMAR_Collection](../Objects/PowerLossSegmentsPMAR_Collection.md)
  * [PowerSensors collection](../Objects/PowerSensors_Collection.md)
  * [Segments collection](../Objects/Segments_Collection.md)
  * [Traces collection](../Objects/Traces_Collection.md)
  * [PathConfigurationManager](../Objects/PathConfigurationManager_Object.md)
  * [PowerMeterInterfaces Collection](../Objects/PowerMeterInterfaces_Collection.md)

  
  
#### Return Type

|  Object  
  
#### Default

|  Not Applicable  
  
#### Examples

|  parentobj = chans.Parent 'returns a handle to the parent object
(Application) of the chans collection. -Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Parent(IApplication* *pApplication); //IChannels, IChannel,
IMeasurements, INAWindows, and IExternalDevices HRESULT get_Parent(IChannel*
*pChannel); //ITraces HRESULT get_Parent(INAWindow* *pWindow); //ISegments
HRESULT get_Parent(IPowerSensor* *pSensor); //ICalFactorSegments(PMAR) HRESULT
get_Parent(ISourcePowerCalibrator* *pCalibrator); //IPowerSensors,
IPowerLossSegments, and IPowerMeterInterfaces  
  
#### Interface

|  All listed above  
  
* * *

