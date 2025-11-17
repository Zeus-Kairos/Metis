##### Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## GetErrorTermStimulus Method

* * *

#### Description

| Returns the stimulus values over which the specific error term was acquired.
For example, with mixer channels, you may get a different set of values for
Directivity at the input port versus Directivity at the output port.

  * Learn more about [Reading and Writing Cal Data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.md)
  * See examples of [Reading](../../COM_Example_Programs/COM_Reading_CalSet_Examples.md) and [Writing](../../COM_Example_Programs/Writing_Cal_Set_Data_using_COM.md) Cal Set Data
  * See [GetCalSetUsageInfo](Get_CalSetUsageInfo_Method.md) to determine the setNumber.
  * See [PutErrorTermStimulus Method](PutErrorTermStimulus_Method.md).

  
---|---  
  
####  VB Syntax

| pdata = calset.GetErrorTermStimulus(setNumber, bufferName)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pdata | (Variant) The VNA will allocate the memory for the returned variant. The data is returned as a SafeArray of Variant elements. Each element is of VarType double.  
calset | A [Cal Set](../Objects/CalSet_Object.md) (object)  
setNumber | (Long) Set number of the required Cal Set data. See [GetCalSetUsageInfo](Get_CalSetUsageInfo_Method.md) to determine the setNumber.

  * SetNumber 0 contains the original "primary" set of error terms for a Cal Set.
  * SetNumbers > 0 refers to the VNA channel number that contains the error terms. When retrieving channel error terms, Correction must be ON. The channel error term data may be [interpolated](../../../S3_Cals/Error_Correction_and_Interpolation.md) and may also be compensating for a fixture if that feature is on.

  1.      * For Balanced Measurements, interpolation, fixturing, and port extensions can be ON independently.
     * For Standard S-parameters, to get port extension data, both fixturing and port extensions must be ON.

  
bufferName | (String) The string name used to identify a particular error term in the Cal Set. An example string for port 3 directivity in a full 2 port cal might be "Directivity(3,3)". To determine the string names of error terms, see [GetErrorTermList2](Get_ErrorTermList2_Method.md).  
  
#### Return Type

| Variant  
  
#### Default

| Not Applicable  
  
#### Examples

| The sequence is: complexData = calset1.GetErrorTermByString(0, BufferName)
frequencyData = calset1.GetErrorTermStimulus(0,BufferName) // manipulate
complex data here Calset2.PutErrorTermByString(BufferName,
manipulatedComplexData) Calset2.PutErrorTermStimulus(BufferName,
frequencyData); [See an
Example](../../COM_Example_Programs/COM_Reading_CalSet_Examples.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT GetErrorTermStimulus (long SetNumber, BSTR bufferName, VARIANT*
pdata);  
  
#### Interface

| ICalSet7  
  
* * *

* * *

