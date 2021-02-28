
import os
from enb import icompression
from enb.config import get_options

options = get_options()

class golomb(icompression.WrapperCodec, icompression.LosslessCodec):
    def __init__(self):
        icompression.WrapperCodec.__init__(
            self,
            compressor_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "golomb_coder"),
            decompressor_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "golomb_coder"),
            param_dict=None, output_invocation_dir=None)

    def get_compression_params(self, original_path, compressed_path, original_file_info):
        return f"{original_path} {compressed_path} c"

    def get_decompression_params(self, compressed_path, reconstructed_path, original_file_info):
        return f"{compressed_path} {reconstructed_path} d"

    @property
    def label(self):
        return "golomb" 
