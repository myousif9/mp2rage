from nipype.interfaces.base import BaseInterface,
BaseInterfaceInputSpec, traits, File, TraitedSpec


class get_unring_InputSpec(BaseInterfaceInputSpec):
    in_file = File(exists=True, desc="file", mandatory=True)


class get_unring_OutputSpec(TraitedSpec):
    in_file = File(desc="file")


class unring(BaseInterface):
    input_spec = get_unring_InputSpec
    output_spec = get_unring_OutputSpec

    def _run_interface(self, runtime):
        # implement unringing
