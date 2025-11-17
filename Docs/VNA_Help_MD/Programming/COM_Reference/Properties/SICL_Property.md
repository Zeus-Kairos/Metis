##### Write/Read

|

##### [Configuring the analyzer for
SICL/VISA](../../Learning_about_GPIB/Configure_for_VISA_and_SICL.htm)  
  
---|---  
  
## SICL Property

* * *

#### Description

|  Allows you to control the VNA via SICL (standard instrument control
library). In this mode, the analyzer can receive SCPI commands from the LAN
interface or from a program residing on the VNA itself. This command performs
the same function as the [SICL /
GPIB](../../Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.htm#SICL)
dialog box - SICL Enabled checkbox. [See Configuring the analyzer for
SICL/VISA](../../Learning_about_GPIB/Configure_for_VISA_and_SICL.htm). When
SICL is enabled, the VNA VXI-11.2 interface is enabled, and if the VNA hard
disk image is new enough to have the VXI-11.3 interface, it also enables that.
[Learn more about LXI / VXI](../../../S0_Start/LXI_Compliance.md). With this
method you can augment a test program written using SICL that resides on the
VNA so that it will run unattended. An automation script can be written to
start the VNA, enable SICL (using the SICL property), and then start the SICL
based program.  
---|---  
  
####  VB Syntax

|  app.SICL value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
value |  (Boolean) Choose from: True \- enable SICL False \- disable SICL  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  Dim Pna as AgilentPNA835x.Application  
Dim siclState as Boolean  
Set Pna = CreateObject(AgilentPNA835x.Application)  
Pna.SICL = true write  
siclState = Pna.SICL 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SICL(VARIANT_BOOL *pVal) HRESULT put_SICL(VARIANT_BOOL newVal)  
  
#### Interface

|  IApplication5

