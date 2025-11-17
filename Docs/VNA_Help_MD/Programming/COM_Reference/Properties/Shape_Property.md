##### Write/Read

|

##### [About Gating](../../../Time/TimeDomain.md#Gating)  
  
---|---  
  
## Shape Property

* * *

#### Description

|  Specifies the shape of the gate filter.  
---|---  
  
####  VB Syntax

|  gat.Shape = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gat |  A Gating (object)  
value |  (enum NAGateShape) \- Choose from: 0 \- naGateShapeMaximum  
1 \- naGateShapeWide  
2 \- naGateShapeNormal  
3 \- naGateShapeMinimum  
  
#### Return Type

|  NAGateShape  
  
#### Default

|  2 - Normal  
  
#### Examples

|  gat.Shape = naGateShapeMaximum 'Write  
filterShape = gat.Shape 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Shape(tagNAGateShape *pVal)  
HRESULT put_Shape(tagNAGateShape newVal)  
  
#### Interface

|  IGating

