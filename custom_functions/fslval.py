import os
from nipype.interfaces.base import BaseInterface,
BaseInterfaceInputSpec, traits, File, TraitedSpec


class get_fslval_InputSpec(BaseInterfaceInputSpec):
    in_file = File(exists=True, desc="file", mandatory=True)


class get_fslval_OutputSpec(TraitedSpec):
    out_file = File(desc="file")


class fslval(BaseInterface):
    input_spec = get_fslval_InputSpec
    output_spec = get_fslval_OutputSpec

    def _run_interface(self, runtime):
        # implement fslval
        fname = self.inputs.in_file
        out_path = self.inputs.out_file

        cmnd = 'fslval'+" "+fname+" "+'dim4'
        val = os.popen(cmnd).read()

        line = ""
        for i in range(0,int(val)):
            line = line + str(1)+" "
        with open(out_path+"/index.txt", "w") as text_file:
            print(line, file=text_file)
        

    def _list_outputs(self):
        outputs = self._outputs().get()
        outputs["out_file"] = self.out_file
        return outputs