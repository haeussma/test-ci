import sdRDM

from typing import List, Optional
from pydantic import Field, StrictBool
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from lmfit import Parameters, report_fit
from .abstractspecies import AbstractSpecies
from .vessel import Vessel


@forge_signature
class Step(sdRDM.DataModel):
    """This is the definition of a step."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("stepINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Name of the pipeline",
    )

    required: bool = Field(
        ...,
        description="True, if step is required for the pipeline",
    )

    species: List[AbstractSpecies] = Field(
        description="Species of the step",
        default_factory=ListPlus,
        multiple=True,
    )

    def add_to_species(
        self,
        name: str,
        vessel_id: Vessel,
        constant: StrictBool,
        init_conc: Optional[float] = None,
        unit: Optional[str] = None,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'AbstractSpecies' to attribute species

        Args:
            id (str): Unique identifier of the 'AbstractSpecies' object. Defaults to 'None'.
            name (): None.
            vessel_id (): None.
            constant (): None.
            init_conc (): None. Defaults to None
            unit (): None. Defaults to None
            uri (): None. Defaults to None
            creator_id (): None. Defaults to None
        """
        params = {
            "name": name,
            "vessel_id": vessel_id,
            "constant": constant,
            "init_conc": init_conc,
            "unit": unit,
            "uri": uri,
            "creator_id": creator_id,
        }
        if id is not None:
            params["id"] = id
        self.species.append(AbstractSpecies(**params))
        return self.species[-1]

    def give_lmfit(lmfit_params: Parameters):
        return lmfit_params

    def give_report(report_fit: report_fit):
        return report_fit
