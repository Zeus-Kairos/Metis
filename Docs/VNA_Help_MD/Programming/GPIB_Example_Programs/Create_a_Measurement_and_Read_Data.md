# Create a Measurement and Read Data

The following C# program demonstrates how to use C# to communicate with the
VNA by creating a measurement and reading the data.

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

// This example demonstrates how to use C# to communicate with Keysight VNA  
// The example demonstrates using helper function to check for all possible
errors  
// during the running of the code. Checking for errors helps identify problems
early  
  
  
// Add visa32.cs to the project.  
// It it is here (after installing IO Libraries on your PC)  
// C:\Program Files\IVI Foundation\VISA\Win64\agvisa\include\agvisa32.cs  
  
using _System_ ;  
using _System_._Text_ ;  
  
class BasicCSharp  
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
string VISA_ADDRESS = "TCPIP0::localhost::hislip0::INSTR";  
int timeout = 1000;  
  
CheckViStatus(visa32.viOpenDefaultRM(out g_defaultSession));  
CheckViStatus(visa32.viOpen(g_defaultSession, VISA_ADDRESS, 0, timeout, out
g_session));  
CheckViStatus(visa32.viSetAttribute(g_session, visa32.VI_ATTR_TMO_VALUE,
timeout));  
  
// Destroy all measurements and add a window  
WriteString("SYST:FPR");  
WriteString("DISP:WIND:STAT 1");  
  
// Check for any SCPI errors that occurred  
CheckForErrors();  
  
// Create S11 measurement.  
// HINT(optional): SCPI commands can use single quotes to delineate strings.
It is easier than escaping double quotes  
WriteString("CALC1:MEAS1:DEF 'S11'");  
  
// Displays measurement 1 in window 1 and assigns the next available trace
number to the measurement  
WriteString("DISP:MEAS1:FEED 1");  
  
// Put the channel in hold mode - good idea for fast setup  
WriteString("SENS1:SWEep:MODE HOLD");  
  
// Change point count to 51  
int pointCount = 51;  
WriteString($"SENS1:SWEep:POINts {pointCount}");  
  
// Change start frequency to 1 GHz and stop to 2 GHz  
WriteString("SENS1:FREQuency:STARt 1e9");  
WriteString("SENS1:FREQuency:STOP 2e9");  
  
// Check for any SCPI errors that occurred  
CheckForErrors();  
  
// Take a sweep  
WriteString("SENS1:SWE:MODE SING");  
  
// Check for any SCPI errors that occurred  
CheckForErrors();  
  
// Block until the sweep is complete. *OPC? is used to block on any
asynchronous (overlapped) operation  
// If the sweep is slow, then this could block for a long time  
Query("*OPC?");  
  
float[] traceData = QueryFloatArray("CALC1:MEAS:DATA:FDATa?",pointCount);  
  
for (int i=0;i<traceData._Length_ ;i++)  
{  
 _Console_._Write_(traceData[i]);  
if (i != traceData._Length_ \- 1)  
 _Console_._Write_(",");  
}  
 _Console_._WriteLine_(); // newline  
 _Console_._WriteLine_("Success!");  
}  
catch (_Exception_ ex)  
{  
 _Console_._WriteLine_("Error occurred:" + ex._Message_);  
}  
  
// Close the handles - even if there was an error  
if (g_session != -1)  
visa32.viClose(g_session);  
if (g_defaultSession != -1)  
visa32.viClose(g_defaultSession);  
}  
  
// Helper function to write a string. Automatically adds the newline  
static void WriteString(string command)  
{  
command += "\n";  
CheckViStatus(visa32.viPrintf(g_session, command));  
CheckForErrors();  
}  
  
// Helper function to query a string  
static string Query(string query)  
{  
query += "\n";  
CheckViStatus(visa32.viPrintf(g_session, query));  
 _StringBuilder_ errorMessage = new _StringBuilder_();  
CheckViStatus(visa32.viScanf(g_session, "%t", errorMessage));  
return errorMessage._ToString_();  
}  
  
// Helper function to query an array of floats  
static float[] QueryFloatArray(string query,int expectedSize)  
{  
query += "\n";  
float[] myArray = new float[expectedSize];  
// Read the formatted data  
CheckViStatus(visa32.viPrintf(g_session,query));  
int pointCountIn = expectedSize;  
  
// viScanF automatically breaks apart comma separated values into the given
array  
CheckViStatus(visa32.viScanf(g_session, "%,#f", ref pointCountIn, myArray));  
if (pointCountIn != expectedSize)  
throw new _Exception_("Point Count read does not match");  
return myArray;  
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
// First check if there was a SCPI error  
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

