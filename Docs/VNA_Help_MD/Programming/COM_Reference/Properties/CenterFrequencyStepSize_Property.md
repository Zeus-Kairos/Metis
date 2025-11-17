##### Write / Read

|

##### [About Frequency Settings](../../../S1_Settings/Frequency_Range.md)  
  
---|---  
  
## CenterFrequencyStepSize Property

* * *

#### Description

|  Sets and reads the center frequency step size of the analyzer. This command
sets the manual step size (only valid when CenterFrequencyStepSizeMode is
FALSE.  
---|---  
  
#### VB Syntax

|  chan.CenterFrequencyStepSize = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  (object) - A [Channel](../Objects/Channel_Object.md) object  
value |  (Double) \- Choose a value (in Hz.) below the stop frequency of the analyzer.  
  
#### Return Type

|  Double  
  
#### Default

|  Default is 40 MHz. When CenterFrequencyStepSizeMode is TRUE, this value is
ignored.  
  
#### Examples

|  chan.CenterFrequencyStepSize = 1e5 'Write  
value = chan.CenterFrequencyStepSize 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CenterFrequencyStepSize(Double* pVal); HRESULT
put_CenterFrequencyStepSize(Double pVal);  
  
#### Interface

|  IChannel25  
  
* * *

