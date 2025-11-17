##### Read-only

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
## GetXAxisValues Method

* * *

#### Description

|  Returns the channel's X-axis values. GetXAxisValues is a convenient method
for determining the frequency of each point when the points are not linearly
spaced - as in segment sweep. See the [Measurement2
Interface](../Objects/Measurement_Object.htm#IMeasurement2Interface) to learn
how this method differs from
[meas.GetXAxisValues](Get_XAxisValues_Method.md). Note: This method returns a
variant which is less efficient than [GetXAxisValues2](Get_X-
Axis_Values_2.htm). Note: In Segment Sweep, chan.NumberofPoints will return
the total number of data points for the combined segments.  
---|---  
  
####  VB Syntax

|  data = chan.GetXAxisValues  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  Variant array to store the data.  
chan |  A Channel (object)  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim varData As Variant  
Dim i As Integer  
varData = chan.GetXAxisValues  
'Print Data  
For i = 0 To chan.NumberOfPoints - 1  
Print varData(i)  
Next i  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetXAxisValues (VARIANT* xData)  
  
#### Interface

|  IChannel

