##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# MultiToneEnable Property

* * *

#### Description

| Enables/disables multitone image rejection. When enabled, the window type is
set to No Window and the list of RBW possible values is recomputed according
to the multitone spacing. When disabled, the window type is set back to what
it was before enabling and the RBW list is also set to the previous setting.  
---|---  
  
####  VB Syntax

| sa.coherence.MultiToneEnable = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.coherence | A [SpectrumAnalyzerCoherence](../Objects/SpectrumAnalyzerCoherence.md) (object)  
value | (Boolean) Choose from: 0 - OFF \- Multitone image rejection disabled. 1 - ON \- Multitone image rejection enabled.  
  
#### Return Type

| Boolean  
  
#### Default

| OFF  
  
#### Examples

| sa.coherence.MultiToneEnable = ON 'Write  
value = sa.coherence.MultiToneEnable 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_MultiToneEnable(VARIANT_BOOL* enable)  
HRESULT put_MultiToneEnable(VARIANT_BOOL enable)  
  
#### Interface

| ICoherenceSA  
  
* * *

