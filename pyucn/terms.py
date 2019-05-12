from enum import Enum

class Url(Enum):
    redlist = "http://apiv3.iucnredlist.org/api/v3/species/"
    species = "http://apiv3.iucnredlist.org/api/v3/species/"
    # bad url
    threats = "http://apiv3.iucnredlist.org/api/v3/threats/species/"
    habitats = "http://apiv3.iucnredlist.org/api/v3/habitats/species/"
    # bad url
    countries = "http://apiv3.iucnredlist.org/api/v3/species/countries/"
    conservation_measures = "http://apiv3.iucnredlist.org/api/v3/measures/species/"
    # bad url
    citation = "http://apiv3.iucnredlist.org/api/v3/species/citation/"
    # bad url
    narrative = "http://apiv3.iucnredlist.org/api/v3/species/narrative/"
    growth_forms = "http://apiv3.iucnredlist.org/api/v3/growth_forms/species/"
    # bad url
    history = "http://apiv3.iucnredlist.org/api/v3/species/history/"
