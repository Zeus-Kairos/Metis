##### Write/Read

|

##### [About LFE](../../../IFAccess/Low_Frequency_Extension/Overview.md)  
  
---|---  
  
# LowFrequencyExtension Property

* * *

#### Description

|  Enables/disables the low frequency extension (LFE). [Learn
more](../../../IFAccess/Low_Frequency_Extension/Overview.htm).  
---|---  
  
####  VB Syntax

|  chan.LowFrequencyExtension = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (boolean) - Choose either: False \- LFE is disabled. True \- LFE is enabled.  
chan |  [Channel](../Objects/Channel_Object.md) (object)  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  chan.LowFrequencyExtension = True 'Write  
lfestate = chan.LowFrequencyExtension 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LowFrequencyExtension(VARIANT_BOOL* lfestate); HRESULT
put_LowFrequencyExtension(VARIANT_BOOL lfestate);  
  
#### Interface

|  IChannel26  
  
* * *

