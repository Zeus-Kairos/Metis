##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# FIFOEnabled Property

* * *

#### Description

|  Enables/disables exporting data to the [FIFO (First-IN, First-OUT) data
buffer](../../../IFAccess/FIFO_and_other_Antenna_Features.htm#FIFO). FIFO is a
circular buffer that allows very fast Read-Write access. Note: FIFO commands
are under the [FIFO Object](../Objects/FIFO_Object.md), and a new set of
commands has been added here for binary data.  
---|---  
  
####  VB Syntax

|  sa.dft.FIFOEnabled = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- Export data to FIFO disabled. 1 - ON \- Export data to FIFO enabled.  
  
#### Return Type

|  Boolean  
  
#### Default

|  OFF  
  
#### Examples

|  sa.dft.FIFOEnabled = ON 'Write  
value = sa.dft.FIFOEnabled 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FIFOEnabled(VARIANT_BOOL* enable)  
HRESULT put_FIFOEnabled(VARIANT_BOOL enable)  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

