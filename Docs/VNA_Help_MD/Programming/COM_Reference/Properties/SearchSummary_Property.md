##### Read-only

|

##### [About GCA](../../../Applications/Gain_Compression_Application.md)  
  
---|---  
  
## SearchSummary Property

* * *

#### Description

|  Returns the status of a compression search. This command can be used to
indicate when a GCA search is complete. Note: The returned value reflects the
current state of the GCA compression search which can vary when in continuous
sweep. This command is intended to be used with
[chan.Single](../Methods/Single_Method.md) (trigger).  
---|---  
  
####  VB Syntax

|  value = gca.SearchSummary  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Enum) Variable to store the returned value.

  * 0 - naSearchNotDone \- Acquisition is still in process.
  * 1 - naSearchSucceeded \- Acquisition is complete and compression value found for all frequency points.
  * 2 - naSearchFailed \- Acquisition is complete and unable to find the compression value at one or more frequency points.

  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
  
#### Return Type

|  Enum  
  
#### Default

|  Not Applicable  
  
#### Examples

|  sum = gca.SearchSummary 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SearchSummary(enum naGCASearchSummary* value)  
  
#### Interface

|  IGainCompression  
  
* * *

