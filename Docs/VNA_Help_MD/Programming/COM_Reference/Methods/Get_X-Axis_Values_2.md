##### Read-only

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
## GetXAxisValues2 Method

* * *

#### Description

|  Returns the channel's X-axis values into a dimensioned Typed array.
GetXAxisValues2 is a convenient method for determining the frequency of each
point when the points are not linearly spaced - as in segment sweep. Note:
This method will fail if called using a scripting client such as VBScript or
Keysight Vee, (see remarks) Note: In Segment Sweep,
chan.[NumberofPoints](../Properties/Number_of__Points_Property.md) will
return the total number of data points for the combined segments.  
---|---  
  
####  VB Syntax

|  chan.GetXAxisValues2 numPts,data  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  (object) \- A Channel object  
numPts |  (long integer) \- Number of data points in the channel  
data |  (double) Single dimensioned array of data matching the number of points in the channel.  
  
#### Return Type

|  double  
  
#### Default

|  Not applicable  
  
#### Examples

|  Dim App As Application  
Set App = New Application  
Dim numPoints As Long  
Dim values() As Double  
numPoints = App.ActiveChannel.NumberOfPoints  
ReDim values(numPoints)  
App.ActiveChannel.GetXAxisValues2 numPoints, values(0)  
Print values(0), values(1)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetXAxisValues2(long* pNumValues, double* stimulus)  
  
#### Interface

|  IChannel  
  
Remarks:

This method will fail if called using a scripting client such as VBScript or
Keysight Vee. Use the [GetXAxisValues](Get_X-axis_Values_Method.md) method as
a replacement for these COM environments.

This method also cannot be called using late-bound typing in Visual Basic. For
instance, if, in the example above, the first line were replaced with "Dim App
as Object", then this method would fail.

