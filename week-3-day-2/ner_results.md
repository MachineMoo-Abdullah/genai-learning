# Named Entity Recognition Results

## Input Text

Microsoft opened a new AI research center in London in 2026. Satya Nadella announced the project during a conference organized by the World Economic Forum on January 15, 2026. Researchers from Google and OpenAI also attended the event.

## Expected Entity Types

The paragraph contains several categories of entities:

* **Microsoft** — Company / Organization
* **London** — Location
* **2026** — Date
* **Satya Nadella** — Person
* **World Economic Forum** — Organization
* **January 15, 2026** — Date
* **Google** — Company / Organization
* **OpenAI** — Company / Organization

## Observations

The exact entities extracted may depend on the pretrained checkpoint used by the pipeline. Some possible issues include:

1. **Companies may be classified as organizations**, which is usually acceptable because many NER models use a general ORG category.
2. **Dates may be missed** because some pretrained NER models were trained mainly on categories such as Person, Organization, Location, and Miscellaneous.
3. **Multi-word entities may be split** into separate tokens. Using `aggregation_strategy="simple"` helps combine related tokens.
4. A model may incorrectly classify an entity because it does not fully understand the context.

## Conclusion

Named Entity Recognition is useful for automatically extracting structured information from unstructured text. However, pretrained models are not perfect, and their predictions should be evaluated according to the domain and task requirements.
