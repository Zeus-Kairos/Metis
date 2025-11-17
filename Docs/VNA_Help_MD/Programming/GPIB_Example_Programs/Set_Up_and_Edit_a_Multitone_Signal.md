# Set Up and Edit a Multitone Signal

The following example demonstrates how to set up and edit a multitone signal.

[See the Modulation Distortion commands.](../GP-
IB_Command_Finder/SourceModulation.htm)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

// Create the MOD channel first. *IDN? SYST:FPR disp:wind1:stat on
calc:cust:def 'ch1_PIn1','Modulation Distortion','PIn1' disp:wind1:trac1:feed
'ch1_PIn1' // Create a new flat-tone modulation file with 1001 tones.
sour:mod:file:type flat sour:mod:file:sign:srat 200e6 sour:mod:file:sign:span
100e6 sour:mod:file:sign:span:pri 1 sour:mod:file:sign:tone:numb 1001
sour:mod:file:sign:tone:numb:pri 1 sour:mod:file:save
'd:\symphony\scpi\flat.mdx' // Edit some of the tones by turning them off.
sour:mod:file:tone:coun? sour:mod:file:tone:freq? 1001 sour:mod:file:tone:stat
1001, OFF sour:mod:file:tone:stat 1002, OFF sour:mod:file:tone:stat 1003, OFF
sour:mod:file:tone:stat 1004, OFF sour:mod:file:tone:stat 1005, OFF
sour:mod:file:tone:stat 1006, OFF sour:mod:file:tone:stat 1007, OFF
sour:mod:file:tone:stat 1008, OFF // Edit some of the tones by changing their
amplitudes. sour:mod:file:tone:pow 1009, 0.0 sour:mod:file:tone:pow 1010, 0.0
// Edit some of the tones by changing their phases. sour:mod:file:tone:phas
1011, 180.0 // Save the above edited tones in a CSV tone setup file for future
use. sour:mod:file:tone:save 'd:\symphony\scpi\multitonesetup.csv' // Save the
edited tones as a modulation file for use. sour:mod:file:save
'd:\symphony\scpi\flat1.mdx' // Turn all the tones on.
sour:mod:file:tone:all:stat on // Save another modulation file with all tones
on. sour:mod:file:save 'd:\symphony\scpi\flat2.mdx' // Load the saved CSV tone
setup file back and save another modulation file. sour:mod:file:tone:load
'd:\symphony\scpi\multitonesetup.csv' sour:mod:file:save
'd:\symphony\scpi\flat3.mdx'  
---

