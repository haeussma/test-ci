import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Step(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("stepINDEX"),
        xml="@id",
    )

    name: Optional[str] = Field(
        default=None,
        description="Name of the pipeline",
    )

    required: Optional[bool] = Field(
        default=None,
        description="True, if step is required for the pipeline",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/haeussma/test-ci.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="d0d45e8e6540389f586b2b094b78e94d65cc91a3"
    )
