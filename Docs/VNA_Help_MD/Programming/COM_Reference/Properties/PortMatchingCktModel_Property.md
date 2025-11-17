##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## PortMatchingCktModel Property

* * *

#### Description

|  Sets and returns the Port Matching circuit model for the specified port
number. Note: This command affects ALL measurements on the channel.  
---|---  
  
####  VB Syntax

|  fixture.PortMatchingCktModel(port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
port |  (Integer) Port number to receive circuit model.  
value |  (Enum as NAFixturingPortMatchCkt) Circuit model. Choose from 0 naFixPMC_SLPC Series L - Parallel C 1 naFixPMC_PCSL Parallel C - Series L 2 naFixPMC_PLSC Parallel L - Series C 3 naFixPMC_SCPL Series C - Parallel L 4 naFixPMC_PLPC Parallel L - Parallel C 5 naFixPMC_USER Load S2P file - also set filename to load with [strPortMatch_S2PFile Property](strPortMatch_S2PFile_Property.md) 6 naFixPMC_NONE No circuit model 7 naFixPMC_SCPC Series C - Parallel C 8 naFixPMC_PCSC Parallel C - Series C 9 naFixPMC_SLPL Series L - Parallel L 10 naFixPMC_PLSL Parallel L - Series L  
  
#### Return Type

|  Long Integer  
  
#### Default

|  naFixPMC_NONE  
  
#### Examples

|  fixture.PortMatchingCktModel(2) = naFixPMC_PLSC 'Write  
value = fixture.PortMatchingCktModel(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortMatchingCktModel(short port tagNAFixturingPortMatchCkt
*pVal)  
HRESULT put_PortMatchingCktModel(short port tagNAFixturingPortMatchCkt newVal)  
  
#### Interface

|  IFixturing

