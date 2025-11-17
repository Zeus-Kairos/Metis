##### Read-only

|

##### [About GCA](../../../Applications/Gain_Compression_Application.md)  
  
---|---  
  
## SearchFailures Property

* * *

#### Description

|  Returns a comma-separated list of the frequency indexes that were out of
tolerance for SMART Sweep mode, or at the power limit for 2D Sweep mode. Zero
(0) is the first frequency data point. Must be Single triggered. Invalid
results occur if the GCA channel is continuously sweeping.  
---|---  
  
####  VB Syntax

|  value = gca.SearchFailures  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Double) Variable to store the returned data.  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
  
#### Return Type

|  Returns a comma-separated list of frequency indexes.  
  
#### Default

|  Not applicable  
  
#### Examples

|  SFA = gca.SearchFailures 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SearchFailures(VARIANT* value)  
  
#### Interface

|  IGainCompression  
  
* * *

