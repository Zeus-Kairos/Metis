##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# DataFormat Property

* * *

#### Description

|  Sets and returns the data format.  
---|---  
  
####  VB Syntax

|  sa.dft.DataFormat = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
value |  (enum NASADataType) \- Choose from: 0 naSAFloatMAGdb: Set data format to log magnitude in dBm. 1 naSAFloatAMPVolt: Set data format to linear magnitude in volts. 2 naSAPackedInt: Set data format to Packed Integers: a more compact (2 bytes) numeric representation for dBm. Each set of 2 bytes is a short number s, to get the dBm value compute (s/200.0 -36.165).  
  
#### Return Type

|  Enum as NASADataType  
  
#### Default

|  naSAFloatMAGdb  
  
#### Examples

|  sa.dft.DataFormat = naSAFloatMAGdb 'Write  
FormatType = sa.dft.DataFormat 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DataFormat(tagNASADataType* pVal)  
HRESULT put_DataFormat(tagNASADataType newVal)  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

