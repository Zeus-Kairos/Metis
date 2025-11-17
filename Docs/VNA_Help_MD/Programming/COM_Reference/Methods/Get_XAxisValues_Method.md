##### Read-only

|  
---|---  
  
## GetXAxisValues Method

* * *

#### Description

|  Returns the stimulus values for the measurement. To understand how this
property is useful, see [IMeasurement2
Interface](../Objects/Measurement_Object.htm#IMeasurement2Interface).  
---|---  
  
####  VB Syntax

|  data = meas.GetXAxisValues  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  (Variant) Array to store the data.  
meas |  A Measurement (object)  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim varData As Variant  
Dim i As Integer  
varData = meas.GetXAxisValues  
'Print Data  
For i = 0 To meas.NumberOfPoints - 1  
Print varData(i)  
Next i [See C++
example](../../COM_Example_Programs/Upload_Segment_Table_in_CPlus.htm)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetXAxisValues(VARIANT* xData);  
  
#### Interface

|  IMeasurement2  
  
* * *

  

