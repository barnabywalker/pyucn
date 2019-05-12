"""Class definition and associated functions for requesting data from
IUCN Red List. Run as a script it downloads the latest Red List.
You need an API token to use it, available from 
http://apiv3.iucnredlist.org/api/v3/token.
"""

import requests
import requests_cache
import time

from .terms import Url


def _make_request(url, token):
    """Utility to make a request and return JSON data"""

    response = requests.get(url=url, params={"token": token})
    response.raise_for_status()

    json_response = response.json()
    result = json_response.get("result", [])
    if len(result) == 0:
        return
    else:
        return result


def _make_throttle_hook(timeout=0.1):
    """Returns a hook that sleeps for timeout seconds if response is
    from cache.
    """
    def hook(response, *args, **kwargs):
        if not getattr(response, "from_cache", False):
            time.sleep(timeout)

        return response

    return hook


class redList(object):
    """An object that gets data from the IUCN red list
    """

    def __init__(self, token=None, cache=True, cache_name=None, delay=0.5):        
        if token is None:
            raise ValueError("You must provide a token for the IUCN API")
        else:
            self.token = token

        if cache_name is None:
            self.cache_name = "redlist_api_cache"
        else:
            self.cache_name = cache_name

        if cache:
            requests_cache.install_cache(self.cache_name)
            self.session = requests_cache.CachedSession()
        else:
            self.session = requests.Session()

        self.session.hooks = {"response": _make_throttle_hook(delay)}


    def get_redlist(self, page):
        """Request specific page of species data

        parameters:
        page - str, page number to request
        """
        url = Url.redlist.value + f'{page}'
        
        return _make_request(url, self.token)

    def _search_redlist(self, search_term, base_url, term_type="id", omit_type=False):
        """Search a Red List API endpoint for a species, given a name or id.

        parameters:
        search_term - species name or id to search for
        base_url - base url for the endpoint to search
        term_type - whether the search term is a name or id
        omit_type - some endpoints omit the term type from the url
        """

        if omit_type:
            url = base_url.value + f'{search_term}'
        else:
            url = base_url.value + f'{term_type}/{search_term}'

        if term_type not in ["name", "id"]:
            raise ValueError("Not a recognised species search type")

        return _make_request(url, self.token)


    def search_assessment(self, species, search_type="id"):
        """Search for assessment details of a species.

        parameters:
        species - species name or id
        search_type - whether you're searching by name or id
        """
        omit_type = False

        if search_type == "name":
            omit_type = True

        return self._search_redlist(species, Url.species, term_type=search_type, omit_type=omit_type)


    def search_threats(self, species, search_type="id"):
        """Search for threats of a species.

        parameters:
        species - species name or id
        search_type - whether you're searching by name or id
        """
        return self._search_redlist(species, Url.threats, term_type=search_type)

    
    def search_habitats(self, species, search_type="id"):
        """Search for habitats a species occurs in.

        parameters:
        species - species name or id
        search_type - whether you're searching by name or id
        """
        return self._search_redlist(species, Url.habitats, term_type=search_type)

    def search_countries(self, species, search_type="id"):
        """Search for countries a species occurs in.

        parameters:
        species - species name or id
        search_type - whether you're searching by name or id
        """
        return self._search_redlist(species, Url.countries, term_type=search_type)

    def search_measures(self, species, search_type="id"):
        """Search for conservation measures of a species.

        parameters:
        species - species name or id
        search_type - whether you're searching by name or id
        """
        return self._search_redlist(species, Url.conservation_measures, term_type=search_type)

    def search_citation(self, species, search_type="id"):
        """Search for the citation string for a species.

        parameters:
        species - species name or id
        search_type - whether you're searching by name or id
        """
        return self._search_redlist(species, Url.citation, term_type=search_type)

    def search_narrative(self, species, search_type="id"):
        """Search for the assessment narrative of a species.

        parameters:
        species - species name or id
        search_type - whether you're searching by name or id
        """
        omit_type = False

        if search_type == "name":
            omit_type = True

        return self._search_redlist(species, Url.narrative, term_type=search_type)

    def search_forms(self, species, search_type="id"):
        """Search for growth forms of a species.

        parameters:
        species - species name or id
        search_type - whether you're searching by name or id
        """
        return self._search_redlist(species, Url.growth_forms, term_type=search_type)

    def search_history(self, species, search_type="id"):
        """Search for historical assessments of a species.

        parameters:
        species - species name or id
        search_type - whether you're searching by name or id
        """
        return self._search_redlist(species, Url.history, term_type=search_type) 
