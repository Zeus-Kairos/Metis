##### Write/Read

|

##### [About Analyzer
Events](../../Learning_about_COM/Working_with_PNA_Events.htm)  
  
---|---  
  
## SetFailOnOverRange Method

* * *

#### Description

|  When set TRUE, configures the analyzer to report outOfRange conditions with
an error code. Any overrange error will return E_NA_LIMIT_OUTOFRANGE_ERROR.
Note: This method is for the benefit of VB clients. The analyzer automatically
adjusts overrange conditions to the closest acceptable setting. The VB user
will not See that an overrange occurred because the HRESULT is not returned if
it has a success code. For more information, See
[Events/OverRange.](../../Learning_about_COM/Working_with_PNA_Events.md#range)  
---|---  
  
####  VB Syntax

|  app.SetFailOnOverRange state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
state |  (boolean) -  
True (1) \- Overrange conditions report an error code  
False (0) \- Overrange conditions report a success code  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  False (0)  
  
#### VB Example

|  app.SetFailOnOverRange TRUE  
On Error Goto ERRHANDLER  
  
'the following overrange will cause ERRHANDLER to be invoked  
  
channel.StartFrequency = 9.9 GHZ  
exit ERRHANDLER:  
print "something failed"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_SetFailOnOverRange(VARIANT_BOOL mode)  
  
#### Interface

|  IApplication

