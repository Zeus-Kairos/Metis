##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# FileEraseEachSweep Property

* * *

#### Description

|  Enables/disables erasing output data files after each sweep. When disabled,
data is appended to the output file after each sweep which could lead to very
large files sizes (and eventually fill the disk).  
---|---  
  
####  VB Syntax

|  sa.dft.FileEraseEachSweep = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- Erase data files after each sweep disabled. 1 - ON \- Erase data files after each sweep enabled.  
  
#### Return Type

|  Boolean  
  
#### Default

|  ON  
  
#### Examples

|  sa.dft.FileEraseEachSweep = ON 'Write  
value = sa.dft.FileEraseEachSweep 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FileEraseEachSweep(VARIANT_BOOL* enable)  
HRESULT put_FileEraseEachSweep(VARIANT_BOOL enable)  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

