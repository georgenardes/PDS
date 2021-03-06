# Generated by the VisualDSP++ IDDE

# Note:  Any changes made to this Makefile will be lost the next time the
# matching project file is loaded into the IDDE.  If you wish to preserve
# changes, rename this file and run it externally to the IDDE.

# The syntax of this Makefile is such that GNU Make v3.77 or higher is
# required.

# The current working directory should be the directory in which this
# Makefile resides.

# Supported targets:
#     filtro_PB_Debug
#     filtro_PB_Debug_clean

# Define this variable if you wish to run this Makefile on a host
# other than the host that created it and VisualDSP++ may be installed
# in a different directory.

ADI_DSP=C:\Program Files (x86)\Analog Devices\VisualDSP 5.1.2


# $VDSP is a gmake-friendly version of ADI_DIR

empty:=
space:= $(empty) $(empty)
VDSP_INTERMEDIATE=$(subst \,/,$(ADI_DSP))
VDSP=$(subst $(space),\$(space),$(VDSP_INTERMEDIATE))

RM=cmd /C del /F /Q

#
# Begin "filtro_PB_Debug" configuration
#

ifeq ($(MAKECMDGOALS),filtro_PB_Debug)

filtro_PB_Debug : ./Debug/filtro_PB.dxe 

Debug/fir_mm.doj :fir_mm.c $(VDSP)/Blackfin/include/stdio.h $(VDSP)/Blackfin/include/yvals.h ../coefs_pb.dat 
	@echo ".\fir_mm.c"
	$(VDSP)/ccblkfn.exe -c .\fir_mm.c -file-attr ProjectName=filtro_PB -g -structs-do-not-overlap -no-multiline -double-size-32 -decls-strong -warn-protos -proc ADSP-BF533 -o .\Debug\fir_mm.doj -MM

Debug/process.doj :process.c 
	@echo ".\process.c"
	$(VDSP)/ccblkfn.exe -c .\process.c -file-attr ProjectName=filtro_PB -g -structs-do-not-overlap -no-multiline -double-size-32 -decls-strong -warn-protos -proc ADSP-BF533 -o .\Debug\process.doj -MM

./Debug/filtro_PB.dxe :$(VDSP)/Blackfin/ldf/adsp-BF533.ldf $(VDSP)/Blackfin/lib/bf532_rev_0.5/crtsf532y.doj ./Debug/fir_mm.doj ./Debug/process.doj $(VDSP)/Blackfin/lib/bf532_rev_0.5/__initsbsz532.doj $(VDSP)/Blackfin/lib/cplbtab533.doj $(VDSP)/Blackfin/lib/bf532_rev_0.5/crtn532y.doj $(VDSP)/Blackfin/lib/bf532_rev_0.5/libsmall532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libio532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libc532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/librt_fileio532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libevent532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libcpp532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libf64ieee532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libdsp532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libsftflt532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libetsi532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/Debug/libssl532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/Debug/libdrv532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/Debug/libusb532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libprofile532y.dlb 
	@echo "Linking..."
	$(VDSP)/ccblkfn.exe .\Debug\fir_mm.doj .\Debug\process.doj -L .\Debug -add-debug-libpaths -flags-link -od,.\Debug -o .\Debug\filtro_PB.dxe -proc ADSP-BF533 -MM

endif

ifeq ($(MAKECMDGOALS),filtro_PB_Debug_clean)

filtro_PB_Debug_clean:
	-$(RM) "Debug\fir_mm.doj"
	-$(RM) "Debug\process.doj"
	-$(RM) ".\Debug\filtro_PB.dxe"
	-$(RM) ".\Debug\*.ipa"
	-$(RM) ".\Debug\*.opa"
	-$(RM) ".\Debug\*.ti"
	-$(RM) ".\Debug\*.pgi"
	-$(RM) ".\*.rbld"

endif


