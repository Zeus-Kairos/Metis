##### Write/Read

|

##### [About
ExternalDevices](../../../System/Configure_an_External_Device.htm)  
  
---|---  
  
## DwellPerPoint Property

* * *

#### Description

|  Sets and returns the amount of time the VNA should wait after for an
external source to settle before making a measurement at each data point.  
---|---  
  
####  VB Syntax

|  extSource.DwellPerPoint = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  An [ExternalSource](../Objects/ExternalSource_Object.md) (object)  
value |  (Double) Dwell time in milliseconds.  
  
#### Return Type

|  Double  
  
#### Default

|  3  
  
#### Examples

|  extSource.DwellPerPoint = 10 'Write  
dpp = extSource.DwellPerPoint 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DwellPerPoint (tagNAExtDevDwellPerPoint *pValue)  
HRESULT put_DwellPerPoint (tagNAExtDevDwellPerPoint newVal)  
  
#### Interface

|  IExternalSource  
  
* * *

