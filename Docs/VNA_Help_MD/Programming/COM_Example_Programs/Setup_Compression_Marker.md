## Set Up Compression Marker

* * *

This example program does the following:

  * Creates a compression marker

  * Queries the Power Out and Power In values

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as CompMkr.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#Setup)

[See the FIFO object.](../COM_Reference/Objects/FIFO_Object.md)

[See Other COM Example Programs](COM_Example_Intro.md)

Set app = CreateObject("AgilentPNA835X.Application") set meas =
app.activemeasurement 'get the COM marker object 'and create marker1 set mark
= meas.marker(1) 'set the compression level mark.compressionlevel = 1.5 'make
it a compression marker 'and find the compression point
mark.searchcompressionpoint 'return power out and power in 'power in dim
answer answer = mark.compressionpin wscript.echo("pin: " & answer) 'power out
answer = mark.compressionpout wscript.echo("pout: " & answer)  
---  
  
* * *

