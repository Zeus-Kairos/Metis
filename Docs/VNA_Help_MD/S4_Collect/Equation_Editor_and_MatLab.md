# Equation Editor and MATLAB®

* * *

MATLAB can be used with Equation Editor in two different ways:

## 1\. When you install a full version of MATLAB on the VNA, MATLAB functions
can be called directly from Equation Editor.

  1. Install the full 32 bit version of MATLAB.

  2. Press Math > Analysis > Equation Editor....

  3. In the Equation Editor dialog, click the Enable MATLAB button.

  4. You can then start calling MATLAB from within your equation editor entry field.

  5. Here are a few example of how you would do this:

     * Matlab("S11.*S22") -> produces an array of multiplying S11*S22

     * Matlab("phase(S11)")-> produces an array of unwrapped phase of the S11 trace.

## 2\. Compile a MATLAB *.dll using the full version on your PC. Then import
the *.dll into Equation Editor

[Learn how to Import Functions into Equation
Editor](Equation_Editor_Import_Functions.htm)

The [MATLAB Compile Runtime on the
VNA](../Support/Licenses.htm#Commercial_Software_License) is currently 7.14,
which is shipped with R2010b (7.11).

If you compile your *.dll using that version of MATLAB, then you don't need to
change the version of MCR on the VNA.

  1. Determine the version of MATLAB you will use.

  * You will need this version of MATLAB installed on your development machine (Step 2). You will also need a C++ compiler (Step 3).

  * You will need the appropriate version of MATLAB Compiler Runtime (MCR) installed on your target machines (Step 5).

  *     * To see installed version of MCR, check the following locations:

    *       * On a 32-bit Windows system:

      *         * C:\Program Files\Matlab\Matlab Compiler Runtime\

        * C:\Program Files\Matlab\Matlab Component Runtime\

      * On a 64-bit Windows system:

      *         * C:\Program Files (x86)\Matlab\Matlab Compiler Runtime\

        * C:\Program Files (x86)\Matlab\Matlab Component Runtime\

  * Use the chart below to compare MATLAB, MCR, and Compiler versions.

  2. Install MATLAB (32-bit) on your development machine.

     * If your development system is 64-bit, manually navigate to \bin\win32\ on your install disk and run setup.exe to use the 32-bit installer. This requirement will be removed in future releases.

     * You must install with the MATLAB Compiler toolbox.

  3. Install a compatible C++ compiler on your development machine.

  1.      * For R2011b through R2013b, Windows SDK 7.1 with .NET 4.0 is sufficient.

     *        * Due to issues with the SDK installer, it is recommended to separately install .NET first, if not already installed.

       * The current SDK installer will also fail if Visual Studio redistributables are installed.

     * For a list of compatible compilers, see <http://www.mathworks.com/support/compilers/>

     * Note that LCC is only a C compiler, not C++, and is not an acceptable option.

  4. In MATLAB, select your installed compiler by running the command: >> mbuild -setup

  5. Install the correct MCR on all target machines. This requires a reboot even if not prompted to do so by the installer.

### Creating a MATLAB DLL

  1. Open the MATLAB Compiler Deployment Tool, either through the user interface or with >> deploytool, and choose to make a "C++ Shared Library" project.

  2. Add any .m files to your project that you need in the DLL through the Deployment Tool window. This includes any helpers for functions need to execute.

     1. Functions must take in 0 to 32 arguments and return 1 value to be used on traces.

     2. The return value can be an array the size of a trace or a single value.

     3. Functions not conforming aren't directly accessible from Equation Editor but must be included if other functions rely on them.

  3. Optional: Add function descriptors. These are separate functions which provide default arguments and tooltips for the function.

     1. Descriptors must have the same name as the function they describe with the postfix desc. For example, MyFunc could have a descriptor MyFuncdesc.

     2. Descriptors take no input arguments.

     3. Descriptors return a single string with the format defaultArgs;tooltip. For example, S11,S22;Performs an operation.

  4. Build the project. This may take a few minutes and, if there are no errors, will generate project, src and distrib folders. The DLL will be under the distrib folder.

     1. Some of the other generated files may be useful but are not needed for Equation Editor.

  5. Optional: Package all the distributable files.

     1. This package can also include the appropriate MCR installer (as large as 0.5 GB).

     2. In general this step isn't needed, only the generated DLL is required.

### Notes about Writing Scripts

The MATLAB functions that will be accessed directly by the Equation Editor
must follow a specific format, as noted briefly above.

  * Inputs: 0 to 32 vectors with dimensions [1, Sweep Size].

  *     * Constants (0, e, channel(), etc.) are expanded and passed as [1, Sweep Size] vectors.

  * Outputs: 1 vector with dimensions [1, Sweep Size] or [1, 1].

  *     * Outputs size [1, 1] are expanded to [1, Sweep Size] vectors automatically.

Functions with other input/output sets are not directly accessible from
Equation Editor but may be included in your DLL and used by other functions,
meaning helpers can be used without risk.

Existing functions that do not fit these parameters can be included along with
wrapper functions which convert the parameters and outputs within the MATLAB
environment.

* * *

