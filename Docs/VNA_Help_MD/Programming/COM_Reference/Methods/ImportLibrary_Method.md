##### Write-only

|

##### [About Equation Editor](../../../S4_Collect/Equation_Editor.md)  
  
---|---  
  
## ImportLibrary Method

* * *

#### Description

| Imports an Equation Editor DLL.  
---|---  
  
####  VB Syntax

| equation.ImportLibrary location  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
equation | A [MeasurementEquation](../Objects/MeasurementEquation_Object.md) object  
location | (string)  Full path and filename of the *.dll to be imported.  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| equation.ImportLibrary C:\Program Files(x86)\Keysight\Network
Analyzer\UserFunctions\Expansion.dll  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT ImportLibrary( BSTR filename);  
  
#### Interface

| IMeasurementEquation  
  
* * *

