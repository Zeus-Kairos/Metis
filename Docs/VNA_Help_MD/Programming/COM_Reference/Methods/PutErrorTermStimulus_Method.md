##### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## PutErrorTermStimulus Method

* * *

#### Description

|  Adds stimulus data to the specified buffer. The size of vdata must agree
with the size of the complex data already attached to the buffer or an error
will be generated. See Also: [GetErrorTermStimulus
Method](GetErrorTermStimulus_Method.htm) Learn more about [Reading and Writing
Cal
Data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
See examples of
[Reading](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md) and
[Writing](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.md) Cal
Set Data  
---|---  
  
####  VB Syntax

|  calSet.PutErrorTermStimulus(bufferName, vdata)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calSet |  (Object) A [CalSet](../Objects/CalSet_Object.md) Object  
bufferName |  (String) The string name used to identify a particular error term in the Cal Set. An example string for port 3 directivity in a full 2 port cal might be "Directivity(3,3)". To determine the string names of error terms, see [GetErrorTermList2](Get_ErrorTermList2_Method.md).  
vdata |  (Variant) Safearray of variants (doubles).  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  The sequence is: complexData = calset1.GetErrorTermByString(0, BufferName)
frequencyData = calset1.GetErrorTermStimulus(0,BufferName) // manipulate
complex data here Calset2.PutErrorTermByString(BufferName,
manipulatedComplexData) Calset2.PutErrorTermStimulus(BufferName,
frequencyData);  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT PutErrorTermStimulus (BSTR bufferName, VARIANT vardata)  
  
#### Interface

|  ICalSet7  
  
* * *

* * *

