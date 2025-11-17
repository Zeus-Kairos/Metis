##### Write-only

|

##### [About Equation Editor](../../../S4_Collect/Equation_Editor.md)  
  
---|---  
  
## RemoveLibrary Method

* * *

#### Description

| Removes an imported an Equation Editor DLL from the VNA.  
---|---  
  
####  VB Syntax

| equation.RemoveLibrary location  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
equation | A [MeasurementEquation](../Objects/MeasurementEquation_Object.md) object  
location | (string)  Full path and filename of the *.dll to be removed.  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| equation.RemoveLibrary C:\Program Files(x86)\Keysight\Network
Analyzer\UserFunctions\Expansion.dll  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT RemoveLibrary( BSTR filename);  
  
#### Interface

| IMeasurementEquation  
  
* * *

