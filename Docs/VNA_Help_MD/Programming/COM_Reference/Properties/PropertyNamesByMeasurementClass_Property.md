##### Read-only

|

##### [About Cal All](../../../S3_Cals/Calibrate_All_Channels.md)  
  
---|---  
  
# PropertyNamesByMeasurementClass Property

* * *

#### Description

| Returns the list of valid property names by measurement class. [See a list
of valid properties and values for each measurement
class](../../../S3_Cals/Calibrate_All_Channels.htm#propertiesDiag).  
---|---  
  
####  VB Syntax

| propNames = calAll.PropertyNamesByMeasurementClass (MeasurementClass)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
propNames | (Variant Array) Variable to store the returned property names.  
calAll | A [CalibrateAllChannels](../Objects/CalibrateAllChannels_Object.md) (object)  
MeasurementClass | (String) Measurement class name for which valid names are to be returned.  
  
#### Return Type

| Variant Array  
  
#### Default

| Not Applicable  
  
#### Examples

| props = calAll.PropertyNamesByMeasurementClass ("SMC")  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_PropertyNamesByMeasurementClass(BSTR MeasurementClass, VARIANT*
propNames);  
  
#### Interface

| CalibrateAllChannels  
  
* * *

