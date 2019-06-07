from nipype.interfaces.base import BaseInterface,
BaseInterfaceInputSpec, traits, File, TraitedSpec


class get_dwidenoise_InputSpec(BaseInterfaceInputSpec):
    in_file = File(exists=True, desc="file", mandatory=True)


class get_dwidenoise_OutputSpec(TraitedSpec):
    in_file = File(desc="file")


class dwidenoise(BaseInterface):
    input_spec = get_dwidenoise_InputSpec
    output_spec = get_dwidenoise_OutputSpec

    def _run_interface(self, runtime):
        # implement unringing
