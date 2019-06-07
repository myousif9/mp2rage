from nipype.interfaces.base import BaseInterface,
BaseInterfaceInputSpec, traits, File, TraitedSpec


class get_unring_InputSpec(BaseInterfaceInputSpec):
    mail_file = File(exists=True, desc="file", mandatory=True)
    mask_file = File(exists=True, desc="file", mandatory=True)
    index_file = File(exists=True, desc="file", mandatory=True)
    acqp_file = File(exists=True, desc="file", mandatory=True)
    bval_file = File(exists=True, desc="file", mandatory=True)
    bvec_file = File(exists=True, desc="file", mandatory=True)


class get_unring_OutputSpec(TraitedSpec):
    out_file = File(desc="file")


class Unring(BaseInterface):
    input_spec = get_unring_InputSpec
    output_spec = get_unring_OutputSpec

    def _run_interface(self, runtime):
        # implement unringing

    def _list_outputs(self):
        outputs = self._outputs().get()
        outputs["out_file"] = self.out_file
        return outputs
