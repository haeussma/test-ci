```mermaid
classDiagram
    AbstractSpecies <-- Protein
    AbstractSpecies <-- Complex
    AbstractSpecies <-- Reactant
    EnzymeMLDocument *-- Creator
    EnzymeMLDocument *-- Vessel
    EnzymeMLDocument *-- Protein
    EnzymeMLDocument *-- Complex
    EnzymeMLDocument *-- Reactant
    EnzymeMLDocument *-- Reaction
    EnzymeMLDocument *-- KineticParameter
    EnzymeMLDocument *-- Measurement
    EnzymeMLDocument *-- File
    AbstractSpecies *-- Vessel
    Protein *-- SBOTerm
    Complex *-- SBOTerm
    Reactant *-- SBOTerm
    Reaction *-- SBOTerm
    Reaction *-- ReactionElement
    Reaction *-- KineticModel
    ReactionElement *-- SBOTerm
    ReactionElement *-- AbstractSpecies
    KineticModel *-- SBOTerm
    KineticModel *-- KineticParameter
    KineticParameter *-- SBOTerm
    Measurement *-- MeasurementData
    MeasurementData *-- AbstractSpecies
    MeasurementData *-- Replicate
    Replicate *-- DataTypes
    Replicate *-- AbstractSpecies
    Pipeline *-- Step
    Step *-- AbstractSpecies
    AbstractSpecies *-- Vessel
    
    class Pipeline {
        +string name*
        +Step[0..*] steps
        +int max_length
    }
    
    class Step {
        +string name*
        +bool required*
        +float[0..*] new_attr
        +AbstractSpecies[0..*] species
    }
    
    class Vessel {
        +string name*
        +posfloat volume*
        +string unit*
        +StrictBool constant*
        +string uri
        +string creator_id
    }
    
    class AbstractSpecies {
        +string name*
        +Vessel vessel_id*
        +float init_conc
        +StrictBool constant*
        +string unit
        +string uri
        +string creator_id
    }
    
    class SBOTerm {
        << Enumeration >>
        +BIOCHEMICAL_REACTION
        +ACID_BASE_REACTION
        +CONFORMATIONAL_TRANSITION
        +CONVERSION
        +DEGRADATION
        +DISSOCIATION
        +IONISATION
        +ISOMERISATION
        +NON_COVALENT_BINDING
        +REDOX_REACTION
        +SPONTANEOUS_REACTION
        +PROTEIN
        +GENE
        +SMALL_MOLECULE
        +ION
        +RADICAL
        +INTERACTOR
        +SUBSTRATE
        +PRODUCT
        +CATALYST
        +INHIBITOR
        +ESSENTIAL_ACTIVATOR
        +NON_ESSENTIAL_ACTIVATOR
        +POTENTIATOR
        +MACROMOLECULAR_COMPLEX
        +PROTEIN_COMPLEX
        +DIMER
        +MICHAELIS_MENTEN
        +K_CAT
        +K_M
        +V_MAX
    }
    
    class DataTypes {
        << Enumeration >>
        +CONCENTRATION
        +ABSORPTION
        +FEED
        +BIOMASS
        +CONVERSION
        +PEAK_AREA
    }
    
    class https://github.com/EnzymeML/enzymeml-specifications.git {
        << External Object >>
        +Repository <sdRDM.markdown.markdownparser.MarkdownParser object at 0x7fd329615220>
    }
    
```