# Shared Memory Example in C#

The following C# program demonstrates how to set up 4 traces and gather the
data using shared memory. This code should be run on the PXI controller
directly.

### See Also

[SYSTem:DATA:MEMory](../GP-IB_Command_Finder/System.md) commands

// This example demonstrates how to use C# to setup 4 traces and to gather
data using the shared memory component  
// This code should be run on the PXI controller directly  
// The example demonstrates using helper function to check for all possible
errors  
// during the running of the code. Checking for errors helps identify problems
early  
  
// Add visa32.cs to the project.  
// It it is here (after installing IO Libraries on your PC)  
// C:\Program Files\IVI Foundation\VISA\Win64\agvisa\include\agvisa32.cs  
using _System_ ;  
using _System_._Text_ ;  
using _System_._IO_._MemoryMappedFiles_ ;  
  
class SharedMemory  
{  
  
// Variables to store the VISA session numbers  
static int g_defaultSession = -1;  
static int g_session = -1;  
  
static void Main(string[] args)  
{  
try  
{  
// Find the VISA address from the SCPI parser console on your VNA  
// System->System Setup->Remote Interface... Show SCPI parser Console ->
Status  
// TODO: CHANGE THIS VISA_ADDRESS to point to your VNA  
string VISA_ADDRESS = "TCPIP0::localhost::hislip0,4880::INSTR";  
int timeout = 1000;  
  
CheckViStatus(visa32.viOpenDefaultRM(out g_defaultSession));  
CheckViStatus(visa32.viOpen(g_defaultSession, VISA_ADDRESS, 0, timeout, out
g_session));  
CheckViStatus(visa32.viSetAttribute(g_session, visa32.VI_ATTR_TMO_VALUE,
timeout));  
  
int s = g_session; // s is a alias for session  
  
WriteString("SYST:FPR");  
WriteString("DISP:WIND:STAT 1");  
  
// initialize memory mapped structures in VNA  
WriteString("SYST:DATA:MEM:INIT\n");  
  
// Create 4 SParameters  
string[] parameters = new string[] { "S11", "S21", "S12", "S22" };  
int[] offsets_for_complex_data = new int[parameters._Length_];  
int[] offsets_for_formatted_data = new int[parameters._Length_];  
for (int i = 0; i < parameters._Length_ ; i++)  
{  
// Create a new parameter  
WriteString($"CALC1:MEAS{i \+ 1}:DEF '{parameters[i]}'");  
WriteString($"DISP:MEAS{i+1}:FEED 1\n");  
  
// Configure a new section of the memory map to monitor the complex data of
this parameter  
WriteString("SYST:DATA:MEM:ADD '1:" \+ (i \+ 1)._ToString_() + ":SDATA:201'");
// add parameter to memory mapped  
offsets_for_complex_data[i] = int._Parse_(Query("SYST:DATA:MEM:OFFSet?"));  
  
  
// Configure a new section of the memory map to monitor the formatted data of
this parameter  
WriteString("SYST:DATA:MEM:ADD '1:" \+ (i \+ 1)._ToString_() + ":FDATA:201'");
// add parameter to memory mapped  
offsets_for_formatted_data[i] = int._Parse_(Query("SYST:DATA:MEM:OFFSet?"));  
}  
  
// Tell the VNA to allocate the memory map. Name it "VNA_MemoryMap"  
WriteString("SYST:DATA:MEM:COMM 'VNA_MemoryMap'");  
  
// Query the size of the memory map  
  
int size = int._Parse_(Query("SYST:DATA:MEM:SIZE?"));  
  
// Create the memory map in C#. This requires .NET 4.5 framework  
 _MemoryMappedFile_ mappedFile =
_MemoryMappedFile_._CreateOrOpen_("VNA_MemoryMap", size);  
 _MemoryMappedViewAccessor_ mappedFileView =
mappedFile._CreateViewAccessor_();  
  
  
// Trigger a single sweep, and wait for it to complete  
WriteString("SENS:SWE:MODE SING");  
Query("*OPC?");  
  
// Allocate buffers to hold the output data  
float[][] complexData = new float[parameters._Length_][];  
for (int i = 0; i < complexData._Length_ ; i++)  
{  
complexData[i] = new float[402];  
}  
  
float[][] formattedData = new float[parameters._Length_][];  
for (int i = 0; i < formattedData._Length_ ; i++)  
{  
formattedData[i] = new float[201];  
}  
  
// Copy the data from the memory map into the output buffers  
// These copy the data from the in-process memory map.  
// This runs very fast - and is just a "memcpy" under the hood  
for (int i = 0; i < parameters._Length_ ; i++)  
{  
ReadBytes(mappedFileView, offsets_for_complex_data[i], 402, complexData[i]);  
ReadBytes(mappedFileView, offsets_for_formatted_data[i], 201,
formattedData[i]);  
}  
  
// Output some data to show that it worked  
 _Console_._WriteLine_(complexData[0][0]._ToString_()); // Output first point
of S11 in complex  
 _Console_._WriteLine_(formattedData[3][200]._ToString_()); // Output last
point of S22 as formatted  
}  
catch (_Exception_ ex)  
{  
 _Console_._WriteLine_(ex._Message_);  
}  
// Close the handles - even if there was an error  
if (g_session != -1)  
visa32.viClose(g_session);  
if (g_defaultSession != -1)  
visa32.viClose(g_defaultSession);  
}  
  
static public unsafe void ReadBytes(_MemoryMappedViewAccessor_ mappedFileView,  
int offset, int num, float[] arr)  
{  
// This is equivalent to:  
// //m_mappedFileView.ReadArray<float>(m_sharedMemoryOffsets[i-1],
complexArray, 0, points*2);  
// But, using this "unsafe" code is 30 times faster. 100usec versus 3ms  
byte* ptr = (byte*)0;  
mappedFileView._SafeMemoryMappedViewHandle_._AcquirePointer_(ref ptr);  
 _System_._Runtime_._InteropServices_._Marshal_._Copy_(_IntPtr_._Add_(new
_IntPtr_(ptr), offset), arr, 0, num);  
mappedFileView._SafeMemoryMappedViewHandle_._ReleasePointer_();  
}  
  
