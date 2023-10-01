import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .step import Step


@forge_signature
class Pipeline(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("pipelineINDEX"),
        xml="@id",
    )

    name: Optional[str] = Field(
        default=None,
        description="Name of the pipeline",
    )

    steps: Optional[Step] = Field(
        default=Step(),
        description="Steps of the pipeline",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/haeussma/test-ci.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="3dba73523b4b2857394f08905522aedb4723b124"
    )

    def print_name(self):
        print(self.name)


