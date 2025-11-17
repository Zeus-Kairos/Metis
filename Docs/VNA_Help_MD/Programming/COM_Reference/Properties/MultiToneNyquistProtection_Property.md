##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# MultiToneNyquistProtection Property

* * *

#### Description

| Sets and returns the Nyquist protection level. Avoids Nyquist images of the
IF higher order signal to fall back on multitone frequencies. This setting can
only be set > 1 if the tone spacing of the multitone is not an integer divider
of 100 MHz.  
---|---  
  
#### VB Syntax

| sa.coherence.MultiToneNyquistProtection = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.coherence | A [SpectrumAnalyzerCoherence](../Objects/SpectrumAnalyzerCoherence.md) (object)  
value | (Long)  Nyquist protection level.  
  
#### Return Type

| Long  
  
#### Default

| 0  
  
#### Examples

| sa.coherence.MultiToneNyquistProtection = 2  'Write  
value = sa.coherence.MultiToneNyquistProtection 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_MultiToneNyquistProtection(long value); HRESULT
get_MultiToneNyquistProtection(long* value);  
  
#### Interface

| ICoherenceSA2  
  
* * *

