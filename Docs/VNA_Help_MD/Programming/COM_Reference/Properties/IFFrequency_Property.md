##### Write/Read

|

##### [IF
Frequencies](../../../IFAccess/IF_Path_Configuration.htm#IFFrquencies)  
  
---|---  
  
## IFFrequency Property

* * *

#### Description

|  Sets and returns the IF frequency for ALL receiver paths being used for the
specified channel. To set this frequency, [IFFrequencyMode
Property](IFFrequencyMode_Property.htm) must be set to OFF (Manual).  
---|---  
  
####  VB Syntax

|  IfConfig.IFFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
IfConfig |  An [IFConfiguration](../Objects/IIFConfiguration_Object.md) (object)  
value |  (double) IF Frequency. Use [MaximumIFFrequency](MaximumIFFrequency_Property.md) and [MinimumIFFrequency](MinimumIFFrequency_Property.md) to determine the range of value for this command.  
  
#### Return Type

|  Double  
  
#### Default

|  9 MHz  
  
#### Examples

|  IfConfig.IFFrequency = 9.3e6  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_IFFrequency (double *pVal); HRESULT put_IFFrequency (double
pVal);  
  
#### Interface

|  IFConfiguration3  
  
* * *

  

