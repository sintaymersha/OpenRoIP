from dataclasses import dataclass


@dataclass
class AudioDevice:
    id: int
    name: str
    type: str
    input_channels: int
    output_channels: int
    sample_rate: int
    default_input: bool = False
    default_output: bool = False

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "input_channels": self.input_channels,
            "output_channels": self.output_channels,
            "sample_rate": self.sample_rate,
            "default_input": self.default_input,
            "default_output": self.default_output,
        }