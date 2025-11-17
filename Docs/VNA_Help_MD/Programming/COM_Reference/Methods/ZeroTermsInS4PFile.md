#### Write-only

|

##### [About Cal Plane Manager](../../../S3_Cals/Cal_Plane_Manager.md)  
  
---|---  
  
# ZeroTermsInS4PFile Method

* * *

#### Description

| Creates a new S4P file.  
---|---  
  
#### VB Syntax

| calmgr.ZeroTermsInS4PFile (original, modified, sParams, format)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calMgr | [Cal Manager](../Objects/CalManager_Object.md) (Object)  
original | (String)  Path and filename of the original S4P file.  
modified | (String) Path and filename of the new S4P file.  
sParams | (String) Comma-separated terms to zero-out.  
format | (Enum as NAPairedDataFormat) Format in which the data is to be saved to the S4P file. Choose from: 0 - naLogMagPhase 1 - naLinMagPhase 2 \- naRealImaginary  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| CalManager.ZeroTermsInS4PFile
"D:\testDiffMatch.s4p","D:\testDiffMatch_com.s4p","S11,S21,S33",0  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT ZeroTermsInS4PFile(BSTR original, BSTR modified, BSTR sParams,
tagNAPairedDataFormat format);  
  
#### Interface

| ICalManager13  
  
* * *

