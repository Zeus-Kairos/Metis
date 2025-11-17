##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetErrorTermByString Method

* * *

#### Description

| Returns error term data from the Cal Set by specifying the string name of
the error term.

  * Learn more about [Reading and Writing Cal Data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.md)
  * See examples of [Reading](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md) and [Writing](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.md) Cal Set Data
  * See [GetCalSetUsageInfo](Get_CalSetUsageInfo_Method.md) to determine the setNumber.

  
---|---  
  
####  VB Syntax

| pdata = calset.GetErrorTermByString(setNumber, errorTerm)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pdata | (Variant) Two-dimensional safe array to store the returned data. Memory for the returned Variant is allocated by the VNA and must be released by client. Note: See also g[etErrorTermComplexByString](Get_ErrorTermComplexByString_Method.md) on the ICalData3 interface to avoid using the variant data type.  
calset | A [Cal Set](../Objects/CalSet_Object.md) (object)  
setNumber | (Long) Set number of the required Cal Set data. See [GetCalSetUsageInfo](Get_CalSetUsageInfo_Method.md) to determine the setNumber.

  * SetNumber 0 contains the original "primary" set of error terms for a Cal Set.
  * SetNumbers > 0 refers to the VNA channel number that contains the error terms. When retrieving channel error terms, Correction must be ON.

The channel error term data contains
[interpolation](../../../S3_Cals/Error_Correction_and_Interpolation.md#Interpolation),
fixturing, and [port extension](../../../S3_Cals/Port_Extensions.md) data if
each is ON.

  1.      * For Balanced Measurements, interpolation, fixturing, and port extensions can be ON independently.
     * For Standard S-parameters, to get port extension data, both fixturing and port extensions must be ON.

  
errorTerm | (String) The string name used to identify a particular error term in the Cal Set. An example string for port 3 directivity in a full 2 port cal might be "Directivity(3,3)". To determine the string names of error terms, see [GetErrorTermList2](Get_ErrorTermList2_Method.md).  
  
#### Return Type

| Variant  
  
#### Default

| Not Applicable  
  
#### Examples

| [See an Example](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT GetErrorTermByString (long SetNumber, BSTR bufferName, VARIANT*
pdata);  
  
#### Interface

| ICalSet2

