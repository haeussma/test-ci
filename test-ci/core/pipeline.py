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
        default="026ae4d5f328f20662eb3e6226c4acbd299b36e6"
    )
