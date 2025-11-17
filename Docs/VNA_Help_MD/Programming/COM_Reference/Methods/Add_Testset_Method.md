##### Write-only

|

##### [About External Testset
Control](../../../System/External_Testset_Control.htm)  
  
---|---  
  
## Add (Testset) Method

* * *

#### Description

|  Adds a testset to the ExternalTestsets Collection and loads the
configuration file.  
---|---  
  
#### VB Syntax

|  testsets.Add (model,address)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
testsets |  An [ExternalTestsets](../Objects/ExternalTestsets_Collection.md) (collection)  
model |  (String) Model of the testset to be added, NOT case-sensitive. There is no COM command to read a list of currently-supported test sets. However, the following SCPI command can be used with the following format: string = [SCPISTringParser](../Objects/SCPIStringParser_Object.md).Execute ("[SENSe:MULTiplexer:CATalog?](../../GP-IB_Command_Finder/Sense/Multiplexer.md#Catalog)")  
address |  (Integer) Address of the testset to be added.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  testsets.Add("Z5623AK66",12) ' add Z5623AK66 test at address 12 to testsets
collection [See an example
program](../../COM_Example_Programs/External_Testset_Control.htm)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Add(BSTR typename, long address)  
  
#### Interface

|  [IExternalTestsets](../Objects/ExternalTestsets_Collection.md)

