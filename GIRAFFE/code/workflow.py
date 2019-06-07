#This is a Nipype generator. Warning, here be dragons.
#!/usr/bin/env python

import sys
import nipype
import nipype.pipeline as pe

import .dwi_preproc.custom_functions as custom_nodes
import nipype.interfaces.fsl as fsl
import nipype.interfaces.io as io

#Wraps dwidenoise function.
dwidenoise = pe.Node(interface = custom_nodes.dwidenoise(), name='dwidenoise')

#Wraps unring function.
unring = pe.Node(interface = custom_nodes.Unring(), name='unring')

#Wraps fslval function.
fslval = pe.Node(interface = custom_nodes.fslval(), name='fslval')

#Wraps the executable command ``eddy_openmp``.
fsl_Eddy = pe.Node(interface = fsl.Eddy(), name='fsl_Eddy')

#Wraps the executable command ``flirt``.
fsl_FLIRT = pe.Node(interface = fsl.FLIRT(), name='fsl_FLIRT')

#Flexibly collect data from disk to feed into workflows.
io_SelectFiles = pe.Node(io.SelectFiles(templates={}), name='io_SelectFiles')

#Create a workflow to connect all those nodes
analysisflow = nipype.Workflow('MyWorkflow')
analysisflow.connect(dwidenoise, "out_file", unring, "in_file")
analysisflow.connect(fslval, "out_file", fsl_Eddy, "in_index")
analysisflow.connect(unring, "out_file", fsl_Eddy, "in_file")
analysisflow.connect(fsl_Eddy, "out_corrected", fsl_FLIRT, "in_file")
analysisflow.connect(io_SelectFiles, "T1", fsl_FLIRT, "reference")
analysisflow.connect(io_SelectFiles, "acqp", fsl_Eddy, "in_acqp")
analysisflow.connect(io_SelectFiles, "bval", fsl_Eddy, "in_bval")
analysisflow.connect(io_SelectFiles, "bvec", fsl_Eddy, "in_bvec")
analysisflow.connect(io_SelectFiles, "mask", fsl_Eddy, "in_mask")
analysisflow.connect(io_SelectFiles, "DWI", dwidenoise, "in_file")

#Run the workflow
plugin = 'MultiProc' #adjust your desired plugin here
plugin_args = {'n_procs': 1} #adjust to your number of cores
analysisflow.write_graph(graph2use='flat', format='png', simple_form=False)
analysisflow.run(plugin=plugin, plugin_args=plugin_args)
