##### Read-only

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
## GetRxLevelingConfiguration Method

* * *

#### Description

|  This method returns a handle to a
[RxLevelingConfiguration](../Objects/RXLevelingConfiguration_Object.md)
object.  
---|---  
  
####  VB Syntax

|  chan.GetRxLevelingConfiguration( )  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
  
#### Return Type

|  IRxLevelingConfiguration  
  
#### Default

|  Not Applicable  
  
#### Example

|  dim app as AgilentPNA835x.Application  
dim mgr as RxLevelingConfiguration  
set mgr = app.GetRxLevelingConfiguration()  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetRxLevelingConfiguration( IRxLevelingConfiguration **mgr);  
  
#### Interface

|  IChannel17  
  
* * *

