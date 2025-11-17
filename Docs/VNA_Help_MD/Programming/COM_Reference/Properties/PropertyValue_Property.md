##### Write/Read

|

##### [About Cal All](../../../S3_Cals/Calibrate_All_Channels.md)  
  
---|---  
  
## PropertyValue Property

* * *

#### Description

| Sets and returns the current property value for a specific property name.
[See a list of valid properties and values for each measurement
class](../../../S3_Cals/Calibrate_All_Channels.htm#propertiesDiag). Use
[PropertyValues](PropertyValues_Property.md) to query a list of valid values.  
---|---  
  
####  VB Syntax

| calAll.PropertyValue (propName) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calAll | A [CalibrateAllChannels](../Objects/CalibrateAllChannels_Object.md) (object)  
propName | (String) Property name for which value is to be set or returned.  
value | (String) Property value.  
  
#### Return Type

| String  
  
#### Default

| Not Applicable  
  
#### Examples

| Example 1:  
calAll.PropertyValue ("Noise Cal Method") = "Scalar" Example 2:  
calAll.PropertyValue ("Enable Extra Power Cals") = "Port 1 Src2,Port3" Example
3:  
calAll.PropertyValue ("Port 1 Src2 Cal Power") = "-20"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_PropertyValue (BSTR propName, BSTR* propValue); HRESULT
put_PropertyValue (BSTR propName, BSTR propValue);  
  
#### Interface

| CalibrateAllChannels  
  
* * *

* * *

