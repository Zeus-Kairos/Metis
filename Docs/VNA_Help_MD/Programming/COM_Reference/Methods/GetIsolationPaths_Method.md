##### Read-only

|  
---|---  
  
## GetIsolationPaths Method

* * *

#### Description

|  Gets the list of paths (port pairings) for which isolation standards will
be measured during calibration.  
---|---  
  
####  VB Syntax

|  value = obj.GetIsolationPaths  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) - Variable to store the returned port paths in pairs. One-dimensional array of Long Integers.  
obj |  Any of the following: [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
  
#### Return Type

|  Variant  Containing one-dimensional array of Long Integers.  
  
#### Default

|  No port pairs (empty Variant variable)  
  
#### Examples

|  pathList = guidedCal.GetIsolationPaths  
'displaying the paths separated by commas,  
'with a dash (-) between the pair of port numbers comprising each path  
  
For i = LBound(portList) To UBound(portList) Step 2  
msg = msg + CStr(portList(i)) + "-" \+ CStr(portList(i+1))  
If i+1 < UBound(portList) Then msg = msg + ","  
Next  
MsgBox msg, 0, "List of isolation paths"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetIsolationPaths(VARIANT* pathList);  
  
#### Interface

|  IGuidedCalibration  
  
* * *

