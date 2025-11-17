# Create Modulation File

This example program creates a source modulation file for modulation
distortion measurements.

This VBScript program can be run as a macro in the VNA. To do this, copy the
code into a text editor file such as Notepad and save on the VNA hard drive as
ModFile.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

[See the Modulation Distortion commands.](../GP-
IB_Command_Finder/SourceModulation.htm)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

'Example code to create/edit modulation signals set app =
CreateObject("Agilentpna835x.application", "k-n5242b-81474") set scpi =
app.ScpiStringParser ' Preset and add a trace in Modulation Distortion channel
scpi.Parse "syst:fpr" scpi.Parse("disp:wind1:stat on")
scpi.Parse("calc:cust:def 'ch1_PIn1','Modulation Distortion','PIn1'")
scpi.Parse "disp:wind1:trac1:feed 'ch1_PIn1'" ' Create an NPR Notch signal
scpi.Parse "sour:mod:file:type nprn" scpi.Parse "sour:mod:file:sign:srat
200e6" scpi.Parse "sour:mod:file:sign:span 100e6" scpi.Parse
"sour:mod:file:sign:span:pri 1" scpi.parse "sour:mod:file:sign:tone:numb 1001"
scpi.parse "sour:mod:file:sign:tone:numb:pri 1" scpi.Parse
"sour:mod:file:sign:npr:notc:numb 1" scpi.Parse
"sour:mod:file:sign:npr:notc:loc cust" scpi.Parse
"sour:mod:file:sign:npr:notc1:span 10e6" scpi.Parse
"sour:mod:file:sign:npr:notc1:offs 0" scpi.parse "sour:mod:file:save
'd:\symphony\scpi\npr.mdx'" ' Create compact signals ' Number of tones =
101/1001/10001 ' Peak-to-avg priority: on/off ' Number of files = 5 ' Original
signal file: 5GNR_256QAM_120kHz_SCS_100MHz_122p88MHzSR.wfm scpi.Parse
"sour:mod:file:type comp" infile = "5GNR_256QAM_120kHz_SCS_100MHz_122p88MHzSR"
scpi.parse "sour:mod:file:sign:comp:ofile 'd:\Symphony\scpi\" & infile &
".wfm'" scpi.parse "sour:mod:file:sign:comp:file:numb 5" scpi.parse
"sour:mod:file:sign:tone:numb:pri 1" for e = 2 to 4 '101/1001/10001 numTones =
10 ^ e + 1 scpi.parse "sour:mod:file:sign:tone:numb " & numTones for i = 1 to
5 scpi.parse "sour:mod:file:sign:comp:pavg:pri 0" scpi.parse
"sour:mod:file:sign:comp:file:sel " & i outfile = "d:\Symphony\scpi\" & infile
& "_" & numTones & "_" & i  scpi.parse "sour:mod:file:save '" & outfile &
".mdx'" scpi.parse "sour:mod:file:sign:comp:pavg:pri 1" outfile = outfile &
"p" scpi.parse "sour:mod:file:save '" & outfile & ".mdx'" next next ' Create a
flat tone signal scpi.Parse "sour:mod:file:type flat" scpi.Parse
"sour:mod:file:sign:srat 200e6" scpi.Parse "sour:mod:file:sign:span 100e6"
scpi.Parse "sour:mod:file:sign:span:pri 1" scpi.parse
"sour:mod:file:sign:tone:numb 1001" scpi.parse
"sour:mod:file:sign:tone:numb:pri 1" scpi.parse "sour:mod:file:save
'd:\symphony\scpi\flat.mdx'" ' Edit a signal scpi.parse "sour:mod:file:load
'd:\symphony\scpi\npr.mdx'" scpi.parse "sour:mod:file:sign:tone:numb 2001"
scpi.parse "sour:mod:file:sign:tone:numb:pri 1" scpi.Parse
"sour:mod:file:sign:npr:notc1:offs 10e6" scpi.parse "sour:mod:file:save
'd:\symphony\scpi\npr_2001tone_notch_offset_10M.mdx'" msgbox "Done"  
---

