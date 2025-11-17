##### Write-only

|

##### [About Save/Recall](../../../S5_Output/SaveRecall.md)  
  
---|---  
  
## SaveCitiFormattedData Method - Superseded

* * *

#### Description

| This command is replaced with [SaveData Method](SaveData_Method.md) Saves
FORMATTED trace data to .cti file. [Learn more about
citifiles.](../../../S5_Output/SaveRecall.htm#cti)  
---|---  
  
####  VB Syntax

| app.SaveCitiFormattedData(filename.cti)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app | An [Application](../Objects/Application_Object.md) (object)  
filename.cti | (string) \- Full path, file name, and .cti extension of the file. Files are typically stored in "D:\"  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| app.SaveCitiFormattedData ("C:\Program Files(x86)\Keysight\Network
Analyzer\Documents\Newfolder\myFDCitifile.cti") 'Saves "myFDCitifile.cti" to
the specified folder  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT SaveCitiFormattedData (BSTR bstrFile)  
  
#### Interface

| IApplication5

