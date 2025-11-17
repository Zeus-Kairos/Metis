##### Write/Read

|

##### [About Math Operations](../../../S4_Collect/Math_Operations.md)  
  
---|---  
  
## TraceMath Property

* * *

#### Description

|  Performs math operations on the measurement object and the trace stored in
memory. (There MUST be a trace stored in Memory to perform math. See
[Meas.DataToMemory](../Methods/DataToMemory_Method.md) method.)  
---|---  
  
####  VB Syntax

|  meas.TraceMath = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
value |  (enum NAMathOperation) - Choose from: 0 \- naDataNormal  
1 \- naDataMinusMemory  
2 \- naDataPlusMemory  
3 \- naDataDivMemory  
4 \- naDataTimesMemory  
  
#### Return Type

|  NAMathOperation  
  
#### Default

|  Normal (0)  
  
#### Examples

|  meas.TraceMath = naDataMinusMemory 'Write  
mathOperation = meas.TraceMath 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_TraceMath(tagNAMathOperation* pMathOp)  
HRESULT put_TraceMath(tagNAMathOperation mathOp)  
  
#### Interface

|  IMeasurement

