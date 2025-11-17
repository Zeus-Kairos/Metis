##### Write/Read

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## EndOfSweepOperation Property

* * *

#### Description

|  Set and read the action which should be taken at the end of the last
frequency or power sweep in the measurement. This setting is used to protect a
sensitive device from too much power during the sweep retrace.  
---|---  
  
####  VB Syntax

|  gca.EndOfSweepOperation = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (NAGCAEndOfSweepOperation) 

  * naStandard (0)  Use the default VNA method. [Learn more.](../../../S1_Settings/Power_Level.md#PowerONOFF)
  * naSetToStartPower (1)  Sweep Start power
  * naSetToStopPower (2) Sweep Stop power.
  * naSetRFOff (3) Always turn power OFF while waiting.

  
  
#### Return Type

|  Enum  
  
#### Default

|  naStandard  
  
#### Examples

|  gca.EndOfSweepOperation = naSetToStartPower 'Write  
eos = gca.EndOfSweepOperation 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_EndOfSweepOperation(tagNAGCAEndOfSweepOperation* pVal) HRESULT
put_EndOfSweepOperation(tagNAGCAEndOfSweepOperation newVal)  
  
#### Interface

|  IGainCompression  
  
* * *

