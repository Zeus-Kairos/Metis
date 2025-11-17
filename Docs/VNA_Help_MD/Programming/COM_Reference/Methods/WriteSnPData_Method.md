##### Write-only

|

##### Learn about Noise Parameters  
  
---|---  
  
## WriteSnPData Method

* * *

#### Description

| Saves the S-parameters and vector noise parameters to an S2P file. For NFX
channels, mixer setup information is included as comments at the beginning of
the file. The following is sample data for two data points in a Noise Figure
channel: ! Keysight Technologies,N5242A,USxxxxxxx,A.09.85 ! pnan-nn Thu Nov 01
12:26:27 2012 # HZ S MA R 50 !freq (Hz) S11M S11A S21M S21A S12M S12A S22M
S22A 2000000000 9.038147e-001 6.241193e+001 5.855965e+000 -6.116778e+001
2.232653e-002 -1.475392e+002 5.275644e-001 1.750775e+002 8000000000
6.951366e-001 -1.458202e+002 5.307699e+000 -7.055212e+001 7.838612e-002
-1.460951e+002 3.986142e-001 -2.226317e+001 ! Noise Parameters !freq (Hz)
NFMin(dB) Rho_opt(Mag) Rho_opt(deg) Rn/Z0 2000000000 1.251697e+000
2.172018e-001 -8.765875e+001 1.806663e-001 8000000000 1.583849e+000
2.015185e-001 1.029875e+002 1.320403e-001  
---|---  
  
####  VB Syntax

| nf.WriteSnPData (data, filename)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
nf | A [NoiseFigure](../Objects/NoiseFigure_Object.md) (object)  
data | (string) \- Choose "NoiseParameter" \- Noise parameter data The format of the snp data is set with [SnPFormat Property](../Properties/SnPFormat_Property.md)  
filename | Path, filename and suffix of location to store SNP data.  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| nf.WriteSnPData "NoiseParameter","C:\Program Files(x86)\Keysight\Network
Analyzer\Documents\MyNoiseParams.s2p"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT WriteSnPData(BSTR data, BSTR filename);  
  
#### Interface

| INoiseFigure7  
  
* * *

