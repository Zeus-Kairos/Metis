##### Write/Read

|

##### [About IM Spectrum](../../../Applications/IMSpectrum.md)  
  
---|---  
  
## SweepOrder Property

* * *

#### Description

|  Sets and returns the order number of IM products to view when
[SweepType](SweepType_ims_Property.md) = NTH is specified. This actually sets
the frequency span to [DeltaF](DeltaFrequency_Property.md) * N (this command
value).  
---|---  
  
####  VB Syntax

|  ims.SweepOrder = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ims |  An [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value |  (Integer) Order number of IM product.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  9  
  
#### Examples

|  ims.SweepOrder = 5 'Write  
value = ims.SweepOrder 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SweepOrder(long *pVal)  
HRESULT put_SweepOrder(long newVal)  
  
#### Interface

|  IIMSpectrum  
  
* * *

