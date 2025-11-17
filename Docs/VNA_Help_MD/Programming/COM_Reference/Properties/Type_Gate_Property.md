##### Write/Read

|

##### [About Time Domain](../../../Time/TimeDomain.md)  
  
---|---  
  
## Type (gate) Property

* * *

#### Description

|  Specifies the type of gate filter used.  
---|---  
  
####  VB Syntax

|  gat.Type = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gat |  A Gating (object)  
value |  (enum NAGateType) \- Choose from:  
0 - naGateTypeBandpass - Includes (passes) the range between the start and
stop times.  
1 - naGateTypeNotch \- Excludes (attenuates) the range between the start and
stop times.  
  
#### Return Type

|  NAGateType  
  
#### Default

|  Bandpass  
  
#### Examples

|  gate.Type = naGateTypeNotch 'Write  
filterType = gate.Type 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Type(tagNAGateType *pVal)  
HRESULT put_Type(tagNAGateType newVal)  
  
#### Interface

|  IGating

