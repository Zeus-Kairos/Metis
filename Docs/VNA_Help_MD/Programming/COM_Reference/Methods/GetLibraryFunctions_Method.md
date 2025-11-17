##### Read-only

|

##### [About Equation Editor](../../../S4_Collect/Equation_Editor.md)  
  
---|---  
  
## GetLibraryFunctions Method

* * *

#### Description

| Returns the functions in an imported (loaded) DLL.  
---|---  
  
####  VB Syntax

| functions = equation.GetLibraryFunctions location  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
functions | (variant) \- Array to store the returned functions.  
equation | A [MeasurementEquation](../Objects/MeasurementEquation_Object.md) object  
location | (string)  Full path and filename of the *.dll to be read.  
  
#### Return Type

| Variant array  
  
#### Default

| Not Applicable  
  
#### Examples

| functions=equation.GetLibraryFunctions C:\Program
Files(x86)\Keysight\Network Analyzer\UserFunctions\Expansion.dll  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT GetLibraryFunctions( BSTR filename, BSTR* functionList);  
  
#### Interface

| IMeasurementEquation  
  
* * *

