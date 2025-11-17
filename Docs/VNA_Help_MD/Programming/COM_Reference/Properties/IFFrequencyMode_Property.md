##### Write/Read

|

##### [About IF Access](../../../IFAccess/IF_Path_Configuration.md)  
  
---|---  
  
## IFFrequencyMode Property

* * *

#### Description

|  Sets and returns method for specifying the way the IF Frequency is
determined.  
---|---  
  
####  VB Syntax

|  IfConfig.IFFrequencyMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
IfConfig |  An [IFConfiguration](../Objects/IIFConfiguration_Object.md) (object)  
value |  (enum as NAModes) IF Frequency mode. Choose from: 0 - naAUTO The VNA determines the setting for the IF frequency. The IF frequency is based on many VNA settings, including measurement frequency. Therefore, it is NOT possible to read the IF frequency that is being used. 1 - naMANUAL (use [IFFrequency Property](IFFrequency_Property.md) to manually set frequency.  
  
#### Return Type

|  Enum  
  
#### Default

|  0 naAuto  
  
#### Examples

|  IfConfig.IFFrequencyMode = naMANUAL  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_IFFrequencyMode (tagNAModes* pdspMode); HRESULT
put_IFFrequencyMode (tagNAModes* pdspMode);  
  
#### Interface

|  IFConfiguration3  
  
* * *

  

