import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .abstractspecies import AbstractSpecies
from .step import Step


@forge_signature
class Pipeline(sdRDM.DataModel):
    """This is the definition of a pipeline."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("pipelineINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Name of the pipeline",
    )

    steps: List[Step] = Field(
        description="List of steps in the pipeline",
        default_factory=ListPlus,
        multiple=True,
    )

    max_length: Optional[int] = Field(
        default=None,
        description="Maximum length of the pipeline",
    )
    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/haeussma/test-ci.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="b6632df838b334faea009f667f5f4bf7df999ee3"
    )

    def add_to_steps(
        self,
        name: str,
        required: bool,
        new_attr: List[float] = ListPlus(),
        species: List[AbstractSpecies] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Step' to attribute steps

        Args:
            id (str): Unique identifier of the 'Step' object. Defaults to 'None'.
            name (): Name of the pipeline.
            required (): True, if step is required for the pipeline.
            new_attr (): New test attr. Defaults to ListPlus()
            species (): Species of the step. Defaults to ListPlus()
        """
        params = {
            "name": name,
            "required": required,
            "new_attr": new_attr,
            "species": species,
        }
        if id is not None:
            params["id"] = id
        self.steps.append(Step(**params))
        return self.steps[-1]
