import os

from api.routes import Routes
from lib.openapi_spec_generation import generate_api_specs

if __name__ == "__main__":
    EXPOSED_SYSTEM_METHODS = {}
    name: str
    for name, method in Routes.__dict__.items():
        if not name.startswith("_"):
            EXPOSED_SYSTEM_METHODS[name] = Routes
    generate_api_specs(title="P0 system API", classname="P0SystemAPI", methods_dict=EXPOSED_SYSTEM_METHODS,
                       out_folder=os.path.dirname(__file__),
                       package_name="p0_system_api")
