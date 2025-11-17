##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# SourcePower Property

#### Description

|  Set and read the source power level. This command applies to CW or linear
sweep types.  
---|---  
  
#### VB Syntax

|  sa.SourcePower (source) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
source |  (String) Source name enclosed in quotes. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of available source port names. See also [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
value |  (Double) Source power level in dBm. Choose a value within the power range of the source.  
  
#### Return Type

|  Double  
  
#### Default

|  Default of the source.  
  
#### Examples

|  sa.SourcePower("Port 1") = -5  'Write  
value = sa.SourcePower("Port 1") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_SourcePower(BSTR sourcename, double power); HRESULT
get_SourcePower(BSTR sourcename, double* power);  
  
#### Interface

|  ISpectrumAnalyzer

