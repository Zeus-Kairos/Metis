##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# DataLevelThresholdEnabled Property

* * *

#### Description

| Enables/disables data level threshold mode. Set the threshold level using
the [DataLevelThreshold](DataLevelTreshold_Property.md) command.  
---|---  
  
####  VB Syntax

| sa.dft.DataLevelThresholdEnabled = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft | A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
value | (Boolean) Choose from: 0 - OFF \- Disable threshold mode. 1 - ON \- Enable threshold mode.  
  
#### Return Type

| Boolean  
  
#### Default

| OFF  
  
#### Examples

| sa.dft.DataLevelThresholdEnabled = ON 'Write  
value = sa.dft.DataLevelThresholdEnabled 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_DataLevelThresholdEnabled(VARIANT_BOOL* enable)  
HRESULT put_DataLevelThresholdEnabled(VARIANT_BOOL enable)  
  
#### Interface

| ISpectrumAnalyzerDFT2  
  
* * *

