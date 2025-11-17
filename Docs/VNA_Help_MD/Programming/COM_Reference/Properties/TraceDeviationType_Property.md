##### Write/Read

|

##### [About Math Operations](../../../S4_Collect/Math_Operations.md)  
  
---|---  
  
# TraceDeviationType Property

* * *

#### Description

| Calculates the deviation from a least-squares best fit line.  
---|---  
  
####  VB Syntax

| meas.TraceDeviationType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas | A [Measurement](../Objects/Measurement_Object.md) (object)  
value | (enum NATraceDeviationType) - Choose from: 0 \- naTraceDeviationOff  
1 \- naTraceDeviationLinear  
2 \- naTraceDeviationParabolic  
3 \- naTraceDeviationCubic  
  
#### Return Type

| Enum  
  
#### Default

| 0 - naTraceDeviationOff  
  
#### Examples

| meas.TraceDeviationType = naTraceDeviationLinear 'Write  
DeviationType = meas.TraceDeviationType 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_TraceDeviationType(tag NATraceDeviationType* devType)  
HRESULT put_TraceDeviationType(tag NATraceDeviationType devType)  
  
#### Interface

| IMeasurement20

