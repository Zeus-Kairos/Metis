##### Write-only

|

##### [About Measurement
Parameters](../../../S1_Settings/Measurement_Parameters.htm)  
  
---|---  
  
## CreateMeasurement Method

* * *

#### Description

|  Creates a new measurement.  
---|---  
  
####  VB Syntax

|  app.CreateMeasurement chanNum,param,lPort[,window]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  Application (object)  
chanNum |  (long) - Channel number of the new measurement; can exist or be a new channel  
param |  (string) \- New parameter. Case insensitive.

### For S-parameters:

[Any S-parameter that can be measured by your
VNA.](../../../S1_Settings/Measurement_Parameters.htm#S_Params) Single-digit
port numbers can be separated by "_" (underscore). For example: "S21" or
"S2_1" Double-digit port numbers MUST be separated by underscore. For example:
"S10_1"

### For Ratioed measurements:

Any two receivers in your VNA separated by "/". For example: "A/R1" See the
[block diagram](../../../Specs/ManualChoice.md#Block_diag) showing the
receivers in YOUR VNA.

### For Unratioed (absolute power) measurements:

Any receiver in the VNA. For example: "A" See the [block
diagram](../../../Specs/ManualChoice.htm#Block_diag) showing the receivers in
YOUR VNA Ratioed and Unratioed measurements can also use logical receiver
notation to refer to receivers. This notation makes it easy to refer to
receivers with an [external test
set](../../../System/External_Testset_Control.htm) connected to the VNA. You
do not need to know which physical receiver is used for each test port. [Learn
more.](../../../S1_Settings/Measurement_Parameters.htm#RecNotation)

### For ADC measurements

Any ADC receiver in the VNA. For example: "AI1" indicates the Analog Input1.
[Learn more about ADC receiver
measurements.](../../../S1_Settings/ADC_Measurements.htm)

### For Balanced S-parameter measurements:

"topology:Sabxy" topology - Choose from:

  1.      * sbal \- single-ended to balanced
     * ssb \- single-ended / single-ended to balanced
     * bbal \- balanced to balanced

Sabxy - Where a - device output (receive) mode b - device input (source) mode
(choose from the following for both a and b:)

  1.      1.         * d \- differential
        * c \- common
        * s \- single ended

x - device output (receive) logical port number y - device input (source)
logical port number For example:"sbal:sdd42" [See an example
program](../../COM_Example_Programs/Create_a_Balanced_Measurement.htm)

### For [Imbalance](../../../S1_Settings/Balanced_Measurements.md#imbalance)
and [Common Mode
Rejection](../../../S1_Settings/Balanced_Measurements.htm#CMRR) measurements:

"topology:parameter" Choose from: |  Choose this: |  To get this:  
---|---  
|  Topology |  Parameter  
"SBAL:IMBSB" |  single-ended to balanced |  imbalance  
"SBAL:CMRRSB1" |  single-ended to balanced |  common mode rejection (Sds21/Scs21)  
"SBAL:CMRRSB2" |  single-ended to balanced |  common mode rejection (Ssd12/Ssc12)  
"SSB:IMB1SSB" |  single-ended / single-ended to balanced |  imbalance 1  
"SSB:IMB2SSB" |  single-ended / single-ended to balanced |  imbalance 2  
"SSB:CMRRSSB1" |  single-ended / single-ended to balanced |  common mode rejection (Sds31/Scs31)  
"SSB:CMRRSSB2" |  single-ended / single-ended to balanced |  common mode rejection (Sds32/Scs32)  
"BBAL:IMB1BB" |  balanced to balanced |  imbalance 1  
"BBAL:IMB2BB" |  balanced to balanced |  imbalance 2  
"BBAL:CMRRBB" |  balanced to balanced |  common mode rejection (Sdd21/Scc21)  
  
lPort |  (long)

  * Ignored if param is an S-Parameter, balanced, imbalance, or CMRR parameter.
  * Source port if param is ratioed or unratioed (including [ADC](../../../S1_Settings/ADC_Measurements.md)) measurements.
  * Use 0 for [N5264B](../../../IFAccess/N5264A.md).

Note: If the port is defined by a string name, such as an external source, a
balanced port, or one of the Source 2 outputs on the 2-port 2-source VNA-x
model, then you must use [chan.getPortNumber](GetPortNumber_Method.md) to
translate the string into a port number. To learn more see [Remotely
Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.htm).  
window |  (long) Optional argument. Window number of the new measurement. Choose between 1and the [maximum number of windows allowed on the VNA.](../Properties/MaximumNumberOfWindows_Property.md). If unspecified, the measurement will be created in the Active Window. See also [Traces, Channels, and Windows on the VNA](../../../S0_Start/Traces_Channels_and_Windows.md#window)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.CreateMeasurement(1,"A/R1",1,0) app.CreateMeasurement(1,"a1/b1",1,0)
app.CreateMeasurement(1,"bbal:Sdd21",1) app.CreateMeasurement(1,"AI2",2)
app.CreateMeasurement(1,"R1",0) ' for N5264B  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT CreateMeasurement(long ChannelNum, BSTR strParameter, long lPort,
long windowNumber)  
  
#### Interface

|  IApplication  
  
* * *

