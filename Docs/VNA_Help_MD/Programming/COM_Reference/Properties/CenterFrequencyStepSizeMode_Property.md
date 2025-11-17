##### Write / Read

|

##### [About Frequency Settings](../../../S1_Settings/Frequency_Range.md)  
  
---|---  
  
## CenterFrequencyStepSizeMode Property

* * *

#### Description

|  Sets and reads how the center frequency step size is determined. When TRUE,
center steps by 5% of span. When FALSE, center steps by STEP:SIZE value.  
---|---  
  
#### VB Syntax

|  chan.CenterFrequencyStepSizeMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  (object) - A [Channel](../Objects/Channel_Object.md) object  
value |  (Enum as NAModes) Choose from: 0 - naAUTO -Step size is set automatically. 1 - naMaunal - Step size is set manually using [CenterFrequencyStepSize Property](CenterFrequencyStepSize_Property.md).  
  
#### Return Type

|  Enum  
  
#### Default

|  1 - naMaunal  
  
#### Examples

|  chan.CenterFrequencyStepSizeMode = naAUTO 'Write value =
chan.CenterFrequencyStepSizeMode 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CenterFrequencyStepSizeMode(tagNAModes* pVal); HRESULT
put_CenterFrequencyStepSizeMode(tagNAModes pVal);  
  
#### Interface

|  IChannel25  
  
* * *

