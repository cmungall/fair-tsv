

CREATE TABLE "Evaluation" (
	uses_tab_separators VARCHAR(19), 
	uses_unix_newline_characters TEXT, 
	uses_correct_quotation TEXT, 
	avoids_extraneous_whitespace TEXT, 
	avoids_problematic_characters TEXT, 
	avoids_empty_lines TEXT, 
	uses_correct_encoding TEXT, 
	has_column_header TEXT, 
	includes_metadata_header TEXT, 
	includes_data_dictionary TEXT, 
	includes_mappings_to_other_schemas TEXT, 
	dates_use_iso8601 TEXT, 
	"identifiers_are_prefixed_CURIEs" TEXT, 
	"CURIEs_are_syntactically_correct" TEXT, 
	prefixes_are_declared_and_consistent_with_registries TEXT, 
	"prefixes_have_URI_expansions" TEXT, 
	categorical_values_are_enumerated_in_schema TEXT, 
	categorical_values_are_mapped_to_external_resources TEXT, 
	data_is_tidy TEXT, 
	validates_using_schema TEXT, 
	PRIMARY KEY (uses_tab_separators, uses_unix_newline_characters, uses_correct_quotation, avoids_extraneous_whitespace, avoids_problematic_characters, avoids_empty_lines, uses_correct_encoding, has_column_header, includes_metadata_header, includes_data_dictionary, includes_mappings_to_other_schemas, dates_use_iso8601, "identifiers_are_prefixed_CURIEs", "CURIEs_are_syntactically_correct", prefixes_are_declared_and_consistent_with_registries, "prefixes_have_URI_expansions", categorical_values_are_enumerated_in_schema, categorical_values_are_mapped_to_external_resources, data_is_tidy, validates_using_schema)
);

CREATE TABLE "Result" (
	input TEXT, 
	has_evaluation TEXT, 
	PRIMARY KEY (input, has_evaluation)
);
