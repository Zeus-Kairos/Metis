##### Write-only

|

##### [About Dynamic Uncertainty](../../../S3_Cals/Dynamic_Uncertainty.md)  
  
---|---  
  
# Save Method

* * *

#### Description

|  Saves an uncertainty workspace (*.ml4) file from the Uncertainty Manager.  
---|---  
  
#### VB Syntax

|  uncertMan.Save (fileName)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
uncertMan |  An [UncertaintyManager](../Objects/UncertaintyManager_Object.md) Object  
fileName |  (String). Filename and *.ml4 extension of the Uncertainty Manager workspace file to save. If filename is omitted or NULL (0) is passed for this argument, then Uncertainty Managers current workspace is saved to whichever filename that current workspace had been recalled from, even if changes had been made to the workspace since that last Recall.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  uncertMan.Save "MyWorkspace.ml4" 'saves to the specified workspace
filename. uncertMan.Save 'saves to the current workspace filename. [See
example program](../../COM_Example_Programs/Dynamic_Uncertainty.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT Save([in, defaultvalue(0)] BSTR fileName);  
  
#### Interface

|  IUncertaintyManager  
  
* * *

