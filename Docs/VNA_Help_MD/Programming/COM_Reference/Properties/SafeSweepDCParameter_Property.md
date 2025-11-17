##### Write/Read

|

##### [About Safe
Sweep](../../../Applications/Gain_Compression_Application.htm#Safe)  
  
---|---  
  
# SafeSweepDCParameter Property

* * *

#### Description

| Sets and returns the name of the external DC device.  
---|---  
  
####  VB Syntax

| gca.SafeSweepDCParameter = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca | A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value | (string) \- Name of the external DC device.  
  
#### Return Type

| String  
  
#### Default

| Not Applicable  
  
#### Examples

| gca.SafeSweepDCParameter = "MyDCDevice" 'write value =
gca.SafeSweepDCParameter 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_SafeSweepDCParameter(BSTR* dcname) HRESULT
put_SafeSweepDCParameter(BSTR dcname)  
  
#### Interface

| IGainCompression6  
  
* * *

