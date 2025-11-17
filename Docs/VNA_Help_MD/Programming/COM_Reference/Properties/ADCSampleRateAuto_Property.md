##### Write/Read

|

##### [About SA
Application](../../../Applications/Spectrum_Analyzer.htm#ADC_Sample_Rate)  
  
---|---  
  
## EnableADCSampleRateAuto Property

* * *

#### Description

| Set and read how the ADC sample rate is set. When set to 1, ADC sample rate
is set based on the ADC filter setting.  
---|---  
  
#### VB Syntax

| sa.EnableADCSampleRateAuto = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa | A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value | (Boolean) Choose from: 0 - OFF \- ADC sampling rate is set manually using [ADCSampleRate](ADCSampleRate_Property.md). 1 - ON \- Automatically select ADC sample rate based on the ADC filter setting. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#ADC_Sample_Rate).  
  
#### Return Type

| Boolean  
  
#### Default

| 1  
  
#### Examples

| sa.EnableADCSampleRateAuto = 1  'Write  
value = sa.EnableADCSampleRateAuto 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_EnableADCSampleRateAuto(VARIANT_BOOL bEnable); HRESULT
get_EnableADCSampleRateAuto(VARIANT_BOOL* bEnable);  
  
#### Interface

| ISpectrumAnalyzer  
  
* * *

