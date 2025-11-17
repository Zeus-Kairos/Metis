##### Write/Read

|

##### [About Sweeping](../../../S1_Settings/Sweep.md)  
  
---|---  
  
## AlternateSweep Property

* * *

#### Description

|  Sets sweeps to either alternate or chopped.  
---|---  
  
####  VB Syntax

|  object.AlternateSweep = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  Channel (object) or CalSet (object) - Read-only property  
value |  (boolean) - Choose either: False \- Sweep mode set to Chopped \- reflection and transmission are measured on the same sweep. True \- Sweep mode set to Alternate \- reflection and transmission measured on separate sweeps. Improves Mixer bounce and Isolation measurements. Increases cycle time.  
  
#### Return Type

|  boolean  
  
#### Default

|  False (0)  
  
#### Examples

|  chan.AlternateSweep = True 'Write  
altSwp = chan.AlternateSweep 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT AlternateSweep(VARIANT_BOOL *pVal)  
HRESULT AlternateSweep(VARIANT_BOOL newVal)  
  
#### Interface

|  IChannel ICalSet3

