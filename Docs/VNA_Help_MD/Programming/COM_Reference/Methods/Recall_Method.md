##### Write-only

|

##### [About Save/Recall](../../../S5_Output/SaveRecall.md)  
  
---|---  
  
## Recall Method

* * *

#### Description

|  Recalls a measurement state, calibration state, or both, from the hard
drive into the analyzer. Use app.[Save](Save_Method.md) to save files.  
---|---  
  
####  VB Syntax

|  app.Recall (filename.ext)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
filename.ext |  (string) \- Full path, file name, and extension, of the file. Files are typically stored in "D:\" Use one of the following extensions:

  * .sta - Instrument State
  * .cal - Calibration file
  * .cst - Both Instrument State and Calibration reference
  * .cti - Citifile (data will always be formatted. See [Recalling Citifiles Using the VNA](../../../S5_Output/SaveRecall.md#RecallingCTI))
  * .csa - Instrument state and calibration data (not a reference pointer).

  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.Recall ("D:\MyState.cst") 'Recalls "mystate.cst" from the specified
folder  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Recall(BSTR bstrFile)  
  
#### Interface

|  IApplication

