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
        default="6ce3825271a80a3e70440b0c1aeec884a5d77c1f"
    )

    def add_to_steps(
        self,
        name: str,
        required: bool,
        species: List[AbstractSpecies] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Step' to attribute steps

        Args:
            id (str): Unique identifier of the 'Step' object. Defaults to 'None'.
            name (): Name of the pipeline.
            required (): True, if step is required for the pipeline.
            species (): Species of the step. Defaults to ListPlus()
        """
        params = {"name": name, "required": required, "species": species}
        if id is not None:
            params["id"] = id
        self.steps.append(Step(**params))
        return self.steps[-1]
