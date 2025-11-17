##### Write-only

|

##### [About Measurement
Parameters](../../../S1_Settings/Measurement_Parameters.htm)  
  
---|---  
  
## ChangeParameter Method

* * *

#### Description

| Changes the parameter of the measurement.  
---|---  
  
####  VB Syntax

| meas.ChangeParameter(param,src)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas | A [Measurement](../Objects/Measurement_Object.md) (object)  
param | (string) \- New parameter. Case insensitive.

### For
[S-parameters](../../../S1_Settings/Measurement_Parameters.md#S_Params) and
[Applications](../../../Applications/Applications.md) parameters:

Single-digit port numbers can be separated by "_" (underscore). For example:
"S21" or "S2_1" Double-digit port numbers MUST be separated by underscore. For
example: "S10_1"

### For Ratioed receiver measurements:

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

"topology:parameter" Choose from: | Choose this: | To get this:  
---|---  
| Topology | Parameter  
"SBAL:IMBSB" | single-ended to balanced | imbalance  
"SBAL:CMRRSB1" | single-ended to balanced | common mode rejection (Sds21/Scs21)  
"SBAL:CMRRSB2" | single-ended to balanced | common mode rejection (Ssd12/Ssc12)  
"SSB:IMB1SSB" | single-ended / single-ended to balanced | imbalance 1  
"SSB:IMB2SSB" | single-ended / single-ended to balanced | imbalance 2  
"SSB:CMRRSSB1" | single-ended / single-ended to balanced | common mode rejection (Sds31/Scs31)  
"SSB:CMRRSSB2" | single-ended / single-ended to balanced | common mode rejection (Sds32/Scs32)  
"BBAL:IMB1BB" | balanced to balanced | imbalance 1  
"BBAL:IMB2BB" | balanced to balanced | imbalance 2  
"BBAL:CMRRBB" | balanced to balanced | common mode rejection (Sdd21/Scc21)  
  
src | (long integer)

  * Ignored if param is an S-Parameter
  * Source port if param is a ratioed or unratioed receiver measurement (including ADC measurements).

Note: If the port is defined by a string name, such as an external source, a
balanced port, or one of the Source outputs on the 2-port VNA-x model with
multiple sources, then you must use
[chan.getPortNumber](GetPortNumber_Method.md) to translate the string into a
port number. To learn more see [Remotely Specifying a Source
Port](../../Remotely_Specifying_a_Source_Port.htm).  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| meas.ChangeParameter "S11",2 '2 is ignored meas.ChangeParameter "VC21",1 '1
is ignored meas.ChangeParameter "A/R1",2 '2 is the source port
meas.ChangeParameter "a1/b1",1 '1 is the source port meas.ChangeParameter
"R1",2 '2 is the source port 'to change to a parameter with a string name  
dim app  
set app = CreateObject("Agilentpna835x.application")  
dim capabilities  
set capabilities = app.Capabilities  
dim portnum  
portnum = Capabilities.GetPortNumber("Src2 Out1")  
app.activemeasurement.ChangeParameter "A",portnum  
  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT ChangeParameter(BSTR parameter, long lPort)  
  
#### Interface

| IMeasurement  
  
* * *