static void WriteString(string command)  
{  
command += "\n";  
CheckViStatus(visa32.viPrintf(g_session,command));  
CheckForErrors();  
}  
static string Query(string query)  
{  
query += "\n";  
CheckViStatus(visa32.viPrintf(g_session,query));  
 _StringBuilder_ errorMessage = new _StringBuilder_();  
CheckViStatus(visa32.viScanf(g_session, "%t", errorMessage));  
return errorMessage._ToString_();  
}  
  
  
// Helper function to check for any error with a VISA call  
static void CheckViStatus(int viStatus)  
{  
if (viStatus < 0) // If the viStatus is less than 0, then it indicates an
error  
{  
// Convert the error number to a string  
 _StringBuilder_ errorMessage = new _StringBuilder_();  
visa32.viStatusDesc(g_session, viStatus, errorMessage);  
  
// Throw an exception with the string  
throw new _Exception_(errorMessage._ToString_());  
}  
}  
  
// Helper function to check for logical SCPI errors  
static void CheckForErrors()  
{  
// Next check if there was a SCPI error  
CheckViStatus(visa32.viPrintf(g_session, "SYST:ERR:COUN?\n"));  
int errorCount;  
CheckViStatus(visa32.viScanf(g_session, "%d", out errorCount));  
if (errorCount == 0)  
return; // no errors  
  
// There is an error, let's convert it to a string  
 _StringBuilder_ allErrors = new _StringBuilder_();  
for (int i = 0; i < errorCount; i++)  
{  
CheckViStatus(visa32.viPrintf(g_session, "SYST:ERR?\n"));  
 _StringBuilder_ errorMessage = new _StringBuilder_();  
CheckViStatus(visa32.viScanf(g_session, "%t", errorMessage));  
allErrors._Append_(errorMessage);  
}  
throw new _Exception_(allErrors._ToString_());  
}  
  
}  
  
---

