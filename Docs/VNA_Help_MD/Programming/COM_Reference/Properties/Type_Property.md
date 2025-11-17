##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# Type (DFT) Property

* * *

#### Description

|  Sets and returns the DFT record size type. The DFT
[RecordSize](RecordSize_Property.md) is based on the
[ForceADCRecordSize](ForceADCRecordSize_Property.md) and the DFT record size
type. The DFT record size is always equal or larger than the ADC record size.  
---|---  
  
####  VB Syntax

|  sa.dft.Type = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
value |  (enum NASADFTSizeMode) \- Choose from: 0 naSADFT2ToN: (Power of 2) Sets the DFT record size to the next power of 2 greater than or equal to the current ADC record size. 1 naSADFTOptimizeRadix: (Optimized Radix) Sets the DFT record to the next integer number that can be decomposed with 2,3,5,7,11,13 radixes. 2 naSADFTArbitrary: (Arbitrary) Sets DFT record size equal to the ADC record size. If the current ADC record size is a large prime number, then the DFT can be very slow. 3 naSADFTOptimizeSpeed: (Fastest) Sets the DFT record size as close as possible to the ADC record size (larger or equal) while optimizing processing speed.  
  
#### Return Type

|  Enum as NASADFTSizeMode  
  
#### Default

|  naSADFTOptimizeSpeed Note: In previous releases the default was naSADFT2ToN
(Power of 2).  
  
#### Examples

|  sa.dft.Type = naSADFTOptimizeRadix 'Write  
DFTType = sa.dft.Type 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Type(tagNASADFTSizeMode* pVal)  
HRESULT put_Type(tagNASADFTSizeMode newVal)  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

