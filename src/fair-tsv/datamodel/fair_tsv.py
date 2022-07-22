# Auto generated from fair_tsv.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-05-07T20:12:53
# Schema: fair_tsv
#
# id: https://w3id.org/linkml/fair_tsv
# description: Rubrics for FAIR evaluation of TSVs
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
FAMREL = CurieNamespace('famrel', 'http://example.org/famrel/')
FT = CurieNamespace('ft', 'https://w3id.org/linkml/fair_tsv')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = FT


# Types

# Class references



@dataclass
class Result(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FT.Result
    class_class_curie: ClassVar[str] = "ft:Result"
    class_name: ClassVar[str] = "Result"
    class_model_uri: ClassVar[URIRef] = FT.Result

    input: Optional[str] = None
    has_evaluation: Optional[Union[dict, "Evaluation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.input is not None and not isinstance(self.input, str):
            self.input = str(self.input)

        if self.has_evaluation is not None and not isinstance(self.has_evaluation, Evaluation):
            self.has_evaluation = Evaluation(**as_dict(self.has_evaluation))

        super().__post_init__(**kwargs)


@dataclass
class Evaluation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FT.Evaluation
    class_class_curie: ClassVar[str] = "ft:Evaluation"
    class_name: ClassVar[str] = "Evaluation"
    class_model_uri: ClassVar[URIRef] = FT.Evaluation

    uses_tab_separators: Optional[Union[str, "UsesTabSeparatorsResult"]] = None
    uses_unix_newline_characters: Optional[str] = None
    uses_correct_quotation: Optional[str] = None
    avoids_extraneous_whitespace: Optional[str] = None
    avoids_problematic_characters: Optional[str] = None
    avoids_empty_lines: Optional[str] = None
    uses_correct_encoding: Optional[str] = None
    has_column_header: Optional[str] = None
    includes_metadata_header: Optional[str] = None
    includes_data_dictionary: Optional[str] = None
    includes_mappings_to_other_schemas: Optional[str] = None
    dates_use_iso8601: Optional[str] = None
    identifiers_are_prefixed_CURIEs: Optional[str] = None
    CURIEs_are_syntactically_correct: Optional[str] = None
    prefixes_are_declared_and_consistent_with_registries: Optional[str] = None
    prefixes_have_URI_expansions: Optional[str] = None
    categorical_values_are_enumerated_in_schema: Optional[str] = None
    categorical_values_are_mapped_to_external_resources: Optional[str] = None
    data_is_tidy: Optional[str] = None
    validates_using_schema: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.uses_tab_separators is not None and not isinstance(self.uses_tab_separators, UsesTabSeparatorsResult):
            self.uses_tab_separators = UsesTabSeparatorsResult(self.uses_tab_separators)

        if self.uses_unix_newline_characters is not None and not isinstance(self.uses_unix_newline_characters, str):
            self.uses_unix_newline_characters = str(self.uses_unix_newline_characters)

        if self.uses_correct_quotation is not None and not isinstance(self.uses_correct_quotation, str):
            self.uses_correct_quotation = str(self.uses_correct_quotation)

        if self.avoids_extraneous_whitespace is not None and not isinstance(self.avoids_extraneous_whitespace, str):
            self.avoids_extraneous_whitespace = str(self.avoids_extraneous_whitespace)

        if self.avoids_problematic_characters is not None and not isinstance(self.avoids_problematic_characters, str):
            self.avoids_problematic_characters = str(self.avoids_problematic_characters)

        if self.avoids_empty_lines is not None and not isinstance(self.avoids_empty_lines, str):
            self.avoids_empty_lines = str(self.avoids_empty_lines)

        if self.uses_correct_encoding is not None and not isinstance(self.uses_correct_encoding, str):
            self.uses_correct_encoding = str(self.uses_correct_encoding)

        if self.has_column_header is not None and not isinstance(self.has_column_header, str):
            self.has_column_header = str(self.has_column_header)

        if self.includes_metadata_header is not None and not isinstance(self.includes_metadata_header, str):
            self.includes_metadata_header = str(self.includes_metadata_header)

        if self.includes_data_dictionary is not None and not isinstance(self.includes_data_dictionary, str):
            self.includes_data_dictionary = str(self.includes_data_dictionary)

        if self.includes_mappings_to_other_schemas is not None and not isinstance(self.includes_mappings_to_other_schemas, str):
            self.includes_mappings_to_other_schemas = str(self.includes_mappings_to_other_schemas)

        if self.dates_use_iso8601 is not None and not isinstance(self.dates_use_iso8601, str):
            self.dates_use_iso8601 = str(self.dates_use_iso8601)

        if self.identifiers_are_prefixed_CURIEs is not None and not isinstance(self.identifiers_are_prefixed_CURIEs, str):
            self.identifiers_are_prefixed_CURIEs = str(self.identifiers_are_prefixed_CURIEs)

        if self.CURIEs_are_syntactically_correct is not None and not isinstance(self.CURIEs_are_syntactically_correct, str):
            self.CURIEs_are_syntactically_correct = str(self.CURIEs_are_syntactically_correct)

        if self.prefixes_are_declared_and_consistent_with_registries is not None and not isinstance(self.prefixes_are_declared_and_consistent_with_registries, str):
            self.prefixes_are_declared_and_consistent_with_registries = str(self.prefixes_are_declared_and_consistent_with_registries)

        if self.prefixes_have_URI_expansions is not None and not isinstance(self.prefixes_have_URI_expansions, str):
            self.prefixes_have_URI_expansions = str(self.prefixes_have_URI_expansions)

        if self.categorical_values_are_enumerated_in_schema is not None and not isinstance(self.categorical_values_are_enumerated_in_schema, str):
            self.categorical_values_are_enumerated_in_schema = str(self.categorical_values_are_enumerated_in_schema)

        if self.categorical_values_are_mapped_to_external_resources is not None and not isinstance(self.categorical_values_are_mapped_to_external_resources, str):
            self.categorical_values_are_mapped_to_external_resources = str(self.categorical_values_are_mapped_to_external_resources)

        if self.data_is_tidy is not None and not isinstance(self.data_is_tidy, str):
            self.data_is_tidy = str(self.data_is_tidy)

        if self.validates_using_schema is not None and not isinstance(self.validates_using_schema, str):
            self.validates_using_schema = str(self.validates_using_schema)

        super().__post_init__(**kwargs)


# Enumerations
class UsesTabSeparatorsResult(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="UsesTabSeparatorsResult",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "unable to determine",
                PermissibleValue(text="unable to determine") )
        setattr(cls, "tab separated",
                PermissibleValue(text="tab separated") )
        setattr(cls, "command separated",
                PermissibleValue(text="command separated") )
        setattr(cls, "uses non standard",
                PermissibleValue(text="uses non standard") )

# Slots
class slots:
    pass

slots.result__input = Slot(uri=FT.input, name="result__input", curie=FT.curie('input'),
                   model_uri=FT.result__input, domain=None, range=Optional[str])

slots.result__has_evaluation = Slot(uri=FT.has_evaluation, name="result__has_evaluation", curie=FT.curie('has_evaluation'),
                   model_uri=FT.result__has_evaluation, domain=None, range=Optional[Union[dict, Evaluation]])

slots.evaluation__uses_tab_separators = Slot(uri=FT.uses_tab_separators, name="evaluation__uses_tab_separators", curie=FT.curie('uses_tab_separators'),
                   model_uri=FT.evaluation__uses_tab_separators, domain=None, range=Optional[Union[str, "UsesTabSeparatorsResult"]])

slots.evaluation__uses_unix_newline_characters = Slot(uri=FT.uses_unix_newline_characters, name="evaluation__uses_unix_newline_characters", curie=FT.curie('uses_unix_newline_characters'),
                   model_uri=FT.evaluation__uses_unix_newline_characters, domain=None, range=Optional[str])

slots.evaluation__uses_correct_quotation = Slot(uri=FT.uses_correct_quotation, name="evaluation__uses_correct_quotation", curie=FT.curie('uses_correct_quotation'),
                   model_uri=FT.evaluation__uses_correct_quotation, domain=None, range=Optional[str])

slots.evaluation__avoids_extraneous_whitespace = Slot(uri=FT.avoids_extraneous_whitespace, name="evaluation__avoids_extraneous_whitespace", curie=FT.curie('avoids_extraneous_whitespace'),
                   model_uri=FT.evaluation__avoids_extraneous_whitespace, domain=None, range=Optional[str])

slots.evaluation__avoids_problematic_characters = Slot(uri=FT.avoids_problematic_characters, name="evaluation__avoids_problematic_characters", curie=FT.curie('avoids_problematic_characters'),
                   model_uri=FT.evaluation__avoids_problematic_characters, domain=None, range=Optional[str])

slots.evaluation__avoids_empty_lines = Slot(uri=FT.avoids_empty_lines, name="evaluation__avoids_empty_lines", curie=FT.curie('avoids_empty_lines'),
                   model_uri=FT.evaluation__avoids_empty_lines, domain=None, range=Optional[str])

slots.evaluation__uses_correct_encoding = Slot(uri=FT.uses_correct_encoding, name="evaluation__uses_correct_encoding", curie=FT.curie('uses_correct_encoding'),
                   model_uri=FT.evaluation__uses_correct_encoding, domain=None, range=Optional[str])

slots.evaluation__has_column_header = Slot(uri=FT.has_column_header, name="evaluation__has_column_header", curie=FT.curie('has_column_header'),
                   model_uri=FT.evaluation__has_column_header, domain=None, range=Optional[str])

slots.evaluation__includes_metadata_header = Slot(uri=FT.includes_metadata_header, name="evaluation__includes_metadata_header", curie=FT.curie('includes_metadata_header'),
                   model_uri=FT.evaluation__includes_metadata_header, domain=None, range=Optional[str])

slots.evaluation__includes_data_dictionary = Slot(uri=FT.includes_data_dictionary, name="evaluation__includes_data_dictionary", curie=FT.curie('includes_data_dictionary'),
                   model_uri=FT.evaluation__includes_data_dictionary, domain=None, range=Optional[str])

slots.evaluation__includes_mappings_to_other_schemas = Slot(uri=FT.includes_mappings_to_other_schemas, name="evaluation__includes_mappings_to_other_schemas", curie=FT.curie('includes_mappings_to_other_schemas'),
                   model_uri=FT.evaluation__includes_mappings_to_other_schemas, domain=None, range=Optional[str])

slots.evaluation__dates_use_iso8601 = Slot(uri=FT.dates_use_iso8601, name="evaluation__dates_use_iso8601", curie=FT.curie('dates_use_iso8601'),
                   model_uri=FT.evaluation__dates_use_iso8601, domain=None, range=Optional[str])

slots.evaluation__identifiers_are_prefixed_CURIEs = Slot(uri=FT.identifiers_are_prefixed_CURIEs, name="evaluation__identifiers_are_prefixed_CURIEs", curie=FT.curie('identifiers_are_prefixed_CURIEs'),
                   model_uri=FT.evaluation__identifiers_are_prefixed_CURIEs, domain=None, range=Optional[str])

slots.evaluation__CURIEs_are_syntactically_correct = Slot(uri=FT.CURIEs_are_syntactically_correct, name="evaluation__CURIEs_are_syntactically_correct", curie=FT.curie('CURIEs_are_syntactically_correct'),
                   model_uri=FT.evaluation__CURIEs_are_syntactically_correct, domain=None, range=Optional[str])

slots.evaluation__prefixes_are_declared_and_consistent_with_registries = Slot(uri=FT.prefixes_are_declared_and_consistent_with_registries, name="evaluation__prefixes_are_declared_and_consistent_with_registries", curie=FT.curie('prefixes_are_declared_and_consistent_with_registries'),
                   model_uri=FT.evaluation__prefixes_are_declared_and_consistent_with_registries, domain=None, range=Optional[str])

slots.evaluation__prefixes_have_URI_expansions = Slot(uri=FT.prefixes_have_URI_expansions, name="evaluation__prefixes_have_URI_expansions", curie=FT.curie('prefixes_have_URI_expansions'),
                   model_uri=FT.evaluation__prefixes_have_URI_expansions, domain=None, range=Optional[str])

slots.evaluation__categorical_values_are_enumerated_in_schema = Slot(uri=FT.categorical_values_are_enumerated_in_schema, name="evaluation__categorical_values_are_enumerated_in_schema", curie=FT.curie('categorical_values_are_enumerated_in_schema'),
                   model_uri=FT.evaluation__categorical_values_are_enumerated_in_schema, domain=None, range=Optional[str])

slots.evaluation__categorical_values_are_mapped_to_external_resources = Slot(uri=FT.categorical_values_are_mapped_to_external_resources, name="evaluation__categorical_values_are_mapped_to_external_resources", curie=FT.curie('categorical_values_are_mapped_to_external_resources'),
                   model_uri=FT.evaluation__categorical_values_are_mapped_to_external_resources, domain=None, range=Optional[str])

slots.evaluation__data_is_tidy = Slot(uri=FT.data_is_tidy, name="evaluation__data_is_tidy", curie=FT.curie('data_is_tidy'),
                   model_uri=FT.evaluation__data_is_tidy, domain=None, range=Optional[str])

slots.evaluation__validates_using_schema = Slot(uri=FT.validates_using_schema, name="evaluation__validates_using_schema", curie=FT.curie('validates_using_schema'),
                   model_uri=FT.evaluation__validates_using_schema, domain=None, range=Optional[str])