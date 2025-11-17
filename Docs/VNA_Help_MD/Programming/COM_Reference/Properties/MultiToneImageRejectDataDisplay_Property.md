##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# MultiToneDataDisplay Property

* * *

#### Description

| Sets and returns the data display mode.  
---|---  
  
####  VB Syntax

| sa.coherence.MultiToneDataDisplay = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.coherence | A [SpectrumAnalyzerCoherence](../Objects/SpectrumAnalyzerCoherence.md) (object)  
value | (enum NASACoherentDataDisplay) \- Choose from: 0 naSAShowAll: Legacy SA mode - all frequency points are displayed. 1 naSAZeroNonTones: All the frequencies that are not on the multi-tone coherence grid are set to 200 dBm before being displayed.  
  
#### Return Type

| Enum as NASACoherentDataDisplay  
  
#### Default

| naSAShowAll  
  
#### Examples

| sa.coherence.MultiToneDataDisplay = naSAShowAll 'Write  
DisplayMode = sa.coherence.MultiToneDataDisplay 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_MultiToneDataDisplay(tagNASACoherentDataDisplay* value)  
HRESULT put_MultiToneDataDisplay(tagNASACoherentDataDisplay value)  
  
#### Interface

| ICoherenceSA  
  
* * *

