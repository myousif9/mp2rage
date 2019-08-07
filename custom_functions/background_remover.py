from nipype.interfaces.matlab import MatlabCommand
from nipype.interfaces.base import TraitedSpec, BaseInterface, BaseInterfaceInputSpec,File,traits
import os
from string import Template

class T1wgenInputSpec(BaseInterfaceInputSpec):
    uni_in = File(exists=True,
                  desc='input file for UNI image',
                  argstr="%s",
                  mandatory=True)
    inv1_in = File(exisits=True,
                   desc='input file for INV1 image',
                   argstr="%s",
                   mandatory=True)
    inv2_in = File(exisits=True,
                   desc='input file for INV2 image',
                   argstr="%s",
                   mandatory=True)
    reg = traits.Float(desc='input value for regularization')
    out_file = File('t1w_gen.nii.gz',
                   desc='name of output T1w image',
                   genfile=True,
                   usedefault=True)

class T1wgenOutputSpec(TraitedSpec):
    out_file=File(desc="path/name of T1w file (if generated)")

class T1wgen(BaseInterface):
    input_spec = T1wgenInputSpec
    output_spec = T1wgenOutputSpec
    print(os.path.join(os.getcwd(),'DemoRemoveBackgroundNoise.m'))
    def _run_interface(self, runtime):
#         d = dict(uni = self.inputs.uni_in,
#                 inv1 = self.inputs.inv1_in,
#                 inv2 = self.inputs.inv2_in,
#                 reg = self.inputs.reg,
#                 denoise = self.inputs.out_file)
        with open('/home/ROBARTS/myousif/anaconda3/lib/python3.7/site-packages/MP2RAGE_wrapper/DemoRemoveBackgroundNoise.m','r') as script_file:
            script_content = script_file.read()
            
        script = script_content.format(uni = self.inputs.uni_in,
                                       inv1 = self.inputs.inv1_in,
                                       inv2 = self.inputs.inv2_in,
                                       denoise = self.inputs.out_file,
                                      reg = self.inputs.reg)
        
        mlab = MatlabCommand(script=script, mfile=True)
        mlab.inputs.paths = ['func/RobustCombination.m'),
                           os.path.join(os.getcwd(),'nii_func/load_nii_ext.m'),
                           os.path.join(os.getcwd(),'nii_func/load_nii_hdr.m'),
                           os.path.join(os.getcwd(),'nii_func/load_untouch0_nii_hdr.m'),
                           os.path.join(os.getcwd(),'nii_func/load_untouch_nii.m'),
                           os.path.join(os.getcwd(),'nii_func/load_untouch_nii_hdr.m'),
                           os.path.join(os.getcwd(),'nii_func/load_untouch_nii_img.m'),
                           os.path.join(os.getcwd(),'nii_func/save_nii_ext.m'),
                           os.path.join(os.getcwd(),'nii_func/save_untouch0_nii_hdr.m'),
                           os.path.join(os.getcwd(),'nii_func/save_untouch_nii.m'),
                           os.path.join(os.getcwd(),'nii_func/save_untouch_nii_hdr.m'),
                           os.path.join(os.getcwd(),'nii_func/verify_nii_ext.m')]
        result = mlab.run()
        return result.runtime
    def _list_outputs(self):
        outputs = self._outputs().get()
        outputs['out_file'] = os.path.abspath(self.inputs.out_file)
        return outputs
