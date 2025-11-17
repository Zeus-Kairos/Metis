##### Read-only

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# MultitoneSettingsValid Property

* * *

#### Description

| Read the current multitone settings and determine if they are valid or not.  
---|---  
  
#### VB Syntax

| value = sa.coherence.MultitoneSettingsValid  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.coherence | A [SpectrumAnalyzerCoherence](../Objects/SpectrumAnalyzerCoherence.md) (object)  
value | (Long) Variable to store the returned value. A "1" is valid and a "0" is invalid.  
  
#### Return Type

| Boolean  
Example | value = sa.coherence.MultitoneSettingsValid 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_MultitoneSettingsValid(VARIANT_BOOL* value);  
  
#### Interface

| ICoherenceSA2  
  
* * *

