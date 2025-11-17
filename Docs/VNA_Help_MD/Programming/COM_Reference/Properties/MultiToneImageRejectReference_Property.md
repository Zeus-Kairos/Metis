##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# MultiToneReference Property

* * *

#### Description

| Sets and returns the multitone image rejection offset frequency. If the
multitone grid does not start from 0 Hz, this command is used to set its
offset. To make this more convenient, this command accepts as well the
frequency of any tone of the multitone grid (Hz).  
---|---  
  
#### VB Syntax

| sa.coherence.MultiToneReference = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.coherence | A [SpectrumAnalyzerCoherence](../Objects/SpectrumAnalyzerCoherence.md) (object)  
value | (Double)  Offset frequency (in Hz)  
  
#### Return Type

| Double  
  
#### Default

| 0  
  
#### Examples

| sa.coherence.MultiToneReference = 0  'Write  
value = sa.coherence.MultiToneReference 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_MultiToneReference(double freqval); HRESULT
get_MultiToneReference(double* freqval);  
  
#### Interface

| ICoherenceSA  
  
* * *

