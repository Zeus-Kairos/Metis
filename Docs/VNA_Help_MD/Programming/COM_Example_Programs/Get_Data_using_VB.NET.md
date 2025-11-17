# Get Data using VB.NET

In VB.NET,you can use the getData and putData functions shown in the
[IArrayTransfer
interface](../COM_Reference/Objects/Measurement_Object.htm#IArrayTransfer).
However, those functions return Variant data types, and VB.NET does not
support Variant data types.

In this example, getData returns an "object", which is actually an "object[]"
(array of object). Each object in the array is a "float". A new array of
floats is created and then each instance is cast within the array to a float.

Dim DataAsObject As Object Dim DataAsObjectArray(NumPoints - 1) As Object Dim
ResultData (NumPoints - 1) As Double DataAsObject = na.Measurements.Item(1)
DataAsObjectArray =
DataAsObject.getData(AgilentPNA835x.NADataStore.naMeasResult,
AgilentPNA835x.NADataFormat.naDataFormat_LogMag) For i As Integer = 0 To
NumPoints - 1 ResultData(i) = CType(DataAsObjectArray(i), Double) Next i  
---

