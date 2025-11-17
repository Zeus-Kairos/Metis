# SYSTem:CHANnels:GCSetup commands

Configures and makes settings for GCA Parallel measurements.

SYSTem:CHANnels:GCSetup: | PARallel | [:ENABle] | GROup  
---  
  
Click on a red keyword to view the command details.

See Also

  * Learn about: [GCA Parallel Measurement](../../Applications/Gain_Compression_Application.md#GCA_Parallel)

  * Programming example: [Setting Up GCA Parallel Measurement](../GPIB_Example_Programs/Setup_GCA_Parallel_Measurement.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SYSTem:CHANnels:GCSetup:PARallel[:ENABle] <bool>

Applicable Models: M980xA, M983xA (Read-Write) Sets and reads the GCA Parallel
Measurement state.  
---  
Parameters |   
<bool> |  Choose from: ON or 1: GCA parallel measurement are enabled. OFF or 0: GCA parallel measurement are disabled..  
Examples |  SYST:CHAN:GCS:PAR:ENAB ON system:channels:gcsetup:parallel:enable 0  
Query Syntax |  SYSTem:CHANnels:GCSetup:PARallel:ENABle?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:CHANnels:GCSetup:PARallel:GROup <iarray>

Applicable Models: M980xA, M983xA (Read-Write) Sets and reads the group of
channels for the GCA Parallel Measurement.  
---  
Parameters |   
<iarray> |  {<number of group>, <start channel No. of group #1>, <end channel No. of group #1>, <start channel No. of group #2>, <end channel No. of group #2>, ... } The first item means number or groups. Next pairs show start/end channel numbers of the group. 1 pair for 1 group. Example: {0} - Couples all existing GCA channels in one group (default setting) {1,1,4} - Couples channel 1-4 in one group {2,1,3,5,7} - Couples channel 1-3 in first group and channels 5-7 in second group  
Examples |  SYST:CHAN:GCS:PAR:GRO 2,1,3,5,7 system:channels:gcsetup:parallel:group 1,1,4  
Query Syntax |  SYSTem:CHANnels:GCSetup:PARallel:GROup?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

##

